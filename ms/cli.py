"""This module provides the mailsleuth CLI."""
# mailsleuth/cli.py
from email.parser import BytesParser

from typing import Optional

import typer

from ms import __app_name__, __version__

app = typer.Typer()

#---- Commands -----


@app.command("read")
def _read_eml(filepath: str,
              t: Optional[bool] = typer.Option(
                    None,
                    "--table",
                    "-t",
                    help="Display the email information in a table format.") 
            ):
    
    with open(filepath, 'rb') as f:# Bytesparser only takes bytes - must be in bytes mode
        parser = BytesParser()
        header = parser.parse(f)# headeronly is true by default. Creates email object here
    typer.echo(f"Subject: {header['subject']}") # for testing purposes

    if t:
        typer.echo("Displaying email information in table format...")
        # t._get_table(header)  # Placeholder for table display logic

    
#---- Options ----
# def _get_table(eml_header: object) 



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