import os
import shutil

import click


@click.command()
@click.argument('name')
@click.option('-t', '--torrent')
@click.option('--force', '-f', is_flag=True, help="Redownload if model already exists")
@click.pass_obj
def get(config, name, torrent, force):
    '''Download a model'''
    installed = config.model_manager.models

    if torrent is None:
        if name not in config.model_registry.models:
            click.echo(f"The model `{name}` wasn't found.")
            return

        torrent = config.model_registry.models[name]

    model = config.model_manager.models.get(name)

    if model:
        if not force:
            click.echo(f"The model `{name}` is already installed. Use -f to force re-download.")
            return
        else:
            shutil.rmtree(model.root_path)
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
