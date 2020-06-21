#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import unittest

from IPython.testing.globalipapp import get_ipython
from traitlets.config import Configurable
from traitlets.traitlets import TraitError
from pygments.plugin import find_plugin_styles
from pygments.token import Token
from pygments.util import ClassNotFound

from gruvbox.gruvbox import GruvboxStyle


# def setup_module():
#     _ip = get_ipython()
#     if _ip is None:
#         raise unittest.SkipTest("Run inside IPython shell")
def start_test_ip():
    from IPython.terminal.interactiveshell import TerminalInteractiveShell

    return TerminalInteractiveShell()


class TestGruvboxStyleAndIPython(unittest.TestCase):
    """Practicing using the unittest module."""

    def setUp(self):
        self._ip = get_ipython()
        if self._ip is None:
            self._ip = start_test_ip()

        self.style = GruvboxStyle()
        # self.colorscheme = self._ip.highlighting_style.style_rules
        self.colorscheme = self.style.style_rules

    def test_installation_smoketest(self):
        # Probably the first one I should use actually
        find_plugin_styles()

    def test_installation_contains_gruvbox(self):
        # TODO
        pass

    def test_background_color(self):
        self.assertEqual(self.colorscheme[Token.Generic], "#ebdbb2")
        # self.assertIn(self.colorscheme.keys(), "#edbdbb")
        # requires str on left side....why?

    def test_class(self):
        # Admittedly tautological. More of the idea here is to show whether to
        # pass an instance, a class, a str of the class and what have you
        # whether it raises upon assignment. For example, see test_instance
        self._ip.highlighting_style = GruvboxStyle
        self.assertIsInstance(self._ip.highlighting_style(), GruvboxStyle)

    def test_instance(self):
        with self.assertRaises(TraitError):
            self._ip.highlighting_style = GruvboxStyle()
            # self.assertIsInstance(self._ip.highlighting_style, GruvboxStyle)

    def test_str(self):
        self._ip.highlighting_style = "GruvboxStyle"
        # self.assertExists(self._ip.highlighting_style)

    def test_case_sensitivity(self):
        with self.assertRaises(ClassNotFound):
            self._ip.highlighting_style = "gruvboxstyle"


if __name__ == "__main__":
    # Believe it or not this is in fact necessary
    old_sys_argv = sys.argv[:]
    # DONT FORGET SPACES
    sys.argv = [sys.executable, " -m", " unittest", " -v"]
    # todo: add options
    unittest.main()
