# How to use

## Prerequisites

You need to have python3 installed on your computer. Install python3 from python.org

You also need a python package called `pipenv` installed:

```console
> pip install pipenv
```

You can verify that the python version that you normally use is the same:

```console
> python --version
```

You should also have git installed:

```console
> brew install git
```


## Create a virtual environment

After cloning the repository, cd into the repository (`python_for_beginners\`) and run:

```console
> pipenv sync
```

This will create a virtual environment with Python 3.7 and the dependency `jupyterlabs`. As the project evolves, other dependencies may be added to the virtual environment. These dependencies are specified in `Pipfile`, which is found directly under the local repository's top directory (under `python_for_beginners\`). You should run `pipenv sync` everytime you pull a branch from the remote repository in case Pipfile has been updated.

Note that the virtual environment does not affect the Python version you normally use. You can verify this by typing the following in the terminal:

```console
> python --version
```

## Starting jupyter notebook in the virtual environment

Navigate to the directory of your local repository and type in the console:

```console
> pipenv run jupyter notebook
```
This starts Jupyter Notebook in the virtual environment. Verify the the python version is 3.7. When opening a new notebook, you'll see Python3 as an option. When typing `!python --version` in a cell, the version should be printed.

## Pulling master from the remote repository

```console
> git pull origin master
> pipenv sync
```

Or use SourceTree.

1-877-238-4373