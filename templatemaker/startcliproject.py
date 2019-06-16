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


def chmods(shellscripts: List[Text], rtdir: Text) -> None:
    """Changes user permissions of files. Returns None."""
    for el in shellscripts:
        os.chmod(Path(rtdir + "/" + el), 0o755)
    return None


def copy_file(file_: Text, name: Text, rtdir: Text) -> None:
    """Copies file_ to project. Returns None."""
    shutil.copy(file_, rtdir + "/" + name)
    return None


def edit_run(runlines: List[Text], rtdir: Text) -> None:
    """Writes to 'run' file. Returns None."""
    with open(rtdir + "/run", "w+") as f:
        for el in runlines:
            f.write(el)
            f.write("\n")
    return None


def make_dir(relpath: Text) -> None: 
    """Makes all dirs in 'relpath'. Makes a file if the end is a file.
       Returns None."""
    os.makedirs(relpath, exist_ok=True)
    return None


def make_main(dir_: Text) -> None:
    """Makes main script in '<project>/<project>/' dir. Returns None."""
    file_ = dir_.strip("./")
    Path(dir_ + "/" + dir_ + "/" + file_ + ".py").touch()
    return None


def make_subdirs(subdirs: List[Text], rtdir: Text) -> None:
    """Makes sub directories under the root dir. Returns None."""
    for el in subdirs:
        el = rtdir+"/"+str(el)
        if not Path(el).exists():
            Path(el).mkdir()
    return None


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
    return None

    
if __name__ == "__main__":
    projectname = input("Give the project a name: ")
    projectdir = "./" + str(projectname)

    subdirs = [projectdir, ".data", ".testdata", "docs", "tests"]
    runlines = ["#!/bin/bash", "python3 " + projectname + "/" \
                + projectname + ".py"]
    shellscripts = ["run", "Test"]
    current_path = str(Path(__file__).parents[0])

    # make dirs
    main = projectdir + "/" + projectdir + "/" + projectname + ".py"
    make_dir(main)
    make_subdirs(subdirs, projectdir)

    # edit files
    edit_run(runlines, projectdir)

    # copy from templates
    gitignore = current_path + "/gitignoretemplate.txt"
    license = current_path + "/licensetemplate.txt"
    readme = current_path + "/readmetemplate.txt"
    requirements = current_path + "/requirementstemplate.txt"
    testcmd = current_path + "/testcmdtemplate.txt"
    tests = current_path + "/teststemplate.txt"

    copy_file(gitignore, ".gitignore", projectdir)
    copy_file(license, "LICENSE", projectdir)
    copy_file(readme, "README", projectdir)
    copy_file(requirements, "requirements.txt", projectdir)
    copy_file(testcmd, "Test", projectdir)
    copy_file(tests, projectname+"_test.py", projectdir+"/tests/")

    # change file permissions
    chmods(shellscripts, projectdir)

    # update user
    showcreated(projectdir)
