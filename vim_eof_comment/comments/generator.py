# -*- coding: utf-8 -*-
# Copyright (c) 2025 Guennadi Maximov C. All Rights Reserved.
"""
Per-filetype modeline comment class.

Copyright (c) 2025 Guennadi Maximov C. All Rights Reserved.
"""
__all__ = ["list_filetypes", "Comments"]

from typing import Dict, Iterator, List, NoReturn

from ..types import IndentMap
from ..util import die
from .types import GeneratedEOFComments, IndentMapDict

_formats: GeneratedEOFComments = GeneratedEOFComments(
    C="/* vim: set ts={ts} sts={sts} sw={sw} {et} ai si sta: */",
    H="/* vim: set ts={ts} sts={sts} sw={sw} {et} ai si sta: */",
    Makefile="# vim: set ts={ts} sts={sts} sw={sw} {et} ai si sta:",
    bash="# vim: set ts={ts} sts={sts} sw={sw} {et} ai si sta:",
    c="/* vim: set ts={ts} sts={sts} sw={sw} {et} ai si sta: */",
    cc="/* vim: set ts={ts} sts={sts} sw={sw} {et} ai si sta: */",
    cpp="/* vim: set ts={ts} sts={sts} sw={sw} {et} ai si sta: */",
    css="/* vim: set ts={ts} sts={sts} sw={sw} {et} ai si sta: */",
    fish="# vim: set ts={ts} sts={sts} sw={sw} {et} ai si sta:",
    h="/* vim: set ts={ts} sts={sts} sw={sw} {et} ai si sta: */",
    hh="/* vim: set ts={ts} sts={sts} sw={sw} {et} ai si sta: */",
    hpp="/* vim: set ts={ts} sts={sts} sw={sw} {et} ai si sta: */",
    htm="<!-- vim: set ts={ts} sts={sts} sw={sw} {et} ai si sta: -->",
    html="<!-- vim: set ts={ts} sts={sts} sw={sw} {et} ai si sta: -->",
    lua="-- vim: set ts={ts} sts={sts} sw={sw} {et} ai si sta:",
    markdown="<!-- vim: set ts={ts} sts={sts} sw={sw} {et} ai si sta: -->",
    md="<!-- vim: set ts={ts} sts={sts} sw={sw} {et} ai si sta: -->",
    mk="# vim: set ts={ts} sts={sts} sw={sw} {et} ai si sta:",
    py="# vim: set ts={ts} sts={sts} sw={sw} {et} ai si sta:",
    pyi="# vim: set ts={ts} sts={sts} sw={sw} {et} ai si sta:",
    sh="# vim: set ts={ts} sts={sts} sw={sw} {et} ai si sta:",
    xml="<!-- vim: set ts={ts} sts={sts} sw={sw} {et} ai si sta: -->",
    zsh="# vim: set ts={ts} sts={sts} sw={sw} {et} ai si sta:",
)

_DEFAULT: IndentMapDict = IndentMapDict(
    C=IndentMap(level=2, expandtab=True),
    H=IndentMap(level=2, expandtab=True),
    Makefile=IndentMap(level=4, expandtab=False),
    bash=IndentMap(level=4, expandtab=True),
    c=IndentMap(level=2, expandtab=True),
    cc=IndentMap(level=2, expandtab=True),
    cpp=IndentMap(level=2, expandtab=True),
    css=IndentMap(level=4, expandtab=True),
    fish=IndentMap(level=4, expandtab=True),
    h=IndentMap(level=2, expandtab=True),
    hh=IndentMap(level=2, expandtab=True),
    hpp=IndentMap(level=2, expandtab=True),
    htm=IndentMap(level=2, expandtab=True),
    html=IndentMap(level=2, expandtab=True),
    lua=IndentMap(level=4, expandtab=True),
    markdown=IndentMap(level=2, expandtab=True),
    md=IndentMap(level=2, expandtab=True),
    mk=IndentMap(level=4, expandtab=False),
    py=IndentMap(level=4, expandtab=True),
    pyi=IndentMap(level=4, expandtab=True),
    sh=IndentMap(level=4, expandtab=True),
    xml=IndentMap(level=2, expandtab=True),
    zsh=IndentMap(level=4, expandtab=True),
)


class Comments():
    """
    Vim EOF comments class.

    Parameters
    ----------
    mappings : IndentMapDict, optional, default=None
        The ``str`` to ``IndentMap`` dictionary.

    Attributes
    ----------
    __DEFAULT : IndentMapDict
        The default/fallback alternative to ``langs``.
    __formats : GeneratedEOFComments
        The default/fallback alternative to ``comments``.
    langs : IndentMapDict
        A dictionary of ``IndentMap`` type objects.
    comments : GeneratedEOFComments
        A dictionary of file-extension-to-EOF-comment mappings.

    Methods
    -------
    __is_available(lang)
    __fill_langs(langs)
    get_defaults()
    """

    __DEFAULT: IndentMapDict = _DEFAULT.copy()
    __formats: GeneratedEOFComments = _formats.copy()
    comments: GeneratedEOFComments
    langs: IndentMapDict

    def __init__(self, mappings: IndentMapDict | None = None):
        """
        Creates a new Vim EOF comment object.

        Parameters
        ----------
        mappings : IndentMapDict, optional, default=None
            The ``str`` to ``IndentMap`` dictionary.
        """
        if mappings is None or len(mappings) == 0:
            self.langs = self.__DEFAULT.copy()
            return

        langs = dict()
        for lang, mapping in mappings.items():
            if not (self.__is_available(lang)) or len(mapping) == 0:
                continue

            indent, expandtab = mapping["level"], True
            if len(mapping) > 1:
                expandtab = mapping["expandtab"]

            langs[lang] = {"level": indent, "expandtab": expandtab}

        self.__fill_langs(langs)

    def __iter__(self) -> Iterator[str]:
        """Iterate through comment langs."""
        for k, v in self.langs.items():
            yield (k, v)

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
        return lang in self.__DEFAULT.keys()

    def __fill_langs(self, langs: IndentMapDict) -> NoReturn:
        """
        Fill languages dict.

        Parameters
        ----------
        langs : IndentMapDict
            A dictionary of ``IndentMap`` type objects.
        """
        if len(langs) == 0:
            self.langs = self.__DEFAULT.copy()
            return

        for lang, mapping in self.__DEFAULT.items():
            langs[lang] = langs.get(lang, mapping)

        self.langs = IndentMapDict(**langs)

    def get_defaults(self) -> IndentMapDict:
        """
        Retrieve the default comment dictionary.

        Returns
        -------
        IndentMapDict
            A dictionary of ``IndentMap`` type objects.
        """
        return self.__DEFAULT

    def generate(self) -> GeneratedEOFComments:
        """
        Generate the comments list.

        Returns
        -------
        GeneratedEOFComments
            The customly generated comments dictionary.
        """
        comments: Dict[str, str] = dict()
        for lang, fmt in self.__formats.items():
            lvl, expandtab = self.langs[lang]["level"], self.langs[lang]["expandtab"]
            et, sw = "noet", 0

            if expandtab:
                et, sw = "et", lvl

            comments[lang] = fmt.format(ts=lvl, sts=lvl, sw=sw, et=et)

        self.comments: GeneratedEOFComments = GeneratedEOFComments(**comments)
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
        comments: GeneratedEOFComments = self.generate()
        return comments.get(ext, None)


def list_filetypes() -> NoReturn:
    """List all available filetypes."""
    txt: List[str] = [""]

    c: Comments = Comments()
    defaults: IndentMapDict = c.get_defaults()
    for ext, indents in defaults.items():
        txt.append(f"- {ext} - {indents}")

    die(*txt, code=0, sep="\n")

# vim: set ts=4 sts=4 sw=4 et ai si sta:
