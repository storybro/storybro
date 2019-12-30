import click

@click.group()
@click.pass_obj
def models(config):
    pass

from .get import get
from .list import list
from .flatten import flatten

models.add_command(get)
models.add_command(list)
models.add_command(flatten)
