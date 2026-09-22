# Copyright (c) 2026 Guennadi Maximov C. All Rights Reserved.
"""
EOF comments checker regex matching utilities.

Copyright (c) 2026 Guennadi Maximov C. All Rights Reserved.
"""

__all__ = ["matches"]

from re import Pattern, compile


def matches(s: str) -> bool:
    """
    Check if given string matches any of the given patterns.

    Parameters
    ----------
    s : str
        The string to be matched.

    Returns
    -------
    bool
        Whether the string matches the default regex.
    """
    pats: list[Pattern[str]] = [
        compile("vim:([a-zA-Z]+(=[a-zA-Z0-9_]*)?:)+"),
        compile("vim:\\sset(\\s[a-zA-Z]+(=[a-zA-Z0-9_]*)?)*\\s[a-zA-Z]+(=[a-zA-Z0-9_]*)?:"),
    ]
    for pattern in pats:
        if pattern.search(s) is not None:
            return True

    return False


# vim: set ts=4 sts=4 sw=4 et ai si sta:
