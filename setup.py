#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Setup Gruvbox colorscheme as a python package."""
import codecs
import os
import runpy
import setuptools
from setuptools import setup, find_packages

import pkg_resources

try:
    import gruvbox
except ImportError:
    pass

NAME = "gruvbox_pygments"

AUTHOR = ("Faris Chugthai",)
EMAIL = ("farischugthai@gmail.com",)
DESCRIPTION = "A Pygments style using the Gruvbox color scheme."
LICENSE = ("MIT",)
KEYWORDS = [
    "pygments",
    "gruvbox" "ipython",
    "jupyter",
    "colorschemes",
    "syntax highlighting",
]
REQUIRED = ["pygments>=2.4"]
TESTS=["pytest", "IPython"]

here = os.path.abspath(os.path.dirname(__file__))
README = os.path.join(here, "README.rst")

try:
    with codecs.open(README, encoding="utf-8") as f:
        long_description = "\n" + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

about = {}

try:
    f = os.path.join(here, "gruvbox", "__version__.py")
    ret = runpy.run_path(f)
    about = ret["about"]
except OSError:  # the file doesn't exist so hard code it
    about = {"__version__": "0.0.2"}

setup(
    name=NAME,
    version=about["__version__"],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/restructuredtext",
    author=AUTHOR,
    author_email=EMAIL,
    url="https://github.com/farisachugthai/gruvbox_pygments",
    # packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    packages=find_packages(),
    entry_points="""
        [pygments.styles]
        GruvboxStyle = gruvbox:GruvboxStyle
        PtGruvboxStyle = gruvbox:PtGruvboxStyle
        """,
    # namespace_packages=setuptools.find_namespace_packages(),
    install_requires=REQUIRED,
    tests_require=TESTS,
    extras_require={"docs": "sphinx", "IPython": "ipython", "test": TESTS},
    platforms="any",
    include_package_data=True,
    package_data={"": ["*.txt", "*.rst"],},
    keywords=KEYWORDS,
    license=LICENSE,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 4 - Beta ",
        "Environment :: Plugins ",
        "Intended Audience :: Developers ",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: Filters",
        "Topic :: Utilities",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)
