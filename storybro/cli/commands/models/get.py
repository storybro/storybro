import os
import shutil

import click

from storybro.models import models_at_path
from storybro.registry import fetch_model_registry


@click.command()
@click.argument('name')
@click.option('-t', '--torrent')
@click.option('--force', '-f', is_flag=True, help="Redownload if model already exists")
@click.pass_obj
def get(config, name, torrent, force):
    '''Download a model'''
    models = fetch_model_registry(config.model_registry)
    installed = models_at_path(config.models_path)

    if torrent is None:
        if name not in models:
            click.echo(f"The model `{name}` wasn't found.")
            return

        torrent = models[name]

    if name in installed:
        if not force:
            click.echo(f"The model `{name}` is already installed.")
            return
        else:
            shutil.rmtree(os.path.join(config.models_path, name))
            click.echo(f"Deleted local model `{name}`. Re-downloading.")

    click.echo(f"Downloading torrent: {torrent}")

    os.execlp('aria2c', 'aria2c',
        "--max-connection-per-server", "16",
        "--bt-max-peers", "500",
        "--seed-time", "0",
        "--summary-interval", "15",
        "--disable-ipv6",
        "--split", "64",
        "-d", config.models_path,
        torrent,
    )
