import click

from {{ proj }}.ext.db.commands import create_db, drop_db, populate_db


def init_app(app):

    app.cli.add_command(app.cli.command()(create_db))
    app.cli.add_command(app.cli.command()(drop_db))
    app.cli.add_command(app.cli.command()(populate_db))

    @app.cli.command()
    def do_something():
        """Simple command that do something"""
        click.echo("Doing something")

