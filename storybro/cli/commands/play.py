import click
import os

from storybro.play import play_aidungeon_2

@click.command()
@click.argument('model', default="model_v5")
@click.option('--force-cpu', '-f', is_flag=True, help="Force the model to run on the CPU")
@click.pass_obj
def play(config, model, force_cpu):
    if model not in config.model_manager.models:
        click.echo(f"Model `{model}` is not installed.")
        return

    if force_cpu:
        os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

    model_path = config.model_manager.models[model]
    play_aidungeon_2(model_path)
