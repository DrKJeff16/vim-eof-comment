# -*- coding: utf-8 -*-
# Copyright (c) 2025 Guennadi Maximov C. All Rights Reserved.
"""Usual comment structures per filetype.

Copyright (c) 2025 Guennadi Maximov C. All Rights Reserved.
"""
from typing import Dict, Iterator, NoReturn, Optional

from .types.typeddict import IndentMap

_formats: Dict[str, str] = {
    "C": "/// vim:ts={}:sts={}:sw={}:et:ai:si:sta:",
    "H": "/// vim:ts={}:sts={}:sw={}:et:ai:si:sta:",
    "bash": "# vim:ts={}:sts={}:sw={}:et:ai:si:sta:",
    "c": "/// vim:ts={}:sts={}:sw={}:et:ai:si:sta:",
    "cc": "/// vim:ts={}:sts={}:sw={}:et:ai:si:sta:",
    "cpp": "/// vim:ts={}:sts={}:sw={}:et:ai:si:sta:",
    "css": "/* vim:ts={}:sts={}:sw={}:et:ai:si:sta: */",
    "fish": "# vim:ts={}:sts={}:sw={}:et:ai:si:sta:",
    "h": "/// vim:ts={}:sts={}:sw={}:et:ai:si:sta:",
    "hh": "/// vim:ts={}:sts={}:sw={}:et:ai:si:sta:",
    "hpp": "/// vim:ts={}:sts={}:sw={}:et:ai:si:sta:",
    "htm": "<!--vim:ts={}:sts={}:sw={}:et:ai:si:sta:-->",
    "html": "<!--vim:ts={}:sts={}:sw={}:et:ai:si:sta:-->",
    "lua": "-- vim:ts={}:sts={}:sw={}:et:ai:si:sta:",
    "markdown": "<!--vim:ts={}:sts={}:sw={}:et:ai:si:sta:-->",
    "md": "<!--vim:ts={}:sts={}:sw={}:et:ai:si:sta:-->",
    "py": "# vim:ts={}:sts={}:sw={}:et:ai:si:sta:",
    "pyi": "# vim:ts={}:sts={}:sw={}:et:ai:si:sta:",
    "sh": "# vim:ts={}:sts={}:sw={}:et:ai:si:sta:",
    "xml": "<!--vim:ts={}:sts={}:sw={}:et:ai:si:sta:-->",
    "zsh": "# vim:ts={}:sts={}:sw={}:et:ai:si:sta:",
}

_DEFAULT: Dict[str, IndentMap] = {
    "C": {"level": 2, "expandtab": True},
    "H": {"level": 2, "expandtab": True},
    "bash": {"level": 4, "expandtab": True},
    "c": {"level": 2, "expandtab": True},
    "cc": {"level": 2, "expandtab": True},
    "cpp": {"level": 2, "expandtab": True},
    "css": {"level": 4, "expandtab": True},
    "fish": {"level": 4, "expandtab": True},
    "h": {"level": 2, "expandtab": True},
    "hh": {"level": 2, "expandtab": True},
    "hpp": {"level": 2, "expandtab": True},
    "htm": {"level": 2, "expandtab": True},
    "html": {"level": 2, "expandtab": True},
    "lua": {"level": 4, "expandtab": True},
    "markdown": {"level": 2, "expandtab": True},
    "md": {"level": 2, "expandtab": True},
    "py": {"level": 4, "expandtab": True},
    "pyi": {"level": 4, "expandtab": True},
    "sh": {"level": 4, "expandtab": True},
    "xml": {"level": 2, "expandtab": True},
    "zsh": {"level": 4, "expandtab": True},
}


class EOFCommentsError(Exception):
    """EOF Comments error type."""

    pass


class Comments():
    """Vim EOF comments class."""

    formats: Dict[str, str]
    langs: Dict[str, IndentMap]
    __DEFAULT: Dict[str, IndentMap] = _DEFAULT.copy()

    def __init__(self, mappings: Optional[Dict[str, IndentMap]] = _DEFAULT):
        """Creates a new Vim EOF comment object."""
        self.formats = _formats.copy()

        if len(mappings) == 0:
            self.langs = self.__DEFAULT.copy()
            return

        self.langs = dict()
        for lang, mapping in mappings.items():
            if not (self.__is_available(lang)):
                continue

            if len(mapping) == 0:
                continue

            indent, expandtab = mapping["level"], True
            if len(mapping) > 1:
                expandtab = mapping["expandtab"]

            self.langs[lang] = {"level": indent, "expandtab": expandtab}

        self.__fill_langs()

    def __iter__(self) -> Iterator[str]:
        """Iterate through comment langs."""
        for k, v in self.langs.items():
            yield (k, v)

    def __is_available(self, lang: str) -> bool:
        """Checks if a given lang is available within the class."""
        return lang in self.__DEFAULT.keys()

    def __fill_langs(self) -> NoReturn:
        """Fill languages dict."""
        if len(self.langs) == 0:
            self.langs = self.__DEFAULT.copy()
            return

        for lang, mapping in self.__DEFAULT.items():
            self.langs[lang] = self.langs.get(lang, mapping)

    def generate(self) -> Dict[str, str]:
        """Generate the comments list."""
        comments: Dict[str, str] = dict()
        for lang, fmt in self.formats.items():
            splitted = fmt.split(":")
            lvl, expandtab = self.langs[lang]["level"], self.langs[lang]["expandtab"]

            et = splitted.index("et")
            ts = splitted.index("ts={}")
            sts = splitted.index("sts={}")
            sw = splitted.index("sw={}")

            splitted[et] = "et" if expandtab else "noet"
            for idx in (ts, sts):
                splitted[idx] = splitted[idx].format(lvl)

            splitted[sw] = splitted[sw].format(lvl if splitted[et] == "et" else 0)

            comments[lang] = ":".join(splitted)

        return comments

# vim:ts=4:sts=4:sw=4:et:ai:si:sta:
