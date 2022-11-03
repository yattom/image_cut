import typer
from pathlib import Path
from . import cutter

app = typer.Typer()

@app.command()
def cut(filename: Path, cut_param: str):
    cutter.cut(filename, cut_param)