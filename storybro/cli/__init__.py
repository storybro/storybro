import os

from appdirs import user_data_dir

import click
import click_config_file

from storybro.models import ModelManager
from .commands.models import models
from .commands.play import play

class Config:
    model_registry = None
    model_manager = None
    models_path = None

data_dir = user_data_dir("storybro", "storybro")

@click.group()
@click.option('-r', '--model-registry',
              default="https://raw.githubusercontent.com/storybro/torrents/master/models.json")
@click.option('-m', '--models-path',
              show_default='current directory',
              default=os.path.join(data_dir, "models"))
@click.option('-g', '--grammars-path',
              default=os.path.join(data_dir, "grammars"))
@click.pass_context
@click_config_file.configuration_option()
def cli(ctx, model_registry, models_path, grammars_path):
    Config.model_registry = model_registry
    Config.models_path = models_path
    Config.grammars_path = grammars_path
    Config.model_manager = ModelManager(models_path)
    ctx.obj = Config

def ep():
    cli.add_command(play)
    cli.add_command(models)
    cli()
