#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 sandvich <sandvich@manjaro>
#
# Distributed under terms of the MIT license.

from tag import Tag

class CodeBlock(Tag):
    language: str = ""
    def __init__(self, content: str, language: str):
        self.language = language
        super().__init__(content)
