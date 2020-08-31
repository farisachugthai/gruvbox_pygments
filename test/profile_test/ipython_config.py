#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging

from traitlets.config.application import get_config

log_datefmt = "%Y-%m-%d %H:%M:%S"
default_log_format = (
    "[ %(name)s : %(relativeCreated)d :] %(levelname)s : %(module)s : --- %(message)s "
)

logging.basicConfig(level=logging.INFO, format=default_log_format, datefmt=log_datefmt)

# ----------------------------------------------------------------------------
# TerminalIPythonApp(BaseIPythonApplication,InteractiveShellApp) configuration
# ----------------------------------------------------------------------------

c = get_config()

# Whether to display a banner upon starting IPython.
c.TerminalIPythonApp.display_banner = False

# If a command or file is given via the command-line, e.g. 'ipython foo.py',
#  start an interactive shell after executing the file or command.
c.TerminalIPythonApp.force_interact = False

# ---
# Class to use to instantiate the TerminalInteractiveShell object. Useful for
#  custom Frontends
# c.TerminalIPythonApp.interactive_shell_class =
# 'IPython.terminal.interactiveshell.TerminalInteractiveShell'


c.TerminalIPythonApplication.log_format = default_log_format

# Start IPython quickly by skipping the loading of config files.
# c.TerminalIPythonApp.quick = False

# Autoformatter to reformat Terminal code. Can be `'black'` or `None`
c.TerminalInteractiveShell.autoformatter = None

# Set to confirm when you try to exit IPython with an EOF (Control-D in Unix,
#  Control-Z/Enter in Windows). By typing 'exit' or 'quit', you can force a
#  direct exit without any confirmation.
c.TerminalInteractiveShell.confirm_exit = False

# The name or class of a Pygments style to use for syntax highlighting.
# To see available styles, run `pygmentize -L styles`.
# default, emacs, friendly, colorful, autumn, murphy, manni, monokai, perldoc,
# pastie, borland, trac, native, fruity, bw, vim, vs, tango, rrt, xcode, igor,
# paraiso-light, paraiso-dark, lovelace, algol, algol_nu, arduino, rainbow_dash

# Try to import my Gruvbox class. Can be found at
# https://github.com/farisachugthai/Gruvbox_IPython

try:
    from gruvbox.gruvbox import GruvboxStyle
except ImportError:
    from pygments.styles import inkpot

    c.TerminalInteractiveShell.highlighting_style = "inkpot"
else:
    c.TerminalInteractiveShell.highlighting_style = GruvboxStyle


# Use 24bit colors instead of 256 colors in prompt highlighting. If your
# terminal supports true color, the following command should print 'TRUECOLOR'
# in orange: printf "\x1b[38;2;255;100;0mTRUECOLOR\x1b[0m\n"
c.TerminalInteractiveShell.true_color = True
