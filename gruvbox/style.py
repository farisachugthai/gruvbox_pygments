#!/usr/bin/env python
# -*- coding: utf-8 -*-
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

from gruvbox import GruvboxStyle as Gruvbox

try:
    from IPython.core.getipython import get_ipython
except ImportError:
    shell = None
else:
    shell = get_ipython()


__all__ = ["Gruvbox"]
