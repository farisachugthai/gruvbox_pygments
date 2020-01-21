"""For use with shells constructed using prompt_toolkit.

Here's some info.::

    In [15]: from prompt_toolkit.styles import default_pygments_style

    In [16]: default_pygments_style().style_rules
    Out[16]:
    [('pygments.whitespace', '#bbbbbb'),
    ('pygments.comment', 'italic #408080'),
    ('pygments.comment.preproc', 'noitalic #bc7a00'),
    ('pygments.keyword', 'bold #008000'),
    ('pygments.keyword.pseudo', 'nobold'),
    ('pygments.keyword.type', 'nobold #b00040'),
    ('pygments.operator', '#666666'),
    ('pygments.operator.word', 'bold #aa22ff'),
    ('pygments.name.builtin', '#008000'),
    ('pygments.name.function', '#0000ff'),
    ('pygments.name.class', 'bold #0000ff'),
    ('pygments.name.namespace', 'bold #0000ff'),
    ('pygments.name.exception', 'bold #d2413a'),
    ('pygments.name.variable', '#19177c'),
    ('pygments.name.constant', '#880000'),
    ('pygments.name.label', '#a0a000'),
    ('pygments.name.entity', 'bold #999999'),
    ('pygments.name.attribute', '#7d9029'),
    ('pygments.name.tag', 'bold #008000'),
    ('pygments.name.decorator', '#aa22ff'),
    ('pygments.literal.string', '#ba2121'),
    ('pygments.literal.string.doc', 'italic'),
    ('pygments.literal.string.interpol', 'bold #bb6688'),
    ('pygments.literal.string.escape', 'bold #bb6622'),
    ('pygments.literal.string.regex', '#bb6688'),
    ('pygments.literal.string.symbol', '#19177c'),
    ('pygments.literal.string.other', '#008000'),
    ('pygments.literal.number', '#666666'),
    ('pygments.generic.heading', 'bold #000080'),
    ('pygments.generic.subheading', 'bold #800080'),
    ('pygments.generic.deleted', '#a00000'),
    ('pygments.generic.inserted', '#00a000'),
    ('pygments.generic.error', '#ff0000'),
    ('pygments.generic.emph', 'italic'),
    ('pygments.generic.strong', 'bold'),
    ('pygments.generic.prompt', 'bold #000080'),
    ('pygments.generic.output', '#888'),
    ('pygments.generic.traceback', '#04d'),
    ('pygments.error', 'border:#ff0000')]

"""
from prompt_toolkit.styles.pygments import style_from_pygments_cls

from gruvbox.gruvboxdarkhard import GruvboxDarkHard


class PtGruvbox(GruvboxDarkHard):
    """Extends the previous GruvboxDarkHard classes.

    Adds in the prompt_toolkit token groups 'pygments.prompt',
    'pygments.promptnum', 'pygments.outprompt', and
    'pygments.outpromptnum'.

    IPython uses these token groups as well, as can be observed
    in the methods for the class :class:`IPython.terminal.prompts.Prompts`.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.styles.update(
            [
                ("pygments.prompt", "#009900"),
                ("pygments.promptnum", "#ansibrightgreen bold"),
                ("pygments.outprompt", "#990000"),
                ("pygments.outpromptnum", "#ansibrightred bold"),
            ]
        )

    @classmethod
    def create_prompt_toolkit_style(self):
        return style_from_pygments_cls(self)

#     def styles(self):
#         return
