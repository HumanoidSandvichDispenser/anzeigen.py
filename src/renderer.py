#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 sandvich <sandvich@manjaro>
#
# Distributed under terms of the GPLv3 license.

from pygments import highlight, util
from pygments.lexers import get_lexer_by_name, TextLexer
from pygments.formatters import TerminalFormatter
import blessed
import getch
from tag import Tag
from character import Character
from header import Header
from code_block import CodeBlock


class Renderer:
    tokens: list[Tag] = None
    term: blessed.Terminal = None
    prerendered_text: str = ""
    rendered_text: list[str] = []

    status_left: str = ""
    status_right: str = ""
    status_middle: str = ""

    def __init__(self, tokens):
        self.term = blessed.Terminal()
        self.tokens = tokens

    """
    Converts Markdown objects into renderable text
    """
    def prerender(self):
        for token in self.tokens:
            if isinstance(token, Character):
                self.prerendered_text += token.content
            else:
                self.prerendered_text += "\n"
                if isinstance(token, Header):
                    header_prefix = self.term.bold_black("#" * token.level)
                    header_title = self.term.bold_green(token.content)
                    self.prerendered_text += header_prefix + " " + header_title
                elif isinstance(token, CodeBlock):
                    lexer = TextLexer()
                    try:
                        lexer = get_lexer_by_name(token.language)
                    except util.ClassNotFound:
                        pass
                    formatter = TerminalFormatter()
                    self.prerendered_text += highlight(token.content, lexer,
                                                       formatter)

    """
    Handles text overflowing the terminal (either wrap or truncate)
    """
    def handle_overflow(self):
        self.rendered_text = self.term.wrap(self.prerendered_text)

    """
    Renders each visible line on the terminal
    """
    def render(self, top: int):
        print(self.term.clear, end="")
        renderable_text = self.rendered_text[top:top
                                             + self.term.height - 2]
        for line in renderable_text:
            print(line)
        with self.term.location(0, self.term.height - 1):
            print(self.status_left, end="")
            #print(self.term.center(self.status_middle), end="")
            print(self.term.rjust(self.status_right), end="")

    def getch(self):
        return getch.getch()
