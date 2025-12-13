# -*- coding: utf-8 -*-
# Copyright (c) 2025 Guennadi Maximov C. All Rights Reserved.
"""Ensure EOF Vim comment in specific filetypes.

Copyright (c) 2025 Guennadi Maximov C. All Rights Reserved.
"""
from io import TextIOWrapper
from typing import Dict, NoReturn, Tuple

from .args.parsing import arg_parser_init, indent_handler
from .comments import Comments
from .file import bootstrap_paths, modify_file, open_batch_paths
from .util import die, gen_indent_maps


def get_last_line(file: TextIOWrapper) -> Tuple[str, bool]:
    """Returns the last line of a file."""
    data = file.read().split("\n")
    has_newline = False
    if len(data) == 1:
        result: str = data[0]
    elif len(data) >= 2:
        if len(data) >= 3:
            has_newline = data[-3] == ""

        result: str = data[-2]
    else:
        result = ""

    file.close()

    return result, has_newline


def eof_comment_search(
        files: Dict[str, Tuple[TextIOWrapper, str]],
        comments: Comments,
        newline: bool
) -> Dict[str, Tuple[Tuple[TextIOWrapper, bool], str, bool]]:
    """Searches through opened files."""
    result = dict()
    comment_map = comments.generate()
    for path, file in files.items():
        last_line, has_nwl = get_last_line(file[0])
        comment = comment_map[file[1]]
        if last_line != comment_map[file[1]] or (newline and not has_nwl):
            # FIXME: This tuple only applies to Lua files!
            bad_lines = ("-" + comment, comment.split(" "), "-" + "".join(comment.split(" ")))
            if last_line in bad_lines or (newline and not has_nwl):
                result[path] = ([open(path, "r"), True], file[1], has_nwl)
            else:
                result[path] = ([open(path, "a"), False], file[1], has_nwl)

    return result


def append_eof_comment(
        files: Dict[str, Tuple[Tuple[TextIOWrapper, bool], str, bool]],
        comments: Comments,
        newline: bool
) -> NoReturn:
    """Append EOF comment to files missing it."""
    comment_map = comments.generate()
    for path, file in files.items():
        needs_modify = file[0][1]
        file_obj = file[0][0]
        ext = file[1]
        has_nwl = file[2]

        txt = f"{comment_map[ext]}\n"

        if needs_modify:
            txt = modify_file(file_obj, comment_map, ext, newline, has_nwl)
            file[0][0] = open(path, "w")

        file[0][0].write(txt)
        file[0][0].close()


def main() -> int:
    """Execute main workflow."""
    parser, namespace = arg_parser_init()

    dirs: Tuple[str] = tuple(namespace.directories)
    exts: Tuple[str] = tuple(namespace.exts.split(","))
    newline: bool = namespace.newline
    indent = indent_handler(namespace.indent)

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
