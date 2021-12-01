from typing import TypeVar, List

T = TypeVar('T')
Foo = List[T]

def foo(f: Foo) -> None:
    pass

def bar(f: List) -> None:
    pass
