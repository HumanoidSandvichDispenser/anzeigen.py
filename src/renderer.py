#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 sandvich <sandvich@manjaro>
#
# Distributed under terms of the MIT license.

from pygments import highlight, util
from pygments.lexers import get_lexer_by_name, TextLexer
from pygments.formatters import TerminalFormatter, Terminal256Formatter, TerminalTrueColorFormatter
import inspect
import blessed
from tag import Tag
from character import Character
from header import Header
from emphatic import Emphatic
from code_block import CodeBlock

class Renderer:
    tokens: list[Tag] = None
    term: blessed.Terminal = None

    def __init__(self, tokens):
        self.term = blessed.Terminal()
        self.tokens = tokens

    def render(self, line: int):
        for token in self.tokens:
            if isinstance(token, Character):
                print(token.content, end = "")
            else:
                print() # Print blank line
                if isinstance(token, Header):
                    print(self.term.green_reverse(token.content), end = "")
                elif isinstance(token, CodeBlock):
                    lexer = TextLexer()
                    try:
                        lexer = get_lexer_by_name(token.language)
                    except util.ClassNotFound:
                        pass
                    formatter = TerminalFormatter()
                    print(highlight(token.content, lexer, formatter), end = "")
                """
                if token.emphatic_type in "*_":
                    if len(token.emphatic_type) == 1:
                        print(self.term.italic(token.content), end = "")
                    elif len(token.emphatic_type) == 2:
                        print(self.term.bold(token.content), end = "")
                """
