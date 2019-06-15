# How to Structure a Project
[docs.python-guide.org][1]
Restructure the template project to meet these requirements.

### Main Dir
```bash
README.rst
LICENSE
setup.py
requirements.txt
sample/__init__.py
sample/core.py
sample/helpers.py
docs/conf.py
docs/index.rst
tests/test_basic.py
tests/test_advanced.py
```

I leave out `setup.py` for now. I need to study up on that one. I have my own script that sets up the files and directory structure called `startcliproject.py` that I use to setup a new project.

[1]: https://docs.python-guide.org/writing/structure/#structure-of-the-repository
