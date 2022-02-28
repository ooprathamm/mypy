from types import CodeType

def compile_command(source: str, filename: str = ..., symbol: str = ...) -> CodeType | None: ...

class Compile:
    flags: int
    def __init__(self) -> None: ...
    def __call__(self, source: str, filename: str, symbol: str) -> CodeType: ...

class CommandCompiler:
    compiler: Compile
    def __init__(self) -> None: ...
    def __call__(self, source: str, filename: str = ..., symbol: str = ...) -> CodeType | None: ...
