#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 sandvich <sandvich@manjaro>
#
# Distributed under terms of the GPLv3 license.

from char_iterator import CharIterator
from header import Header
from paragraph import Paragraph
from code_block import CodeBlock


class Lexer:
    source_content: str = ""

    def __init__(self, source_content: str):
        self.source_content = source_content

    def tokenize_blocks(self, chars: CharIterator):
        while chars.get_next() is not None:
            char: str = chars.move_next()
            if char.index == 0 or char == "\n":
                if char == "#":
                    (header, level) = self._get_header(chars)
                    yield Header(header, level)
                elif char == "`":
                    if chars.get_multi(2) == "``":
                        chars.move_next(2)
                        language = self._delimit("\n", chars)
                        yield CodeBlock(self._delimit_multi("\n```", chars),
                                        language)
                else:  # character not picked up by tokenizer
                    paragraph: str = char
                    while chars.get_next() is not None and chars.get_multi(
                            2) != "\n\n":
                        if chars.get_next() == "\n":
                            paragraph += " "
                        else:
                            paragraph += chars.move_next()
                    yield Paragraph(paragraph)
                 
    def tokenize_inline(self):  # TODO: implement
        raise NotImplementedError()

    def _delimit(self, delimiter: str, chars: CharIterator) -> str:
        value = ""
        while chars.get_next() != delimiter:
            next_char = chars.move_next()
            if next_char is None:
                raise Exception("Unexpected EOL")
            value += next_char
        chars.move_next()  # chars.get_next() == delimiter, skip the delimiter
        return value

    def _delimit_multi(self, delimiter: str, chars: CharIterator) -> str:
        value = ""
        while chars.get_multi(len(delimiter)) != delimiter:
            next_char = chars.move_next()
            if next_char is None:
                raise Exception("Unexpected EOL")
            value += next_char
        chars.move_next(len(delimiter))
        return value

    """
    @return Tuple (value: str, repeated_delimiter: str) of the delimited string
    """
    def _delimit_repeated(self, delimiter: str,
                          chars: CharIterator) -> (str, str):
        value = ""
        delimiter_count = 1
        while chars.get_next() == delimiter and delimiter_count < 3:
            delimiter_count += 1
            chars.move_next()

        while True:
            char: str = chars.get_next()
            if char == "\\":
                chars.move_next()
                value += chars.move_next()
            elif char != delimiter and char is not None:
                value += chars.move_next()
            elif char == delimiter:
                if chars.get_multi(delimiter_count + 1) == delimiter * delimiter_count:
                    chars.move_next(delimiter_count)
                    return (value, delimiter * delimiter_count)
                else:
                    value += chars.move_next()
            elif char is None:
                break
        return (value, delimiter * delimiter_count)


    """
    @return Tuple (value: str, level: int) of the header
    """
    def _get_header(self, chars: CharIterator) -> (str, int):
        value: str = ""
        level: int = 1
        found_whitespace: bool = False
        while chars.get_next() != "\n" and chars.get_next() is not None:
            next_char = chars.move_next()
            if next_char == "#":
                level += 1
            elif next_char == " " and not found_whitespace:
                found_whitespace = True
            elif found_whitespace:
                value += next_char
        return (value, level)

    def _reduce_newline(self, chars: CharIterator):
        while chars.get_next() == "\n":
            chars.move_next()
