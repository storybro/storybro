import os

import click

from storybro.models import models_at_path, flatten_model


@click.command()
@click.argument('name')
@click.pass_obj
def flatten(config, name):
    '''Bring all files of a model to the root'''
    installed = models_at_path(config.models_path)

    if name not in installed:
        click.echo(f"Model `{name}` wasn't found.")
        return

    model_path = os.path.join(config.models_path, name)
    click.echo(f"Models path: {model_path}")
    flatten_model(model_path)
    click.echo(f"Flattened `{name}` model.")
