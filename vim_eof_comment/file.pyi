from io import TextIOWrapper

from .types.typeddict import BatchPairDict, BatchPathDict, LineBool

__all__ = ['bootstrap_paths', 'open_batch_paths', 'modify_file', 'get_last_line']

def bootstrap_paths(paths: tuple[str], exts: tuple[str]) -> list[BatchPairDict]:
    """
    Bootstrap all the matching paths in current dir and below.

    Parameters
    ----------
    paths : array_like
        A list of specified file paths.
    exts : array_like
        A list of specified file extensions.

    Returns
    -------
    List[BatchPairDict]
        A list of ``BatchPairDict`` type objects.
    """
def open_batch_paths(paths: list[BatchPairDict]) -> dict[str, BatchPathDict]:
    """
    Return a list of TextIO objects given file path strings.

    Parameters
    ----------
    paths : List[BatchPairDict]
        A list of BatchPairDict type objects.

    Returns
    -------
    Dict[str, BatchPathDict]
        A ``str`` to ``BatchPathDict``` dictionary.
    """
def modify_file(file: TextIOWrapper, comments: dict[str, str], ext: str, newline: bool, has_nwl: bool, matching: bool) -> str:
    """
    Modify a file containing a bad EOF comment.

    Parameters
    ----------
    file : TextIOWrapper
        The file object to be read.
    comments : Dict[str, str]
        A filetype-to-comment dictionary.
    ext : str
        The filetype extension given by the user.
    newline : bool
        Flag to whether add a newline before the comment.
    has_nwl : bool
        Indicates whether the file already has a newline at the end
        (not counting LF/CRLF line endings).
    matching : bool
        Indicates whether the file already has a matching EOF comment.

    Returns
    -------
    str
        The modified contents of the given file.
    """
def get_last_line(file: TextIOWrapper) -> LineBool:
    """
    Return the last line of a file and indicates whether it already has a newline.

    Parameters
    ----------
    file : TextIOWrapper
        The file to retrieve the last line data from.

    Returns
    -------
    LineBool
        An object containing both the last line in a string and a boolean indicating a newline.
    """

# vim: set ts=4 sts=4 sw=4 et ai si sta:
