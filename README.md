# TDDskeleton
The purpose of this is to allow you to quickly get started with test driven development without getting bogged down in setting up a testing pipeile.

This uses [tox](https://tox.readthedocs.io/en/latest/) to set up a full testing pipeline for the code that is installed via `setup.py` which in this case is the package you can put in the `app/` folder.

After you have installed `tox` as per the installation steps below you just have to write your tests in `tests/` and your code in `app/` then run the `tox` command.

Doing this will get you the following testing pipeline run:

- pylint
- mypy
- pytest
- coverage

## Installation

There's some Python packages that you need to install in order to get started.

These are found in `test_requirements.txt`, install with:

```bash
pip install -U pip
pip install -r test_requirements.txt
```

(Updating pip may not be required but is recommended)

## Usage

There's a folder called `app/` that contains a python package.

You can write tests for code that resides in `app/` in the `tests/` folder.

To run the test suite just issue the command `tox` and it will then run the test suite.

### Packages

Because this is structured in such a way that it installs your code as a package via `setup.py`, you will need to set up any package dependencies your code has in `setup.py`.

Go to `setup.py` and add any packages you depend on into the list for `install_requires`.

## How to setup test-driven development for your own project:

1. Clone https://github.com/PythonCharmers/TDDskeleton
2. Copy these files to your project folder:
    - setup.py (and modify it)
    - tox.ini
3. Add `tox` to your project's `requirements.txt` file.
4. pip install -r `requirements.txt`
5. Change every reference to `app` in `setup.py` and `tox.ini` to your package name.
6. Update `tox.ini` to refer to the location of your `requirements.txt` if renamed or somewhere else.
7. Ensure you have a `tests` folder with at least one `test_....py` file.

Now run
```
tox
```
