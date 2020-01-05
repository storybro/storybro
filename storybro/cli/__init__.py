import os

from appdirs import user_data_dir

import click
import click_config_file

from storybro.cli.config import Config
from storybro.models.manager import ModelManager
from storybro.models.registry import ModelRegistry
from storybro.stories.manager import StoryManager
from storybro.story.grammars import GrammarManager

from .commands.models import models
from .commands.stories import stories
from .commands.play import play


data_dir = user_data_dir("storybro", "storybro")


@click.group()
@click.option('-r', '--model-registry',
              default="https://raw.githubusercontent.com/storybro/torrents/master/models.json")
@click.option('-m', '--models-path',
              show_default=os.path.join(data_dir, "models"),
              default=os.path.join(data_dir, "models"))
@click.option('-s', '--stories-path',
              show_default=os.path.join(data_dir, "stories"),
              default=os.path.join(data_dir, "stories"))
@click.option('-g', '--grammars-path',
              show_default=os.path.join(data_dir, "grammars"),
              default=os.path.join(data_dir, "grammars"))
@click.pass_context
@click_config_file.configuration_option()
def cli(ctx, model_registry, models_path, stories_path, grammars_path):
    config = Config()
    config.model_registry = ModelRegistry(model_registry)
    config.models_path = models_path
    config.grammars_path = grammars_path
    config.stories_path = stories_path
    config.story_manager = StoryManager(stories_path)
    config.model_manager = ModelManager(models_path)
    config.grammar_manager = GrammarManager(grammars_path)
    ctx.obj = config


def ep():
    cli.add_command(play)
    cli.add_command(models)
    cli.add_command(stories)
    cli()
