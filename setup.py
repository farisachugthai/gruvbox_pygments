"""Setup IPython initialization files as it's own package.

Install gruvbox as a colorscheme in pygments, and we'll
also probably need to add the IPython doctest plugin somewhere.
"""
import codecs
import os
from setuptools import setup, find_packages

NAME = 'gruvbox_ipython'
AUTHOR = "Faris Chugthai",
EMAIL = "farischugthai@gmail.com",
DESCRIPTION = "Pygments style using the gruvbox color scheme."
LICENSE = "MIT",
KEYWORDS = "pygments gruvbox ipython jupyter colorschemes",
REQUIRED = ['pygments']

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = "\n" + f.read()

# Load the package's __version__.py module as a dictionary.
about = {'__version__': '0.0.1'}
# TODO:
# if not VERSION:
#     try:
#         with open(os.path.join(here, NAME, '__version__.py')) as f:
#             exec(f.read(), about)
#     except IOError:  # the file doesn't exist
#         about['__version__'] = None



setup(
        name=NAME,
        version=about['__version__'],
        description=DESCRIPTION,
        long_description=long_description,
        long_description_content_type='text/restructuredtext',
        author=AUTHOR,
        author_email=EMAIL,
        packages=find_packages(where='.'),
        entry_points=
        """
        [pygments.styles]
        Gruvbox = gruvbox.style:GruvboxStyle
        """,
        install_requires=REQUIRED,
        include_package_data=True,
        package_data={
            # If any package contains *.txt or *.rst files, include them:
            '': ['*.txt', '*.rst'],
        },
        license=LICENSE,

        classifiers=[
            # Trove classifiers
            # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python',
            'Programming Language :: Python :: Implementation :: CPython',
        ],
)
