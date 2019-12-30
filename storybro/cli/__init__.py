import os

from appdirs import user_data_dir

import click
import click_config_file

from .commands.models import models

class Config:
    model_registry = None
    models_path = None

@click.group()
@click.option('-r', '--model-registry',
              default="https://raw.githubusercontent.com/storybro/torrents/master/models.json")
@click.option('-m', '--models-path',
              show_default='current directory',
              default=user_data_dir("storybro", "storybro"))
@click.pass_context
@click_config_file.configuration_option()
def cli(ctx, model_registry, models_path):
    Config.model_registry = model_registry
    Config.models_path = models_path
    ctx.obj = Config

def ep():
    cli.add_command(models)
    cli()
