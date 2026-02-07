# -*- coding: utf-8 -*-
# Copyright (c) 2025 Guennadi Maximov C. All Rights Reserved.
"""
Ensure EOF Vim comments.

Copyright (c) 2025 Guennadi Maximov C. All Rights Reserved.
"""

__all__ = [
    "BatchPairDict",
    "BatchPathDict",
    "CommentMap",
    "EOFCommentSearch",
    "IndentHandler",
    "IndentMap",
    "LineBool",
    "ParserSpec",
    "VersionInfo",
    "__version__",
    "append_eof_comment",
    "args",
    "comments",
    "eof_comment_search",
    "file",
    "main",
    "regex",
    "util",
    "version",
]

from . import args, comments, file, regex, util, version
from .main import append_eof_comment, eof_comment_search, main
from .types import (BatchPairDict, BatchPathDict, CommentMap, EOFCommentSearch, IndentHandler,
                    IndentMap, LineBool, ParserSpec, VersionInfo)
from .version import __version__

# vim: set ts=4 sts=4 sw=4 et ai si sta:
