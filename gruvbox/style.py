# -*- coding: utf-8 -*-
"""Gruvbox for IPython.

===================
Gruvbox Colorscheme
===================

A retro groove color scheme for Vim.
`<https://github.com/morhetz/gruvbox>`_

Pygments Tokens
===================

The following are notes for anyone developing with Pygments and for those
who want to customize this colorscheme further.

First:
The full list of pygments tokens.


Keyword Tokens
-----------------

Keyword
    For any kind of keyword (especially if it doesn’t match any of the subtypes of course).
Keyword.Constant
    For keywords that are constants (e.g. None in future Python versions).
Keyword.Declaration
    For keywords used for variable declaration (e.g. var in some programming languages like JavaScript).
Keyword.Namespace
    For keywords used for namespace declarations (e.g. import in Python and Java and package in Java).
Keyword.Pseudo
    For keywords that aren’t really keywords (e.g. None in old Python versions).
Keyword.Reserved
    For reserved keywords.
Keyword.Type
    For builtin types that can’t be used as identifiers (e.g. int, char etc. in C).

Name Tokens
------------
Name
    For any name (variable names, function names, classes).
Name.Attribute
    For all attributes (e.g. in HTML tags).
Name.Builtin
    Builtin names; names that are available in the global namespace.
Name.Builtin.Pseudo
    Builtin names that are implicit (e.g. self in Ruby, this in Java).
Name.Class
    Class names. Because no lexer can know if a name is a class or a
    function or something else this token is meant for class declarations.
Name.Constant
    Token type for constants. In some languages you can recognise a token
    by the way it’s defined (the value after a const keyword for example).
    In other languages constants are uppercase by definition (Ruby).
Name.Decorator
    Token type for decorators. Decorators are syntactic elements in the
    Python language. Similar syntax elements exist in C# and Java.
Name.Entity
    Token type for special entities. (e.g. &nbsp; in HTML).
Name.Exception
    Token type for exception names (e.g. RuntimeError in Python). Some
    languages define exceptions in the function signature (Java). You can
    highlight the name of that exception using this token then.
Name.Function
    Token type for function names.
Name.Function.Magic
    Same as ``Name.Function`` but for special function names that have an
    implicit use in a language (e.g. ``__init__`` method in Python).
Name.Label
    Token type for label names (e.g. in languages that support goto).
Name.Namespace
    Token type for namespaces. (e.g. import paths in Java/Python), names
    following the module/namespace keyword in other languages.
Name.Other
    Other names. Normally unused.
Name.Tag
    Tag names (in HTML/XML markup or configuration files).
Name.Variable
    Token type for variables. Some languages have prefixes for variable
    names (PHP, Ruby, Perl). You can highlight them using this token.
Name.Variable.Class
    Same as Name.Variable but for class variables (also static variables).
Name.Variable.Global
    Same as Name.Variable but for global variables (used in Ruby, for example).
Name.Variable.Instance
    Same as Name.Variable but for instance variables.
Name.Variable.Magic
    same as Name.Variable but for special variable names that have an implicit
    use in a language (e.g. __doc__ in Python).

Literals
---------
Literal
    For any literal (if not further defined).
Literal.Date
    for date literals (e.g. 42d in Boo).
String
    For any string literal.
String.Affix
    Token type for affixes that further specify the type of the string they’re attached to (e.g. the prefixes r and u8 in r"foo" and u8"foo").
String.Backtick
    Token type for strings enclosed in backticks.
String.Char
    Token type for single characters (e.g. Java, C).
String.Delimiter
    Token type for delimiting identifiers in “heredoc”, raw and other similar strings (e.g. the word END in Perl code print <<'END';).
String.Doc
    Token type for documentation strings (for example Python).
String.Double
    Double quoted strings.
String.Escape
    Token type for escape sequences in strings.
String.Heredoc
    Token type for “heredoc” strings (e.g. in Ruby or Perl).
String.Interpol
    Token type for interpolated parts in strings (e.g. #{foo} in Ruby).
String.Other
    Token type for any other strings (for example %q{foo} string constructs in Ruby).
String.Regex
    Token type for regular expression literals (e.g. /foo/ in JavaScript).
String.Single
    Token type for single quoted strings.
String.Symbol
    Token type for symbols (e.g. :foo in LISP or Ruby).
Number
    Token type for any number literal.
Number.Bin
    Token type for binary literals (e.g. 0b101010).
Number.Float
    Token type for float literals (e.g. 42.0).
Number.Hex
    Token type for hexadecimal number literals (e.g. 0xdeadbeef).
Number.Integer
    Token type for integer literals (e.g. 42).
Number.Integer.Long
    Token type for long integer literals (e.g. 42L in Python).
Number.Oct
    Token type for octal literals.

Operators
-----------
Operator
    For any punctuation operator (e.g. +, -).
Operator.Word
    For any operator that is a word (e.g. not).

Punctuation
-------------
New in version 0.7.

Punctuation
    For any punctuation which is not an operator (e.g. [, (...)

Comments
---------
Comment
    Token type for any comment.
Comment.Hashbang
    Token type for hashbang comments (i.e. first lines of files that start with ``#!``).
Comment.Multiline
    Token type for multiline comments.
Comment.Preproc
    Token type for preprocessor comments (also <?php/<% constructs).
Comment.Single
    Token type for comments that end at the end of a line (e.g. # foo).
Comment.Special
    Special data in comments. For example code tags, author and license information, etc.

Generic Tokens
---------------
Generic tokens are for special lexers like the DiffLexer that doesn’t
really highlight a programming language but a patch file.

Generic
    A generic, unstyled token. Normally you don’t use this token type.
Generic.Deleted
    Marks the token value as deleted.
Generic.Emph
    Marks the token value as emphasized.
Generic.Error
    Marks the token value as an error message.
Generic.Heading
    Marks the token value as headline.
Generic.Inserted
    Marks the token value as inserted.
Generic.Output
    Marks the token value as program output (e.g. for python cli lexer).
Generic.Prompt
    Marks the token value as command prompt (e.g. bash lexer).
Generic.Strong
    Marks the token value as bold (e.g. for rst lexer).
Generic.Subheading
    Marks the token value as subheadline.
Generic.Traceback
    Marks the token value as a part of an error traceback.

Development
------------

Now let's map those tokens to CSS.

Pygments Tokens
^^^^^^^^^^^^^^^

.. Pygments Standard Types {{{1

Here's the src from :mod:`pygments/token`

.. code-block:: python3

    # Map standard token types to short names, used in CSS class naming.
    # If you add a new item, please be sure to run this file to perform
    # a consistency check for duplicate values.
    STANDARD_TYPES = {
        Token:                         '',

        Text:                          '',
        Whitespace:                    'w',
        Escape:                        'esc',
        Error:                         'err',
        Other:                         'x',

        Keyword:                       'k',
        Keyword.Constant:              'kc',
        Keyword.Declaration:           'kd',
        Keyword.Namespace:             'kn',
        Keyword.Pseudo:                'kp',
        Keyword.Reserved:              'kr',
        Keyword.Type:                  'kt',

        Name:                          'n',
        Name.Attribute:                'na',
        Name.Builtin:                  'nb',
        Name.Builtin.Pseudo:           'bp',
        Name.Class:                    'nc',
        Name.Constant:                 'no',
        Name.Decorator:                'nd',
        Name.Entity:                   'ni',
        Name.Exception:                'ne',
        Name.Function:                 'nf',
        Name.Function.Magic:           'fm',
        Name.Property:                 'py',
        Name.Label:                    'nl',
        Name.Namespace:                'nn',
        Name.Other:                    'nx',
        Name.Tag:                      'nt',
        Name.Variable:                 'nv',
        Name.Variable.Class:           'vc',
        Name.Variable.Global:          'vg',
        Name.Variable.Instance:        'vi',
        Name.Variable.Magic:           'vm',

        Literal:                       'l',
        Literal.Date:                  'ld',

        String:                        's',
        String.Affix:                  'sa',
        String.Backtick:               'sb',
        String.Char:                   'sc',
        String.Delimiter:              'dl',
        String.Doc:                    'sd',
        String.Double:                 's2',
        String.Escape:                 'se',
        String.Heredoc:                'sh',
        String.Interpol:               'si',
        String.Other:                  'sx',
        String.Regex:                  'sr',
        String.Single:                 's1',
        String.Symbol:                 'ss',

        Number:                        'm',
        Number.Bin:                    'mb',
        Number.Float:                  'mf',
        Number.Hex:                    'mh',
        Number.Integer:                'mi',
        Number.Integer.Long:           'il',
        Number.Oct:                    'mo',

        Operator:                      'o',
        Operator.Word:                 'ow',

        Punctuation:                   'p',

        Comment:                       'c',
        Comment.Hashbang:              'ch',
        Comment.Multiline:             'cm',
        Comment.Preproc:               'cp',
        Comment.PreprocFile:           'cpf',
        Comment.Single:                'c1',
        Comment.Special:               'cs',

        Generic:                       'g',
        Generic.Deleted:               'gd',
        Generic.Emph:                  'ge',
        Generic.Error:                 'gr',
        Generic.Heading:               'gh',
        Generic.Inserted:              'gi',
        Generic.Output:                'go',
        Generic.Prompt:                'gp',
        Generic.Strong:                'gs',
        Generic.Subheading:            'gu',
        Generic.Traceback:             'gt',

.. }}}

One can programatically produce CSS from a pygments class.

Pygments also exports methods to create a CSS file directly from a colorscheme.

Original VimScript
^^^^^^^^^^^^^^^^^^

The only :mod:`Pygments` port I could find frequently uses hex colors not found
in the original `Gruvbox <https://github.com/morhetz/gruvbox>`_, and does not
link colors in even a slightly similar manner to the original.

Here's the relevant source code from the original `Gruvbox <https://github.com/morhetz/gruvbox>`_.

.. Source Code Blob {{{1

.. code-block:: vim

   hi! link pythonBuiltin GruvboxOrange
   hi! link pythonBuiltinObj GruvboxOrange
   hi! link pythonBuiltinFunc GruvboxOrange
   hi! link pythonFunction GruvboxAqua
   hi! link pythonDecorator GruvboxRed
   hi! link pythonInclude GruvboxBlue
   hi! link pythonImport GruvboxBlue
   hi! link pythonRun GruvboxBlue
   hi! link pythonCoding GruvboxBlue
   hi! link pythonOperator GruvboxRed
   hi! link pythonException GruvboxRed
   hi! link pythonExceptions GruvboxPurple
   hi! link pythonBoolean GruvboxPurple
   hi! link pythonDot GruvboxFg3
   hi! link pythonConditional GruvboxRed
   hi! link pythonRepeat GruvboxRed
   hi! link pythonDottedName GruvboxGreenBold

.. }}}

And the definitions for what those keywords mean.

.. code-block:: vim

    " Palette: {{{2

    " setup palette dictionary
    let s:gb = {}

     " fill it with absolute colors
    let s:gb.dark0_hard  = ['#1d2021', 234]     " 29-32-33
    let s:gb.dark0       = ['#282828', 235]     " 40-40-40
    let s:gb.dark0_soft  = ['#32302f', 236]     " 50-48-47
    let s:gb.dark1       = ['#3c3836', 237]     " 60-56-54
    let s:gb.dark2       = ['#504945', 239]     " 80-73-69
    let s:gb.dark3       = ['#665c54', 241]     " 102-92-84
    let s:gb.dark4       = ['#7c6f64', 243]     " 124-111-100
    let s:gb.dark4_256   = ['#7c6f64', 243]     " 124-111-100
    let s:gb.gray_245    = ['#928374', 245]     " 146-131-116
    let s:gb.gray_244    = ['#928374', 244]     " 146-131-116
    let s:gb.light0_hard = ['#f9f5d7', 230]     " 249-245-215
    let s:gb.light0      = ['#fbf1c7', 229]     " 253-244-193
    let s:gb.light0_soft = ['#f2e5bc', 228]     " 242-229-188
    let s:gb.light1      = ['#ebdbb2', 223]     " 235-219-178
    let s:gb.light2      = ['#d5c4a1', 250]     " 213-196-161
    let s:gb.light3      = ['#bdae93', 248]     " 189-174-147
    let s:gb.light4      = ['#a89984', 246]     " 168-153-132
    let s:gb.light4_256  = ['#a89984', 246]     " 168-153-132
    let s:gb.bright_red     = ['#fb4934', 167]     " 251-73-52
    let s:gb.bright_green   = ['#b8bb26', 142]     " 184-187-38
    let s:gb.bright_yellow  = ['#fabd2f', 214]     " 250-189-47
    let s:gb.bright_blue    = ['#83a598', 109]     " 131-165-152
    let s:gb.bright_purple  = ['#d3869b', 175]     " 211-134-155
    let s:gb.bright_aqua    = ['#8ec07c', 108]     " 142-192-124
    let s:gb.bright_orange  = ['#fe8019', 208]     " 254-128-25
    let s:gb.neutral_red    = ['#cc241d', 124]     " 204-36-29
    let s:gb.neutral_green  = ['#98971a', 106]     " 152-151-26
    let s:gb.neutral_yellow = ['#d79921', 172]     " 215-153-33
    let s:gb.neutral_blue   = ['#458588', 66]      " 69-133-136
    let s:gb.neutral_purple = ['#b16286', 132]     " 177-98-134
    let s:gb.neutral_aqua   = ['#689d6a', 72]      " 104-157-106
    let s:gb.neutral_orange = ['#d65d0e', 166]     " 214-93-14
    let s:gb.faded_red      = ['#9d0006', 88]      " 157-0-6
    let s:gb.faded_green    = ['#79740e', 100]     " 121-116-14
    let s:gb.faded_yellow   = ['#b57614', 136]     " 181-118-20
    let s:gb.faded_blue     = ['#076678', 24]      " 7-102-120
    let s:gb.faded_purple   = ['#8f3f71', 96]      " 143-63-113
    let s:gb.faded_aqua     = ['#427b58', 66]      " 66-123-88
    let s:gb.faded_orange   = ['#af3a03', 130]     " 175-58-3

.. }}}

Straightforward enough.

In addition, here's a mapping from Honza mapping Vim highlighting
groups to Pygments tokens.

Original source:

    https://github.com/honza/vim2pygments/vim2pygments.py

.. code-block:: python

    TOKENS = {
        'normal':           '',
        'string':           'String',
        'number':           'Number',
        'float':            'Number.Float',
        'constant':         'Name.Constant',
        'number':           'Number',
        'statement':        ('Keyword', 'Name.Tag'),
        'identifier':       'Name.Variable',
        'operator':         'Operator.Word',
        'label':            'Name.Label',
        'exception':        'Name.Exception',
        'function':         ('Name.Function', 'Name.Attribute'),
        'preproc':          'Comment.Preproc',
        'comment':          'Comment',
        'type':             'Keyword.Type',
        'diffadd':          'Generic.Inserted',
        'diffdelete':       'Generic.Deleted',
        'error':            'Generic.Error',
        'errormsg':         'Generic.Traceback',
        'title':            ('Generic.Heading', 'Generic.Subheading'),
        'underlined':       'Generic.Emph',
        'special':          'Name.Entity',
        'nontext':          'Generic.Output'
    }



04/14/2019:

In case you were wondering how to find all the pygment tokens in a more
consistent way, literally just viewing the ``styles`` attributes for the
:ref:`~gruvbox.style.GruvboxStyle` should be plenty.

.. code-block:: python3

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

Also pygments styles have a method {or a property that looks like a method}
:ref:`pygments.styles.Style._styles`.

It's hard not to hate a namespace like that but it's worth looking at.

Simplified Gruvbox
===================
https://github.com/lifepillar/vim-gruvbox8

A much more straightforward mapping of hex codes to Vim highlighting groups.
Honza got us a mapping of the important groups.

Where do we go now?
===================

We have a description of what the lexer is doing for the rest.

If we define a Gruvbox base class that maps color names to tokens, then we
can define a Boolean that chooses whether we use GruvboxDark or GruvboxLight.::

    class GruvboxStyle(Style, token_styles=None):

        styles = {
            Comment.Multiline: NEUTRAL_YELLOW + ' italic',
            ...
            Whitespace: 'underline ' + FADED_YELLOW,
        }

        def __init__(self):
            self.token_styles = token_styles

    class GruvboxDark(GruvboxStyle):

        @property
        def token_styles(self):
            BG0 = "1d2021"
            ...
            FADED_ORANGE = '#af3a03'  # 175-58-3

Nah cant do that. The invariant of the user initializing the base class and
not the child is problematic.

Plus it should have a more clear switch that toggles light or dark.

"""
from pygments.style import Style
from pygments.token import (Token, Comment, Name, Keyword, Generic, Number,
                            Whitespace, Error, Punctuation, Operator, String,
                            Literal)

__all__ = ['GruvboxStyle']

# Palette: {{{1
BG0_HARD = "1d2021"

dark1 = '#3c3836'  # 60-56-54
DARK2 = '#504945'  # 80-73-69
dark3 = '#665c54'  # 102-92-84
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
        Comment.Multiline: NEUTRAL_YELLOW + ' italic',
        Comment.Preproc: BRIGHT_AQUA,
        Comment.Singleline: FG3 + ' italic',
        Comment: FG3,
        Error: BRIGHT_RED,
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
        Keyword: NEUTRAL_RED,
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
        Name.Variable: FG1,
        Name: FG1,
        Number.Float: BRIGHT_PURPLE,
        Number: BRIGHT_PURPLE,
        Operator: BRIGHT_ORANGE,
        Operator.Word: NEUTRAL_RED,
        Punctuation: FG1,
        String.Symbol: BRIGHT_BLUE,
        String: BRIGHT_GREEN,
        Token: FG1,
        Whitespace: 'underline ' + FADED_YELLOW,
    }

    def __init__(self, **kwargs):
        """Create the Version object."""
        self.__dict__.update(kwargs)

    def __repr__(self):
        """Return str representation of the Version."""
        keys = sorted(self.__dict__)
        items = ("{}={!r}".format(k, self.__dict__[k]) for k in keys)
        return "{}({})".format(type(self).__name__, ", ".join(items))

    def __eq__(self, other):
        """Check if version is same as other."""
        return self.__dict__ == other.__dict__
