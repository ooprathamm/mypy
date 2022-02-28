from typing import MutableSequence, Sequence, TypeVar

_T = TypeVar("_T")

def bisect_left(a: Sequence[_T], x: _T, lo: int = ..., hi: int | None = ...) -> int: ...
def bisect_right(a: Sequence[_T], x: _T, lo: int = ..., hi: int | None = ...) -> int: ...
def insort_left(a: MutableSequence[_T], x: _T, lo: int = ..., hi: int | None = ...) -> None: ...
def insort_right(a: MutableSequence[_T], x: _T, lo: int = ..., hi: int | None = ...) -> None: ...
