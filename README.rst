=========================================================
Gruvbox IPython --- A Pygments Style Designed for IPython
=========================================================

.. module:: readme
    :synopsis: A Pygments Style Designed for IPython


.. _Gruvbox: https://github.com/morhetz/gruvbox


`Gruvbox <https://github.com/morhetz/gruvbox>`_ is a phenomenal colorscheme for
Vim, and gives a fantastic base for any terminal based application.

According to it's author:

    Designed as a bright theme with pastel 'retro groove' colors and light/dark
    mode switching in the way of solarized. The main focus when developing
    gruvbox is to keep colors easily distinguishable, contrast enough and still
    pleasant for the eyes.

To an impressive extent :ref:`Gruvbox` achieves this.

So why this repository?

Despite it's popularity as a Vim colorscheme, I have yet to find a faithful
port of :ref:`Gruvbox` to :mod:`Pygments`.

Installation
------------
To install simply ``git clone`` this repository and run the following in your
terminal of choice.


.. code-block:: shell-session

    python setup.py build && python setup.py install


Setup
-----
To use this colorscheme in :mod:`IPython`, navigate to ``$HOME/.ipython`` and
create/edit your ``ipython_config.py`` file like so:

.. code-block:: python3

    from traitlets.config import get_config
    c = get_config()
    c.TerminalInteractiveShell.highlighting_style = 'Gruvbox'


Pygments Tokens
---------------

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

Original VimScript
------------------
The only :mod:`Pygments` port I could find frequently uses hex colors not found
in the original :ref:`Gruvbox`, and does not link colors in even a slightly similar
manner to the original.

Here's the relevant source code from the original :ref:`Gruvbox`.

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
