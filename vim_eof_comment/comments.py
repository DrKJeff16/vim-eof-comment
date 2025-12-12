# -*- coding: utf-8 -*-
# Copyright (c) 2025 Guennadi Maximov C. All Rights Reserved.
"""Usual comment structures per filetype.

Copyright (c) 2025 Guennadi Maximov C. All Rights Reserved.
"""
from collections import OrderedDict
from typing import Dict, List, NoReturn, Optional, Tuple

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
    "htm": "<!--\nvim:ts={}:sts={}:sw={}:et:ai:si:sta:\n-->",
    "html": "<!--\nvim:ts={}:sts={}:sw={}:et:ai:si:sta:\n-->",
    "lua": "-- vim:ts={}:sts={}:sw={}:et:ai:si:sta:",
    "markdown": "<!--\nvim:ts={}:sts={}:sw={}:et:ai:si:sta:\n-->",
    "md": "<!--\nvim:ts={}:sts={}:sw={}:et:ai:si:sta:\n-->",
    "py": "# vim:ts={}:sts={}:sw={}:et:ai:si:sta:",
    "pyi": "# vim:ts={}:sts={}:sw={}:et:ai:si:sta:",
    "sh": "# vim:ts={}:sts={}:sw={}:et:ai:si:sta:",
    "xml": "<!--\nvim:ts={}:sts={}:sw={}:et:ai:si:sta:\n-->",
    "zsh": "# vim:ts={}:sts={}:sw={}:et:ai:si:sta:",
}


class EOFCommentsError(Exception):
    """EOF Comments error type."""

    pass


class Comments():
    """Vim EOF comments class."""

    formats: OrderedDict[str, str]
    langs: OrderedDict[str, Tuple[int, bool]]

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

    def __init__(self, **kwargs: Dict[str, Tuple[int, Optional[bool]]]):
        """Creates a new Vim EOF comment object."""
        self.formats = OrderedDict(sorted(formats.items()))

        if len(kwargs) == 0:
            self.langs = OrderedDict(sorted(self._DEFAULT.items()))
            return

        langs = dict()
        for lang, tup in kwargs.items():
            if not (self.is_available(lang) and isinstance(tup, (tuple, list))):
                continue

            expandtab = True
            if len(tup) == 0:
                continue
            if len(tup) > 1:
                expandtab = tup[1]

            indent = tup[0]

            langs[lang] = (indent, expandtab)

        self.langs = OrderedDict(sorted(langs.items()))

    def is_available(self, lang: str) -> bool:
        """Checks if a given lang is available within the class."""
        return lang in self._DEFAULT.keys()

    def fill_langs(self) -> NoReturn:
        """Fill languages dict."""
        if len(self.langs) == 0:
            self.langs = OrderedDict(sorted(self._DEFAULT.items()))
            return

        for lang, tup in self._DEFAULT.items():
            self.langs[lang] = self.langs.get(lang, tup)

    def generate(self) -> Dict[str, str]:
        """Generate the comments list."""
        self.fill_langs()

        comments: Dict[str, str] = dict()
        for fmt, tup in zip(self.formats.values(), self.langs.items()):
            splitted: List[str] = fmt.split(":")
            et = splitted.index("et")
            ts = splitted.index("ts={}")
            sts = splitted.index("sts={}")
            sw = splitted.index("sw={}")

            splitted[et] = "et" if tup[1][1] else "noet"
            for idx in (ts, sts):
                splitted[idx] = splitted[idx].format(tup[1][0])

            splitted[sw] = splitted[sw].format(tup[1][0] if splitted[et] == "et" else 0)

            comments[tup[0]] = ":".join(splitted)

        return comments

# vim:ts=4:sts=4:sw=4:et:ai:si:sta:
