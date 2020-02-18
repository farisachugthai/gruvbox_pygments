"""For use with shells constructed using prompt_toolkit.

Still not 100% sure what's wrong with this class but if you enter
the recursive shell, (*AKA* IPython --> pdb, run interact --> IPython

The coloring on the prompt goes away with the highlighting style set to
`PtGruvbox`. Hrm.

"""
from prompt_toolkit.styles.pygments import style_from_pygments_cls

from .gruvbox import GruvboxStyle


class PtGruvboxStyle(GruvboxStyle):
    """Extends the previous GruvboxDarkHard classes.

    Adds in the prompt_toolkit token groups 'pygments.prompt',
    'pygments.promptnum', 'pygments.outprompt', and
    'pygments.outpromptnum'.

    IPython uses these token groups as well, as can be observed
    in the methods for the class :class:`IPython.terminal.prompts.Prompts`.

    In [15]: get_ipython().prompts.in_prompt_tokens()
    Out[15]:
    [(Token.Prompt, ''),
    (Token.Prompt, 'In ['),
    (Token.PromptNum, '15'),
    (Token.Prompt, ']: ')]

    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.styles.update(
            [
                ("pygments.prompt", "#a9b665"),
                ("pygments.promptnum", "#ansibrightgreen bold"),
                ("pygments.outprompt", "#ea6962"),
                ("pygments.outpromptnum", "#ansibrightred bold"),
            ]
        )

    @classmethod
    def create_prompt_toolkit_style(self):
        return style_from_pygments_cls(self)

#     def styles(self):
#         return
