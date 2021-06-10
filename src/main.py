#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 sandvich <sandvich@manjaro>
#
# Distributed under terms of the GPLv3 license.

from bs4 import BeautifulSoup
from markdown2 import Markdown
import click
from renderer import Renderer
from interface import Interface


@click.command()
@click.argument("filename")
@click.option("-c", "--cat", default=False)
# set default parameters in the function to silence missing arguments error
def main(filename: str = None, cat: bool = False):
    file = open(filename, "r")
    markdown = Markdown()
    html = markdown.convert(file.read())
    soup = BeautifulSoup(html, "html.parser")
    interface = Interface(Renderer(soup.contents))
    interface.start_loop()


if __name__ == "__main__":
    main()
