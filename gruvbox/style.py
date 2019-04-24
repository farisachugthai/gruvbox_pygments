# -*- coding: utf-8 -*-
"""Gruvbox for IPython.

Gruvbox Colorscheme
===================
A retro groove color scheme for Vim.
`<https://github.com/morhetz/gruvbox>`_

Definitely could consider creating a base class that inherits from Style.
Then come up with subclasses that implement the varying contrasts.

<<<<<<< Updated upstream
Define __repr__ and __str__?

Because the ``print(GruvboxStyle)`` thing doesn't give you a memory address which
is nice but it may as well.

04/14/2019:

In case you were wondering how to find all the pygment tokens in a more
consistent way, literally just viewing the ``styles`` attributes for the
:ref:`~gruvbox/style/GruvboxStyle` should be plenty.

.. source-code:: python

    >>> print(GruvboxStyle.styles)
    {Token.Comment.Preproc: 'noinherit #8ec07c',
    Token.Comment: '#928374 italic',
    Token.Generic.Deleted: 'noinherit #282828 bg:#fb4934',
    Token.Generic.Emph: '#83a598 underline',
    Token.Generic.Error: 'bg:#fb4934 bold',
    Token.Generic.Heading: '#b8bb26 bold',
    Token.Generic.Inserted: 'noinherit #282828 bg:#b8bb26',
    Token.Generic.Output: 'noinherit #504945',
    Token.Generic.Prompt: '#ebdbb2',
    Token.Generic.Strong: '#ebdbb2',
    Token.Generic.Subheading: '#b8bb26 bold',
    Token.Generic.Traceback: 'bg:#fb4934 bold',
    Token.Generic: '#ebdbb2',
    Token.Keyword.Type: 'noinherit #fabd2f',
    Token.Keyword: 'noinherit #fe8019',
    Token.Name.Attribute: '#b8bb26 bold',
    Token.Name.Builtin: '#fabd2f',
    Token.Name.Constant: 'noinherit #d3869b',
    Token.Name.Entity: 'noinherit #fabd2f',
    Token.Name.Exception: 'noinherit #fb4934',
    Token.Name.Function: '#fabd2f',
    Token.Name.Label: 'noinherit #fb4934',
    Token.Name.Tag: 'noinherit #fb4934',
    Token.Name.Variable: 'noinherit #ebdbb2',
    Token.Name: '#ebdbb2',
    Token.Literal.Number.Float: 'noinherit #d3869b',
    Token.Literal.Number: 'noinherit #d3869b',
    Token.Operator: '#fe8019',
    Token.Literal.String.Symbol: '#83a598',
    Token.Literal.String: 'noinherit #b8bb26',
    Token: 'noinherit #ebdbb2 bg:#282828',
    Token.Text: '',
    Token.Text.Whitespace: '',
    Token.Escape: '',
    Token.Error: '',
    Token.Other: '',
    Token.Keyword.Constant: '',
    Token.Keyword.Declaration: '',
    Token.Keyword.Namespace: '',
    Token.Keyword.Pseudo: '',
    Token.Keyword.Reserved: '',
    Token.Name.Builtin.Pseudo: '',
    Token.Name.Class: '',
    Token.Name.Decorator: '',
    Token.Name.Function.Magic: '',
    Token.Name.Property: '',
    Token.Name.Namespace: '',
    Token.Name.Other: '',
    Token.Name.Variable.Class: '',
    Token.Name.Variable.Global: '',
    Token.Name.Variable.Instance: '',
    Token.Name.Variable.Magic: '',
    Token.Literal: '',
    Token.Literal.Date: '',
    Token.Literal.String.Affix: '',
    Token.Literal.String.Backtick: '',
    Token.Literal.String.Char: '',
    Token.Literal.String.Delimiter: '',
    Token.Literal.String.Doc: '',
    Token.Literal.String.Double: '',
    Token.Literal.String.Escape: '',
    Token.Literal.String.Heredoc: '',
    Token.Literal.String.Interpol: '',
    Token.Literal.String.Other: '',
    Token.Literal.String.Regex: '',
    Token.Literal.String.Single: '',
    Token.Literal.Number.Bin: '',
    Token.Literal.Number.Hex: '',
    Token.Literal.Number.Integer: '',
    Token.Literal.Number.Integer.Long: '',
    Token.Literal.Number.Oct: '',
    Token.Operator.Word: '',
    Token.Punctuation: '',
    Token.Comment.Hashbang: '',
    Token.Comment.Multiline: '',
    Token.Comment.PreprocFile: '',
    Token.Comment.Single: '',
    Token.Comment.Special: ''}




"""
from pygments.style import Style
from pygments.token import (Token, Comment, Name, Keyword, Generic, Number,
                            Whitespace, Error, Punctuation, Operator, String,
                            Other, Literal)

# Palette: {{{1
BG0_HARD = "1d2021"
FG0 = "#ebdbb2"

dark1 = '#3c3836'  # 60-56-54
DARK2 = '#504945'  # 80-73-69
dark3 = '#665c54'  # 102-92-84
dark4 = '#7c6f64'  # 124-111-100

GRAY_245 = '#928374'  # 146-131-116
gray_244 = '#928374'  # 146-131-116

LIGHT0_HARD = '#f9f5d7'  # 249-245-215
light0 = '#fbf1c7'  # 253-244-193
light0_soft = '#f2e5bc'  # 242-229-188
light1 = '#ebdbb2'  # 235-219-178
light2 = '#d5c4a1'  # 213-196-161
light3 = '#bdae93'  # 189-174-147
light4 = '#a89984'  # 168-153-132
light4_256 = '#a89984'  # 168-153-132

BRIGHT_RED = '#fb4934'  # 251-73-52
BRIGHT_GREEN = '#b8bb26'  # 184-187-38
BRIGHT_YELLOW = '#fabd2f'  # 250-189-47
BRIGHT_BLUE = '#83a598'  # 131-165-152
BRIGHT_PURPLE = '#d3869b'  # 211-134-155
bright_aqua = '#8ec07c'  # 142-192-124
BRIGHT_ORANGE = '#fe8019'  # 254-128-25

NEUTRAL_RED = '#cc241d'  # 204-36-29
neutral_green = '#98971a'  # 152-151-26
neutral_yellow = '#d79921'  # 215-153-33
neutral_blue = '#458588'  # 69-133-136
neutral_purple = '#b16286'  # 177-98-134
neutral_aqua = '#689d6a'  # 104-157-106
NEUTRAL_ORANGE = '#d65d0e'  # 214-93-14

faded_red = '#9d0006'  # 157-0-6
faded_green = '#79740e'  # 121-116-14
FADED_YELLOW = '#b57614'  # 181-118-20
faded_blue = '#076678'  # 7-102-120
faded_purple = '#8f3f71'  # 143-63-113
faded_aqua = '#427b58'  # 66-123-88
FADED_ORANGE = '#af3a03'  # 175-58-3

# }}}


class GruvboxStyle(Style):
    """Retro groove color scheme for Vim by Github: @morhetz.

    Using this as an easy and clearly visible way to experiment with classes.
    Could I set the styles dict inside of a method then decorate that with
    ``@property`` to make accessing it easier?
    """

    default_style = ''

    background_color = BG0_HARD
    # highlight_color = SELECTION

    styles = {
        Comment.Multiline: 'italic #B5B5B5',  # not gruvbox
        Comment: 'italic ' + GRAY_245,
        Error: BRIGHT_RED,
        Generic.Deleted: LIGHT0_HARD,
        Generic.Emph: 'underline ' + BRIGHT_BLUE,
        Generic.Heading: BRIGHT_GREEN + ' bold',
        Generic.Inserted: LIGHT0_HARD,
        Generic.Output: DARK2,
        Generic.Prompt: BRIGHT_BLUE,
        Generic.Strong: FG0 + ' bold',
        Generic.Subheading: BRIGHT_GREEN + ' bold',
        Generic: FG0,
        Keyword.Type: BRIGHT_YELLOW,
        Keyword: BRIGHT_ORANGE,
        Keyword.Constant: FADED_ORANGE,
        Keyword.Declaration: BRIGHT_ORANGE,
        Literal: NEUTRAL_ORANGE,  # class: 'l'
        Name.Attribute: BRIGHT_GREEN,
        Name.Builtin: BRIGHT_YELLOW,
        Name.Constant: BRIGHT_PURPLE,
        Name.Entity: BRIGHT_YELLOW,
        Name.Exception: 'bold ' + BRIGHT_RED,
        Name.Function: BRIGHT_YELLOW,
        Name.Label: BRIGHT_RED,
        Name.Tag: BRIGHT_RED,
        Name.Variable: FG0,
        Name: FG0,
        Number.Float: BRIGHT_PURPLE,
        Number: BRIGHT_PURPLE,
        Operator: BRIGHT_ORANGE,
        Operator.Word: NEUTRAL_RED,
        Punctuation: FG0,
        String.Symbol: BRIGHT_BLUE,
        String: BRIGHT_GREEN,
        Token: FG0,
        Whitespace: 'underline ' + FADED_YELLOW,
    }

    def __str__(self):
        return self.styles.values()
