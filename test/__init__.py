#!
"""TODO: Add a package_name parameter to the ask_import function.

The only reason I'm putting functionality here is because it'll be needed
across the package.
"""
import importlib


def ask_import(mod):
    """Try to import things and fail silently otherwise."""
    try:
        return importlib.import_module(mod)
    except (ImportError, ModuleNotFoundError):
        pass

ask_import('gruvbox')
ask_import('IPython')
# ask_import(GruvboxDarkHard, package=gruvbox.style)
