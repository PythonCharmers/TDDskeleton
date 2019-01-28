# TDDskeleton
The purpose of this is to allow you to quickly get started with test driven development without getting bogged down in setting up a testing pipeile.

This uses [tox](https://tox.readthedocs.io/en/latest/) to set up a full testing pipeline for the code that is installed via `setup.py` which in this case is the package you can put in the `app/` folder.

After you have installed `tox` as per the installation steps below it's as simple as running `tox` from the command line to get the following testing pipeline run:

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