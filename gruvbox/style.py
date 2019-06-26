#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Vim: set fdm=marker:
"""A retro groove color scheme for Pygments.

As originally introduced as a Vim colorscheme. [1]

.. [1]https://github.com/morhetz/gruvbox

This pygments colorscheme can be used with any API that allows for Pygments
syntax highlighting. It has; however, been primarily tested with IPython.

.. todo::

    Get the rest of them in here.
    CSS names too please.

     Token.Text.Whitespace: 'w',
     Token.Other: 'x',
     Token.Keyword: 'k',
     Token.Keyword.Constant: 'kc',
     Token.Keyword.Declaration: 'kd',
     Token.Keyword.Namespace: 'kn',
     Token.Keyword.Pseudo: 'kp',
     Token.Keyword.Reserved: 'kr',
     Token.Keyword.Type: 'kt',
     Token.Name: 'n',
     Token.Name.Attribute: 'na',
     Token.Name.Builtin: 'nb',
     Token.Name.Builtin.Pseudo: 'bp',
     Token.Name.Class: 'nc',
     Token.Name.Constant: 'no',
     Token.Name.Decorator: 'nd',
     Token.Name.Entity: 'ni',
     Token.Name.Exception: 'ne',
     Token.Name.Function: 'nf',
     Token.Name.Function.Magic: 'fm',
     Token.Name.Property: 'py',
     Token.Name.Label: 'nl',
     Token.Name.Namespace: 'nn',
     Token.Name.Other: 'nx',
     Token.Name.Tag: 'nt',
     Token.Name.Variable: 'nv',
     Token.Name.Variable.Class: 'vc',
     Token.Name.Variable.Global: 'vg',
     Token.Name.Variable.Instance: 'vi',
     Token.Name.Variable.Magic: 'vm',
     Token.Literal: 'l',
     Token.Literal.Date: 'ld',
     Token.Literal.String: 's',
     Token.Literal.String.Affix: 'sa',
     Token.Literal.String.Backtick: 'sb',
     Token.Literal.String.Char: 'sc',
     Token.Literal.String.Delimiter: 'dl',
     Token.Literal.String.Doc: 'sd',
     Token.Literal.String.Double: 's2',
     Token.Literal.String.Escape: 'se',
     Token.Literal.String.Heredoc: 'sh',
     Token.Literal.String.Interpol: 'si',
     Token.Literal.String.Other: 'sx',
     Token.Literal.String.Regex: 'sr',
     Token.Literal.String.Single: 's1',
     Token.Literal.String.Symbol: 'ss',
     Token.Literal.Number: 'm',
     Token.Literal.Number.Bin: 'mb',
     Token.Literal.Number.Float: 'mf',
     Token.Literal.Number.Hex: 'mh',
     Token.Literal.Number.Integer: 'mi',
     Token.Literal.Number.Integer.Long: 'il',
     Token.Literal.Number.Oct: 'mo',
     Token.Operator: 'o',
     Token.Operator.Word: 'ow',
     Token.Punctuation: 'p',
     Token.Comment: 'c',
     Token.Comment.Hashbang: 'ch',
     Token.Comment.Multiline: 'cm',
     Token.Comment.Preproc: 'cp',
     Token.Comment.PreprocFile: 'cpf',

"""
from pygments.style import Style
from pygments.token import (Token, Comment, Name, Keyword, Generic,
                            Number,
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

# GRAY_245 = '#928374'  # 146-131-116

LIGHT0_HARD = '#f9f5d7'  # 249-245-215
# light0 = '#fbf1c7'  # 253-244-193
# light0_soft = '#f2e5bc'  # 242-229-188
FG1 = '#ebdbb2'  # 235-219-178
FG2 = '#d5c4a1'  # 213-196-161
FG3 = '#bdae93'  # 189-174-147
light4 = '#a89984'  # 168-153-132
light4_256 = '#a89984'  # 168-153-132

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
neutral_purple = '#b16286'  # 177-98-134
neutral_aqua = '#689d6a'  # 104-157-106
NEUTRAL_ORANGE = '#d65d0e'  # 214-93-14

faded_red = '#9d0006'  # 157-0-6
faded_green = '#79740e'  # 121-116-14
FADED_YELLOW = '#b57614'  # 181-118-20
faded_blue = '#076678'  # 7-102-120
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
        Comment: FG3,  # 'c'
        # Comment.Hashbang  # ch
        Comment.Multiline: NEUTRAL_YELLOW + ' italic',  # cm
        Comment.Preproc: BRIGHT_AQUA,
        Comment.Singleline: FG3 + ' italic',
        Escape: DARK3,  # esc
        Error: BRIGHT_RED + ' bold',  # err
        Generic.Deleted: LIGHT0_HARD,
        Generic.Emph: 'underline ' + BRIGHT_BLUE,
        Generic.Heading: BRIGHT_GREEN + ' bold',
        Generic.Inserted: LIGHT0_HARD,
        Generic.Output: FG2,
        Generic.Prompt: BRIGHT_BLUE,
        Generic.Strong: FG1 + ' bold',
        Generic.Subheading: BRIGHT_GREEN + ' bold',
        Generic: FG1,
        Keyword.Type: BRIGHT_YELLOW,
        # not gonna lie I'm not a huge fan of this one
        # hi Keyword ctermfg=203 ctermbg=NONE guifg=#fb4934 guibg=NONE
        # guisp=NONE cterm=NONE gui=NONE
        # Keyword: NEUTRAL_RED,
        Keyword: BRIGHT_RED,
        Keyword.Constant: FADED_ORANGE,
        Keyword.Declaration: BRIGHT_ORANGE,
        Literal: BRIGHT_GREEN,  # class: 'l'
        Literal.String: BRIGHT_GREEN,  # class:
        Literal.String.Other: BRIGHT_GREEN,  # sx
        Literal.Number: FADED_PURPLE,
        Name.Attribute: BRIGHT_GREEN,
        Name.Builtin: BRIGHT_YELLOW,
        Name.Constant: BRIGHT_PURPLE,
        Name.Decorator: BRIGHT_YELLOW,
        Name.Entity: BRIGHT_YELLOW,
        Name.Exception: 'bold ' + BRIGHT_RED,
        Name.Function: BRIGHT_YELLOW,  # nf
        # Name.Function.Magic:  # fm
        Name.Label: BRIGHT_RED,
        Name.Tag: BRIGHT_RED,
        Name.Variable: FG1,
        Name: FG1,
        Number.Float: BRIGHT_PURPLE,
        Number: BRIGHT_PURPLE,
        Operator: BRIGHT_ORANGE,
        Operator.Word: NEUTRAL_RED,
        Name.Property: BRIGHT_AQUA,
        Punctuation: FG1,  # p
        String.Symbol: BRIGHT_BLUE,
        String: BRIGHT_GREEN,
        Text: FG1,
        Text.Whitespace: FG1,
        # treating this key as Vim's Identifier token.
        Name.Variable.Class: BRIGHT_BLUE,  # vc
        Name.Variable.Global: BRIGHT_BLUE,  # vg
        Name.Variable.Instance: BRIGHT_BLUE,  # vi
        Name.Variable.Magic: BRIGHT_BLUE,  # vm
        Whitespace: 'underline ' + FADED_YELLOW,
    }

    def __init__(self, **kwargs):
        """Create the colorscheme object."""
        self.__dict__.update(kwargs)

    def __repr__(self):
        """Return repr representation."""
        keys = sorted(self.__dict__)
        items = ("{}={!r}".format(k, self.__dict__[k]) for k in keys)
        return "{}({})".format(type(self).__name__, ", ".join(items))

    def __eq__(self, other):
        """Check if style is the same as the other."""
        return self.__dict__ == other.__dict__
