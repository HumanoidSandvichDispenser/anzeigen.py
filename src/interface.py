#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 sandvich <sandvich@manjaro>
#
# Distributed under terms of the MIT license.

from renderer import Renderer


class Interface:
    commands: dict = None

    keymaps: dict = {
        "j": "down",
        "k": "up",
        ":": "open_prompt",
        "\x1b": None,
    }

    repeat_command: str = ""
    prompt_open: bool = False
    prompt_text: str = ""

    renderer: Renderer = None

    line_number: int = 0

    def __init__(self, renderer: Renderer):
        self.commands = {
            "down": self.down,
            "up": self.up
        }

        self.renderer = renderer
        renderer.prerender()

    def start_loop(self):
        self.renderer.handle_overflow()
        while True:
            self.renderer.render(self.line_number)
            self.handle_key(self.renderer.getch())

    def handle_key(self, char: str):
        if self.prompt_open:
            if char == "\n":
                self.parse_command(self.prompt_text)
                self.prompt_text = self.renderer.status_left = ""
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

    def parse_command(self, command: str, repeat_count: int = 1):
        for i in range(repeat_count):
            if command in self.commands:
                self.commands[command]()

    def open_prompt(self):
        self.prompt_open = True

    def down(self):
        if self.line_number < len(self.renderer.rendered_text) - 1:
            self.line_number += 1
            self.renderer.status_middle = str(self.line_number + 1)

    def up(self):
        if self.line_number > 0:
            self.line_number -= 1
            self.renderer.status_middle = str(self.line_number + 1)
