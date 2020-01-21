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

    default_style = ""

    background_color = BACKGROUND
    highlight_color = SELECTION

    styles = {
        # No corresponding class for the following:
        Text: FOREGROUND,  # class:  ''
        Text.Whitespace: RED,  # class: 'w'
        # `:hi pythonEscape`
        Escape: ORANGE,
        Error: "border:" + RED,  # class: 'err'
        # Other: "",  # class 'x'
        Comment: COMMENT,  # class: 'c'
        # Comment.Multiline: "",  # class: 'cm'
        # Comment.Preproc: "",  # class: 'cp'
        # Comment.Single: "",  # class: 'c1'
        # Comment.Special: "",  # class: 'cs'
        Keyword: RED,  # class: 'k'
        # Keyword.Constant: "",  # class: 'kc'
        # Keyword.Declaration: "",  # class: 'kd'
        Keyword.Namespace: "noinherit " + AQUA,  # class: 'kn'
        Keyword.Pseudo: ORANGE,  # class: 'kp'
        # Keyword.Reserved: "",  # class: 'kr'
        Keyword.Type: "noinherit " + YELLOW,  # class: 'kt'
        Operator: ORANGE,  # class: 'o'
        # Operator.Word: "",  # class: 'ow'
        Punctuation: FOREGROUND,  # class: 'p'
        Name: "noinherit " + FOREGROUND,  # class: 'n'
        Name.Attribute: "noinherit " + BLUE,  # class: 'na'
        Name.Builtin: "noinherit " + YELLOW,  # class: 'nb'
        # raise None <---
        Name.Builtin.Pseudo: ORANGE,  # class: 'bp'
        Name.Class: "noinherit " + RED,  # class: 'nc'
        Name.Constant: "noinherit " + RED,  # class: 'no'
        Name.Decorator: "noinherit " + RED,  # class: 'nd'
        Name.Entity: "",  # class: 'ni'
        Name.Exception: "noinherit " + RED,  # class: 'ne'
        Name.Function: "noinherit " + GREEN,  # class: 'nf'
        Name.Property: "",  # class: 'py'
        Name.Label: "",  # class: 'nl'
        # I think might be imports. check pygments.lexers.python
        Name.Namespace: BLUE,  # class: 'nn'
        Name.Other: BLUE,  # class: 'nx'
        Name.Tag: AQUA,  # class: 'nt'
        Name.Variable: RED,  # class: 'nv'
        Name.Variable.Class: "",  # class: 'vc'
        Name.Variable.Global: "",  # class: 'vg'
        Name.Variable.Instance: "",  # class: 'vi'

        Number              : PURPLE,  # class : 'm'
        Number.Float        : PURPLE,  # class : 'mf'
        Number.Hex          : PURPLE,  # class : 'mh'
        Number.Integer      : PURPLE,  # class : 'mi'
        Number.Integer.Long : PURPLE,  # class : 'il'
        Number.Oct          : PURPLE,  # class : 'mo'

        Literal: BLUE,  # class: 'l'
        Literal.Date: "noinherit " + GREEN,  # class: 'ld'

        Literal.Number               : PURPLE,  # class      : 'm'
        Literal.Number.Bin: PURPLE,
        Literal.Number.Float         : PURPLE,  # class      : 'mf'
        Literal.Number.Hex           : PURPLE,  # class      : 'mh'
        Literal.Number.Integer       : PURPLE,  # class      : 'mi'
        Literal.Number.Integer.Long  : PURPLE,  # class      : 'il'
        Literal.Number.Oct           : PURPLE,  # class      : 'mo'

        Literal.String.Affix : GREEN + " underline",
        Literal.String.Backtick: GREEN,
        String: GREEN,  # class: 's'
        String.Affix: GREEN + " underline",
        String.Backtick: GREEN,  # class: 'sb'
        String.Char: FOREGROUND,  # class: 'sc'
        String.Doc: COMMENT,  # class: 'sd'
        String.Double: GREEN,  # class: 's2'
        String.Escape: "noinherit " + ORANGE,  # class: 'se'
        String.Heredoc: "",  # class: 'sh'
        # the old style '%s' % (...) string formatting
        String.Interpol: "noinherit " + ORANGE,  # class: 'si'
        String.Other: "",  # class: 'sx'
        String.Regex: "",  # class: 'sr'
        String.Single: GREEN,  # class: 's1'
        String.Symbol: "",  # class: 'ss'
        Generic: FOREGROUND,  # class: 'g'
        Generic.Deleted: "noinherit " + BRIGHT_RED,  # class: 'gd',
        Generic.Emph: "italic ",  # class: 'ge'
        Generic.Error: BRIGHT_RED,  # class: 'gr'
        Generic.Heading: "bold " + FOREGROUND,  # class: 'gh'
        Generic.Inserted: "noinherit " + GREEN,  # class: 'gi'
        Generic.Output: "italic ",  # class: 'go'
        Generic.Prompt: "bold " + COMMENT,  # class: 'gp'
        Generic.Strong: "bold ",  # class: 'gs'
        Generic.Subheading: "bold " + AQUA,  # class: 'gu'
        Generic.Traceback: RED,  # class: 'gt'
    }

    style_rules = styles
