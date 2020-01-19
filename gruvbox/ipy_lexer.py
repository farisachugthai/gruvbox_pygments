"""This is the example from pygments.

We could use this as a very easy hack to stop that error highlighting
when the lexer sees a python statement that starts with a :kbd:`!` or
:kbd:`%` at the beginning of magics.

FYI.

    In [46]: _ip.pt_app.lexer
    Out[46]: <IPython.terminal.ptutils.IPythonPTLexer at 0x151087677c0>

    In [47]: _ip.pt_app.lexer.python_lexer.pygments_lexer
    Out[47]: <pygments.lexers.PythonLexer with {'stripnl': False, 'stripall': False, 'ensurenl': False}


"""
from pygments.lexers.python import PythonLexer
from pygments.token import Keyword, Name


class MyPythonLexer(PythonLexer):
    # EXTRA_KEYWORDS = set(('foo', 'bar', 'foobar', 'barfoo', 'spam', 'eggs'))
    EXTRA_KEYWORDS = set("!")

    def get_tokens_unprocessed(self, text):
        for index, token, value in PythonLexer.get_tokens_unprocessed(self, text):
            # How silly is it that I just realized that class attributes
            # still bind to the instance object?
            if token is Name and value in self.EXTRA_KEYWORDS:
                yield index, Keyword.Pseudo, value
            else:
                yield index, token, value


class MyPythonLexer(PythonLexer):
    # EXTRA_KEYWORDS = set(('foo', 'bar', 'foobar', 'barfoo', 'spam', 'eggs'))
    EXTRA_KEYWORDS = set("!")

    def get_tokens_unprocessed(self, text):
        for index, token, value in PythonLexer.get_tokens_unprocessed(self, text):
            # How silly is it that I just realized that class attributes
            # still bind to the instance object?
            if token is Name and value in self.EXTRA_KEYWORDS:
                yield index, Keyword.Pseudo, value
            else:
                yield index, token, value
