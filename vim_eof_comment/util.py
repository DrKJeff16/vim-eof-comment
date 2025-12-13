# -*- coding: utf-8 -*-
# Copyright (c) 2025 Guennadi Maximov C. All Rights Reserved.
"""EOF comments checker utilities.

Copyright (c) 2025 Guennadi Maximov C. All Rights Reserved.
"""
from sys import exit as Exit
from sys import stderr as STDERR
from typing import Dict, List, NoReturn, Tuple


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


def gen_indent_maps(
        maps: List[Tuple[str, int, bool]]
) -> Dict[str, Tuple[int] | Tuple[int, bool]] | None:
    """Generate a dictionary from the custom indent maps."""
    if len(maps) == 0:
        return None

    map_d: Dict[str, Tuple[int, bool]] = dict()
    for mapping in maps:
        mapping_len = len(mapping)
        if mapping_len <= 1:
            raise ValueError(f"One of the custom mappings is not formatted properly! (`{mapping}`)")

        if mapping[0] in map_d.keys():
            continue

        mapping_len = mapping_len if mapping_len <= 3 else 3
        map_d[mapping[0]] = (mapping[1], True) if mapping_len == 2 else (mapping[1], mapping[2])

    return map_d

# vim:ts=4:sts=4:sw=4:et:ai:si:sta:
