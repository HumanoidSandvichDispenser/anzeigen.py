#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 sandvich <sandvich@manjaro>
#
# Distributed under terms of the GPLv3 license.

from element import Element


class Header(Element):
    level: int = 1

    def __init__(self, level: int, inner: str):
        self.level = level
        self.inner = inner
