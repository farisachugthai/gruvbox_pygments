"""Setup IPython initialization files as it's own package.

Install gruvbox as a colorscheme in pygments, and we'll
also probably need to add the IPython doctest plugin somewhere.
"""
import codecs
import os
from setuptools import setup

NAME = 'gruvbox_ipython'
AUTHOR = "Faris Chugthai",
EMAIL = "farischugthai@gmail.com",
DESCRIPTION = "Pygments style using the gruvbox color scheme."
LICENSE = "MIT",
KEYWORDS = "pygments gruvbox ipython jupyter colorschemes",
REQUIRED = ['pygments']

here = os.path.abspath(os.path.dirname(__file__))


# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with codecs.open(os.path.join(here, "README.rst"), encoding="utf-8") as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

# Load the package's __version__.py module as a dictionary.
about = {}

PROJECT_SLUG = NAME.lower().replace("-", "_").replace(" ", "_")

# For those moments when you forget your iskeyword necessities
try:
    with open(os.path.join(here, PROJECT_SLUG, '__version__.py')) as f:
        exec(f.read(), about)
except IOError:  # the file doesn't exist so hard code it
    about['__version__'] = '0.0.1'

setup(
        name=NAME,
        version=about['__version__'],
        description=DESCRIPTION,
        long_description=long_description,
        long_description_content_type='text/restructuredtext',
        author=AUTHOR,
        author_email=EMAIL,
        # packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
        # If your package is a single module, use this instead of 'packages':
        # py_modules=['mypackage'],

        entry_points=
        """
        [pygments.styles]
        Gruvbox = gruvbox.style:GruvboxStyle
        """,
        install_requires=REQUIRED,
        # is there a way i can do if extras_require inside of the function call?
        # extras_require=EXTRAS,
        include_package_data=True,
        package_data={
            # If any package contains *.txt or *.rst files, include them:
            '': ['*.txt', '*.rst'],
        },
        license=LICENSE,

        # TODO: Need to install on py2 and make sure this works but pygments
        # should
        classifiers=[
            # Trove classifiers
            # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: Implementation :: CPython',
            'Programming Language :: Python :: Implementation :: PyPy'
        ],
)
