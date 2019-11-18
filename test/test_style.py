#!
"""Bout to leave right now so here's a quick unit test to leave myself a
bookmark of where I was at when I come back.

I can easily imagine this being a really useful way of leaving myself
remiders in the future.
"""
import sys
import unittest

from gruvbox.style import GruvboxDarkHard


class TestGruvboxDarkHard:

    def setUp(self):
        start_ipython()
        self._ip = get_ipython()
        if not self._ip:
            sys.exit()
        self.colorscheme = _ip.styles.style_rules

    def test_background_color(self):
        """Practicing using the unittest module."""
        unittest.assertEqual(self.colorscheme.BACKGROUND_COLOR, '#edbdbb')


if __name__ == "__main__":
    try:
        import IPython
        from IPython import get_ipython, start_ipython
    except ImportError:
        IPython = None

    unittest.Skipif(IPython is None)

