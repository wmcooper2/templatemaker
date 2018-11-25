#!/usr/bin/env python3
"""This module sets up a new project.
    Creates these files and dirs;
        - NOTES.md
        - README.md
        - 'run' shell command file
        - 'test' shell command file
        - .gitignore
        - <root>/ (specified by user)
        - src/
        - data/
        - testdata/
"""

#stand lib
from pathlib import Path

dirs    = ["src", "data", "testdata"]
files   = ["NOTES.md", "README.md", ".gitignore"]

rootdir = input("Give the project a name: ")
rootdir = "./"+str(rootdir)

def make_run():
    """"""
    pass

def make_test():
    """"""
    pass

def make_files():
    """Makes files under the root dir. Returns None."""
    for el in files:
        el = rootdir+"/"+str(el)
        if not Path(el).exists():
            Path(el).touch()


def make_subdirs():
    """Makes sub directories under the root dir. Returns None."""
    for el in dirs:
        el = rootdir+"/"+str(el)
        if not Path(el).exists():
            Path(el).mkdir()

def make_rootdir():
    """Makes project root dir. Returns None."""
    if not Path(rootdir).exists():
        Path(rootdir).mkdir()

if __name__ == "__main__":
    make_rootdir()
    make_subdirs()
#    make_run()
#    make_test()
    make_files()



