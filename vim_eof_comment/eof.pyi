from .args.parsing import arg_parser_init as arg_parser_init, indent_handler as indent_handler
from .comments import Comments as Comments
from .file import bootstrap_paths as bootstrap_paths, modify_file as modify_file, open_batch_paths as open_batch_paths
from .types.typeddict import BatchPathDict as BatchPathDict, EOFCommentSearch as EOFCommentSearch, IOWrapperBool as IOWrapperBool, IndentHandler as IndentHandler, LineBool as LineBool
from .util import die as die, gen_indent_maps as gen_indent_maps
from io import TextIOWrapper
from typing import NoReturn

def get_last_line(file: TextIOWrapper) -> LineBool:
    """Returns the last line of a file."""
def eof_comment_search(files: dict[str, BatchPathDict], comments: Comments, newline: bool) -> dict[str, EOFCommentSearch]:
    """Searches through opened files."""
def append_eof_comment(files: dict[str, EOFCommentSearch], comments: Comments, newline: bool) -> NoReturn:
    """Append EOF comment to files missing it."""
def main() -> int:
    """Execute main workflow."""
# vim:ts=4:sts=4:sw=4:et:ai:si:sta:
