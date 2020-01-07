
from prompt_toolkit.styles.pygments import style_from_pygments_cls
from .gruvboxdarkhard import GruvboxDarkHard

class PtGruvbox(GruvboxDarkHard):
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
