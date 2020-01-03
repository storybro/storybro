# Storybro

Storybro is a community maintained fork of [AI Dungeon 2](https://github.com/AIDungeon/AIDungeon). AI Dungeon was originally created by [Nick Walton](https://github.com/nickwalton).

Visit our Wiki here: [Storybro wiki](https://github.com/storybro/storybro/wiki)

Read more about AI Dungeon 2 and how it was built [here](https://pcc.cs.byu.edu/2019/11/21/ai-dungeon-2-creating-infinitely-generated-text-adventures-with-deep-learning-language-models/).

This fork aims to provide:
- Improvements the original codebase
- A command-line tool `storybro` for managing models, stories, etc
- An improved interactive play mode
- A model registry where models can be downloaded
- An http web-service exposing most features
- A Pip installable Python package

### Note

Storybro's AI can use your GPU or CPU. *A GPU will produce AI responses much faster than a CPU.* An nVidia GPU with 12 GB or more of memory, and CUDA installed, **is required** for GPU play. If you do not have such a GPU, you can play on your CPU. However, *each turn can take a couple of minutes or more* for the game to compose its response.

# Playing

This README only covers installation. To learn how to play visit our [Wiki](http://github.com/storybro/storybro/wiki).

# Installation

Installing Storybro requires the following software:

- Python 3.4 - 3.7

Grab the source code with Git and clone it to your machine:

    git clone https://github.com/storybro/storybro/

## Windows Installation

Storybro comes with a few Windows Batch scripts to facilitate installation. If you'd like to install manually, see [Manual Installation](#manual-installation).

Storybro uses [Chocolatey](http://chocolatey.org), a package manager, to install dependencies:

1: Using an **ADMINISTRATOR** terminal from the root of this repo:


    ./bin/windows/install/install-choco.bat

2: Close your terminal and re-open it.
    
3: Now that Chocolatey is installed, install our dependencies and Storybro:


    ./bin/windows/install/install-storybro.bat

4: Once installation is done you should be in a shell. You can now use the `storybro` command:

## Linux Installation

Storybro comes with a few shell scripts to faciliate installation. If you'd like to install manually, see [Manual Installation](#manual-installation). 

To install Storybro simply run the install script:

    ./bin/linux/install/install
    
You can now use [Poetry](https://python-poetry.org/) to enter a shell where you can use the `storybro` command:

    poetry shell

## Manual Installation

Storybro is a Python application and uses [Poetry](https://python-poetry.org/) for its environment.

Install Poetry with Pip:

    $ pip install poetry
    
Use Poetry to install Storybro:

    $ poetry install
    
Use Poetry to run Storybro:

    $ poetry run storybro
    
Storybro uses [Aria2](https://aria2.github.io/) to download models. Make sure that it is installed and on your `$PATH` if you intend to use Storybro to download models.


Community
------------------------

Storybro is an open source project. Questions, discussion, and contributions are welcome. Contributions can be anything from new packages to bugfixes, documentation, or even new core features.

Resources:

* **Reddit**: [r/AIDungeon](https://www.reddit.com/r/AIDungeon/)
* **Discord**: [aidungeon discord](https://discord.gg/Dg8Vcz6)


Contributing
------------------------
Contributing to Storybro is easy! Just send us a [pull request](https://help.github.com/articles/using-pull-requests/) from your fork. Make sure ``develop`` is the destination branch. 

Storybro uses a rough approximation of the [Git Flow](http://nvie.com/posts/a-successful-git-branching-model/) branching model.  The ``develop`` branch contains the latest contributions, and ``master`` is always tagged and points to the latest stable release.

If you're a contributor, make sure you're testing and playing on `develop`. That's where all the magic is happening (and where we hope bugs stop).
