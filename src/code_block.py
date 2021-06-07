#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 sandvich <sandvich@manjaro>
#
# Distributed under terms of the GPLv3 license.

from element import Element


class CodeBlock(Element):
    language: str

    def __init__(self, language: str, inner: str):
        self.language = language
        self.inner = inner
