from io import TextIOWrapper
from typing import Any
from typing_extensions import TypedDict

class ParserSpec(TypedDict):
    opts: list[str]
    kwargs: dict[str, Any]

class CommentMap(TypedDict):
    level: int

class IndentMap(TypedDict):
    level: int
    expandtab: bool

class IndentHandler(TypedDict):
    ext: str
    level: int
    expandtab: bool

class IOWrapperBool(TypedDict):
    file: TextIOWrapper
    has_nwl: bool

class LineBool(TypedDict):
    line: str
    has_nwl: bool

class BatchPathDict(TypedDict):
    file: TextIOWrapper
    ext: str

class BatchPairDict(TypedDict):
    fpath: str
    ext: str

class EOFCommentSearch(TypedDict):
    state: IOWrapperBool
    lang: str
# vim:ts=4:sts=4:sw=4:et:ai:si:sta:
