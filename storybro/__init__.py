"""A community fork of AI Dungeon 2"""
import os

# from appdirs import user_data_dir

# from storybro.cli.commands import play
# from storybro.models.manager import ModelManager
# from storybro.play.block_formatter import BlockFormatter
# from storybro.play.player import Player
# from storybro.play.settings import PlayerSettings
# from storybro.stories.manager import StoryManager
import cmd2

__version__ = "0.1.0"

from .cli import ep

# def main():
#     ep()


class Simple(cmd2.Cmd):
    def __init__(self):
        super().__init__()

def play_now():
    app = Simple()
    app.cmdloop()
