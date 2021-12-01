FROM python:3.9-buster

# Install pyright
RUN bash -c ' \
    set -e; \
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash; \
    export NVM_DIR="$HOME/.nvm"; \
    \. "$NVM_DIR/nvm.sh"; \
    nvm install --lts; \
    npm install -g pyright; \
'

WORKDIR /app
COPY . .
RUN pip install -e .

# Run pyright
CMD bash -c 'export NVM_DIR="$HOME/.nvm"; \. "$NVM_DIR/nvm.sh"; pyright --verifytypes pyright_2625'
