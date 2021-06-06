#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 sandvich <sandvich@manjaro>
#
# Distributed under terms of the MIT license.

from lexer import Lexer
from char_iterator import CharIterator

lexer = Lexer()
char_iterator = CharIterator("**hello *world**")
char_iterator.index = 0
lexer._delimit_repeated("**", char_iterator)
