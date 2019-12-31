import click

from storybro.play import play_aidungeon_2

@click.command()
def play():
    play_aidungeon_2("~/.local/share/storybro/models/official_v5/")
