import os

import click
import click_config_file

from sh import aria2c

from storybro.models import models_at_path, flatten_model

@click.command()
@click.argument('name')
@click.pass_obj
def flatten(config, name):
    '''List models available for download'''
    installed = models_at_path(config.models_path)

    if name not in installed:
        click.echo(f"Model `{name}` wasn't found.")
        return

    model_path = os.path.join(config.models_path, name)
    click.echo(f"Models path: {model_path}")
    flatten_model(model_path)
    click.echo(f"Flattened `{name}` model.")
