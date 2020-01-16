import click

@click.group()
@click.pass_obj
def models(config):
    pass

from .get import get
from .list import list
from .delete import delete

models.add_command(get)
models.add_command(list)
models.add_command(delete)

