import click

from discrete_integration.decorators.config import Config, di_config
from discrete_integration.commands.init import init


@click.group()
@di_config
def cli(config: Config):
    config.assume_project_root()


cli.add_command(init, name='init')
