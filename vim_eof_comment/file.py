# -*- coding: utf-8 -*-
# Copyright (c) 2025 Guennadi Maximov C. All Rights Reserved.
"""File management utilities.

Copyright (c) 2025 Guennadi Maximov C. All Rights Reserved.
"""
from io import TextIOWrapper
from os import walk
from os.path import isdir, join
from typing import Dict, List, Tuple

from .util import die, error


def bootstrap_paths(paths: Tuple[str], exts: Tuple[str]) -> Tuple[Tuple[str, str]]:
    """Bootstraps all the matching paths in current dir and below."""
    result = list()
    for path in paths:
        if not isdir(path):
            continue

        for root, dirs, files in walk(path):
            for file in files:
                for ext in exts:
                    if file.endswith(ext):
                        result.append((join(root, file), ext))

    return tuple(result)


def open_batch_paths(paths: Tuple[Tuple[str, str]]) -> Dict[str, Tuple[TextIOWrapper, str]]:
    """Return a list of TextIO objects given file path strings."""
    result = dict()
    for path in paths:
        try:
            result[path[0]] = (open(path[0], "r"), path[1])
        except KeyboardInterrupt:
            die("\nProgram interrupted!", code=1)  # Kills the program
        except FileNotFoundError:
            error(f"File `{path[0]}` is not available!")
        except Exception:
            error(f"Something went wrong while trying to open `{path[0]}`!")

    return result


def modify_file(
        file: TextIOWrapper,
        comments: List[str],
        ext: str,
        newline: bool,
        has_nwl: bool
) -> str:
    """Modifies a file containing a bad EOF comment."""
    data = file.read().split("\n")
    data[-2] = comments[ext]

    if newline and not has_nwl:
        data.insert(-2, "")  # Newline

    return "\n".join(data)

# vim:ts=4:sts=4:sw=4:et:ai:si:sta:
