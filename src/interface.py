#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 sandvich <sandvich@manjaro>
#
# Distributed under terms of the GPLv3 license.

import blessed
import signal
from renderer import Renderer


class Interface:
    commands: dict = None

    keymaps: dict = {
        "j": "down",
        "k": "up",
        "q": "quit",
        ":": "open_prompt",
        "\x1b": None,
    }

    repeat_command: str = ""
    prompt_open: bool = False
    prompt_text: str = ""

    renderer: Renderer = None
    term: blessed.Terminal = None
    stdscr = None

    line_number: int = 0

    def __init__(self, renderer: Renderer):
        self.commands = {
            "down": self.down,
            "up": self.up,
            "quit": self.quit,
            "open_prompt": self.open_prompt
        }

        self.renderer = renderer
        self.term = renderer.term
        renderer.prerender_tree(renderer.tags)

    def start_loop(self):
        def on_resize(*args):
            self.renderer.handle_overflow()
            self.renderer.render(self.line_number)
        self.renderer.handle_overflow()
        signal.signal(signal.SIGWINCH, on_resize)
        with self.term.hidden_cursor(), \
                self.term.raw(), \
                self.term.fullscreen():
            while True:
                self.renderer.render(self.line_number)
                self.handle_key(self.term.getch())

    def handle_key(self, char: str):
        if char == "\x03":
            exit(0)
        elif self.prompt_open:
            if char == "\r":
                self.parse_command(self.prompt_text)
                self.prompt_text = self.renderer.status_left = ""
                self.prompt_open = False
            else:
                self.prompt_text += char
                self.renderer.status_left = self.prompt_text
        elif char in self.keymaps:
            repeat_count = 1
            try:
                repeat_count = int(self.repeat_command)
            except ValueError:
                pass
            self.parse_command(self.keymaps[char], repeat_count)
            self.repeat_command = self.renderer.status_right = ""
        elif char.isnumeric():
            self.repeat_command += char
            self.renderer.status_right = self.repeat_command

    def parse_command(self, command: str, count: int = 1):
        if command in self.commands:
            self.commands[command](count)

    def open_prompt(self, count: int):
        self.prompt_open = True

    def quit(self, count: int):
        exit(0)

    def down(self, count: int):
        self.line_number = min(self.line_number + count,
                               len(self.renderer.rendered_text) - 1)

    def up(self, count: int):
        self.line_number = max(self.line_number - count, 0)
