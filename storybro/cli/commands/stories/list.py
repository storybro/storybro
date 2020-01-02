import click

from storybro.cli.config import Config


@click.command()
@click.pass_obj
def list(config: Config):
    '''List locally saved stories'''
    for key in config.story_manager.stories:
        print(key, end=" ")
        print("\n")
