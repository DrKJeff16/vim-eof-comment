# Copyright (c) 2026 Guennadi Maximov C. All Rights Reserved.
"""
Per-filetype modeline comment class.

Copyright (c) 2026 Guennadi Maximov C. All Rights Reserved.
"""

__all__ = [
    "Comments",
    "generate_list_items",
    "get_extensions",
    "list_comments",
    "list_filetypes",
]

import json
import os
from os.path import exists, isdir, realpath

from colorama import Fore, Style
from colorama import init as color_init

from ..types import IndentMap
from ..util import die

_COMMENT_STR: str = "vim: set ts={ts} sts={sts} sw={sw} {et} ai si sta:"
_JSON_FILE: str = realpath("./vim_eof_comment/comments/filetypes.json")
_BLUE: int = Fore.BLUE
_YELLOW: int = Fore.YELLOW
_CYAN: int = Fore.CYAN
_BRIGHT: int = Style.BRIGHT
_RESET: int = Style.RESET_ALL
_BOLD: int = Style.BRIGHT


def import_json() -> tuple[dict[str, str], dict[str, IndentMap]]:
    """
    Import default vars from JSON file.

    Returns
    -------
    comments : dict[str, str]
        The default ``dict[str, str]``.
    map_dict : dict[str, IndentMap]
        The default indent mappings dict.
    """
    splitter: str = "/" if os.name != "nt" else "\\"
    split = __file__.split(splitter)
    length = len(split) - 1
    parent: str = splitter.join(split[:length])

    with open(parent + f"{splitter}filetypes.json", "r") as file:
        data: str = "".join(file.read().split("\n"))

    result: tuple[dict[str, str], dict[str, IndentMap]] = json.loads(data)
    comments = result[0]
    maps = result[1]

    for k, v in comments.items():
        comments[k] = v.format(comment=_COMMENT_STR)

    return comments, maps


class Comments:
    """
    Vim EOF comments class.

    Parameters
    ----------
    mappings : dict[str, IndentMap], optional, default=None
        The ``str`` to ``IndentMap`` dictionary.

    Attributes
    ----------
    __DEFAULT : dict[str, IndentMap]
        The default/fallback alternative to ``langs``.
    formats : dict[str, str]
        The default/fallback alternative to ``comments``.
    langs : dict[str, IndentMap]
        A dictionary of ``IndentMap`` type objects.
    comments : dict[str, str]
        A dictionary of file-extension-to-EOF-comment mappings.

    Methods
    -------
    __is_available(lang)
    __fill_langs(langs)
    get_defaults()
    get_ft()
    """

    __DEFAULT: dict[str, IndentMap]
    formats: dict[str, str]
    comments: dict[str, str]
    langs: dict[str, IndentMap]

    def __init__(self, mappings: dict[str, IndentMap] | None = None):
        """
        Create a new Vim EOF comment object.

        Parameters
        ----------
        mappings : dict[str, IndentMap], optional, default=None
            The ``str`` to ``IndentMap`` dictionary.
        """
        self.formats, self.__DEFAULT = import_json()

        if mappings is None or len(mappings) == 0:
            self.langs = self.__DEFAULT.copy()
            return

        langs: dict[str, IndentMap] = {}
        for lang, mapping in mappings.items():
            if not (self.__is_available(lang)) or len(mapping) == 0:
                continue

            indent, expandtab = mapping["level"], True
            if len(mapping) > 1:
                expandtab = mapping["expandtab"]

            langs[lang] = IndentMap(level=indent, expandtab=expandtab)

        self.__fill_langs(langs)

    def __is_available(self, lang: str) -> bool:
        """
        Check if a given lang is available within the class.

        Parameters
        ----------
        lang : str
            The file extension.

        Returns
        -------
        bool
            Represents whether the file extension has been included in the defaults.
        """
        return lang in self.__DEFAULT

    def __fill_langs(self, langs: dict[str, IndentMap]) -> None:
        """
        Fill languages dict.

        Parameters
        ----------
        langs : dict[str, IndentMap]
            A dictionary of ``IndentMap`` type objects.
        """
        if len(langs) == 0:
            self.langs = self.__DEFAULT.copy()
            return

        for lang, mapping in self.__DEFAULT.items():
            langs[lang] = langs.get(lang, mapping)

        self.langs = langs.copy()

    def get_defaults(self) -> dict[str, IndentMap]:
        """
        Retrieve the default comment dictionary.

        Returns
        -------
        dict[str, IndentMap]
            A dictionary of ``IndentMap`` type objects.
        """
        return self.__DEFAULT

    def generate(self) -> dict[str, str]:
        """
        Generate the comments list.

        Returns
        -------
        dict[str, str]
            The customly generated comments dictionary.
        """
        comments: dict[str, str] = {}
        for lang, fmt in self.formats.items():
            lvl, expandtab = self.langs[lang]["level"], self.langs[lang]["expandtab"]
            et, sw = "noet", 0

            if expandtab:
                et, sw = "et", lvl

            comments[lang] = fmt.format(ts=lvl, sts=lvl, sw=sw, et=et)

        self.comments: dict[str, str] = comments.copy()
        return self.comments

    def get_ft(self, ext: str) -> str | None:
        """
        Get the comment string by filetype (or None if it doesn't exist).

        Parameters
        ----------
        ext : str
            The file extension to be fetched.

        Returns
        -------
        str or None
            Either the file extension string, or if not available then ``None``.
        """
        comments: dict[str, str] = self.generate()
        return comments.get(ext, None)


def generate_list_items(ft: str, level: int, expandtab: str) -> str:
    """
    Generate a colored string for filetypes listing.

    Parameters
    ----------
    ft : str
        The filetype item in question.
    level : int
        Indent size.
    expandtab : str
        Either ``"Yes"`` or ``"No"``.

    Returns
    -------
    str
        The generated string.
    """
    txt = f"{_RESET}{_BRIGHT}{_BLUE}{ft}\n"
    txt += f"   {_RESET}{_BRIGHT}indent size{_RESET}{_BRIGHT} ==> {_CYAN}{level}\n"
    txt += f"   {_RESET}{_BRIGHT}expandtab{_RESET}{_BRIGHT} ==> {_CYAN}{expandtab}"

    return txt


def list_comments(exts: list[str]) -> None:
    """
    List the supported comments per-file extension, then stop command execution.

    Parameter can be an empty list, in which case all available comments will be printed.

    Parameters
    ----------
    exts : list[str]
        List of supported file extensions (can be empty).

    Raises
    ------
    ValueError
        Raised when a given extension is not supported.
    """
    color_init()

    formats: dict[str, str] = Comments().formats
    max_len: int = 0
    extensions: dict[str, str] = {}
    for ext, comment in formats.items():
        extensions[ext] = comment
        max_len = max(max_len, len(ext))

    fmt_exts: dict[str, tuple[str, str]] = {}
    for ext, comment in extensions.items():
        prefix = f"{_RESET}{_BOLD}{_BLUE}{ext}"
        suffix = (" " * (max_len - len(ext) + 2)) + f"{_RESET}"
        fmt_exts[ext] = (prefix + suffix, f"{_BOLD}{_YELLOW}{comment}{_RESET}")

    if len(exts) == 0:
        die(
            "\n".join([f"{extension[0]}==>  {extension[1]}" for extension in fmt_exts.values()]),
            code=0,
        )

    dedup_exts: list[str] = []
    for ext in exts:
        if ext not in fmt_exts:
            raise ValueError(f"`{ext}` is not supported!")

        if ext not in dedup_exts:
            dedup_exts.append(ext)

    data: list[str] = [f"{fmt_exts[ext][0]}==>  {fmt_exts[ext][1]}" for ext in dedup_exts]
    die("\n".join(data), code=0)


def get_extensions() -> list[str]:
    """
    Return the list of supported file extensions.

    Returns
    -------
    list[str]
        List of strings with all the available file extensions.
    """
    res: list[str] = [ext for ext in Comments().get_defaults()]
    return res


def list_filetypes() -> None:
    """List all available filetypes, then stop command execution."""
    color_init()

    defaults = Comments().get_defaults()
    items: dict[str, tuple[int, str]] = {}
    for ft_ext, indents in defaults.items():
        level: int = indents.get("level", 4)
        et = "Yes" if indents.get("expandtab") else "No"
        items[ft_ext] = (level, et)

    keys: list[str] = list(items.keys())
    keys.sort()

    sorted_items: dict[str, tuple[int, str]] = {i: items[i] for i in keys}

    txt = [generate_list_items(k, v[0], v[1]) for k, v in sorted_items.items()]
    die(*txt, code=0, sep="\n")


def export_json() -> None:
    """Export default vars to JSON."""
    if exists("./vim_eof_comment/comments") and isdir("./vim_eof_comment/comments"):
        try:
            data: str = json.dumps(import_json(), ensure_ascii=False)
        except KeyboardInterrupt:
            die(code=1)

        with open(_JSON_FILE, "w") as file_o:
            file_o.write(data + "\n")


# vim: set ts=4 sts=4 sw=4 et ai si sta:
