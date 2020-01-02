# Storybro

Storybro is a community maintained fork of [AI Dungeon 2](https://github.com/AIDungeon/AIDungeon) by [Nick Walton](https://github.com/nickwalton).

Visit our Wiki here: [Storybro wiki](https://github.com/storybro/storybro/wiki)

Read more about AI Dungeon 2 and how it was built [here](https://pcc.cs.byu.edu/2019/11/21/ai-dungeon-2-creating-infinitely-generated-text-adventures-with-deep-learning-language-models/).

This fork aims to:
- Improve the existing code
- Consolidate community improvements into one project
- Offer a pip installable Python package
- Build a basic http web-service
- Build a basic web-frontend

To play the game locally, it is recommended that you have an nVidia GPU with 12 GB or more of memory, and CUDA installed. If you do not have such a GPU, each turn can take a couple of minutes or more for the game to compose its response. To install and play locally:

Windows Users:

1: If you do not already have Chocolatey then go ahead and run Install_choco.bat as ADMINISTRATOR and wait for it to finish
2: Run Install_win afterwards as ADMINISTRATOR, at the end it will automatically launch itself into the storybro shell
3: Now type in 'storybro models get models_v5' without quote's. allow that to install then type in 'storybro play' to play!
4: You can quickly access the shell by opening the OpenShell.bat

Note: The reason chocolatey is a seperate install is due to some instances of CMD not working correctly with choco until it has been resetted.

Manual Install:
```
git clone --branch master https://github.com/storybro/storybro/
cd storybroy
./bin/linux/install/install # Installs system and python packages
poetry shell
storybro models get model_v5
storybro play
```

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
