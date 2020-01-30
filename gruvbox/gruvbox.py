#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Vim: set fdm=marker:foldlevelstart=99:foldlevel=99:
"""A retro groove color scheme for Pygments.

As originally introduced as a Vim colorscheme. [1]

.. [1]https://github.com/morhetz/gruvbox

This pygments colorscheme can be used with any API that allows for
Pygments syntax highlighting. It has; however, been primarily tested
with :mod:`IPython`.

"""
import reprlib

from pygments.style import Style
from pygments.token import (
    Comment,
    Error,
    Escape,
    Generic,
    Keyword,
    Literal,
    Name,
    Number,
    Operator,
    Other,
    Punctuation,
    String,
    Text,
    Token,
    Whitespace,
)

try:
    from IPython.core.getipython import get_ipython
except ImportError:
    shell = None
else:
    shell = get_ipython()

from pygments.lexers.python import PythonLexer   # noqa

__all__ = ["Gruvbox"]


class Gruvbox(Style):
    """Creates a Gruvbox pygments class with a few amenities builtin."""

    BACKGROUND = "#1d2021"
    CURRENT_LINE = "#ebdbb2"
    SELECTION = "#7c6f54"
    FOREGROUND = "#ebdbb2"
    COMMENT = "#928374"

    BRIGHT_RED = "#fb4934"
    RED = "#cc241d"
    ORANGE = "#fe8019"
    YELLOW = "#fabd2f"
    GREEN = "#b8bb26"
    AQUA = "#83a598"
    BLUE = "#458588"
    PURPLE = "#d3869b"

    default_style = FOREGROUND

    background_color = BACKGROUND
    highlight_color = SELECTION

    styles = {
        Comment: COMMENT,  # class: 'c'
        Comment.Hashbang: COMMENT,
        Comment.Multiline: "noinherit " + GREEN,  # class: 'cm'
        # cython's IF DEF etc
        Comment.Preproc: "noinherit " + AQUA,  # class: 'cp'
        Comment.Single: "noinherit " + GREEN,  # class: 'c1'
        # Comment.Special: "",  # class: 'cs'

        # `:hi pythonEscape`
        Escape: ORANGE,
        Error: "border:" + BRIGHT_RED,  # class: 'err'
        Generic: FOREGROUND,  # class: 'g'
        Generic.Deleted: "noinherit " + BRIGHT_RED,  # class: 'gd',
        Generic.Emphasis: "italic ",  # class: 'ge'
        Generic.Error: BRIGHT_RED,  # class: 'gr'
        Generic.Heading: "bold " + FOREGROUND,  # class: 'gh'
        Generic.Inserted: "noinherit " + GREEN,  # class: 'gi'
        Generic.Output: "italic ",  # class: 'go'
        Generic.Prompt: "bold " + COMMENT,  # class: 'gp'
        Generic.Strong: "bold ",  # class: 'gs'
        Generic.Subheading: "bold " + AQUA,  # class: 'gu'
        # This is the text before the traceback
        Generic.Traceback: FOREGROUND,  # class: 'gt'

        # Note: In Pygments, Token.String is an alias for Token.Literal.String,
        #       and Token.Number as an alias for Token.Literal.Number.
        Literal: BLUE,  # class: 'l'
        Literal.Date: "noinherit " + GREEN,  # class: 'ld'

        Literal.Number               : PURPLE,  # class      : 'm'
        Literal.Number.Bin: PURPLE,
        Literal.Number.Float         : PURPLE,  # class      : 'mf'
        Literal.Number.Hex           : PURPLE,  # class      : 'mh'
        Literal.Number.Integer       : PURPLE,  # class      : 'mi'
        Literal.Number.Integer.Long  : PURPLE,  # class      : 'il'
        Literal.Number.Oct           : PURPLE,  # class      : 'mo'

        # basically the foundation of everything
        Keyword: ORANGE,  # class: 'k'

        # True, False, None. `:hi pythonBoolean` is Purple
        Keyword.Constant: "noinherit " + PURPLE,  # class: 'kc'
        # Keyword.Declaration: "",  # class: 'kd'
        # from <---- x import y
        Keyword.Namespace: "noinherit " + BLUE,  # class: 'kn'

        Keyword.Pseudo: "italic " + ORANGE,  # class: 'kp'
        # Keyword.Reserved: "",  # class: 'kr'
        Keyword.Type: "noinherit " + YELLOW,  # class: 'kt'

        Name: "noinherit " + FOREGROUND,  # class: 'n'
        Name.Attribute: "noinherit " + BLUE,  # class: 'na'

        # Builtin functions like max, zip, min
        Name.Builtin: "noinherit " + YELLOW,  # class: 'nb'
        # raise None <---
        Name.Builtin.Pseudo: "noinherit " + ORANGE,  # class: 'bp'
        # Matches Name.Function. Unfortunately not
        # ---> class FooBar:
        Name.Class: "noinherit " + GREEN,  # class: 'nc'
        Name.Constant: "noinherit " + BRIGHT_RED,  # class: 'no'
        # Only the @ in a decorator
        Name.Decorator: "noinherit " + BRIGHT_RED,  # class: 'nd'
        Name.Entity: "",  # class: 'ni'
        Name.Exception: "noinherit " + PURPLE,  # class: 'ne'
        Name.Function: "noinherit " + GREEN,  # class: 'nf'
        # Dunders
        Name.Function.Magic: "noinherit " + AQUA,
        Name.Label: "",  # class: 'nl'
        # import mod <----
        Name.Namespace: FOREGROUND,  # class: 'nn'
        Name.Other: BLUE,  # class: 'nx'
        Name.Property: "",  # class: 'py'
        Name.Tag: AQUA,  # class: 'nt'
        Name.Variable: BRIGHT_RED,  # class: 'nv'
        Name.Variable.Class: "noinherit bold " + BLUE,  # class: 'vc'
        Name.Variable.Global: "",  # class: 'vg'
        # Instance dunders
        Name.Variable.Magic: "noinherit " + AQUA,
        Name.Variable.Instance: "",  # class: 'vi'

        Operator: GREEN,  # class: 'o'
        Operator.Word: ORANGE,  # class: 'ow'
        # Can be the text in a traceback
        Other: FOREGROUND,  # class 'x'

        Punctuation: FOREGROUND,  # class: 'p'

        String: GREEN,  # class: 's'
        String.Affix: GREEN + " underline",
        String.Backtick: GREEN,  # class: 'sb'
        String.Char: FOREGROUND,  # class: 'sc'
        String.Doc: GREEN,  # class: 'sd'
        String.Double: GREEN,  # class: 's2'
        String.Escape: "noinherit " + ORANGE,  # class: 'se'
        String.Heredoc: "",  # class: 'sh'
        # the old style '%s' % (...) string formatting
        String.Interpol: "noinherit " + ORANGE,  # class: 'si'
        String.Other: "",  # class: 'sx'
        String.Regex: "",  # class: 'sr'
        String.Single: GREEN,  # class: 's1'
        String.Symbol: "",  # class: 'ss'
        # No corresponding class for the following:
        Text: FOREGROUND,  # class:  ''
        Text.Whitespace: BRIGHT_RED,  # class: 'w'
        Token: FOREGROUND,
    }

    style_rules = styles

    def __repr__(self):
        return reprlib.Repr().repr_dict(self.styles, 30)
