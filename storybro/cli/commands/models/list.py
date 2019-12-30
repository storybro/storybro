import click
import click_config_file

from sh import aria2c

from storybro.registry import fetch_model_registry
from storybro.models import models_at_path

@click.command()
@click.pass_obj
def list(config):
    '''List models available for download'''
    installed = models_at_path(config.models_path)
    available = fetch_model_registry(config.model_registry)
    keys = set(installed).union(set(available))
    for key in keys:
        bullet = "-" if key not in installed else "*"
        print(f"{bullet} {key}")
