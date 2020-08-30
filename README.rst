=========================================================
Gruvbox IPython --- A Pygments Style Designed for IPython
=========================================================

.. moduleauthor:: Faris Chugthai

:date: |today|

`Gruvbox <https://github.com/morhetz/gruvbox>`_ is a phenomenal
colorscheme for Vim, and gives a fantastic base for any terminal
based application.

According to it's author:

    Designed as a bright theme with pastel 'retro groove' colors and
    light/dark mode switching in the way of solarized. The main focus
    when developing gruvbox is to keep colors easily distinguishable,
    contrast enough and still pleasant for the eyes.

To an impressive extent `Gruvbox <https://github.com/morhetz/gruvbox>`_
achieves this.

So why this repository?

Despite it's popularity as a Vim colorscheme, I have yet to find a
faithful port of `Gruvbox <https://github.com/morhetz/gruvbox>`_
to pygments.


Installation
============
To install simply ``git clone`` this repository and run the following
in your terminal of choice.

.. code-block:: bash

    python setup.py build
    python3 -m pip install -U -e .

Adjust the version of python as needed, as pygments as well as this library
have been intentionally written to be compatible across versions of python
2.7 and up.

.. exception:: PermissionError

   If raised during installation, add the ``--user`` flag to the end of the
   ``python -m pip`` command.


IPython Setup
=============
To use this colorscheme in :mod:`IPython`, navigate to ``$HOME/.ipython``
and create/edit your ``ipython_config.py`` file like so:

.. code-block:: bash

   ipython profile create default

This command will pre-populate a well commented default configuration
file.

At the top of the file add the following:

.. code-block:: ipython

    from traitlets.config import get_config
    c = get_config()
    c.TerminalInteractiveShell.true_color = True
    c.TerminalInteractiveShell.highlighting_style = 'GruvboxStyle'


Usage
=====
Pygments colorschemes can be used for a wide variety of applications;
however, and limiting it's use to only IPython is not necessary.

For example, the Sphinx documentation project also uses Pygments when
highlighting blocks of code, and the documentation for this project is
highlighted with the `Gruvbox`_ colorscheme.


Bundled Colorschemes
--------------------
One can use :class:`~gruvbox.GruvboxStyle`,
:class:`~gruvbox.ptgruvbox.PtGruvboxStyle`, and/or in any project that utilizes
pygments in addition to providing them as parameters for prompt_toolkit and the
``PromptSession`` class.

Additional tokens have been provided in the `PtGruvboxStyle` class for users to style
a non-IPython prompt-toolkit application.

Specifically, the `PtGruvboxStyle` class exists to providing them as parameters for
prompt_toolkit and the ``PromptSession`` class.


API
====

.. currentmodule:: gruvbox.gruvbox

.. autoclass:: GruvboxStyle
   :show-inheritance:

The `Gruvbox` class in the style module represents the main class of the
repository.

.. currentmodule:: gruvbox.ptgruvbox

.. autoclass:: PtGruvboxStyle
   :members:
   :show-inheritance:

This class is for use with prompt_toolkit applications, and as such,
provides a few utility methods not found in the super-classes.

Deprecated
-----------

.. currentmodule:: gruvbox.style

.. autoclass:: Gruvbox
   :no-show-inheritance:
   :no-members:


Contributing
============

The official source code for this library exists at
`<https://github.com/farisachugthai/Gruvbox-IPython>`_ and documentation
that details how this Pygments plugin was made can be found at
`<https://farisachugthai.github.io/Gruvbox-IPython/>`_.

Please open a pull request or an issue with any problems you see or any
changes you'd recommend to the source code!


License
========

MIT
