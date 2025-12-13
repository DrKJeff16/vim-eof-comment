# -*- coding: utf-8 -*-
# Copyright (c) 2025 Guennadi Maximov C. All Rights Reserved.
"""Argparse utilities.

Copyright (c) 2025 Guennadi Maximov C. All Rights Reserved.
"""
from argparse import ArgumentError, ArgumentParser, Namespace
from sys import stdout as STDOUT
from typing import Any, Dict, List, Tuple

from ..util import die


def bootstrap_args(
        parser: ArgumentParser,
        specs: Tuple[Tuple[List[str], Dict[str, Any]]]
) -> Namespace:
    """Bootstraps the program arguments."""
    for spec in specs:
        parser.add_argument(*spec[0], **spec[1])

    try:
        namespace = parser.parse_args()
    except KeyboardInterrupt:
        die(code=130)
    except ArgumentError:
        parser.print_help(STDOUT)
        die(code=1)

    return namespace


def arg_parser_init() -> Tuple[ArgumentParser, Namespace]:
    """Generates the argparse namespace."""
    parser = ArgumentParser(
        prog="ensure_eof_comment.py",
        description="Checks for Vim EOF comments in all matching files in specific directories",
        exit_on_error=False
    )
    spec: Tuple[Tuple[List[str], Dict[str, Any]]] = (
        (
            ["directories"],
            {
                "nargs": "+",
                "help": "The target directories to be checked",
                "metavar": "/path/to/directory",
            },
        ),
        (
            ["-e", "--file-extensions"],
            {
                "required": True,
                "metavar": "EXT1[,EXT2[,EXT3[,...]]]",
                "help": "A comma-separated list of file extensions (e.g. \"lua,c,cpp,cc,c++\")",
                "dest": "exts",
            }
        ),
        (
            ["-n", "--newline"],
            {
                "required": False,
                "action": "store_true",
                "help": "Add newline before EOF comment",
                "dest": "newline",
            }
        ),
        (
            ["-i", "--indent-levels"],
            {
                "required": False,
                "metavar": "EXT1:INDENT1[:<Y|N>][,EXT2:INDENT2[:<Y|N>][,...]]",
                "help": """
                A comma-separated list of per-extension mappings
                (indent level and, optionally, a Y/N value to indicate if tabs are expanded).
                For example: "lua:4,py:4:Y,md:2:N"
                """,
                "default": "",
                "dest": "indent",
            },
        )
    )

    return parser, bootstrap_args(parser, spec)


def indent_handler(indent: str) -> List[Tuple[str, int, bool]]:
    """Parse indent levels defined by the user."""
    if indent == "":
        return list()

    indents: List[str] = indent.split(",")
    maps: List[Tuple[str, int, bool]] = list()
    for ind in indents:
        inds: List[str] = ind.split(":")
        if len(inds) <= 1:
            continue

        ext, ind_level, et = inds[0], int(inds[1]), True
        if len(inds) >= 3:
            if inds[2].upper() in ("Y", "N"):
                et = False if inds[2].upper() == "N" else True

        append = [ext, ind_level, et]
        maps.append(tuple(append))

    return maps

# vim:ts=4:sts=4:sw=4:et:ai:si:sta:
