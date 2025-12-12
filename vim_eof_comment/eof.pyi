from .args.parsing import arg_parser_init as arg_parser_init
from .comments import Comments as Comments
from .file import bootstrap_paths as bootstrap_paths, modify_file as modify_file, open_batch_paths as open_batch_paths
from .util import die as die
from _typeshed import Incomplete
from io import TextIOWrapper
from typing import NoReturn

COMMENTS: Incomplete

def get_last_line(file: TextIOWrapper) -> tuple[str, bool]: ...
def eof_comment_search(files: dict[str, tuple[TextIOWrapper, str]], newline: bool) -> dict[str, tuple[tuple[TextIOWrapper, bool], str, bool]]: ...
def append_eof_comment(files: dict[str, tuple[tuple[TextIOWrapper, bool], str, bool]], newline: bool) -> NoReturn: ...
def main() -> int: ...
