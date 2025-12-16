from .args.parsing import arg_parser_init as arg_parser_init, indent_handler as indent_handler
from .comments.generator import Comments as Comments
from .file import bootstrap_paths as bootstrap_paths, get_last_line as get_last_line, modify_file as modify_file, open_batch_paths as open_batch_paths
from .regex import matches as matches
from .types.typeddict import BatchPathDict as BatchPathDict, EOFCommentSearch as EOFCommentSearch, IOWrapperBool as IOWrapperBool, IndentHandler as IndentHandler
from .types.version import version_info as version_info
from .util import die as die, gen_indent_maps as gen_indent_maps, verbose_print as verbose_print, version_print as version_print
from typing import NoReturn

_RED: int
_GREEN: int
_BRIGHT: int
_RESET: int

def eof_comment_search(files: dict[str, BatchPathDict], comments: Comments, newline: bool, verbose: bool) -> dict[str, EOFCommentSearch]:
    """
    Searches through opened files.

    Parameters
    ----------
    files : Dict[str, BatchPathDict]
        A dictionary of ``str`` to ``BatchPathDict`` objects.
    comments : Comments
        The ``Comments`` object containing the hardcoded comments per file extension.
    newline : bool
        Indicates whether a newline should be added before the comment.
    verbose : bool
        Sets verbose mode.

    Returns
    -------
    result : Dict[str, EOFCommentSearch]
        A dictionary of ``str`` to ``EOFCommentSearch`` objects.
    """
def append_eof_comment(files: dict[str, EOFCommentSearch], comments: Comments, newline: bool) -> NoReturn:
    """
    Append a Vim EOF comment to files missing it.

    Parameters
    ----------
    files : Dict[str, EOFCommentSearch]
        A dictionary of ``str`` to ``EOFCommentSearch`` objects.
    comments : Comments
        The ``Comments`` object containing the hardcoded comments per file extension.
    newline : bool
        Indicates whether a newline should be added before the comment.
    """
def main() -> int:
    """
    Execute the main workflow.

    Returns
    -------
    int
        The exit code for the program.
    """

# vim: set ts=4 sts=4 sw=4 et ai si sta:
