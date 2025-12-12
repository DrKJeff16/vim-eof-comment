# -*- coding: utf-8 -*-
# Copyright (c) 2025 Guennadi Maximov C. All Rights Reserved.
"""Coloured output for argparse ArgumentParser.

Copyright (c) 2025 Guennadi Maximov C. All Rights Reserved.
"""
import sys
from argparse import ArgumentParser
from gettext import gettext
from io import TextIOWrapper
from typing import Dict, NoReturn


class ColorArgParser(ArgumentParser):
    """
    Object for parsing command line strings into Python objects.

    Keyword Arguments
    -----------------
    - `prog` -- The name of the program (default: `os.path.basename(sys.argv[0])`)
    - `usage` -- A usage message (default: auto-generated from arguments)
    - `description` -- A description of what the program does
    - `epilog` -- Text following the argument descriptions
    - `parents` -- Parsers whose arguments should be copied into this one
    - `formatter_class` -- HelpFormatter class for printing help messages
    - `prefix_chars` -- Characters that prefix optional arguments
    - `fromfile_prefix_chars` -- Characters that prefix files containing additional arguments
    - `argument_default` -- The default value for all arguments
    - `conflict_handler` -- String indicating how to handle conflicts
    - `add_help` -- Add a -h/-help option
    - `allow_abbrev` -- Allow long options to be abbreviated unambiguously
    - `exit_on_error` -- Determines whether or not ArgumentParser exits
                         with error info when an error occurs
    """

    colors: Dict[str, str] = {
        "black": "1;30",
        "red": "1;31",
        "green": "1;32",
        "yellow": "1;33",
        "blue": "1;34",
        "magenta": "1;35",
        "cyan": "1;36",
        "grey": "1;37",

        "light_grey": "1;90",
        "light_red": "1;91",
        "light_green": "1;92",
        "light_yellow": "1;93",
        "light_blue": "1;94",
        "light_magenta": "1;95",
        "light_cyan": "1;96",
        "white": "1;97",
    }

    def print_usage(self, file=None):
        """Coloured argparse `print_usage()`."""
        if file is None:
            file = sys.stdout

        format = self.format_usage()
        self._print_message(format[0].upper() + format[1:], file=file, color=self.color["yellow"])

    def print_help(self, file=None):
        """Coloured argparse `print_help()`."""
        if file is None:
            file = sys.stdout

        format = self.format_help()
        self._print_message(format[0].upper() + format[1:], file=file, color=self.colors["blue"])

    def _print_message(
            self,
            *message,
            file: TextIOWrapper = sys.stderr,
            color: str | None = None
    ):
        """Print coloured help/usage."""
        if not message or len(message) == 0:
            return

        txt = "".join(message)
        if color is None:
            file.write(txt)
        else:
            file.write("\x1b[" + color + "m" + txt + "\x1b[0m\n")

    def exit(self, status: int = 0, message: str | None = None) -> NoReturn:
        """Print message and exit with given code."""
        if message and len(message) >= 1:
            file = sys.stdout if status == 0 else sys.stderr
            self._print_message(*message, file, self.colors["red"])

        sys.exit(status)

    def error(self, message: str) -> NoReturn:
        """Print error and then exit with error status."""
        self.print_usage(sys.stderr)
        self.exit(
            gettext("%(prog)s: Error: %(message)s\n") % {"prog": self.prog, "message": message},
            status=2
        )

# vim:ts=4:sts=4:sw=4:et:ai:si:sta:
