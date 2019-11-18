#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Setup Gruvbox colorscheme as a python package."""
import codecs
import os
from setuptools import setup

NAME = 'gruvbox_ipython'
AUTHOR = "Faris Chugthai",
EMAIL = "farischugthai@gmail.com",
DESCRIPTION = "A Pygments style using the Gruvbox color scheme."
LICENSE = "MIT",
KEYWORDS = [
    'pygments', 'gruvbox'
    'ipython', 'jupyter', 'colorschemes', 'syntax highlighting'
]
REQUIRED = ['pygments>=2.4']

here = os.path.abspath(os.path.dirname(__file__))
README = os.path.join(here, 'README.rst')

try:
    with codecs.open(README, encoding="utf-8") as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

about = {}

PROJECT_SLUG = NAME.lower().replace("-", "_").replace(" ", "_")

try:
    with open(os.path.join(here, PROJECT_SLUG, '__version__.py')) as f:
        exec(f.read(), about)
except IOError:  # the file doesn't exist so hard code it
    about['__version__'] = '0.0.2'

setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/restructuredtext',
    author=AUTHOR,
    author_email=EMAIL,
    url='https://github.com/farisachugthai/Gruvbox-IPython',
    # packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    # If your package is a single module, use this instead of 'packages':
    py_modules=['gruvbox.style'],
    entry_points="""
        [pygments.styles]
        GruvboxDarkHard = gruvbox.style:GruvboxDarkHard
        GruvboxLight = gruvbox.style:GruvboxLightHard
        """,
    install_requires=REQUIRED,

    # is there a way i can do if extras_require inside of the function call?
    # extras_require=EXTRAS,
    include_package_data=True,
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst'],
    },
    keywords=KEYWORDS,
    license=LICENSE,
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Development Status :: 4 - Beta ',
        'Environment :: Plugins ',
        'Intended Audience :: Developers ',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Text Processing :: Filters',
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)
