"""This module provides the mailsleuth CLI."""
# mailsleuth/cli.py
from email.parser import BytesParser

from typing import Optional

import typer

from mailsleuth import __app_name__, __version__

app = typer.Typer()

#---- Commands -----

def _read_eml(filepath: str)-> None:
    with open(filepath, 'rb') as f:# Bytesparser only takes bytes - must be in bytes mode
        parser = BytesParser()
        header = parser.parse(f)# headeronly is true by default. Creates email object here
        print(header)#for testing







#---- Callbacks ----

def _version_callback(value: bool) -> None:
    logo = (r"""               .__.__         .__                 __  .__     
  _____ _____  |__|  |   _____|  |   ____  __ ___/  |_|  |__  
 /     \\__  \ |  |  |  /  ___/  | _/ __ \|  |  \   __\  |  \ 
|  Y Y  \/ __ \|  |  |__\___ \|  |_\  ___/|  |  /|  | |   Y  \
|__|_|  (____  /__|____/____  >____/\___  >____/ |__| |___|  /
      \/     \/             \/          \/                 \/ """)
    if value:
        typer.echo(f"{logo} \n \n {__app_name__} v{__version__} \n")
        raise typer.Exit()

@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return