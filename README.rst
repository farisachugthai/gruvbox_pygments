=========================================================
Gruvbox IPython --- A Pygments Style Designed for IPython
=========================================================

.. module:: readme
    :synopsis: A Pygments Style Designed for IPython

`Gruvbox <https://github.com/morhetz/gruvbox>`_ is a phenomenal colorscheme for
Vim, and gives a fantastic base for any terminal based application.

According to it's author:

    Designed as a bright theme with pastel 'retro groove' colors and light/dark
    mode switching in the way of solarized. The main focus when developing
    gruvbox is to keep colors easily distinguishable, contrast enough and still
    pleasant for the eyes.

To an impressive extent `Gruvbox <https://github.com/morhetz/gruvbox>`_ achieves this.

So why this repository?

Despite it's popularity as a Vim colorscheme, I have yet to find a faithful
port of `Gruvbox <https://github.com/morhetz/gruvbox>`_ to :mod:`Pygments`.

Installation
------------
To install simply ``git clone`` this repository and run the following in your
terminal of choice.


.. code-block:: shell-session

    python setup.py build && python -m pip install -U -e .


If you prefer to use the Conda environment manager from Continuum Analytics,
one can alternatively run:

.. code-block:: shell-session

   python setup.py build
   python setup.py install
   conda develop .

while in the root of the repository.


Setup
-----
To use this colorscheme in :mod:`IPython`, navigate to ``$HOME/.ipython`` and
create/edit your ``ipython_config.py`` file like so:

.. code-block:: python3

    from traitlets.config import get_config
    c = get_config()
    c.TerminalInteractiveShell.highlighting_style = 'Gruvbox'

Pygments colorschemes can be used for a wide variety of applications; however,
and limiting it's use to only IPython is not necessary. For example, the Sphinx
documentation project also uses Pygments when highlighting blocks of code!

Contributing
------------

The official source code for this library exists at 
`<https://github.com/farisachugthai/Gruvbox-IPython>`_ and documentation that details
*in gruesome detail* how this Pygments plugin was made can be found at
`<https://farisachugthai.github.io/Gruvbox-IPython/>`_.


Please open a pull request or an issue with any problems you see or any changes
you'd recommend to the source code!

License
--------
MIT
