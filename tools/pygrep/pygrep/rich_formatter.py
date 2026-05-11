# Singleton console instance
from enum import Enum
from rich.console import Console
from rich.theme import Theme

INFO_THEME_STRING = "info"
MATCH_THEME_STRING = "match"

GREP_THEME = Theme({
    INFO_THEME_STRING: "dim cyan",
    MATCH_THEME_STRING: "bold red"
})

console = Console(theme=GREP_THEME)
