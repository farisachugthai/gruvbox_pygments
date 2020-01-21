import copy
import reprlib
# from pygments.style import Style
from pygments.token import (
    Comment,
    Error,
    Escape,
    Generic,
    Keyword,
    Literal,
    Name,
    Number,
    Operator,
    Other,
    Punctuation,
    String,
    Text,
    Token,
    Whitespace,
)

from pygments.style import Style
# from prompt_toolkit.styles import Style

try:
    from IPython.core.getipython import get_ipython
except ImportError:
    shell = None
else:
    shell = get_ipython()

__all__ = ["GruvboxDarkHard"]


class GruvboxHard(Style):
    """Retro groove color scheme for Pygments.

    Extends previous repositories that have ported Gruvbox to Pygments, and
    adds in new definitions for different tokens.

    """

    default_style = ""

    # Palette: {{{1
    BG0_HARD = "#1d2021"

    DARK1 = "#3c3836"  # 60-56-54
    DARK2 = "#504945"  # 80-73-69
    DARK3 = "#665c54"  # 102-92-84

    # Comments
    GRAY_245 = "#928374"  # 146-131-116

    LIGHT0_HARD = "#f9f5d7"  # 249-245-215
    LIGHT0 = "#fbf1c7"  # 253-244-193
    # light0_soft = '#f2e5bc'  # 242-229-188
    FG1 = "#ebdbb2"  # 235-219-178
    FG2 = "#d5c4a1"  # 213-196-161
    FG3 = "#bdae93"  # 189-174-147
    LIGHT4 = "#a89984"  # 168-153-132

    BRIGHT_RED = "#fb4934"  # 251-73-52
    BRIGHT_ORANGE = "#fe8019"  # 254-128-25
    BRIGHT_YELLOW = "#fabd2f"  # 250-189-47
    BRIGHT_GREEN = "#b8bb26"  # 184-187-38
    BRIGHT_BLUE = "#83a598"  # 131-165-152
    BRIGHT_PURPLE = "#b16286"
    BRIGHT_AQUA = "#8ec07c"  # 142-192-124

    RED = "#cc241d"
    ORANGE = "#d65d0e"  # 214-93-14
    GREEN = "#8ec07c"
    BLUE = "#458588"
    PURPLE = "#d3869b"  # 211-134-155
    # }}}

    background_color = BG0_HARD
    # highlight_color = SELECTION

    styles = {
        Comment: GRAY_245,  # class:'c'
        Comment.Hashbang: GRAY_245,  # class: 'ch'
        Comment.Multiline: BRIGHT_YELLOW + " italic",  # class: 'cm'
        # Comment.Preproc: BRIGHT_AQUA,  # class: 'cp'
        # Comment.PreprocFile: 'cpf',
        Comment.Single: GRAY_245 + " italic",  # class: 'c1'
        # Comment.Special: ,  # class: 'cs'
        Escape: DARK3,  # class: 'Esc'
        Error: BRIGHT_RED + " bold",  # class: 'Err'
        Generic: LIGHT0,  # class: 'g'
        Generic.Deleted: BRIGHT_RED,  # class: 'gd'
        Generic.Emph: "italic ",  # class: 'ge'
        Generic.Heading: BRIGHT_GREEN + " bold",  # class: 'gh'
        Generic.Inserted: LIGHT0_HARD,  # class: 'gi'
        Generic.Output: FG2,  # class: 'go'
        Generic.Prompt: FG1,  # class: 'gp'
        Generic.Strong: FG1 + " bold",  # class: 'gs'
        Generic.Subheading: BRIGHT_GREEN + " bold",  # class: 'gu'
        # Generic.Traceback  # class: 'gt'
        Keyword: BRIGHT_RED,  # class: 'k'
        Keyword.Constant: BRIGHT_ORANGE,  # class: 'kc'
        Keyword.Declaration: BRIGHT_ORANGE,  # class: 'kd'
        # Keyword.Namespace: 'kn',
        # class: 'kp', the NumPy Lexer registers tokens as this class
        Keyword.Pseudo: BRIGHT_GREEN,
        Keyword.Reserved: BLUE,  # class: 'kr',
        Keyword.Type: BRIGHT_YELLOW,  # class: 'kt'
        # The fully qualified name for these tokens is Token.Name.*
        Name: FG1,  # class: 'n'
        Name.Attribute: "noinherit " + BRIGHT_GREEN,  # class: 'na'
        Name.Builtin: "noinherit " + BRIGHT_YELLOW,  # class: 'nb'
        # Name.Builtin.Pseudo: 'bp',
        Name.Class: "noinherit " + BRIGHT_ORANGE,  # class: 'nc',
        Name.Constant: "noinherit " + BRIGHT_PURPLE,  # class: 'no'
        Name.Decorator: "noinherit " + BRIGHT_YELLOW,  # class: 'nd'
        Name.Entity: "noinherit " + BRIGHT_YELLOW,  # class: 'ni'
        Name.Exception: "bold " + BRIGHT_RED,  # class: 'ne'
        # Consider this the same as `:hi Function`
        Name.Function: "noinherit " + GREEN,
        # dunder methods
        Name.Function.Magic: "noinherit " + BRIGHT_AQUA,  # class: 'fm'
        Name.Label: "noinherit " + BRIGHT_RED,  # class: 'nl'
        # import statements
        Name.Namespace: "noinherit " + BRIGHT_AQUA,  # class: 'nn',
        # Name.Other: 'nx',
        Name.Property: BRIGHT_AQUA,  # class: 'py'
        Name.Tag: "noinherit " + BRIGHT_RED,  # class: 'nt'
        Name.Variable: FG1,  # class: 'nv'
        # Name.Variable.Class: 'noinherit ' + BRIGHT_BLUE,  # class: 'vc'
        # Name.Variable.Global: 'noinherit ' + BRIGHT_BLUE,  # class: 'vg'
        # Name.Variable.Instance: 'noinherit ' + BRIGHT_BLUE,  # class:'vi'
        # Name.Variable.Magic: 'noinherit ' + BRIGHT_BLUE,  # class: 'vm'
        Literal: "noinherit " + BRIGHT_ORANGE,  # class: 'l'
        Literal.Date: "noinherit " + BRIGHT_GREEN,  # class: 'ld',
        # These tokens have the FQDN Token.Literal.String.*
        String: BRIGHT_GREEN,  # class: 's'
        # String.Affix: BRIGHT_ORANGE,  # class: 'sa',
        # Literally matches `.* lol
        String.Backtick: LIGHT4,  # class: 'sb',
        String.Char: "noinherit " + PURPLE,  # class: 'sc',
        # String.Delimiter: 'dl',
        String.Doc: GRAY_245,  # class: 'sd',
        # String.Double: 's2',
        # String.Escape: 'se',
        # String.Heredoc: 'sh',
        # Interpolated strings!
        String.Interpol: BRIGHT_GREEN,  # class 'si',
        # String.Other: BRIGHT_GREEN,  # class: 'sx'
        String.Regex: BRIGHT_YELLOW,  # class: 'sr',
        # String.Single: 's1',
        # String.Symbol: FG2,  # class: 'ss',
        # String.Symbol: BRIGHT_BLUE,
        # These fully qualified name for these tokens is Token.Literal.Number*
        Number: BRIGHT_ORANGE,  # class: 'm',
        # Number.Bin: 'mb',
        # Number.Float:  # class: 'mf',
        # Number.Hex: 'mh',
        # Number.Integer: 'mi',
        # Number.Integer.Long: 'il',
        # Number.Oct: 'mo',
        Punctuation: FG1,  # class: 'p'
        Operator: BRIGHT_ORANGE,  # class: 'o'
        # Operator.Word: RED,  # class: 'ow'
        # really hard to read
        # Operator.Word: 'noinherit ' + BRIGHT_RED,
        Text: FG1,  # class: 't'
        # treating this key as Vim's Identifier token.
        Text.Whitespace: "",  # class: 'w'
    }

    if shell is not None:
        styles.update(
            {
                Token.Prompt: BRIGHT_GREEN,
                Token.PromptNum: "bold {}".format(BRIGHT_GREEN),
                Token.OutPrompt: BRIGHT_GREEN,
                Token.OutPromptNum: BRIGHT_GREEN,
                # TODO:
                # Token.Menu.Completions.Completion
                # Token.Menu.Completions.Completion.Current
                # Token.MatchingBracket.Other
                # For prompt_toolkit
                # Token.bottom-toolbar: FG3 + "bg:" + DARK1,
                # TODO:
                # Token.bottom-toolbar.text:
            }
        )

    # I think this is a reasonable way of checking if we're in IPython or not

    def __repr__(self):
        """Return repr representation."""
        return "<{}:> {}".format(
            self.__class__.__name__, reprlib.Repr().repr_dict(self.styles, 6)
        )

    def __eq__(self, other):
        """Check if style is the same as the other."""
        return self.styles == other.styles

    def __copy__(self):
        return copy(self.styles)


class GruvboxDarkHard(GruvboxHard):
    def __init__(self, style_overrides=None, *args, **kwargs):
        """Call the super method."""
        super().__init__()
        if style_overrides is not None:
            self.styles.update(style_overrides)

    def style_rules(self):
        return self.styles
