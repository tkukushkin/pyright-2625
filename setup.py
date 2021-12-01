from setuptools import find_packages, setup


setup(
    name='pyright-2625',
    version='0.0.0',
    license='MIT',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=[],
)
