#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 sandvich <sandvich@manjaro>
#
# Distributed under terms of the GPLv3 license.

from pygments import highlight, util
from pygments.lexers import get_lexer_for_filename, TextLexer
from pygments.formatters import TerminalFormatter
from bs4 import NavigableString, Tag
import blessed
import re


class Renderer:
    tags: list = None
    term: blessed.Terminal = None
    prerendered_text: str = ""
    rendered_text: list[str] = []

    status_left: str = ""
    status_right: str = ""
    status_middle: str = ""

    document_margin_top: int = 0
    document_margin_bot: int = 1

    def __init__(self, tags):
        self.term = blessed.Terminal()
        self.tags = tags

    """
    Converts Markdown objects into renderable text
    """
    def prerender_tree(self, tags, line_prefix: str = ""):
        for tag in tags:
            name = tag.name
            if name is not None:  # check if none for invalid/blank tags
                self.prerendered_text += line_prefix
            if match := re.match(r"h([1-6])", str(name)):
                header_prefix = self.term.bold_black("#" * int(match.group(1)))
                header_title = self.term.bold_green(tag.contents[0])
                self.prerendered_text += ("\n" + header_prefix + " "
                                          + header_title + "\n\n")
            elif name == "p":
                self.prerender_par_tree(tag.contents, 0, self.term.normal)
            elif name == "blockquote":
                self.prerender_tree(tag.contents, "!blockquote")
            if name is not None:
                # add line break since it is at block level
                self.prerendered_text += "\n"

    def prerender_par_tree(self, children, level: int = 0, *attr: tuple):
        for content in children:
            if isinstance(content, NavigableString):
                # apply attributes at current level,
                # append the content string,
                # and apply previous attributes (from previous level)
                self.prerendered_text += "".join(attr) + str(
                        content.string) + "".join(attr[:-1])
            elif isinstance(content, Tag):
                if content.name == "strong":
                    self.prerender_par_tree(content.contents, level + 1, *attr,
                                            self.term.bold)
                elif content.name == "em":
                    self.prerender_par_tree(content.contents, level + 1, *attr,
                                            self.term.italic)
                elif content.name == "code":
                    # inline codeblocks do not have line breaks
                    if str(content).find("\n") == -1:
                        self.prerender_par_tree(content.contents, level + 1,
                                                *attr, self.term.on_gray10)
                    else:
                        self.prerender_code(content.contents)

    def prerender_code(self, children):
        for content in children:
            if isinstance(content, NavigableString):
                content_str = str(content.string)
                code_str = ""
                extension = ""
                lexer = TextLexer()
                try:
                    code_split_by_line = content_str.split("\n")
                    # extension is always the first line
                    extension = code_split_by_line[0]
                    if len(code_split_by_line) > 1:
                        code_str = "\n".join(code_split_by_line[1:])
                    lexer = get_lexer_for_filename("file." + extension)
                except util.ClassNotFound:
                    pass
                formatter = TerminalFormatter()
                self.prerendered_text += "[{0}]\n{1}".format(
                        self.term.gray40(extension),
                        highlight(code_str, lexer, formatter))

    """
    Handles text overflowing the terminal (either wrap or truncate)
    """
    def handle_overflow(self):
        self.rendered_text.clear()
        for line in self.prerendered_text.split("\n"):
            prefix = ""
            while line.startswith("!blockquote"):
                prefix += self.term.blue("▌ ")
                line = line[11:]
            self.rendered_text.extend(self.term.wrap(line,
                                      initial_indent=prefix,
                                      subsequent_indent=prefix))

    """
    Renders each visible line on the terminal
    """
    def render(self, top: int):
        print(self.term.clear, end="")
        renderable_text = self.rendered_text[top:top
                                             + self.term.height - 2]
        for line in renderable_text:
            print(line, end="\r\n")
        with self.term.location(0, self.term.height - 1):
            print(self.status_left, end="")
            print(self.term.rjust(self.status_right), end="")
