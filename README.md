<pre>
             ..~rr,,                                                                     
            .d╨"""╙╝╬N                                                                   
           ╔`        ╣Ñ                                                                  
      ,╓▄▄▄▓▄         ▌N             .oPYo.   o                      8                   
    #▀"` `Ñ"▀        ║ÜÑ             8        8                      8                   
        `".          ▀▀▀▀█▄,         `Yooo.  o8P .oPYo. oPYo. o    o 8oPYo. oPYo. .oPYo. 
     ,╗▄▄,  :         *    ╙▌            `8   8  8    8 8  `' 8    8 8    8 8  `' 8    8 
 .  ║▓▓███▌  r       ,,      '            8   8  8    8 8     8    8 8    8 8     8    8 
  -  ╙▀▀▀▀ .«      ╓▓▓███∩           `YooP'   8  `YooP' 8     `YooP8 `YooP' 8     `YooP' 
    "ⁿ~╔▄µ^`     .  ▀███▀  »`        :.....:::..::.....:..:::::....8 :.....:..:::::.....:
       ╟▓M        `~µ,.:;«*          :::::::::::::::::::::::::::ooP'.::::::::::::::::::::
       ║▓M ,,      .▓▓    ,          :::::::::::::::::::::::::::...::::::::::::::::::::::
       ║▓M ╫╫      ╒▓▓   ╬▓┘                                                             
       ║╫Ñ ╫╫      :▓╫  ╠╫▌                                                              
       j╫╫ ╫╫       ▓Ñ  Ñ╫                                                               
        ▌░ ╬╩       ▓N  K╫                                                               
        ▌` ╟H       ╣Ñ  Ü╫                                                               
        ▓H  ▓>      ╨░  ╣░                    Looks like you're writing a story.         
        ║▌  ╙Ñ»     ,┘  ╟ÑH                                                              
         ▌    ╚N╗▄æ╩    ║╫╡                          Would you like help?                
         ║N.            ║╫╡                                                              
          ▓             ]╫`                                                              
           ▓..         .╠M                                                               
            ▀▄,        .^                                                                
              ╙ΦNww≥═*^                                                                  
</pre>

**Storybro** is a community maintained fork of [AI Dungeon 2](https://github.com/AIDungeon/AIDungeon).

Visit our wiki here: [Storybro wiki](https://github.com/storybro/storybro/wiki)

Read more about AI Dungeon 2 and how it was built [here](https://pcc.cs.byu.edu/2019/11/21/ai-dungeon-2-creating-infinitely-generated-text-adventures-with-deep-learning-language-models/).

This fork of AI Dungeon 2 aims to provide:
- Improvements the original codebase
- A command-line tool for managing models, stories, prompts, etc
- An improved interactive play mode
- A model registry where models can be downloaded
- An HTTP web-service exposing most features
- A Pip installable Python package

### Note

Storybro's AI can use your GPU or CPU. *A GPU will produce AI responses much faster than a CPU.* An nVidia GPU with 12 GB or more of memory, with CUDA installed, **is required** for GPU play. If you do not have such a GPU, you can play on your CPU. However, *each turn can take a couple of minutes or more* for the game to compose its response.

# Installation

Installing Storybro requires the following software:

- [Python](https://www.python.org/downloads/) 3.4 - 3.7
- [Pip](https://pip.pypa.io/en/stable/installing/) >= 19.1
- [Git](https://git-scm.com/downloads)

Use Pip to install the latest release of Storybro:

    pip install storybro
    
To install the development version:

    pip install git+https://github.com/storybro/storybro.git

Or run this if you have cloned the source and are in that directory:

    pip install .

*(Optional)* To use the model torrenting in Storybro, install [Aria2](https://aria2.github.io/) and ensure it is on your `$PATH`.

**For troubleshooting [see the wiki](https://github.com/storybro/storybro/wiki/Troubleshooting-Guide)**

# Playing

Visit our [Wiki](http://github.com/storybro/storybro/wiki) to learn how to play and use Storybro.

# Community

Storybro is an open source project. Questions, discussion, and contributions are welcome. Contributions can be anything from new packages to bugfixes, documentation, or even new core features.

Resources:

* **Reddit**: [r/AIDungeon](https://www.reddit.com/r/AIDungeon/)
* **Discord**: [aidungeon discord](https://discord.gg/Dg8Vcz6)


# Contributing

Contributing to Storybro is easy! Just send us a [pull request](https://help.github.com/articles/using-pull-requests/) from your fork. Make sure ``develop`` is the destination branch. 

Storybro uses a rough approximation of the [Git Flow](http://nvie.com/posts/a-successful-git-branching-model/) branching model.  The ``develop`` branch contains the latest contributions, and ``master`` is always tagged and points to the latest stable release.

If you're a contributor, make sure you're testing and playing on `develop`. That's where all the magic is happening (and where we hope bugs stop).
