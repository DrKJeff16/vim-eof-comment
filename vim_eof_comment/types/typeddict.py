# -*- coding: utf-8 -*-
# Copyright (c) 2025 Guennadi Maximov C. All Rights Reserved.
"""Custom vim-eof-comment TypeDict objects.

Copyright (c) 2025 Guennadi Maximov C. All Rights Reserved.
"""
from io import TextIOWrapper
from typing import Any, Dict, List, TypedDict

ParserSpec = TypedDict("ParserSpec", {"opts": List[str], "kwargs": Dict[str, Any]})

CommentMap = TypedDict("CommentMap", {"level": int})

IndentMap = TypedDict("IndentMap", {"level": int, "expandtab": bool})

IndentHandler = TypedDict("IndentHandler", {"ext": str, "level": int, "expandtab": bool})

IOWrapperBool = TypedDict("IOWrapperBool", {"file": TextIOWrapper, "has_nwl": bool})
LineBool = TypedDict("LineBool", {"line": str, "has_nwl": bool})

BatchPathDict = TypedDict("BatchPathDict", {"file": TextIOWrapper, "ext": str})

BatchPairDict = TypedDict("BatchPairDict", {"fpath": str, "ext": str})

EOFCommentSearch = TypedDict("EOFCommentSearch", {
    "state": IOWrapperBool,
    "lang": str,
})

# vim:ts=4:sts=4:sw=4:et:ai:si:sta:
