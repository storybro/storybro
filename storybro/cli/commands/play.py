import click

from storybro.play import play_aidungeon_2

@click.command()
@click.argument('model', default="model_v5")
@click.pass_obj
def play(config, model):
    if model not in config.model_manager.models:
        click.echo(f"Model `{model}` is not installed.")
        return

    model_path = config.model_manager.models[model]
    play_aidungeon_2(model_path)
