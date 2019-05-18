===================
Pygments Tokens
===================

.. contents::
   :local:


The following are notes for anyone developing with Pygments and for those
who want to customize this colorscheme further.

First:

The full list of pygments tokens.
=================================


Keyword Tokens
-----------------

- Keyword
    For any kind of keyword (especially if it doesn’t match any of the
    subtypes of course).
- Keyword.Constant
    For keywords that are constants (e.g. None in future Python versions).
- Keyword.Declaration
    For keywords used for variable declaration (e.g. var in some programming
    languages like JavaScript).
- Keyword.Namespace
    For keywords used for namespace declarations (e.g. import in Python and
    Java and package in Java).
- Keyword.Pseudo
    For keywords that aren’t really keywords (e.g. None in old Python versions).
- Keyword.Reserved
    For reserved keywords.
- Keyword.Type
    For builtin types that can’t be used as identifiers (e.g. int, char etc.
    in C).

Name Tokens
------------
- Name
    For any name (variable names, function names, classes).
- Name.Attribute
    For all attributes (e.g. in HTML tags).
- Name.Builtin
    Builtin names; names that are available in the global namespace.
- Name.Builtin.Pseudo
    Builtin names that are implicit (e.g. self in Ruby, this in Java).
- Name.Class
    Class names. Because no lexer can know if a name is a class or a
    function or something else this token is meant for class declarations.
- Name.Constant
    Token type for constants. In some languages you can recognise a token
    by the way it’s defined (the value after a const keyword for example).
    In other languages constants are uppercase by definition (Ruby).
- Name.Decorator
    Token type for decorators. Decorators are syntactic elements in the
    Python language. Similar syntax elements exist in C# and Java.
- Name.Entity
    Token type for special entities. (e.g. &nbsp; in HTML).
- Name.Exception
    Token type for exception names (e.g. :const:`RuntimeError` in Python). Some
    languages define exceptions in the function signature (Java). You can
    highlight the name of that exception using this token then.
- Name.Function
    Token type for function names.
- Name.Function.Magic
    Same as ``Name.Function`` but for special function names that have an
    implicit use in a language (e.g. ``__init__`` method in Python).
- Name.Label
    Token type for label names (e.g. in languages that support goto).
- Name.Namespace
    Token type for namespaces. (e.g. import paths in Java/Python), names
    following the module/namespace keyword in other languages.
- Name.Other
    Other names. Normally unused.
- Name.Tag
    Tag names (in HTML/XML markup or configuration files).
- Name.Variable
    Token type for variables. Some languages have prefixes for variable
    names (PHP, Ruby, Perl). You can highlight them using this token.
- Name.Variable.Class
    Same as Name.Variable but for class variables (also static variables).
- Name.Variable.Global
    Same as Name.Variable but for global variables (used in Ruby, for example).
- Name.Variable.Instance
    Same as Name.Variable but for instance variables.
- Name.Variable.Magic
    same as Name.Variable but for special variable names that have an implicit
    use in a language (e.g. ``__doc__`` in Python).

Literals
---------
- Literal
    For any literal (if not further defined).
- Literal.Date
    for date literals (e.g. 42d in Boo).
- String
    For any string literal.
- String.Affix
    Token type for affixes that further specify the type of the string they’re
    attached to (e.g. the prefixes r and u8 in r"foo" and u8"foo").
- String.Backtick
    Token type for strings enclosed in backticks.
- String.Char
    Token type for single characters (e.g. Java, C).
- String.Delimiter
    Token type for delimiting identifiers in “heredoc”, raw and other similar
    strings (e.g. the word END in Perl code print <<'END';).
- String.Doc
    Token type for documentation strings (for example Python).
- String.Double
    Double quoted strings.
- String.Escape
    Token type for escape sequences in strings.
- String.Heredoc
    Token type for “heredoc” strings (e.g. in Ruby or Perl).
- String.Interpol
    Token type for interpolated parts in strings (e.g. #{foo} in Ruby).
- String.Other
    Token type for any other strings (for example %q{foo} string constructs in Ruby).
- String.Regex
    Token type for regular expression literals (e.g. /foo/ in JavaScript).
- String.Single
    Token type for single quoted strings.
- String.Symbol
    Token type for symbols (e.g. :foo in LISP or Ruby).
- Number
    Token type for any number literal.
- Number.Bin
    Token type for binary literals (e.g. 0b101010).
- Number.Float
    Token type for float literals (e.g. 42.0).
- Number.Hex
    Token type for hexadecimal number literals (e.g. 0xdeadbeef).
- Number.Integer
    Token type for integer literals (e.g. 42).
- Number.Integer.Long
    Token type for long integer literals (e.g. 42L in Python).
- Number.Oct
    Token type for octal literals.

Operators
-----------
- Operator
    For any punctuation operator (e.g. +, -).
- Operator.Word
    For any operator that is a word (e.g. not).

Punctuation
-------------
**New in version 0.7.**

- Punctuation
    For any punctuation which is not an operator (e.g. [, (...)

Comments
---------
- Comment
    Token type for any comment.
- Comment.Hashbang
    Token type for hashbang comments (i.e. first lines of files that start
    with ``#!``).
- Comment.Multiline
    Token type for multiline comments.
- Comment.Preproc
    Token type for preprocessor comments (also <?php/<% constructs).
- Comment.Single
    Token type for comments that end at the end of a line (e.g. # foo).
- Comment.Special
    Special data in comments. For example code tags, author and license
    information, etc.

Generic Tokens
---------------
Generic tokens are for special lexers like the
:class:`~pygments.lexers.diff.DiffLexer` that doesn’t really highlight a
programming language but a patch file.

- Generic
    A generic, unstyled token. Normally you don’t use this token type.
- Generic.Deleted
    Marks the token value as deleted.
- Generic.Emph
    Marks the token value as emphasized.
- Generic.Error
    Marks the token value as an error message.
- Generic.Heading
    Marks the token value as headline.
- Generic.Inserted
    Marks the token value as inserted.
- Generic.Output
    Marks the token value as program output (e.g. for python cli lexer).
- Generic.Prompt
    Marks the token value as command prompt (e.g. bash lexer).
- Generic.Strong
    Marks the token value as bold (e.g. for rst lexer).
- Generic.Subheading
    Marks the token value as subheadline.
- Generic.Traceback
    Marks the token value as a part of an error traceback.

Development
============

Now let's map those tokens to CSS.

Standard Types as Defined by Pygments
-------------------------------------

.. Pygments Standard Types {{{1

Here's the src from :mod:`pygments.token`

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

One can programmatically produce CSS from a pygments class.

Pygments also exports methods to create a CSS file directly from a colorscheme.

Original VimScript
------------------

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

Also pygments styles have a method {or a property that looks like a method}
:ref:`pygments.style.Style._styles`.

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

Nah can't do that. The invariant of the user initializing the base class and
not the child is problematic.

Plus it should have a more clear switch that toggles light or dark.


Prompt Toolkit
===============

.. sourcecode::

   #!/usr/bin/env python
   # -*- coding: utf-8 -*-
   """Use the code from a ptpython help doc to stylize IPython.

   Pygments in IPython
   ====================
   We still need to do a lot here but there's the skeleton for you.

   .. note::

       The help from ptpython actually lists the wrong import

   Arguments
   ----------
   style : :class:`pygments.styles.Style`
       Dict with hex codes to colorize IPython with.


   See Also
   ----------
   :mod:`ptpython.styles`


   """
   from __future__ import unicode_literals

   from prompt_toolkit.styles import Style, merge_styles
   from prompt_toolkit.styles.pygments import style_from_pygments_cls
   from prompt_toolkit.utils import is_windows, is_conemu_ansi, is_windows_vt100_supported
   from pygments.styles import get_style_by_name, get_all_styles

   __all__ = (
       'get_all_code_styles',
       'get_all_ui_styles',
       'generate_style',
   )


   def get_all_code_styles():
       """Return a mapping from style names to their classes."""
       result = dict((name, style_from_pygments_cls(get_style_by_name(name)))
                     for name in get_all_styles())
       result['win32'] = Style.from_dict(win32_code_style)

       return result


   def get_all_ui_styles():
       """Return a dict mapping {ui_style_name -> style_dict}."""

       return {
           'default': Style.from_dict(default_ui_style),
           'blue': Style.from_dict(blue_ui_style),
       }


   def generate_style(python_style, ui_style):
       """Generate Pygments Style class from two dictionaries containing style rules."""

       return merge_styles([python_style, ui_style])


   # Code style for Windows consoles. They support only 16 colors,
   # so we choose a combination that displays nicely.
   win32_code_style = {
       'pygments.comment': "#00ff00",
       'pygments.keyword': '#44ff44',
       'pygments.number': '',
       'pygments.operator': '',
       'pygments.string': '#ff44ff',
       'pygments.name': '',
       'pygments.name.decorator': '#ff4444',
       'pygments.name.class': '#ff4444',
       'pygments.name.function': '#ff4444',
       'pygments.name.builtin': '#ff4444',
       'pygments.name.attribute': '',
       'pygments.name.constant': '',
       'pygments.name.entity': '',
       'pygments.name.exception': '',
       'pygments.name.label': '',
       'pygments.name.namespace': '',
       'pygments.name.tag': '',
       'pygments.name.variable': '',
   }

   default_ui_style = {
       'control-character': 'ansiblue',

       # Classic prompt.
       'prompt': 'bold',
       'prompt.dots': 'noinherit',

       # (IPython <5.0) Prompt: "In [1]:"
       'in': 'bold #008800',
       'in.number': '',

       # Return value.
       'out': '#ff0000',
       'out.number': '#ff0000',

       # Separator between windows. (Used above docstring.)
       'separator': '#bbbbbb',

       # System toolbar
       'system-toolbar': '#22aaaa noinherit',

       # "arg" toolbar.
       'arg-toolbar': '#22aaaa noinherit',
       'arg-toolbar.text': 'noinherit',

       # Signature toolbar.
       'signature-toolbar': 'bg:#44bbbb #000000',
       'signature-toolbar.currentname': 'bg:#008888 #ffffff bold',
       'signature-toolbar.operator': '#000000 bold',
       'docstring': '#888888',

       # Validation toolbar.
       'validation-toolbar': 'bg:#440000 #aaaaaa',

       # Status toolbar.
       'status-toolbar': 'bg:#222222 #aaaaaa',
       'status-toolbar.title': 'underline',
       'status-toolbar.inputmode': 'bg:#222222 #ffffaa',
       'status-toolbar.key': 'bg:#000000 #888888',
       'status-toolbar.pastemodeon': 'bg:#aa4444 #ffffff',
       'status-toolbar.pythonversion': 'bg:#222222 #ffffff bold',
       'status-toolbar paste-mode-on': 'bg:#aa4444 #ffffff',
       'record': 'bg:#884444 white',
       'status-toolbar.input-mode': '#ffff44',

       # The options sidebar.
       'sidebar': 'bg:#bbbbbb #000000',
       'sidebar.title': 'bg:#668866 #ffffff',
       'sidebar.label': 'bg:#bbbbbb #222222',
       'sidebar.status': 'bg:#dddddd #000011',
       'sidebar.label selected': 'bg:#222222 #eeeeee',
       'sidebar.status selected': 'bg:#444444 #ffffff bold',
       'sidebar.separator': 'underline',
       'sidebar.key': 'bg:#bbddbb #000000 bold',
       'sidebar.key.description': 'bg:#bbbbbb #000000',
       'sidebar.helptext': 'bg:#fdf6e3 #000011',

       #        # Styling for the history layout.
       #        history.line:                          '',
       #        history.line.selected:                 'bg:#008800  #000000',
       #        history.line.current:                  'bg:#ffffff #000000',
       #        history.line.selected.current:         'bg:#88ff88 #000000',
       #        history.existinginput:                  '#888888',

       # Help Window.
       'window-border': '#aaaaaa',
       'window-title': 'bg:#bbbbbb #000000',

       # Meta-enter message.
       'accept-message': 'bg:#ffff88 #444444',

       # Exit confirmation.
       'exit-confirmation': 'bg:#884444 #ffffff',
   }

   # Some changes to get a bit more contrast on Windows consoles.
   # (They only support 16 colors.)

   if is_windows() and not is_conemu_ansi() and not is_windows_vt100_supported():
       default_ui_style.update({
           'sidebar.title':
           'bg:#00ff00 #ffffff',
           'exitconfirmation':
           'bg:#ff4444 #ffffff',
           'toolbar.validation':
           'bg:#ff4444 #ffffff',
           'menu.completions.completion':
           'bg:#ffffff #000000',
           'menu.completions.completion.current':
           'bg:#aaaaaa #000000',
       })

   blue_ui_style = {}
   blue_ui_style.update(default_ui_style)
   #blue_ui_style.update({
   #        # Line numbers.
   #        Token.LineNumber:                             '#aa6666',
   #
   #        # Highlighting of search matches in document.
   #        Token.SearchMatch:                            '#ffffff bg:#4444aa',
   #        Token.SearchMatch.Current:                    '#ffffff bg:#44aa44',
   #
   #        # Highlighting of select text in document.
   #        Token.SelectedText:                           '#ffffff bg:#6666aa',
   #
   #        # Completer toolbar.
   #        Token.Toolbar.Completions:                    'bg:#44bbbb #000000',
   #        Token.Toolbar.Completions.Arrow:              'bg:#44bbbb #000000 bold',
   #        Token.Toolbar.Completions.Completion:         'bg:#44bbbb #000000',
   #        Token.Toolbar.Completions.Completion.Current: 'bg:#008888 #ffffff',
   #
   #        # Completer menu.
   #        Token.Menu.Completions.Completion:            'bg:#44bbbb #000000',
   #        Token.Menu.Completions.Completion.Current:    'bg:#008888 #ffffff',
   #        Token.Menu.Completions.Meta:                  'bg:#449999 #000000',
   #        Token.Menu.Completions.Meta.Current:          'bg:#00aaaa #000000',
   #        Token.Menu.Completions.ProgressBar:           'bg:#aaaaaa',
   #        Token.Menu.Completions.ProgressButton:        'bg:#000000',
   #})

   if __name__ == "__main__":
       from prompt_toolkit.styles.pygments import style_from_pygments_cls  # noqa F401
       from pygments.styles import get_style_by_name  # noqa F401
       style = style_from_pygments_cls(get_style_by_name('monokai'))
