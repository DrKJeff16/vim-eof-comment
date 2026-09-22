# Copyright (c) 2026 Guennadi Maximov C. All Rights Reserved.
"""
Main entrypoint for `vim-eof-comment`.

Copyright (c) 2026 Guennadi Maximov C. All Rights Reserved.
"""

import sys

from .args.parsing import arg_parser_init
from .core import main

if __name__ == "__main__":
    parser, args = arg_parser_init()
    sys.exit(main())

# vim: set ts=4 sts=4 sw=4 et ai si sta:
