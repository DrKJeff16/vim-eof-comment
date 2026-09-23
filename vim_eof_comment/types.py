# Copyright (c) 2026 Guennadi Maximov C. All Rights Reserved.
"""
Custom vim-eof-comment ``TypedDict`` objects.

Copyright (c) 2026 Guennadi Maximov C. All Rights Reserved.
"""

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

from io import TextIOWrapper
from typing import Any, TypedDict

from shtab import CompleteType


class VersionInfo:
    """
    A ``sys.version_info``-like object type.

    Parameters
    ----------
    all_versions : list[tuple[int, int, int]]
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
    all_versions : list[tuple[int, int, int]]
        A list of tuples containing all the versions in the object instance.

    Methods
    -------
    get_all_versions()
    """

    major: int
    minor: int
    patch: int
    all_versions: list[tuple[int, int, int]]

    def __init__(self, all_versions: list[tuple[int, int, int]]):
        """
        Initialize VersionInfo object.

        Parameters
        ----------
        all_versions : list[tuple[int, int, int]]
            A list of tuples of three-integers, containing (in order) the major, minor and patch
            components.
        """
        self.all_versions = all_versions.copy()

        all_versions = all_versions.copy()[::-1]
        self.major = all_versions[0][0]
        self.minor = all_versions[0][1]
        self.patch = all_versions[0][2]

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
        if not isinstance(b, VersionInfo):
            return False

        return self.major == b.major and self.minor == b.minor and self.patch == b.patch

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
        return (self.major, self.minor, self.patch)

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
        result = ""
        for i, info in enumerate(self.all_versions):
            result += f"{info[0]}.{info[1]}.{info[2]}"
            if i == len(self.all_versions) - 1:
                result += " (latest)"
            else:
                result += "\n"

        return result


class ParserSpec:
    """
    Stores the spec for ``argparse`` operations in a constant value.

    Parameters
    ----------
    opts : list[str]
        A list containing all the relevant iterations of the same option.
    kwargs : dict[str, Any]
        Extra arguments for ``argparse.ArgumentParser``.
    complete : shtab.CompleteType or dict[str, CompleteType] or None, default=None
        Opptional ``shtab`` complete type.

    Attributes
    ----------
    opts : list[str]
        A list containing all the relevant iterations of the same option.
    kwargs : dict[str, Any]
        Extra arguments for ``argparse.ArgumentParser``.
    complete : shtab.CompleteType or dict[str, CompleteType] or None, default=None
        Opptional ``shtab`` complete type.
    """

    opts: list[str]
    kwargs: dict[str, Any]
    complete: CompleteType | dict[str, CompleteType] | None

    def __init__(
        self,
        opts: list[str],
        kwargs: dict[str, Any],
        complete: CompleteType | dict[str, CompleteType] | None = None,
    ):
        self.opts = opts
        self.kwargs = kwargs
        self.complete = complete


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

    def __init__(self, level: int):
        self.level = level


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

    def __init__(self, file: TextIOWrapper, had_nwl: bool, crlf: bool):
        self.file = file
        self.had_nwl = had_nwl
        self.crlf = crlf

    def __iterables(self) -> tuple[TextIOWrapper, bool, bool]:
        """
        Generate iterables.

        Returns
        -------
        tuple[io.TextIOWrapper, bool, bool]
            The ``file``, ``had_nwl`` and ``crlf`` attributes.
        """
        return (self.file, self.had_nwl, self.crlf)

    def __iter__(self):
        """Iterate over objects."""
        yield from self.__iterables()


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

    def __init__(self, line: str, had_nwl: bool, crlf: bool):
        self.line = line
        self.had_nwl = had_nwl
        self.crlf = crlf

    def __iterables(self) -> tuple[str, bool, bool]:
        """
        Generate iterables.

        Returns
        -------
        tuple[str, bool, bool]
            The ``line``, ``had_nwl`` and ``crlf`` attributes.
        """
        return (self.line, self.had_nwl, self.crlf)

    def __iter__(self):
        """Iterate over objects."""
        yield from self.__iterables()


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

    def __init__(self, file: TextIOWrapper, ft_ext: str):
        self.file = file
        self.ft_ext = ft_ext

    def __iterables(self) -> tuple[TextIOWrapper, str]:
        """
        Generate iterables.

        Returns
        -------
        tuple[io.TextIOWrapper, str]
            The ``file`` and ``ft_ext`` attributes.
        """
        return (self.file, self.ft_ext)

    def __iter__(self):
        """Iterate over objects."""
        yield from self.__iterables()


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

    def __init__(self, fpath: str, ft_ext: str):
        self.fpath = fpath
        self.ft_ext = ft_ext

    def __iterables(self) -> tuple[str, str]:
        """
        Generate iterables.

        Returns
        -------
        tuple[str, str]
            The ``fpath`` and ``ft_ext`` attributes.
        """
        return (self.fpath, self.ft_ext)

    def __iter__(self):
        """Iterate over objects."""
        yield from self.__iterables()


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

    def __init__(self, state: IOWrapperBool, lang: str, match: bool):
        self.state = state
        self.lang = lang
        self.match = match

    def __iterables(self) -> tuple[IOWrapperBool, str, bool]:
        """
        Generate iterables.

        Returns
        -------
        tuple[IOWrapperBool, str, bool]
            The ``state``, ``lang`` and ``match`` attributes.
        """
        return (self.state, self.lang, self.match)

    def __iter__(self):
        """Iterate over objects."""
        yield from self.__iterables()


# vim: set ts=4 sts=4 sw=4 et ai si sta:
