import click

@click.group()
def cli():
    pass

@cli.command()
def download_model():
    click.echo("Downloading model...")

@cli.command()
def play():
    click.echo("Generating story...")

def main():
    cli()
