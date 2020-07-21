import click


def init_app(app):
    # here we create our commands (cli)
    # exemple:
    @app.cli.command()
    def do_something():
        '''Simple command that do something'''
        click.echo('Doing something')
        