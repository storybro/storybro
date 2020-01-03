import os
import sys

import click

from storybro.play.block_formatter import BlockFormatter
from storybro.play.player import Player
from storybro.play.settings import PlayerSettings


@click.command()
@click.argument('story-name', required=True)
@click.option('-m', '--model-name', default="model_v5")
@click.option('--memory', type=int)
@click.option('--max-repeats', type=int)
@click.option('--icon-for-input')
@click.option('--top-separator')
@click.option('--bottom-separator')
@click.option('--fill-width', type=int)
@click.option('--force-cpu', '-f', is_flag=True, help="Force the model to run on the CPU")
@click.pass_obj
def play(config,
         story_name,
         model_name,
         memory, max_repeats,
         icon_for_input,
         top_separator, bottom_separator,
         fill_width,
         force_cpu):

    if force_cpu:
        os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

    model = config.model_manager.models.get(model_name)
    if not model:
        click.echo(f"Model `{model_name}` is not installed.")
        return

    for name in config.story_manager.stories:
        print(f"- {name}")

    story = config.story_manager.stories.get(story_name)
    if not story:
        if not click.confirm('Story does not exist. Create new story?'):
            return
        story = config.story_manager.new_story(story_name)

    sys.argv = ['storybro']
    settings = PlayerSettings(memory, max_repeats, icon_for_input, top_separator, bottom_separator, fill_width)
    formatter = BlockFormatter(settings)
    player = Player(model, story, settings, formatter)
    player.run()
