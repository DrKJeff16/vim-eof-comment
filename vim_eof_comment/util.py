# -*- coding: utf-8 -*-
# Copyright (c) 2025 Guennadi Maximov C. All Rights Reserved.
"""EOF comments checker utilities.

Copyright (c) 2025 Guennadi Maximov C. All Rights Reserved.
"""
from sys import exit as Exit
from sys import stderr as STDERR
from typing import NoReturn


def error(*msg, end: str = "\n", sep: str = " ", flush: bool = False) -> NoReturn:
    """Prints to stderr."""
    try:
        end = str(end)
    except KeyboardInterrupt:
        Exit(1)
    except Exception:
        end = "\n"

    try:
        sep = str(sep)
    except KeyboardInterrupt:
        Exit(1)
    except Exception:
        sep = " "

    try:
        flush = bool(flush)
    except KeyboardInterrupt:
        Exit(1)
    except Exception:
        flush = False

    print(*msg, end=end, sep=sep, flush=flush, file=STDERR)


def die(*msg, code: int = 0, end: str = "\n", sep: str = " ", flush: bool = False) -> NoReturn:
    """Kill program execution."""
    try:
        code = int(code)
    except Exception:
        code = 1

    try:
        end = str(end)
    except Exception:
        end = "\n"
        code = 1

    try:
        sep = str(sep)
    except Exception:
        sep = " "
        code = 1

    try:
        flush = bool(flush)
    except Exception:
        flush = False
        code = 1

    if msg and len(msg) > 0:
        if code == 0:
            print(*msg, end=end, sep=sep, flush=flush)
        else:
            error(*msg, end=end, sep=sep, flush=flush)

    Exit(code)

# vim:ts=4:sts=4:sw=4:et:ai:si:sta:
