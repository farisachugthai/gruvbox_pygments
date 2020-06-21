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

__all__ = ["GruvboxStyle"]


class GruvboxStyle(Style):

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
    AQUA = "#8ec07c"
    BLUE = "#458588"
    PURPLE = "#d3869b"

    default_style = FOREGROUND

    background_color = BACKGROUND
    highlight_color = SELECTION

    styles = {
        Comment: COMMENT,  # class: 'c'
        Comment.Hashbang: COMMENT,
        Comment.Multiline: COMMENT,  # class: 'cm'
        # cython's IF DEF etc
        Comment.Preproc: "noinherit " + AQUA,  # class: 'cp'
        Comment.Single: COMMENT,  # class: 'c1'
        # Comment.Special: "",  # class: 'cs'
        # `:hi pythonEscape`
        Escape: ORANGE,
        Error: BRIGHT_RED,  # class: 'err'
        Generic: FOREGROUND,  # class: 'g'
        Generic.Deleted: "noinherit " + BRIGHT_RED,  # class: 'gd',
        Generic.Emph: "italic " + FOREGROUND,  # class: 'ge'
        Generic.Emphasis: "italic " + FOREGROUND,  # class: 'ge'
        Generic.Error: BRIGHT_RED,  # class: 'gr'
        Generic.Heading: "bold " + RED,  # class: 'gh'
        Generic.Inserted: "noinherit " + GREEN,  # class: 'gi'
        Generic.Output: "italic ",  # class: 'go'
        Generic.Prompt: "bold " + COMMENT,  # class: 'gp'
        Generic.Strong: "bold ",  # class: 'gs'
        Generic.Subheading: "bold " + GREEN,  # class: 'gu'
        # This is the text before the traceback
        Generic.Traceback: FOREGROUND,  # class: 'gt'
        # Note: In Pygments, Token.String is an alias for Token.Literal.String,
        #       and Token.Number as an alias for Token.Literal.Number.
        Literal: BLUE,  # class: 'l'
        Literal.Date: "noinherit " + GREEN,  # class: 'ld'
        Literal.Number: PURPLE,  # class      : 'm'
        Literal.Number.Bin: PURPLE,
        Literal.Number.Float: PURPLE,  # class      : 'mf'
        Literal.Number.Hex: PURPLE,  # class      : 'mh'
        Literal.Number.Integer: PURPLE,  # class      : 'mi'
        Literal.Number.Integer.Long: PURPLE,  # class      : 'il'
        Literal.Number.Oct: PURPLE,  # class      : 'mo'
        Literal.String.Heredoc: GREEN,  # class: 'sh'
        Literal.String.Other: GREEN,  # class: 'sx'
        Literal.String.Regex: GREEN,  # class: 'sr'
        Literal.String.Single: GREEN,  # class: 's1'
        Literal.String.Symbol: GREEN,  # class: 'ss'
        # basically the foundation of everything
        Keyword: "bold " + ORANGE,  # class: 'k'
        Keyword: ORANGE,  # class: 'k'
        # True, False, None. `:hi pythonBoolean` is Purple
        Keyword.Constant: "noinherit " + PURPLE,  # class: 'kc'

        Keyword.Declaration: "nobold " + AQUA,  # class: 'kd'

        # from <---- x import y
        Keyword.Namespace: "noinherit " + BLUE,  # class: 'kn'

        # Keyword.Pseudo: "nobold",  # + GREEN,  # class: 'kp'
        Keyword.Pseudo: "italic " + GREEN,  # class: 'kp'
        # Keyword.Reserved: "",  # class: 'kr'
        Keyword.Type: "nobold " + YELLOW,  # class: 'kt'
        Name: "noinherit " + FOREGROUND,  # class: 'n'
        Name.Attribute: "noinherit " + BLUE,  # class: 'na'
        # Builtin functions like max, zip, min
        Name.Builtin: "noinherit " + YELLOW,  # class: 'nb'
        # raise None <---
        Name.Builtin.Pseudo: "noinherit " + ORANGE,  # class: 'bp'
        # So these should be coming up aqua. Why are they orange...?
        # Note it's only the clas name not the word class
        # class FooBar <-----
        Name.Class: AQUA,  # class: 'nc'
        Name.Constant: "noinherit " + BRIGHT_RED,  # class: 'no'
        # Only the @ in a decorator
        Name.Decorator: "bold " + BRIGHT_RED,  # class: 'nd'

        Name.Entity: AQUA,  # class: 'ni'
        Name.Exception: "noinherit " + PURPLE,  # class: 'ne'
        # You guessed it
        Name.Function: "noinherit " + AQUA,  # class: 'nf'
        # Dunders
        Name.Function.Magic: "noinherit " + AQUA,
        # import mod <----
        Name.Namespace: FOREGROUND,  # class: 'nn'
        Name.Other: BLUE,  # class: 'nx'
        # Name.Property: "",  # class: 'py'

        Name.Tag: "bold " + AQUA,  # class: 'nt'
        Name.Variable: BRIGHT_RED,  # class: 'nv'
        Name.Variable.Class: "noinherit bold " + BLUE,  # class: 'vc'
        Name.Variable.Global: "italic",  # class: 'vg'
        # Instance dunders
        Name.Variable.Magic: "noinherit " + AQUA,
        Name.Variable.Instance: "italic",  # class: 'vi'
        Operator: GREEN,  # class: 'o'
        Operator.Word: ORANGE,  # class: 'ow'
        # Can be the text in a traceback
        Other: FOREGROUND,  # class 'x'
        # Might be better suited as Delimiter. *Blue. Or Aqua?* nah
        Punctuation: FOREGROUND,  # class: 'p'
        String: GREEN,  # class: 's'
        String.Affix: GREEN + " underline",
        String.Backtick: GREEN,  # class: 'sb'
        String.Char: FOREGROUND,  # class: 'sc'
        String.Doc: "italic " + GREEN,  # class: 'sd'
        String.Double: GREEN,  # class: 's2'
        String.Escape: "bold " + ORANGE,  # class: 'se'
        # the old style '%s' % (...) string formatting
        String.Interpol: "noinherit " + ORANGE,  # class: 'si'
        # No corresponding class for the following:
        Text: FOREGROUND,  # class:  ''
        Text.Whitespace: BRIGHT_RED,  # class: 'w'
        Token: ORANGE,
    }

    style_rules = styles

    def __repr__(self):
        return "%s" % (self.__class__.__name__)

    def __iter__(self):
        """Iter needs to be defined for use with pygments formatters."""
        return iter(self.style_rules)

    def dict_to_list_of_tuples(self, dictionary):
        tmp = []
        for i, j in dictionary.items():
            tmp.append((i, j))
        return tmp

    def _styles(self):
        return self.dict_to_list_of_tuples(self.style_rules)

    def __str__(self):
        return f"{self.__class__.__name__}"
