import os

import click

from storybro.cli.config import Config


@click.command()
@click.argument('name')
@click.pass_obj
def delete(config: Config, name):
    '''Delete a locally saved story'''
    stories = config.story_manager.stories.keys()
    
    if name not in stories:
        click.echo(f"The story `{name}` wasn't found.")
        return
    
    story = config.story_manager.stories.get(name)
    os.remove(story.path)
    click.echo(f"Deleted story `{name}`.")
