# -*- coding: utf-8 -*-
# Copyright (c) 2025 Guennadi Maximov C. All Rights Reserved.
"""
Custom vim-eof-comment ``TypedDict`` objects.

Copyright (c) 2025 Guennadi Maximov C. All Rights Reserved.
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

from typing import Any, Dict, List, TextIO, Tuple, TypedDict

import argcomplete


class VersionInfo():
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
    all_versions: List[Tuple[int, int, int]]

    def __init__(self, all_versions: List[Tuple[int, int, int]]):
        """
        Initialize VersionInfo object.

        Parameters
        ----------
        all_versions : List[Tuple[int, int, int]]
            A list of tuples of three-integers, containing (in order) the major, minor and patch
            components.
        """
        self.all_versions = all_versions.copy()

        all_versions = all_versions.copy()[::-1]
        self.major = all_versions[0][0]
        self.minor = all_versions[0][1]
        self.patch = all_versions[0][2]

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
        return f"{self.major}.{self.minor}.{self.patch}"

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
        return self.__str__()

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

        b: VersionInfo = b
        return self.major == b.major and self.minor == b.minor and self.patch == b.patch

    def get_current_version(self) -> Tuple[int, int, int]:
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
        return (self.major, self. minor, self.patch)

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


class ParserSpec(TypedDict):
    """
    Stores the spec for ``argparse`` operations in a constant value.

    This is a ``TypedDict``-like object.

    Attributes
    ----------
    opts : List[str]
        A list containing all the relevant iterations of the same option.
    kwargs : Dict[str, Any]
        Extra arguments for ``argparse.ArgumentParser``.
    completer : argcomplete.DirectoriesCompleter
        An ``argcomplete`` completer object.
    """

    opts: List[str]
    kwargs: Dict[str, Any]
    completer: argcomplete.DirectoriesCompleter


class CommentMap(TypedDict):
    """
    Stores a dict with a ``level`` key.

    This is a ``TypedDict``-like object.

    Attributes
    ----------
    level : int
        The indentation level.
    """

    level: int


class IndentMap(TypedDict):
    """
    A dict containing ``level`` and ``expandtab`` as keys.

    This is a ``TypedDict``-like object.

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
    A dict containing ``ft_ext``, ``level`` and ``expandtab`` as keys.

    This is a ``TypedDict``-like object.

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


class IOWrapperBool(TypedDict):
    """
    A dict containing ``file`` and ``had_nwl`` as keys.

    This is a ``TypedDict``-like object.

    Attributes
    ----------
    file : TextIO
        The opened file as a ``TextIO`` wrapper.
    had_nwl : bool
        Whether the file has a newline or not.
    """

    file: TextIO
    had_nwl: bool


class LineBool(TypedDict):
    """
    A dict containing ``line`` and ``had_nwl`` as keys.

    This is a ``TypedDict``-like object.

    Attributes
    ----------
    line : str
        The last line of the target file.
    had_nwl : bool
        Whether the file has a newline or not.
    """

    line: str
    had_nwl: bool


class BatchPathDict(TypedDict):
    """
    A dict containing ``file`` and ``ft_ext`` as keys.

    This is a ``TypedDict``-like object.

    Attributes
    ----------
    file : TextIO
        The opened file as a ``TextIO`` wrapper.
    ft_ext : str
        The file-type/file-extension.
    """

    file: TextIO
    ft_ext: str


class BatchPairDict(TypedDict):
    """
    A dict containing ``fpath`` and ``ft_ext`` as keys.

    This is a ``TypedDict``-like object.

    Attributes
    ----------
    fpath : str
        The target file's path.
    ft_ext : str
        The file-type/file-extension.
    """

    fpath: str
    ft_ext: str


class EOFCommentSearch(TypedDict):
    """
    A dict containing ``state``, ``lang`` and ``match`` as keys.

    This is a ``TypedDict``-like object.

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

# vim: set ts=4 sts=4 sw=4 et ai si sta:
