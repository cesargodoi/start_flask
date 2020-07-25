import click

from start_flask.project_builder import ProjectBuilder


@click.command()
@click.argument("project_name")
@click.option("--afp", is_flag=True, help="Application Factory Pattern.")
@click.option("--sqlal", is_flag=True, help="Install SQLAlchemy.")
@click.option("--venv", is_flag=True, help="Install virtual environment.")
@click.option("--all", is_flag=True, help="All options(afp + sqlal + venv).")
def main(project_name, afp, sqlal, venv, all):

    if all:
        afp, sqlal, venv = True, True, True

    click.echo("\n### Flask Project Builder ###\n")
    click.echo(f"- Project name: {project_name}")

    project = ProjectBuilder(project_name, afp, sqlal)

    click.echo("- Creating the directories ...")
    project.directories()

    click.echo("- Writing the files ...")
    project.files()

    if venv:
        click.echo("- Creating virtual environment as .venv ...")
        project.create_venv()

    click.echo("\nAll done!")
