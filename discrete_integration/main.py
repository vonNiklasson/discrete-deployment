import click

from discrete_integration.utils.directory_helper import DirectoryHelper


@click.group()
@click.pass_context
def cli(context):
    context.working_dir = DirectoryHelper.get_working_dir()


@cli.command()
@click.pass_context
def init(context):
    pass
