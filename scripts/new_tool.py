from pathlib import Path
import argparse

TEMPLATE = """[project]
name = "{name}"
version = "0.1.0"

[project.scripts]
{name} = "{name}.cli:main"

[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"
"""

MAIN_FUNCTION = """def main():
    print("Hello from the {name} tool.")
"""

GITIGNORE_TEXT = """{name}.egg-info
{name}/__pycache__
build/
"""


def create_tool(name):
    project_root = Path(__file__).resolve().parent.parent
    
    root = project_root / "tools" / name
    package = root / name

    package.mkdir(parents=True)

    (package / "__init__.py").write_text("")
    (package / "cli.py").write_text(MAIN_FUNCTION.format(name=name))
    (root / "pyproject.toml").write_text(TEMPLATE.format(name=name))
    (root / ".gitignore").write_text(GITIGNORE_TEXT.format(name=name))


def main():
    parser = argparse.ArgumentParser(description="Simple script to initialize a new tool.")
    parser.add_argument("toolname", nargs=1, help="The name of the tool to be created.", type=str)

    args = parser.parse_args()
    create_tool(args.toolname[0])


if __name__ == "__main__":
    main()
