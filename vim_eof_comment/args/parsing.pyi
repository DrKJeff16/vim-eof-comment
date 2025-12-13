from ..util import die as die
from .color import ColorArgParser as ColorArgParser
from argparse import Namespace
from typing import Any

def bootstrap_args(parser: ColorArgParser, specs: tuple[tuple[list[str], dict[str, Any]]]) -> Namespace: ...
def arg_parser_init() -> tuple[ColorArgParser, Namespace]: ...

# vim:ts=4:sts=4:sw=4:et:ai:si:sta:
