# -*- coding: utf-8 -*-
"""Gruvbox for IPython.

Gruvbox Colorscheme
===================
A retro groove color scheme for Vim.
`<https://github.com/morhetz/gruvbox>`_


Definitely could consider creating a base class that inherits from Style.
Then come up with subclasses that implement the varying contrasts.

"""
from pygments.style import Style
from pygments.token import Token, Comment, Name, Keyword, Generic, Number, Operator, String

# Stuff I added
from pygments.token import Whitespace, Error, Punctuation


class GruvboxStyle(Style):
    """Retro groove color scheme for Vim by Github: @morhetz."""

    background_color = '#1d2021'
    styles = {
        # Comment.Preproc: 'noinherit #8ec07c',
        Comment: '#f9f5d7 italic',
        Error: '#fb4934',
        Generic.Deleted: 'noinherit #282828',
        Generic.Emph: '#83a598 underline',
        Generic.Heading: '#b8bb26 bold',
        Generic.Inserted: 'noinherit #282828',
        Generic.Output: 'noinherit #504945',
        Generic.Prompt: '#83a598',
        Generic.Strong: '#ebdbb2',
        Generic.Subheading: '#b8bb26 bold',
        Generic: '#ebdbb2',
        Keyword.Type: 'noinherit #fabd2f',
        Keyword: 'noinherit #fe8019',
        Keyword.Constant: '#fe8019',
        Keyword.Declaration: '#fe8019',
        Name.Attribute: '#b8bb26 bold',
        Name.Builtin: '#fabd2f',
        Name.Constant: 'noinherit #d3869b',
        Name.Entity: 'noinherit #fabd2f',
        Name.Exception: 'noinherit #fb4934',
        Name.Function: '#fabd2f',
        Name.Label: 'noinherit #fb4934',
        Name.Tag: 'noinherit #fb4934',
        Name.Variable: 'noinherit #ebdbb2',
        Name: '#ebdbb2',
        Number.Float: 'noinherit #d3869b',
        Number: 'noinherit #d3869b',
        Operator: '#fe8019',
        Punctuation: '#ebdbb2',
        String.Symbol: '#83a598',
        String: 'noinherit #b8bb26',
        Token: 'noinherit #ebdbb2',
        Whitespace: 'underline #f8f8f8',
    }
