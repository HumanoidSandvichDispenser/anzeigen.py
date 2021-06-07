#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 sandvich <sandvich@manjaro>
#
# Distributed under terms of the MIT license.

import click
from lexer import Lexer
from char_iterator import CharIterator
from renderer import Renderer
from interface import Interface


@click.command()
@click.argument("filename")
@click.option("-c", "--cat", default=False)
# set default parameters in the function to silence missing arguments error
def main(filename: str = None, cat: bool = False):
    file = open(filename, "r")
    lex = Lexer(file.read())
    tokens = list(lex.tokenize_blocks(CharIterator(lex.source_content)))
    interface = Interface(Renderer(tokens))
    interface.start_loop()


if __name__ == "__main__":
    main()
