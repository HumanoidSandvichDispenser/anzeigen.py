#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 sandvich <sandvich@manjaro>
#
# Distributed under terms of the MIT license.

class CharIterator:
    index: int = -1
    content: str = ""

    def __init__(self, content):
        self.content = content

    def get_next(self, count: int = 1) -> str:
        if self.index >= len(self.content) - count or self.index < -1:
            return None
        else:
            return self.content[self.index + count]

    def get_multi(self, count: int = 1) -> str:
        if self.index >= len(self.content) - count or self.index < -1:
            return None
        else:
            return self.content[self.index + 1 : self.index + 1 + count]

    def move_next(self, count: int = 1) -> str:
        self.index += count
        if self.index >= len(self.content) or self.index < 0:
            return None
        else:
            return self.content[self.index]
