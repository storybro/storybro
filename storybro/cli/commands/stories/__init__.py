import click

@click.group()
@click.pass_obj
def stories(config):
    pass

from .list import list
from .delete import delete

stories.add_command(list)
stories.add_command(delete)

