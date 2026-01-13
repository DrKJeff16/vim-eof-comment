# -*- coding: utf-8 -*-
# Copyright (c) 2025 Guennadi Maximov C. All Rights Reserved.
"""
Custom vim-eof-comment versioning objects.

Copyright (c) 2025 Guennadi Maximov C. All Rights Reserved.
"""
__all__ = ["VersionInfo", "list_versions", "version_info", "version_print", "__version__"]

from typing import NoReturn

from .types import VersionInfo
from .util import die

version_info = VersionInfo([
    (0, 1, 1),
    (0, 1, 2),
    (0, 1, 3),
    (0, 1, 4),
    (0, 1, 5),
    (0, 1, 6),
    (0, 1, 7),
    (0, 1, 8),
    (0, 1, 9),
    (0, 1, 10),
    (0, 1, 11),
    (0, 1, 12),
    (0, 1, 13),
    (0, 1, 14),
    (0, 1, 15),
    (0, 1, 16),
    (0, 1, 17),
    (0, 1, 18),
    (0, 1, 19),
    (0, 1, 20),
    (0, 1, 21),
    (0, 1, 22),
    (0, 1, 23),
    (0, 1, 24),
    (0, 1, 25),
    (0, 1, 26),
    (0, 1, 27),
    (0, 1, 28),
    (0, 1, 29),
    (0, 1, 30),
    (0, 1, 31),
    (0, 1, 32),
    (0, 1, 33),
    (0, 1, 34),
    (0, 1, 35),
    (0, 1, 36),
    (0, 1, 37),
    (0, 1, 38),
    (0, 2, 0),
    (0, 2, 1),
    (0, 2, 2),
    (0, 2, 3),
    (0, 3, 0),
    (0, 3, 1),
    (0, 3, 2),
    (0, 3, 3),
    (0, 3, 4),
    (0, 3, 5),
    (0, 3, 6),
    (0, 3, 7),
    (0, 3, 8),
    (0, 3, 9),
    (0, 3, 10),
    (0, 3, 11),
    (0, 3, 12),
    (0, 3, 13),
    (0, 3, 14),
    (0, 3, 15),
    (0, 3, 16),
    (0, 3, 17),
    (0, 3, 18),
    (0, 3, 19),
    (0, 3, 20),
    (0, 3, 21),
    (0, 4, 0),
    (0, 4, 1),
    (0, 4, 2),
    (0, 5, 0),
    (0, 5, 1),
])

__version__: str = str(version_info)


def list_versions() -> NoReturn:
    """List all versions."""
    die(version_info.get_all_versions(), code=0)


def version_print(version: str) -> NoReturn:
    """
    Print project version, then exit.

    Parameters
    ----------
    version : str
        The version string.
    """
    die(f"vim-eof-comment-{version}", code=0)

# vim: set ts=4 sts=4 sw=4 et ai si sta:
