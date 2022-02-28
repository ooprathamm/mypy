import sys
from _typeshed import Self, SupportsRead, SupportsReadline
from socket import socket
from ssl import SSLContext
from types import TracebackType
from typing import Any, Callable, Iterable, Iterator, TextIO, Type
from typing_extensions import Literal

MSG_OOB: int
FTP_PORT: int
MAXLINE: int
CRLF: str
B_CRLF: bytes

class Error(Exception): ...
class error_reply(Error): ...
class error_temp(Error): ...
class error_perm(Error): ...
class error_proto(Error): ...

all_errors: tuple[Type[Exception], ...]

class FTP:
    debugging: int
    host: str
    port: int
    maxline: int
    sock: socket | None
    welcome: str | None
    passiveserver: int
    timeout: int
    af: int
    lastresp: str
    file: TextIO | None
    encoding: str
    def __enter__(self: Self) -> Self: ...
    def __exit__(
        self, exc_type: Type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> None: ...
    source_address: tuple[str, int] | None
    if sys.version_info >= (3, 9):
        def __init__(
            self,
            host: str = ...,
            user: str = ...,
            passwd: str = ...,
            acct: str = ...,
            timeout: float = ...,
            source_address: tuple[str, int] | None = ...,
            *,
            encoding: str = ...,
        ) -> None: ...
    else:
        def __init__(
            self,
            host: str = ...,
            user: str = ...,
            passwd: str = ...,
            acct: str = ...,
            timeout: float = ...,
            source_address: tuple[str, int] | None = ...,
        ) -> None: ...
    def connect(
        self, host: str = ..., port: int = ..., timeout: float = ..., source_address: tuple[str, int] | None = ...
    ) -> str: ...
    def getwelcome(self) -> str: ...
    def set_debuglevel(self, level: int) -> None: ...
    def debug(self, level: int) -> None: ...
    def set_pasv(self, val: bool | int) -> None: ...
    def sanitize(self, s: str) -> str: ...
    def putline(self, line: str) -> None: ...
    def putcmd(self, line: str) -> None: ...
    def getline(self) -> str: ...
    def getmultiline(self) -> str: ...
    def getresp(self) -> str: ...
    def voidresp(self) -> str: ...
    def abort(self) -> str: ...
    def sendcmd(self, cmd: str) -> str: ...
    def voidcmd(self, cmd: str) -> str: ...
    def sendport(self, host: str, port: int) -> str: ...
    def sendeprt(self, host: str, port: int) -> str: ...
    def makeport(self) -> socket: ...
    def makepasv(self) -> tuple[str, int]: ...
    def login(self, user: str = ..., passwd: str = ..., acct: str = ...) -> str: ...
    # In practice, `rest` rest can actually be anything whose str() is an integer sequence, so to make it simple we allow integers.
    def ntransfercmd(self, cmd: str, rest: int | str | None = ...) -> tuple[socket, int]: ...
    def transfercmd(self, cmd: str, rest: int | str | None = ...) -> socket: ...
    def retrbinary(
        self, cmd: str, callback: Callable[[bytes], Any], blocksize: int = ..., rest: int | str | None = ...
    ) -> str: ...
    def storbinary(
        self,
        cmd: str,
        fp: SupportsRead[bytes],
        blocksize: int = ...,
        callback: Callable[[bytes], Any] | None = ...,
        rest: int | str | None = ...,
    ) -> str: ...
    def retrlines(self, cmd: str, callback: Callable[[str], Any] | None = ...) -> str: ...
    def storlines(self, cmd: str, fp: SupportsReadline[bytes], callback: Callable[[bytes], Any] | None = ...) -> str: ...
    def acct(self, password: str) -> str: ...
    def nlst(self, *args: str) -> list[str]: ...
    # Technically only the last arg can be a Callable but ...
    def dir(self, *args: str | Callable[[str], None]) -> None: ...
    def mlsd(self, path: str = ..., facts: Iterable[str] = ...) -> Iterator[tuple[str, dict[str, str]]]: ...
    def rename(self, fromname: str, toname: str) -> str: ...
    def delete(self, filename: str) -> str: ...
    def cwd(self, dirname: str) -> str: ...
    def size(self, filename: str) -> int | None: ...
    def mkd(self, dirname: str) -> str: ...
    def rmd(self, dirname: str) -> str: ...
    def pwd(self) -> str: ...
    def quit(self) -> str: ...
    def close(self) -> None: ...

class FTP_TLS(FTP):
    if sys.version_info >= (3, 9):
        def __init__(
            self,
            host: str = ...,
            user: str = ...,
            passwd: str = ...,
            acct: str = ...,
            keyfile: str | None = ...,
            certfile: str | None = ...,
            context: SSLContext | None = ...,
            timeout: float = ...,
            source_address: tuple[str, int] | None = ...,
            *,
            encoding: str = ...,
        ) -> None: ...
    else:
        def __init__(
            self,
            host: str = ...,
            user: str = ...,
            passwd: str = ...,
            acct: str = ...,
            keyfile: str | None = ...,
            certfile: str | None = ...,
            context: SSLContext | None = ...,
            timeout: float = ...,
            source_address: tuple[str, int] | None = ...,
        ) -> None: ...
    ssl_version: int
    keyfile: str | None
    certfile: str | None
    context: SSLContext
    def login(self, user: str = ..., passwd: str = ..., acct: str = ..., secure: bool = ...) -> str: ...
    def auth(self) -> str: ...
    def prot_p(self) -> str: ...
    def prot_c(self) -> str: ...
    def ccc(self) -> str: ...

def parse150(resp: str) -> int | None: ...  # undocumented
def parse227(resp: str) -> tuple[str, int]: ...  # undocumented
def parse229(resp: str, peer: Any) -> tuple[str, int]: ...  # undocumented
def parse257(resp: str) -> str: ...  # undocumented
def ftpcp(
    source: FTP, sourcename: str, target: FTP, targetname: str = ..., type: Literal["A", "I"] = ...
) -> None: ...  # undocumented
