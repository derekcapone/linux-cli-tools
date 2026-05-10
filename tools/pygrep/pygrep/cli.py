import sys
from rich import print, inspect
from pygrep.rich_console import console

def main():
    print(sys.path)
    
    for line in sys.stdin:
        print(line, end="")


if __name__ == "__main__":
    main()
