import sys
from typing import Any, Callable, Mapping

class BaseProcess:
    name: str
    daemon: bool
    authkey: bytes
    _identity: tuple[int, ...]  # undocumented
    def __init__(
        self,
        group: None = ...,
        target: Callable[..., Any] | None = ...,
        name: str | None = ...,
        args: tuple[Any, ...] = ...,
        kwargs: Mapping[str, Any] = ...,
        *,
        daemon: bool | None = ...,
    ) -> None: ...
    def run(self) -> None: ...
    def start(self) -> None: ...
    def terminate(self) -> None: ...
    if sys.version_info >= (3, 7):
        def kill(self) -> None: ...
        def close(self) -> None: ...
    def join(self, timeout: float | None = ...) -> None: ...
    def is_alive(self) -> bool: ...
    @property
    def exitcode(self) -> int | None: ...
    @property
    def ident(self) -> int | None: ...
    @property
    def pid(self) -> int | None: ...
    @property
    def sentinel(self) -> int: ...

def current_process() -> BaseProcess: ...
def active_children() -> list[BaseProcess]: ...

if sys.version_info >= (3, 8):
    def parent_process() -> BaseProcess | None: ...
