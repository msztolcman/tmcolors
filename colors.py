# Copyright (c) 2012 Giorgos Verigakis <verigak@gmail.com>
#               2015 Marcin Sztolcman <marcin@urzenia.net>
#
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Derived from https://github.com/verigak/colors

from __future__ import print_function

import re

from functools import partial

__version__ = '0.1.0'

COLORS = ('black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white')
STYLES = ('bold', 'faint', 'italic', 'underline', 'blink', 'blink2', 'negative', 'concealed', 'crossed')


def color(fg=None, bg=None, style=None):
    sgr = []

    if fg:
        if fg in COLORS:
            sgr.append(str(30 + COLORS.index(fg)))
        elif isinstance(fg, int) and 0 <= fg <= 255:
            sgr.append('38;5;%d' % int(fg))
        else:
            raise Exception('Invalid color "%s"' % fg)

    if bg:
        if bg in COLORS:
            sgr.append(str(40 + COLORS.index(bg)))
        elif isinstance(bg, int) and 0 <= bg <= 255:
            sgr.append('48;5;%d' % bg)
        else:
            raise Exception('Invalid color "%s"' % bg)

    if style:
        for st in style.split('+'):
            if st in STYLES:
                sgr.append(str(1 + STYLES.index(st)))
            else:
                raise Exception('Invalid style "%s"' % st)

    if sgr:
        prefix = '\x1b[' + ';'.join(sgr) + 'm'
        return prefix
    else:
        return ''


def reset():
    suffix = '\x1b[0m'
    return suffix


def colorize(msg, fg=None, bg=None, style=None):
    prefix = color(fg, bg, style)

    if not prefix:
        return msg

    return prefix + msg + reset()


def strip_color(s):
    return re.sub('\x1b\[.+?m', '', s)


def cprint(msg, fg=None, bg=None, style=None, **kwargs):
    print(colorize(msg, fg=fg, bg=bg, style=style, **kwargs))


black = partial(colorize, fg='black')
red = partial(colorize, fg='red')
green = partial(colorize, fg='green')
yellow = partial(colorize, fg='yellow')
blue = partial(colorize, fg='blue')
magenta = partial(colorize, fg='magenta')
cyan = partial(colorize, fg='cyan')
white = partial(colorize, fg='white')

bold = partial(colorize, style='bold')
faint = partial(colorize, style='faint')
italic = partial(colorize, style='italic')
underline = partial(colorize, style='underline')
blink = partial(colorize, style='blink')
blink2 = partial(colorize, style='blink2')
negative = partial(colorize, style='negative')
concealed = partial(colorize, style='concealed')
crossed = partial(colorize, style='crossed')
