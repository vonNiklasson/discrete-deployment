import click

from discrete_integration.decorators.config import Config, di_config
from discrete_integration.commands.init import Init
from discrete_integration.utils.directory_helper import DirectoryHelper


@click.group()
@di_config
def cli(config: Config):
    config.project_root.assume_project_root(
        DirectoryHelper.get_working_dir()
    )


cli.add_command(Init.command, name='init')
