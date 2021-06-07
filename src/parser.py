#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 sandvich <sandvich@manjaro>
#
# Distributed under terms of the MIT license.

class Parser():
    header_regex = r"^(#{1,6}) (.+)"  # gm
    paragraph_regex = r"(.+)\n\n"  # sgm
    code_block_regex = r"```(.*?)\n([^`]*)\n```"  # sgm

    content: str = ""
    source_content: str = ""

    def __init__(self, source_content: str):
        self.source_content = source_content

