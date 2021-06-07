#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 sandvich <sandvich@manjaro>
#
# Distributed under terms of the MIT license.

class Element:
    inner_elements: list = []

    def __init__(self, *inner):
        self.inner_elements.append(inner)
