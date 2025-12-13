# -*- coding: utf-8 -*-
# Copyright (c) 2025 Guennadi Maximov C. All Rights Reserved.
"""Usual comment structures per filetype.

Copyright (c) 2025 Guennadi Maximov C. All Rights Reserved.
"""
from typing import Dict, NoReturn, Tuple

formats: Dict[str, str] = {
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

_DEFAULT: Dict[str, Tuple[int, bool]] = {
    "C": (2, True),
    "H": (2, True),
    "bash": (4, True),
    "c": (2, True),
    "cc": (2, True),
    "cpp": (2, True),
    "css": (4, True),
    "fish": (4, True),
    "h": (2, True),
    "hh": (2, True),
    "hpp": (2, True),
    "htm": (2, True),
    "html": (2, True),
    "lua": (4, True),
    "markdown": (2, True),
    "md": (2, True),
    "py": (4, True),
    "pyi": (4, True),
    "sh": (4, True),
    "xml": (2, True),
    "zsh": (4, True),
}


class EOFCommentsError(Exception):
    """EOF Comments error type."""

    pass


class Comments():
    """Vim EOF comments class."""

    formats: Dict[str, str]
    langs: Dict[str, Tuple[int, bool]]

    _DEFAULT: Dict[str, Tuple[int, bool]] = _DEFAULT.copy()

    def __init__(self, mappings: Dict[str, Tuple[int, bool]] = _DEFAULT):
        """Creates a new Vim EOF comment object."""
        self.formats = formats.copy()

        if len(mappings) == 0:
            self.langs = self._DEFAULT.copy()
            return

        langs = dict()
        for lang, tup in mappings.items():
            if not (self.is_available(lang) and isinstance(tup, (tuple, list))):
                continue

            indent, expandtab = tup[0], True
            if len(tup) == 0:
                continue

            if len(tup) > 1:
                expandtab = tup[1]

            langs[lang] = (indent, expandtab)

        self.langs = langs.copy()

        self.fill_langs()

    def is_available(self, lang: str) -> bool:
        """Checks if a given lang is available within the class."""
        return lang in self._DEFAULT.keys()

    def fill_langs(self) -> NoReturn:
        """Fill languages dict."""
        if len(self.langs) == 0:
            self.langs = self._DEFAULT.copy()
            return

        for lang, tup in self._DEFAULT.items():
            self.langs[lang] = self.langs.get(lang, tup)

    def generate(self) -> Dict[str, str]:
        """Generate the comments list."""
        comments: Dict[str, str] = dict()
        for lang, fmt in self.formats.items():
            splitted = fmt.split(":")
            lvl, expandtab = self.langs[lang][0], self.langs[lang][1]

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
