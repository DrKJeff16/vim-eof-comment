from io import TextIOWrapper
from typing import Any, TypedDict

from argcomplete.completers import DirectoriesCompleter

__all__ = [
    "BatchPairDict",
    "BatchPathDict",
    "CommentMap",
    "EOFCommentSearch",
    "IOWrapperBool",
    "IndentHandler",
    "IndentMap",
    "LineBool",
    "ParserSpec",
    "VersionInfo",
]

class VersionInfo:
    """
    A ``sys.version_info``-like object type.

    Parameters
    ----------
    all_versions : List[Tuple[int, int, int]]
        A list of three number tuples, containing (in order) the major, minor and patch
        components.

    Attributes
    ----------
    major : int
        The major component of the version.
    minor : int
        The minor component of the version.
    patch : int
        The patch component of the version.
    all_versions : List[Tuple[int, int, int]]
        A list of tuples containing all the versions in the object instance.

    Methods
    -------
    get_all_versions()
    """

    major: int
    minor: int
    patch: int
    all_versions: list[tuple[int, int, int]]
    def __init__(self, all_versions: list[tuple[int, int, int]]) -> None:
        """
        Initialize VersionInfo object.

        Parameters
        ----------
        all_versions : List[Tuple[int, int, int]]
            A list of tuples of three-integers, containing (in order) the major, minor and patch
            components.
        """
    def __str__(self) -> str:
        """
        Representate this object as a string.

        This is what is returned when using ``str(VersionInfo(...))``.

        Returns
        -------
        str
            The string representation of the instance.

        Examples
        --------
        Only one definition in constructor.

        >>> from vim_eof_comment.version import VersionInfo
        >>> print(str(VersionInfo([(0, 0, 1)])))
        0.0.1

        Multiple definitions in constructor.

        >>> from vim_eof_comment.version import VersionInfo
        >>> print(str(VersionInfo([(0, 0, 1), (0, 0, 2)])))
        0.0.2
        """
    def __repr__(self) -> str:
        """
        Representate this object as a string.

        This is what is returned when using ``print(VersionInfo(...))``.

        Returns
        -------
        str
            The string representation of the instance.

        Examples
        --------
        Only one definition in constructor.

        >>> from vim_eof_comment.version import VersionInfo
        >>> print(repr(VersionInfo([(0, 0, 1)])))
        0.0.1

        Multiple definitions in constructor.

        >>> from vim_eof_comment.version import VersionInfo
        >>> print(repr(VersionInfo([(0, 0, 1), (0, 0, 2)])))
        0.0.2
        """
    def __eq__(self, b) -> bool:
        """
        Check the equality between two ``VersionInfo`` instances.

        Parameters
        ----------
        b : VersionInfo
            The other instance to compare.

        Returns
        -------
        bool
            Whether they are equal or not.
        """
    def get_current_version(self) -> tuple[int, int, int]:
        """
        Get a tuple representing the current version.

        Returns
        -------
        major : int
            Major component.
        minor : int
            Minor component.
        patch : int
            Patch component.
        """
    def get_all_versions(self) -> str:
        """
        Retrieve all versions as a string.

        Returns
        -------
        str
            A string, containing the program versions, in ascending order.

        Examples
        --------
        To generate a single string.
        >>> from vim_eof_comment.version import VersionInfo
        >>> print(VersionInfo([(0, 0, 1), (0, 0, 2), (0, 1, 0)]).get_all_versions())
        0.0.1
        0.0.2
        0.0.3 (latest)
        """

class ParserSpec:
    """
    Stores the spec for ``argparse`` operations in a constant value.

    Parameters
    ----------
    opts : List[str]
        A list containing all the relevant iterations of the same option.
    kwargs : Dict[str, Any]
        Extra arguments for ``argparse.ArgumentParser``.
    completer : argcomplete.completers.DirectoriesCompleter
        An ``argcomplete`` completer object.

    Attributes
    ----------
    opts : List[str]
        A list containing all the relevant iterations of the same option.
    kwargs : Dict[str, Any]
        Extra arguments for ``argparse.ArgumentParser``.
    completer : argcomplete.completers.DirectoriesCompleter
        An ``argcomplete`` completer object.
    """

    opts: list[str]
    kwargs: dict[str, Any]
    completer: DirectoriesCompleter
    def __init__(
        self, opts: list[str], kwargs: dict[str, Any], completer: DirectoriesCompleter
    ) -> None: ...

class CommentMap:
    """
    An object containing ``level``.

    Parameters
    ----------
    level : int
        The indentation level.

    Attributes
    ----------
    level : int
        The indentation level.
    """

    level: int
    def __init__(self, level: int) -> None: ...

class IndentMap(TypedDict):
    """
    An object containing ``level`` and ``expandtab``.

    Attributes
    ----------
    level : int
        The indent level.
    expandtab : bool
        Whether to expand tabs or not.
    """

    level: int
    expandtab: bool

class IndentHandler(TypedDict):
    """
    An object containing ``ft_ext``, ``level`` and ``expandtab``.

    Attributes
    ----------
    ft_ext : str
        The file-extension/file-type.
    level : str
        The string representation of the indent level.
    expandtab : bool
        Whether to expand tabs or not.
    """

    ft_ext: str
    level: str
    expandtab: bool

class IOWrapperBool:
    """
    An object containing ``file``, ``had_nwl`` and ``crlf``.

    Parameters
    ----------
    file : io.TextIOWrapper
        The opened file as a ``io.TextIOWrapper`` wrapper.
    had_nwl : bool
        Whether the file has a newline or not.
    crlf : bool
        Whether the file is CRLF-terminated.

    Attributes
    ----------
    file : io.TextIOWrapper
        The opened file as a ``io.TextIOWrapper`` wrapper.
    had_nwl : bool
        Whether the file has a newline or not.
    crlf : bool
        Whether the file is CRLF-terminated.
    """

    file: TextIOWrapper
    had_nwl: bool
    crlf: bool
    def __init__(self, file: TextIOWrapper, had_nwl: bool, crlf: bool) -> None: ...
    def __iterables(self) -> tuple[TextIOWrapper, bool, bool]:
        """
        Generate iterables.

        Returns
        -------
        Tuple[io.TextIOWrapper, bool, bool]
            The ``file``, ``had_nwl`` and ``crlf`` attributes.
        """
    def __iter__(self):
        """Iterate over objects."""

class LineBool:
    """
    An object containing ``line``, ``had_nwl`` and ``crlf``.

    Parameters
    ----------
    line : str
        The last line of the target file.
    had_nwl : bool
        Whether the file has a newline or not.
    crlf : bool
        Whether the file is CRLF-terminated.

    Attributes
    ----------
    line : str
        The last line of the target file.
    had_nwl : bool
        Whether the file has a newline or not.
    crlf : bool
        Whether the file is CRLF-terminated.
    """

    line: str
    had_nwl: bool
    crlf: bool
    def __init__(self, line: str, had_nwl: bool, crlf: bool) -> None: ...
    def __iterables(self) -> tuple[str, bool, bool]:
        """
        Generate iterables.

        Returns
        -------
        Tuple[str, bool, bool]
            The ``line``, ``had_nwl`` and ``crlf`` attributes.
        """
    def __iter__(self):
        """Iterate over objects."""

class BatchPathDict:
    """
    An object containing ``file`` and ``ft_ext``.

    Parameters
    ----------
    file : io.TextIOWrapper
        The opened file as a ``TextIO`` wrapper.
    ft_ext : str
        The file-type/file-extension.

    Attributes
    ----------
    file : io.TextIOWrapper
        The opened file as a ``TextIO`` wrapper.
    ft_ext : str
        The file-type/file-extension.
    """

    file: TextIOWrapper
    ft_ext: str
    def __init__(self, file: TextIOWrapper, ft_ext: str) -> None: ...
    def __iterables(self) -> tuple[TextIOWrapper, str]:
        """
        Generate iterables.

        Returns
        -------
        Tuple[io.TextIOWrapper, str]
            The ``file`` and ``ft_ext`` attributes.
        """
    def __iter__(self):
        """Iterate over objects."""

class BatchPairDict:
    """
    An object containing ``fpath`` and ``ft_ext``.

    Parameters
    ----------
    fpath : str
        The target file's path.
    ft_ext : str
        The file-type/file-extension.

    Attributes
    ----------
    fpath : str
        The target file's path.
    ft_ext : str
        The file-type/file-extension.
    """

    fpath: str
    ft_ext: str
    def __init__(self, fpath: str, ft_ext: str) -> None: ...
    def __iterables(self) -> tuple[str, str]:
        """
        Generate iterables.

        Returns
        -------
        Tuple[str, str]
            The ``fpath`` and ``ft_ext`` attributes.
        """
    def __iter__(self):
        """Iterate over objects."""

class EOFCommentSearch:
    """
    A dict containing ``state``, ``lang`` and ``match`` as keys.

    This is a ``TypedDict``-like object.

    Parameters
    ----------
    state : IOWrapperBool
        The target ``IOWrapperBool`` object.
    lang : str
        The file language.
    match : bool
        Whether it has a variation of an EOF comment at the end.

    Attributes
    ----------
    state : IOWrapperBool
        The target ``IOWrapperBool`` object.
    lang : str
        The file language.
    match : bool
        Whether it has a variation of an EOF comment at the end.
    """

    state: IOWrapperBool
    lang: str
    match: bool
    def __init__(self, state: IOWrapperBool, lang: str, match: bool) -> None: ...
    def __iterables(self) -> tuple[IOWrapperBool, str, bool]:
        """
        Generate iterables.

        Returns
        -------
        Tuple[IOWrapperBool, str, bool]
            The ``state``, ``lang`` and ``match`` attributes.
        """
    def __iter__(self):
        """Iterate over objects."""

# vim: set ts=4 sts=4 sw=4 et ai si sta:
