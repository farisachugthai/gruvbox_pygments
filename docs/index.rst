.. Gruvbox IPython documentation master file, created by
   sphinx-quickstart on Wed Mar 27 09:54:40 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. include:: ../README.rst

Couldn't think of where else to put this. Is this gonna warrant a bug report?

.. code-block:: bash

   C:\Users\faris\projects\gruvbox_pygments Microsoft Windows [Version 10.0.18362.207]
   Sat 01/18/2020  (hotfix -> origin)
   λ ipython --TerminalInteractiveShell.highlighting_style=gruvbox

.. code-block:: py3tb

   Traceback (most recent call last):
     File "c:\python38\lib\runpy.py", line 193, in _run_module_as_main
       return _run_code(code, main_globals, None,
     File "c:\python38\lib\runpy.py", line 86, in _run_code
       exec(code, run_globals)
     File "C:\Python38\Scripts\ipython.exe\__main__.py", line 7, in <module>
       sys.exit(start_ipython())

     ...

     File "c:\python38\lib\site-packages\IPython\terminal\interactiveshell.py", line 184, in _highlighting_style_changed
       self.refresh_style()
     File "c:\python38\lib\site-packages\IPython\terminal\interactiveshell.py", line 187, in refresh_style
       self._style = self._make_style_from_name_or_cls(self.highlighting_style)
     File "c:\python38\lib\site-packages\IPython\terminal\interactiveshell.py", line 387, in _make_style_from_name_or_cls
       style_from_pygments_cls(style_cls),
     File "c:\python38\lib\site-packages\prompt_toolkit\styles\pygments.py", line 41, in style_from_pygments_cls
       assert issubclass(pygments_style_cls, PygmentsStyle)
   TypeError: issubclass() arg 1 must be a class


So you can see right there that prompt_toolkit raises an error because the style
that we provided to it was the class we wanted.

.. code-block:: bash

   C:\Users\faris\projects\gruvbox_pygments Microsoft Windows [Version 10.0.18362.207]
   Sat 01/18/2020  (hotfix -> origin)
   λ ipython --TerminalInteractiveShell.highlighting_style=gruvbox.Gruvbox

Problematically, that's not how pygments wants it!

.. code-block:: py3tb

   Traceback (most recent call last):
     File "c:\python38\lib\site-packages\pygments\styles\__init__.py", line 71, in get_style_by_name
       mod = __import__('pygments.styles.' + mod, None, None, [cls])
   ModuleNotFoundError: No module named 'pygments.styles.gruvbox'

   During handling of the above exception, another exception occurred:

   Traceback (most recent call last):
     File "c:\python38\lib\runpy.py", line 193, in _run_module_as_main
       return _run_code(code, main_globals, None,
     File "c:\python38\lib\runpy.py", line 86, in _run_code
       exec(code, run_globals)
     File "C:\Python38\Scripts\ipython.exe\__main__.py", line 7, in <module>
       sys.exit(start_ipython())

    ...

     File "c:\python38\lib\site-packages\IPython\terminal\interactiveshell.py", line 184, in _highlighting_style_changed
       self.refresh_style()
     File "c:\python38\lib\site-packages\IPython\terminal\interactiveshell.py", line 187, in refresh_style
       self._style = self._make_style_from_name_or_cls(self.highlighting_style)
     File "c:\python38\lib\site-packages\IPython\terminal\interactiveshell.py", line 376, in _make_style_from_name_or_cls
       style_cls = get_style_by_name(name_or_cls)
     File "c:\python38\lib\site-packages\pygments\styles\__init__.py", line 73, in get_style_by_name
       raise ClassNotFound("Could not find style module %r" % mod +
   pygments.util.ClassNotFound: Could not find style module 'gruvbox.Gruvbox'.

   If you suspect this is an IPython 7.11.1 bug, please report it at:
       https://github.com/ipython/ipython/issues
   or send an email to the mailing list at ipython-dev@python.org

   You can print a more detailed traceback right now with "%tb", or use "%debug"
   to interactively debug it.

   Extra-detailed tracebacks for bug-reporting purposes can be enabled via:
       c.Application.verbose_crash=True


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
