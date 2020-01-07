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
        Text.Whitespace: "",  # class: 'w'
        Error: RED,  # class: 'err'
        Other: "",  # class 'x'
        Comment: COMMENT,  # class: 'c'
        Comment.Multiline: "",  # class: 'cm'
        Comment.Preproc: "",  # class: 'cp'
        Comment.Single: "",  # class: 'c1'
        Comment.Special: "",  # class: 'cs'
        Keyword: RED,  # class: 'k'
        Keyword.Constant: "",  # class: 'kc'
        Keyword.Declaration: "",  # class: 'kd'
        Keyword.Namespace: AQUA,  # class: 'kn'
        Keyword.Pseudo: "",  # class: 'kp'
        Keyword.Reserved: "",  # class: 'kr'
        Keyword.Type: YELLOW,  # class: 'kt'
        Operator: ORANGE,  # class: 'o'
        Operator.Word: "",  # class: 'ow'
        Punctuation: FOREGROUND,  # class: 'p'
        Name: FOREGROUND,  # class: 'n'
        Name.Attribute: BLUE,  # class: 'na'
        Name.Builtin: "",  # class: 'nb'
        Name.Builtin.Pseudo: "",  # class: 'bp'
        Name.Class: RED,  # class: 'nc'
        Name.Constant: RED,  # class: 'no'
        Name.Decorator: GREEN,  # class: 'nd'
        Name.Entity: "",  # class: 'ni'
        Name.Exception: RED,  # class: 'ne'
        Name.Function: "bold " + GREEN,  # class: 'nf'
        Name.Property: "",  # class: 'py'
        Name.Label: "",  # class: 'nl'
        Name.Namespace: FOREGROUND,  # class: 'nn'
        Name.Other: BLUE,  # class: 'nx'
        Name.Tag: AQUA,  # class: 'nt'
        Name.Variable: RED,  # class: 'nv'
        Name.Variable.Class: "",  # class: 'vc'
        Name.Variable.Global: "",  # class: 'vg'
        Name.Variable.Instance: "",  # class: 'vi'
        Number: ORANGE,  # class: 'm'
        Number.Float: "",  # class: 'mf'
        Number.Hex: "",  # class: 'mh'
        Number.Integer: "",  # class: 'mi'
        Number.Integer.Long: "",  # class: 'il'
        Number.Oct: "",  # class: 'mo'
        Literal: ORANGE,  # class: 'l'
        Literal.Date: GREEN,  # class: 'ld'
        String: GREEN,  # class: 's'
        String.Backtick: "",  # class: 'sb'
        String.Char: FOREGROUND,  # class: 'sc'
        String.Doc: COMMENT,  # class: 'sd'
        String.Double: "",  # class: 's2'
        String.Escape: ORANGE,  # class: 'se'
        String.Heredoc: "",  # class: 'sh'
        String.Interpol: ORANGE,  # class: 'si'
        String.Other: "",  # class: 'sx'
        String.Regex: "",  # class: 'sr'
        String.Single: "",  # class: 's1'
        String.Symbol: "",  # class: 'ss'
        Generic: FOREGROUND,  # class: 'g'
        Generic.Deleted: BRIGHT_RED,  # class: 'gd',
        Generic.Emph: "italic",  # class: 'ge'
        Generic.Error: "",  # class: 'gr'
        Generic.Heading: "bold " + FOREGROUND,  # class: 'gh'
        Generic.Inserted: GREEN,  # class: 'gi'
        Generic.Output: "",  # class: 'go'
        Generic.Prompt: "bold " + COMMENT,  # class: 'gp'
        Generic.Strong: "bold",  # class: 'gs'
        Generic.Subheading: "bold " + AQUA,  # class: 'gu'
        Generic.Traceback: RED,  # class: 'gt'
    }


