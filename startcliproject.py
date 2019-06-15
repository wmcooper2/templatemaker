#!/usr/bin/env python3
"""This module sets up a new project.
    Creates these files; 
        - NOTES.md
        - README.md
        - LICENSE
        - 'run' shell command file
        - 'test' shell command file
        - <projectname>.py

    Creates these dirs;
        - .gitignore/
        - <project>/
        - <project>/<project>/
        - .data/
        - .testdata/
"""

#stand lib
from glob import glob
import os
from pathlib import Path
import shutil
from typing import List
from typing import Text

projectname = input("Give the project a name: ")
projectdir = "./"+str(projectname)
subdirs = [projectdir, ".data", ".testdata", "docs", "tests"]
files = ["NOTES.md", "README.md", ".gitignore", "run", "Test",
         "requirements.txt"]
testlines = ["#!/bin/bash", "pytest **/*_test.py"]
gitignores = [".gitignore", "NOTES.md", "data/", "testdir/",
              "__pycache__/", ".pytest_cache/", ".mypy_cache/",
              "*.conf", "*.ini", ".git/", ".DS_Store/", ".testdata/",
              "testdata/"]
runlines = ["#!/bin/bash", "python3 " + projectname + "/" \
            + projectname + ".py"]
shellscripts = ["run", "Test"]

def make_rootdir(rtdir: Text) -> None:
    """Makes project root dir. Returns None."""
    if not Path(rtdir).exists():
        Path(rtdir).mkdir()

def make_subdirs(subdirs: List[Text], rtdir: Text) -> None:
    """Makes sub directories under the root dir. Returns None."""
    for el in subdirs:
        el = rtdir+"/"+str(el)
        if not Path(el).exists():
            Path(el).mkdir()

def make_files(files: List[Text], rtdir: Text) -> None:
    """Makes files under the root dir. Returns None."""
    for el in files:
        el = rtdir+"/"+str(el)
        if not Path(el).exists():
            Path(el).touch()

def edit_test(testlines: List[Text], rtdir: Text) -> None:
    """Writes to 'Test' file. Returns None."""
    with open(rtdir + "/Test", "w+") as f:
        for el in testlines:
            f.write(el)
            f.write("\n")

def edit_gitignore(gitignores: List[Text], rtdir: Text):
    """Writes to '.gitignore'. Returns None."""
    with open(rtdir + "/.gitignore", "w+") as f:
        for el in gitignores:
            f.write(el)
            f.write("\n")

def edit_run(runlines: List[Text], rtdir: Text) -> None:
    """Writes to 'run' file. Returns None."""
    with open(rtdir + "/run", "w+") as f:
        for el in runlines:
            f.write(el)
            f.write("\n")

def chmods(shellscripts: List[Text], rtdir: Text) -> None:
    """Changes user permissions of files. Returns None."""
    for el in shellscripts:
        os.chmod(Path(rtdir + "/" + el), 0o755)

def makemain(dir_: Text) -> None:
    """Makes main script in '<project>/<project>/' dir. Returns None."""
    file_ = dir_.strip("./")
    Path(dir_ + "/" + dir_ + "/" + file_ + ".py").touch()

def showcreated(rtdir: Text) -> None:
    """Shows the files and dirs that were created. Returns None."""
    print("These files and dirs were created...")
    for path_ in Path(rtdir).iterdir():
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
    make_rootdir(projectdir)
    make_subdirs(subdirs, projectdir)
    make_files(files, projectdir)
    copy_license()
    edit_test(testlines, projectdir)
    edit_run(runlines, projectdir)
    edit_gitignore(gitignores, projectdir)
    chmods(shellscripts, projectdir)
    makemain(projectdir)
    showcreated(projectdir)
