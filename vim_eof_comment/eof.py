# -*- coding: utf-8 -*-
# Copyright (c) 2025 Guennadi Maximov C. All Rights Reserved.
"""Ensure EOF Vim comment in specific filetypes.

Copyright (c) 2025 Guennadi Maximov C. All Rights Reserved.
"""
from io import TextIOWrapper
from typing import Dict, List, NoReturn, Tuple

from .args.parsing import arg_parser_init, indent_handler
from .comments import Comments
from .file import bootstrap_paths, modify_file, open_batch_paths
from .types.typeddict import (BatchPathDict, EOFCommentSearch, IndentHandler,
                              IOWrapperBool, LineBool)
from .util import die, gen_indent_maps


def get_last_line(file: TextIOWrapper) -> LineBool:
    """Returns the last line of a file."""
    data = file.read().split("\n")
    has_newline = False
    if len(data) == 1:
        line: str = data[0]
    elif len(data) >= 2:
        if len(data) >= 3:
            has_newline = data[-3] == ""

        line: str = data[-2]
    else:
        line = ""

    file.close()

    return LineBool(line=line, has_nwl=has_newline)


def eof_comment_search(
        files: Dict[str, BatchPathDict],
        comments: Comments,
        newline: bool
) -> Dict[str, EOFCommentSearch]:
    """Searches through opened files."""
    result = dict()
    comment_map = comments.generate()
    for path, file in files.items():
        file_obj, ext = file["file"], file["ext"]

        wrapper = get_last_line(file_obj)
        last_line, has_nwl = wrapper["line"], wrapper["has_nwl"]

        comment = comment_map[ext]
        if last_line != comment_map[ext]:
            # FIXME: This tuple only applies to Lua files!
            bad_lines = ("-" + comment, comment.split(" "), "-" + "".join(comment.split(" ")))
            if last_line in bad_lines or (newline and not has_nwl):
                state = IOWrapperBool(file=open(path, "r"), has_nwl=True)
            else:
                state = IOWrapperBool(file=open(path, "a"), has_nwl=False)

            result[path] = EOFCommentSearch(state=state, lang=ext)

    return result


def append_eof_comment(
        files: Dict[str, EOFCommentSearch],
        comments: Comments,
        newline: bool
) -> NoReturn:
    """Append EOF comment to files missing it."""
    comment_map = comments.generate()
    for path, file in files.items():
        has_nwl, file_obj, ext = file["state"]["has_nwl"], file["state"]["file"], file["lang"]

        txt = f"{comment_map[ext]}\n"
        if has_nwl:
            txt = modify_file(file_obj, comment_map, ext, newline, has_nwl)
            file["state"]["file"] = open(path, "w")

        file["state"]["file"].write(txt)
        file["state"]["file"].close()


def main() -> int:
    """Execute main workflow."""
    parser, namespace = arg_parser_init()

    dirs: Tuple[str] = tuple(namespace.directories)
    exts: Tuple[str] = tuple(namespace.exts.split(","))
    newline: bool = namespace.newline
    indent: List[IndentHandler] = indent_handler(namespace.indent)

    indent = gen_indent_maps(indent.copy())

    if indent is None:
        comments = Comments()
    else:
        comments = Comments(indent)

    files = open_batch_paths(bootstrap_paths(dirs, exts))
    if len(files) == 0:
        die("No matching files found!", code=1)

    results = eof_comment_search(files, comments, newline)
    if len(results) > 0:
        append_eof_comment(results, comments, newline)

    return 0

# vim:ts=4:sts=4:sw=4:et:ai:si:sta:
