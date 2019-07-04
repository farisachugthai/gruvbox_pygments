#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Vim: set fdm=marker:foldlevelstart=99:foldlevel=99:
"""A retro groove color scheme for Pygments.

As originally introduced as a Vim colorscheme. [1]

.. [1]https://github.com/morhetz/gruvbox

This pygments colorscheme can be used with any API that allows for Pygments
syntax highlighting. It has; however, been primarily tested with IPython.

"""
from pygments.style import Style
from pygments.token import (Token, Comment, Name, Keyword, Generic, Number,
                            Whitespace, Error, Punctuation, Operator, String,
                            Literal, Escape, Text)

# We're still exporting ALL these globals. Let's not.
__all__ = ['GruvboxStyle']

# Palette: {{{1
BG0_HARD = "#1d2021"

dark1 = '#3c3836'  # 60-56-54
DARK2 = '#504945'  # 80-73-69
DARK3 = '#665c54'  # 102-92-84
dark4 = '#7c6f64'  # 124-111-100

# Comments
GRAY_245 = '#928374'  # 146-131-116

LIGHT0_HARD = '#f9f5d7'  # 249-245-215
# light0 = '#fbf1c7'  # 253-244-193
# light0_soft = '#f2e5bc'  # 242-229-188
FG1 = '#ebdbb2'  # 235-219-178
FG2 = '#d5c4a1'  # 213-196-161
FG3 = '#bdae93'  # 189-174-147
LIGHT4 = '#a89984'  # 168-153-132

BRIGHT_RED = '#fb4934'  # 251-73-52
BRIGHT_GREEN = '#b8bb26'  # 184-187-38
BRIGHT_YELLOW = '#fabd2f'  # 250-189-47
BRIGHT_BLUE = '#83a598'  # 131-165-152
BRIGHT_PURPLE = '#d3869b'  # 211-134-155
BRIGHT_AQUA = '#8ec07c'  # 142-192-124
BRIGHT_ORANGE = '#fe8019'  # 254-128-25

NEUTRAL_RED = '#cc241d'  # 204-36-29
neutral_green = '#98971a'  # 152-151-26
NEUTRAL_YELLOW = '#d79921'  # 215-153-33
neutral_blue = '#458588'  # 69-133-136
NEUTRAL_PURPLE = '#b16286'  # 177-98-134
NEUTRAL_AQUA = '#689d6a'  # 104-157-106
NEUTRAL_ORANGE = '#d65d0e'  # 214-93-14

FADED_RED = '#9d0006'  # 157-0-6
FADED_GREEN = '#79740e'  # 121-116-14
FADED_YELLOW = '#b57614'  # 181-118-20
FADED_BLUE = '#076678'  # 7-102-120
FADED_PURPLE = '#8f3f71'  # 143-63-113
faded_aqua = '#427b58'  # 66-123-88
FADED_ORANGE = '#af3a03'  # 175-58-3

# }}}


class GruvboxStyle(Style):
    """Retro groove color scheme for Pygments.

    Extends previous repositories that have ported Gruvbox to Pygments, and
    adds in new definitions for different tokens.

    """

    default_style = ''

    background_color = BG0_HARD
    # highlight_color = SELECTION

    styles = {
        Comment: GRAY_245,  # class:'c'
        Comment.Hashbang: GRAY_245,  # class: 'ch'
        Comment.Multiline: NEUTRAL_YELLOW + ' italic',  # class: 'cm'
        # Comment.Preproc: BRIGHT_AQUA,  # class: 'cp'
        # Comment.PreprocFile: 'cpf',
        Comment.Singleline: GRAY_245 + ' italic',
        Escape: DARK3,  # class: 'Esc'
        Error: BRIGHT_RED + ' bold',  # class: 'Err'
        Generic: FG1,
        Generic.Deleted: LIGHT0_HARD,
        Generic.Emph: 'underline ' + BRIGHT_BLUE,
        Generic.Heading: BRIGHT_GREEN + ' bold',
        Generic.Inserted: LIGHT0_HARD,
        Generic.Output: FG2,
        Generic.Prompt: BRIGHT_BLUE,
        Generic.Strong: FG1 + ' bold',
        Generic.Subheading: BRIGHT_GREEN + ' bold',
        Keyword: BRIGHT_ORANGE,  # class: 'k'
        Keyword.Constant: FADED_ORANGE,  # class: 'kc'
        Keyword.Declaration: BRIGHT_ORANGE,  # class: 'kd'
        Keyword.Type: BRIGHT_YELLOW,  # class: 'kt'
        # Keyword.Namespace: 'kn',
        Keyword.Pseudo: NEUTRAL_PURPLE, # class: 'kp', the NumPy Lexer registers tokens as this class
        # Keyword.Reserved: 'kr',
        # Literal: BRIGHT_GREEN,  # class: 'l'
        # Literal.Date: 'ld',
        Literal.Number: BRIGHT_PURPLE,  # class: 'm',
        # Literal.Number.Bin: 'mb',
        # Literal.Number.Float: 'mf',
        # Literal.Number.Hex: 'mh',
        # Literal.Number.Integer: 'mi',
        # Literal.Number.Integer.Long: 'il',
        # Literal.Number.Oct: 'mo',
        Literal.String: BRIGHT_GREEN,  # class: 's'
        Literal.String.Other: BRIGHT_GREEN,  # class: 'sx'
        Literal.String.Affix: BRIGHT_ORANGE,  # class: 'sa',

        # Literally matches `.* lol
        Literal.String.Backtick: LIGHT4, # class: 'sb',
        # Literal.String.Char: 'sc',
        # Literal.String.Delimiter: 'dl',
        Literal.String.Doc: FG1,  # class: 'sd',
        # Literal.String.Double: 's2',
        # Literal.String.Escape: 'se',
        # Literal.String.Heredoc: 'sh',
        # Interpolated strings!
        Literal.String.Interpol: FADED_GREEN, # class 'si',
        Literal.String.Regex: BRIGHT_YELLOW,  # class: 'sr',
        # Literal.String.Single: 's1',
        Literal.String.Symbol: FG2,  # class: 'ss',
        Name: FG1,  # class: 'n'
        Name.Attribute: BRIGHT_GREEN,  # class: 'na'
        Name.Builtin: BRIGHT_YELLOW,  # class: 'nb'
        # Name.Builtin.Pseudo: 'bp',
        Name.Class: NEUTRAL_ORANGE,  # class: 'nc',
        Name.Constant: BRIGHT_PURPLE,  # class: 'no'
        Name.Decorator: BRIGHT_YELLOW,  # class: 'nd'
        Name.Entity: BRIGHT_YELLOW,  # class: 'ni'
        Name.Exception: 'bold ' + BRIGHT_RED,  # class: 'ne'

        Name.Function: 'noinherit ' + BRIGHT_YELLOW,  # class: 'nf'
        # dunder methods
        Name.Function.Magic: 'noinherit ' + NEUTRAL_AQUA,  # class: 'fm'
        Name.Label: BRIGHT_RED,  # class: 'nl'
        # import statements
        Name.Namespace: FADED_BLUE,  # class: 'nn',
        # Name.Other: 'nx',
        Name.Property: BRIGHT_AQUA,  # class: 'py'
        Name.Tag: BRIGHT_RED,  # class: 'nt'
        Name.Variable: FG1,  # class: 'nv'
        Name.Variable.Class: 'noinherit ' + BRIGHT_BLUE,  # class: 'vc'
        Name.Variable.Global: 'noinherit ' + BRIGHT_BLUE,  # class: 'vg'
        Name.Variable.Instance: 'noinherit ' + BRIGHT_BLUE,  # class:'vi'
        Name.Variable.Magic: 'noinherit ' + BRIGHT_BLUE,  # class: 'vm'
        Number.Float: BRIGHT_PURPLE,
        Number: BRIGHT_PURPLE,
        Operator: BRIGHT_RED,  # class: 'o'
        # Operator.Word: NEUTRAL_RED,  # class: 'ow'
        # really hard to read
        Operator.Word: 'noinherit ' + FADED_RED,
        Punctuation: FG1,  # class: 'p'
        String.Symbol: BRIGHT_BLUE,
        String: BRIGHT_GREEN,
        Text: FG1,  # class: 't'
        # treating this key as Vim's Identifier token.
        Text.Whitespace: 'underline ' + FADED_YELLOW,  # class: 'w'
    }

    def __init__(self, **kwargs):
        """Create the colorscheme object."""
        self.__dict__.update(kwargs)

    def __repr__(self):
        """Return repr representation."""
        keys = sorted(self.__dict__)
        items = ("{}={!r}".format(k, self.__dict__[k]) for k in keys)
        return "{!r}: ({!r})".format(type(self).__name__, ", ".join(items))

    def __eq__(self, other):
        """Check if style is the same as the other."""
        return self.__dict__ == other.__dict__
