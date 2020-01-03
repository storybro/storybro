import click

@click.group()
@click.pass_obj
def stories(config):
    pass

from .list import list

stories.add_command(list)

