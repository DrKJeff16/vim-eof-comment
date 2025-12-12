# -*- coding: utf-8 -*-
# Copyright (c) 2025 Guennadi Maximov C. All Rights Reserved.
"""Argparse utilities.

Copyright (c) 2025 Guennadi Maximov C. All Rights Reserved.
"""
from argparse import ArgumentError, Namespace
from sys import stdout as STDOUT
from typing import Any, Dict, List, Tuple

from ..util import die
from .color import ColorArgParser


def bootstrap_args(
        parser: ColorArgParser,
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


def arg_parser_init() -> Tuple[ColorArgParser, Namespace]:
    """Generates the argparse namespace."""
    parser = ColorArgParser(
        prog="ensure_eof_comment.py",
        description="Checks for Vim EOF comments in all matching files in specific directories",
        exit_on_error=False
    )
    spec = [
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
    ]

    return parser, bootstrap_args(parser, spec)

# vim:ts=4:sts=4:sw=4:et:ai:si:sta:
