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
from glob import glob
import os
from pathlib import Path
import shutil

rootdir     = input("Give the project a name: ")
rootdir     = "./"+str(rootdir)
subdirs     = ["src", "data", "testdata"]
files       = ["NOTES.md", "README.md", ".gitignore", "run", "Test"]
testlines   = ["#!/bin/bash", "pytest **/*_test.py"]
gitignores  = [".gitignore", "NOTES.md", "data/", "testdir/"]
runlines    = ["#!/bin/bash", "python3 src/"+rootdir.strip("./")+".py"]
shellscripts= ["run", "Test"]

def make_rootdir(rootdir):
    """Makes project root dir. Returns None."""
    if not Path(rootdir).exists():
        Path(rootdir).mkdir()

def make_subdirs(subdirs):
    """Makes sub directories under the root dir. Returns None."""
    for el in subdirs:
        el = rootdir+"/"+str(el)
        if not Path(el).exists():
            Path(el).mkdir()

def make_files(files):
    """Makes files under the root dir. Returns None."""
    for el in files:
        el = rootdir+"/"+str(el)
        if not Path(el).exists():
            Path(el).touch()

def edit_test(testlines):
    """Writes to 'Test' file. Returns None."""
    with open(rootdir+"/Test", "w+") as f:
        for el in testlines:
            f.write(el)
            f.write("\n")

def edit_gitignore(gitignores):
    """Writes to '.gitignore'. Returns None."""
    with open(rootdir+"/.gitignore", "w+") as f:
        for el in gitignores:
            f.write(el)
            f.write("\n")

def edit_run(runlines):
    """Writes to 'run' file. Returns None."""
    with open(rootdir+"/run", "w+") as f:
        for el in runlines:
            f.write(el)
            f.write("\n")

def chmods(shellscripts):
    """Changes user permissions of files. Returns None."""
    for el in shellscripts:
        os.chmod(Path(rootdir+"/"+el), 0o755)

def makemain(rootdir):
    """Makes the main script in <root>/src/ dir. Returns None."""
    main = rootdir.strip("./")
    Path(rootdir+"/src/"+main+".py").touch()

def showcreated():
    """Shows the files and dirs that were created. Returns None."""
    print("These files and dirs were created...")
    for path_ in Path(rootdir).iterdir():
        if path_.is_file():
            print(path_)
        else:
            print(path_)
            for sub in Path(path_).iterdir():
                print(sub)

def copy_license():
    """Copies MIT license to rootdir. Returns None."""
    pass
    
if __name__ == "__main__":
    make_rootdir(rootdir)
    make_subdirs(subdirs)
    make_files(files)
    copy_license()
    edit_test(testlines)
    edit_run(runlines)
    edit_gitignore(gitignores)
    chmods(shellscripts)
    makemain(rootdir)
    showcreated()
