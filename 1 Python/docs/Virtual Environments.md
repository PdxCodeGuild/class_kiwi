# VirtualEnv

- [Overview](#overview)
- [Install](#install)
- [Create](#create)
- [Activate](#activate)
- [Running Python](#running-python)
- [Freeze](#freeze)
- [Installing](#installing)
- [Deactivate](#deactivate)


## Overview

If your Python interpreter and packages are installed globally, how can you run multiple different Python programs, each with its own interpreter and package dependencies? A **virtualenv** is a way to isolate dependencies and swap them out quickly as we move between them. A virtualenv is an isolated installation of Python and packages, it is just a directory that contains a version of the Python interpreter, the standard library, a set of installed packages, and some scripts to enable and disable itself. You can read more about virtualenv [here](https://virtualenv.pypa.io/en/stable/).

When you **activate** a virtualenv, any commands that deal with Python or packages will only affect further commands inside the virtualenv. You should create a virtualenv for each separate project you're working on that needs packages. Realize that virtualenv commands are totally unrelated to Git commands. Changing your Git branch will not modify your virtualenv; changing your virtualenv will not change your Git commands.

Confusingly, there are many different packages to create virtual environments. You can view a comparison [here](https://stackoverflow.com/questions/41573587/what-is-the-difference-between-venv-pyvenv-pyenv-virtualenv-virtualenvwrappe). The most popular is `virtualenv`, but `venv` comes with the standard library.

## Install

Virtualenv is also the name of the command to manage virtualenvs. You need to install it system-wide to be able to use it. You should only need to run this once on your computer.

```bash
pip install virtualenv
```

## Create

The first action is to **create** a new, empty virtualenv. I recommend you use the name `venv`. This will create a directory called `venv` in the working directory. You'll not need to modify this directory by hand.

```bash
virtualenv venv
```

## Activate

Once you've created a virtualenv, you can **activate** it. Run a script in the virtualenv directory. Your prompt should change and show `(venv)` at the beginning to let you know you've activated. After you have activated a virtualenv, all `python` and `pip` commands will use **their virtualenv versions** and not the ones installed system-wide. If you're using PowerShell you may get the error "execution of scripts is disabled on this system", you can fix this by running [Set-ExecutionPolicy RemoteSigned
](https://stackoverflow.com/questions/4037939/powershell-says-execution-of-scripts-is-disabled-on-this-system).

On bash:
```bash
source venv/bin/activate
```

On PowerShell:
```
venv\Scripts\activate
```


## Running Python

Once a virtualenv has been activated, you can use `python` to run Python code. It will have access to all the installed packages in the virtualenv. You don't need to worry about running `python3` once activated.

## Freeze

**Freezing** is the process of taking all of the current packages and their versions and writing it out to `requirements.txt`. This is how you save the specific dependencies of your application. `>` is a special shell operator that takes the output of the previous command and writes it to a file. If you ever install more dependent packages, you should re-freeze.

```bash
pip freeze > requirements.txt
```


## Installing

If you include the `requirements.txt` in the repository, when you or someone else clones it they can quickly and easily create a virtual environmental that contains all the required libraries.

```bash
pip install -r requirements.txt
```

## Deactivate

To exit your virtualenv, **deactivate** it. It is available only inside of the virtualenv. Your prompt should change back to normal showing you've deactivated.

```bash
deactivate
```

