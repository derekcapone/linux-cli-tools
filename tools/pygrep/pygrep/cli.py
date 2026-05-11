import sys
from rich import print, inspect
import pygrep.rich_formatter as rf
import re
import typer

console = rf.console


def match_and_output_substrings(substring: str, full_string: str):
    matches = list(re.finditer(substring, full_string))
    if not matches: 
        return
    
    working_str = ""
    last_index = 0
    for match in matches:
        working_str += full_string[last_index:match.start()] 
        working_str += f"[{rf.MATCH_THEME_STRING}]{substring}[/]"
        last_index = match.end()
    working_str += full_string[last_index:]
    
    console.print(working_str)


def app(str_to_match: str):
    for line in sys.stdin:
        clean_line = line.rstrip("\n")
        match_and_output_substrings(str_to_match, clean_line)


def main():
    typer.run(app)


if __name__ == "__main__":
    main()
