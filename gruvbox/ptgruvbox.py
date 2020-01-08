"""For use with shells constructed using prompt_toolkit."""
from prompt_toolkit.styles.pygments import style_from_pygments_cls

from .gruvboxdarkhard import GruvboxDarkHard


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
        self.styles = super().styles
        self.styles.extend(
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
