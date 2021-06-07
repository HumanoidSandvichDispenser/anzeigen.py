#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 sandvich <sandvich@manjaro>
#
# Distributed under terms of the GPLv3 license.

from dataclasses import dataclass


@dataclass
class Tag:
    content = ""

    def __init__(self, content):
        self.content = content
        pass
