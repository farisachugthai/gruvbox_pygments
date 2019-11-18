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
    Comment, Name, Keyword, Generic, Number, Error, Punctuation, Operator,
    String, Literal, Escape, Text, Token
)
try:
    from IPython import get_ipython
except ImportError:
    shell = None
else:
    shell = get_ipython()


# We're still exporting ALL these globals. Let's not.
__all__ = ['GruvboxDarkHard', 'GruvboxLightHard']

# Palette: {{{1
BG0_HARD = "#1d2021"

dark1 = '#3c3836'  # 60-56-54
DARK2 = '#504945'  # 80-73-69
DARK3 = '#665c54'  # 102-92-84

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

NEUTRAL_ORANGE = '#d65d0e'  # 214-93-14

# }}}


class GruvboxBase(Style):
    """Do subclasses inherit class attributes?"""
    default_style = ''

    background_color = BG0_HARD
    # highlight_color = SELECTION

    styles = {
        Comment: GRAY_245,  # class:'c'
        Comment.Hashbang: GRAY_245,  # class: 'ch'
        Comment.Multiline: BRIGHT_YELLOW + ' italic',  # class: 'cm'
        # Comment.Preproc: BRIGHT_AQUA,  # class: 'cp'
        # Comment.PreprocFile: 'cpf',
        Comment.Single: GRAY_245 + ' italic',  # class: 'c1'
        # Comment.Special: ,  # class: 'cs'

        Escape: DARK3,  # class: 'Esc'
        Error: BRIGHT_RED + ' bold',  # class: 'Err'

        Generic: FG1,  # class: 'g'
        Generic.Deleted: LIGHT0_HARD,  # class: 'gd'
        Generic.Emph: 'underline ' + BRIGHT_BLUE,  # class: 'ge'
        Generic.Heading: BRIGHT_GREEN + ' bold',  # class: 'gh'
        Generic.Inserted: LIGHT0_HARD,  # class: 'gi'
        Generic.Output: FG2,  # class: 'go'
        Generic.Prompt: BRIGHT_BLUE,  # class: 'gp'
        Generic.Strong: FG1 + ' bold',  # class: 'gs'
        Generic.Subheading: BRIGHT_GREEN + ' bold',  # class: 'gu'
        # Generic.Traceback  # class: 'gt'

        Keyword: BRIGHT_ORANGE,  # class: 'k'
        Keyword.Constant: BRIGHT_ORANGE,  # class: 'kc'
        Keyword.Declaration: BRIGHT_ORANGE,  # class: 'kd'
        # Keyword.Namespace: 'kn',
        # class: 'kp', the NumPy Lexer registers tokens as this class
        Keyword.Pseudo: BRIGHT_PURPLE,
        # Keyword.Reserved: 'kr',
        Keyword.Type: BRIGHT_YELLOW,  # class: 'kt'

        # The fully qualified name for these tokens is Token.Name.*
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
        Name.Function.Magic: 'noinherit ' + BRIGHT_AQUA,  # class: 'fm'
        Name.Label: BRIGHT_RED,  # class: 'nl'

        # import statements
        Name.Namespace: BRIGHT_BLUE,  # class: 'nn',

        # Name.Other: 'nx',
        Name.Property: BRIGHT_AQUA,  # class: 'py'
        Name.Tag: BRIGHT_RED,  # class: 'nt'
        Name.Variable: FG1,  # class: 'nv'
        Name.Variable.Class: 'noinherit ' + BRIGHT_BLUE,  # class: 'vc'
        Name.Variable.Global: 'noinherit ' + BRIGHT_BLUE,  # class: 'vg'
        Name.Variable.Instance: 'noinherit ' + BRIGHT_BLUE,  # class:'vi'
        Name.Variable.Magic: 'noinherit ' + BRIGHT_BLUE,  # class: 'vm'

        Literal: BRIGHT_ORANGE,  # class: 'l'
        Literal.Date: BRIGHT_GREEN,  # class: 'ld',

        # These tokens have the FQDN Token.Literal.String.*
        String: BRIGHT_GREEN,  # class: 's'
        # String.Affix: BRIGHT_ORANGE,  # class: 'sa',

        # Literally matches `.* lol
        String.Backtick: LIGHT4,  # class: 'sb',
        String.Char: FG1,  # class: 'sc',
        # String.Delimiter: 'dl',
        String.Doc: GRAY_245,  # class: 'sd',
        # String.Double: 's2',
        # String.Escape: 'se',
        # String.Heredoc: 'sh',
        # Interpolated strings!
        String.Interpol: BRIGHT_GREEN,  # class 'si',
        # String.Other: BRIGHT_GREEN,  # class: 'sx'
        String.Regex: BRIGHT_YELLOW,  # class: 'sr',
        # String.Single: 's1',
        # String.Symbol: FG2,  # class: 'ss',
        String.Symbol: BRIGHT_BLUE,

        # These fully qualified name for these tokens is Token.Literal.Number*
        Number: BRIGHT_ORANGE,  # class: 'm',
        # Number.Bin: 'mb',
        # Number.Float:  # class: 'mf',
        # Number.Hex: 'mh',
        # Number.Integer: 'mi',
        # Number.Integer.Long: 'il',
        # Number.Oct: 'mo',

        Punctuation: FG1,  # class: 'p'

        Operator: BRIGHT_AQUA,  # class: 'o'
        # Operator.Word: NEUTRAL_RED,  # class: 'ow'
        # really hard to read
        # Operator.Word: 'noinherit ' + BRIGHT_RED,

        Text: FG1,  # class: 't'
        # treating this key as Vim's Identifier token.
        Text.Whitespace: '',  # class: 'w'
    }

    if shell is not None:
        styles.update(
            {
                Token.Prompt: BRIGHT_GREEN,
                Token.PromptNum: 'bold {}'.format(BRIGHT_GREEN),

                Token.OutPrompt: BRIGHT_GREEN,
                Token.OutPromptNum: BRIGHT_GREEN,
                # TODO:
                # Token.Menu.Completions.Completion
                # Token.Menu.Completions.Completion.Current
                # Token.MatchingBracket.Other
            }
        )

    # I think this is a reasonable way of checking if we're in IPython or not

    def __repr__(self):
        """Return repr representation."""
        keys = sorted(self.__dict__)
        return ("{!r}={!r}".format(self.__class__.__name__, self.styles[k]) for k in keys)

    def __eq__(self, other):
        """Check if style is the same as the other."""
        return self.styles == other.styles


class GruvboxDarkHard(GruvboxBase):
    """Retro groove color scheme for Pygments.

    Extends previous repositories that have ported Gruvbox to Pygments, and
    adds in new definitions for different tokens.

    """

    def __init__(self):
        """Call the super method."""
        super().__init__()


class GruvboxLightHard:

    """Docstring for GruvboxLightHard."""

    pass
