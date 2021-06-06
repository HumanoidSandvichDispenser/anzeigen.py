#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 sandvich <sandvich@manjaro>
#
# Distributed under terms of the MIT license.

import ueberzug
import blessed
import pygments
import click
import os
from lexer import Lexer
from char_iterator import CharIterator
from renderer import Renderer

@click.command()
@click.argument("filename")
@click.option("-c", "--cat", default = False)
# set default parameters in the function to silence missing arguments error
def main(filename: str = None, cat: bool = False):
    file = open(filename, "r")
    lex = Lexer(file.read())
    lex.measure_time = True
    tokens = list(lex.tokenize_blocks(CharIterator(lex.source_content)))
    renderer = Renderer(tokens)
    renderer.render(0)

if __name__ == "__main__":
    main()
