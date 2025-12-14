from .types.typeddict import IndentHandler as IndentHandler, IndentMap as IndentMap
from typing import Callable, NoReturn, TextIO

def error(*msg, end: str = '\n', sep: str = ' ', flush: bool = False) -> NoReturn:
    """Prints to stderr."""
def die(*msg, code: int = 0, end: str = '\n', sep: str = ' ', flush: bool = False, func: Callable[[TextIO], None] | None = None) -> NoReturn:
    """Kill program execution."""
def gen_indent_maps(maps: list[IndentHandler]) -> dict[str, IndentMap] | None:
    """Generate a dictionary from the custom indent maps."""
from .types.typeddict import IndentHandler as IndentHandler, IndentMap as IndentMap
from typing import Callable, NoReturn, TextIO

def error(*msg, end: str = '\n', sep: str = ' ', flush: bool = False) -> NoReturn:
    """Prints to stderr."""
def die(*msg, code: int = 0, end: str = '\n', sep: str = ' ', flush: bool = False, func: Callable[[TextIO], None] | None = None) -> NoReturn:
    """Kill program execution."""
def gen_indent_maps(maps: list[IndentHandler]) -> dict[str, IndentMap] | None:
    """Generate a dictionary from the custom indent maps."""

# vim:ts=4:sts=4:sw=4:et:ai:si:sta:
