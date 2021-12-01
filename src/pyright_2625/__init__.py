from typing import TypeVar, List, Union

T = TypeVar('T')
Foo = List[T]
U = Union[str, List[T]]

def foo(f: Foo) -> None:
    pass

def bar(f: List) -> None:
    pass

def baz(x: U) -> None:
    pass
