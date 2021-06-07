#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 sandvich <sandvich@manjaro>
#
# Distributed under terms of the MIT license.

class CommandParser:
    commands: dict = {
        down: 
    }

    keymaps: dict = {
        "j": "down",
        "k": "up"
        ":": "open_prompt"
    }

    repeat_command: string = ""

    def parse_command(self, char: str):
        if char in self.commands:
            pass
        elif char.isnumeric():
            repeat_command += char

