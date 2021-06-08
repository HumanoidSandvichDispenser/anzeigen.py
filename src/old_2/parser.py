#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 sandvich <sandvich@manjaro>
#
# Distributed under terms of the GPLv3 license.

import re
from element import Element
from header import Header
from code_block import CodeBlock
from paragraph import Paragraph


class Parser():
    header_regex = r"^(#{1,6}) (.+)\n?"  # gm
    code_block_regex = r"```(.*?)\n([^`]*)\n```"  # sgm
    paragraph_regex = r"(.+)\n\n"  # sgm, match paragraphs last

    source_content: str = ""

    def __init__(self, source_content: str):
        self.source_content = source_content

    def parse_blocks(self):
        content = self.source_content
        for match in re.finditer(self.header_regex, content):
            yield Header(len(match.group(1)), match.group(2))
            content[:match.start()] + content[match.end():]  # remove match

        for match in re.finditer(self.code_block_regex, content):
            yield CodeBlock(match.group(1), match.group(2))
            content[:match.start()] + content[match.end():]

        for match in re.finditer(self.paragraph_regex, content):
            yield 
