import sys
import unittest

from gruvbox.gruvboxdarkhard import GruvboxDarkHard


class TestGruvboxDarkHard(unittest.TestCase):

     def setUp(self):
         self._ip = get_ipython()
         self.colorscheme = self._ip.styles.style_rules

     def test_background_color(self):
         """Practicing using the unittest module."""
         self.assertEqual(self.colorscheme.BACKGROUND_COLOR, '#edbdbb')


if __name__ == "__main__":
    unittest.main()
