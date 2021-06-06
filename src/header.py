#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 sandvich <sandvich@manjaro>
#
# Distributed under terms of the MIT license.

from tag import Tag

class Header(Tag):
    level: int = 0
    def __init__(self, content: str, level: int):
        self.level = level
        super().__init__(content)
