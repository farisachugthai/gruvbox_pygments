import sys
import unittest

from IPython.core.getipython import get_ipython
from traitlets.config import Configurable
from pygments.plugin import find_plugin_styles

from gruvbox.gruvboxdarkhard import GruvboxDarkHard


def setup_module():
    _ip = get_ipython()
    if _ip is not None:
        raise unittest.SkipTest()


class TestGruvboxDarkHard(unittest.TestCase):
    def setUp(self):
        self._ip = get_ipython()
        self.style = self._ip.highlighting_style
        self.colorscheme = self._ip.highlighting_style.style_rules

    def test_installation(self):
        # Probably the first one I should use actually
        self.assertExists(find_plugins_styles)

    def test_installation_contains_gruvbox(self):
        # TODO
        pass

    def test_background_color(self):
        """Practicing using the unittest module."""
        self.assertEqual(self.colorscheme.BACKGROUND_COLOR, "#edbdbb")


if __name__ == "__main__":
    # Believe it or not this is in fact necessary
    old_sys_argv = sys.argv[:]
    # DONT FORGET SPACES
    sys.argv = [sys.executable, " -m", " unittest", " -v"]
    # todo: add options
    unittest.main()
