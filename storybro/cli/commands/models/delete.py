import shutil

import click


@click.command()
@click.argument('name')
@click.pass_obj
def delete(config, name):
    '''Delete a model'''
    installed = config.model_manager.models.keys()

    if name not in installed:
        click.echo(f"The model `{name}` wasn't found.")
        return

    model = config.model_manager.models.get(name)
    shutil.rmtree(model.root_path)
    click.echo(f"Deleted model `{name}`.")
