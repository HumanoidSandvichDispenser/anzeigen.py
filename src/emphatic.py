#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 sandvich <sandvich@manjaro>
#
# Distributed under terms of the MIT license.

from tag import Tag
from character import Character

class Emphatic(Tag):
    emphatic_type: str = "*"
    content_children: list = None
    def __init__(self, content: all, emphatic_type: str):
        self.content_children = content
        self.emphatic_type = emphatic_type
