"""A community fork of AI Dungeon 2"""
import os

import click
from appdirs import user_data_dir

from storybro.cli.commands import play

from storybro.models.manager import ModelManager
from storybro.play.block_formatter import BlockFormatter
from storybro.play.player import Player
from storybro.play.settings import PlayerSettings
from storybro.stories.manager import StoryManager

__version__ = "0.1.0"

from .cli import ep

def main():
    ep()


def play_now():
    data_dir = user_data_dir("storybro", "storybro")

    story_manager = StoryManager(os.path.join(data_dir, "stories"))
    model_manager = ModelManager(os.path.join(data_dir, "models"))

    model = model_manager.models.get("model_v5")
    if not model:
        click.echo(f"Model `model_v5` is not installed.")
        return

    story = story_manager.stories.get("story")
    if not story:
        if not click.confirm('Story `story` does not exist. Create new story?'):
            return
        story = story_manager.new_story("story")


    settings = PlayerSettings(20, 5, ">", "", "", 80)
    formatter = BlockFormatter(settings)
    player = Player(model, story, settings, formatter)
    player.run()


