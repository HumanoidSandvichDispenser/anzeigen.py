#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 sandvich <sandvich@sandvich-pc>
#
# Distributed under terms of the GPLv3 license.

import re
import emoji


def get_visible_length(text: str):
    text = strip_ansi(text)

    # emojis are double length
    emoji_count = 0
    for char in text:
        if char in emoji.UNICODE_EMOJI_ENGLISH:
            emoji_count += 1

    return len(text) + emoji_count

def strip_ansi(text: str):
    s = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])").sub("", text)
    return s
