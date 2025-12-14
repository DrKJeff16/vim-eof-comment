# -*- coding: utf-8 -*-
# Copyright (c) 2025 Guennadi Maximov C. All Rights Reserved.
"""File management utilities.

Copyright (c) 2025 Guennadi Maximov C. All Rights Reserved.
"""
from io import TextIOWrapper
from os import walk
from os.path import isdir, join
from typing import Dict, List, Tuple

from .types.typeddict import BatchPairDict, BatchPathDict
from .util import die, error


def bootstrap_paths(paths: Tuple[str], exts: Tuple[str]) -> List[BatchPairDict]:
    """Bootstraps all the matching paths in current dir and below."""
    result = list()
    for path in paths:
        if not isdir(path):
            continue

        file: str
        for root, dirs, files in walk(path):
            for file in files:
                for ext in exts:
                    if not file.endswith(ext):
                        continue

                    result.append(BatchPairDict(fpath=join(root, file), ext=ext))

    return result


def open_batch_paths(paths: List[BatchPairDict]) -> Dict[str, BatchPathDict]:
    """Return a list of TextIO objects given file path strings."""
    result = dict()
    for path in paths:
        fpath, ext = path["fpath"], path["ext"]
        try:
            result[fpath] = {"file": open(fpath, "r"), "ext": ext}
        except KeyboardInterrupt:
            die("\nProgram interrupted!", code=1)  # Kills the program
        except FileNotFoundError:
            error(f"File `{fpath}` is not available!")
        except Exception:
            error(f"Something went wrong while trying to open `{fpath}`!")

    return result


def modify_file(
        file: TextIOWrapper,
        comments: Dict[str, str],
        ext: str,
        newline: bool,
        has_nwl: bool
) -> str:
    """Modifies a file containing a bad EOF comment."""
    data: List[str] = file.read().split("\n")
    data_len = len(data)
    if data_len == 0:
        data = [comments[ext], ""]
    elif data_len == 1:
        data.insert(0, comments[ext])
    elif data_len >= 2:
        data.insert(-1, comments[ext])

    if newline and not has_nwl:
        data.insert(-2, "")  # Newline

    return "\n".join(data)

# vim:ts=4:sts=4:sw=4:et:ai:si:sta:
