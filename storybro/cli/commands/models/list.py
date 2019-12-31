import click


@click.command()
@click.pass_obj
def list(config):
    '''List models available for download'''
    installed = config.model_manager.models.keys()
    available = config.model_registry.models.keys()
    keys = set(installed).union(set(available))
    for key in keys:
        bullet = "-" if key not in installed else "*"
        print(f"{bullet} {key}")
