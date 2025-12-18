# -*- coding: utf-8 -*-
# Copyright (c) 2025 Guennadi Maximov C. All Rights Reserved.
"""
Main entrypoint for `vim-eof-comment`.

Copyright (c) 2025 Guennadi Maximov C. All Rights Reserved.
"""
from sys import exit as Exit

from .eof import main

if __name__ == "__main__":
    Exit(main())

# vim: set ts=4 sts=4 sw=4 et ai si sta:
