"""Initialize the Gruvbox package."""
import logging
import os
import sys

logging.getLogger(__name__).addHandler(logging.NullHandler())

sys.path.insert(0, os.path.dirname(os.path.abspath('.')))
