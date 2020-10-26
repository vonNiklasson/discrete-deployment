import click
import os

from discrete_integration.context_helpers import DirectoryHelper, ProjectRoot


class Config:

    def __init__(self):
        self.project_root: ProjectRoot = ProjectRoot('', False, False)
        self.working_dir: str = os.getcwd()

    def assume_project_root(self, current_path: str = None):
        current_path = self.working_dir if current_path is None else current_path
        while True:
            # Check if init file exists in the given path
            if DirectoryHelper.init_file_exists(current_path):
                self.project_root.path = current_path
                self.project_root.is_assumed = True
                self.project_root.exists = True

            # If not make sure we're not at system root and traverse up one directory
            if DirectoryHelper.is_system_root(current_path):
                break
            current_path = DirectoryHelper.traverse_up(current_path)


di_config = click.make_pass_decorator(Config, ensure=True)


@click.group()
@di_config
def cli(config):
    config.assume_project_root()


@cli.command()
@di_config
@click.argument('init_path', required=False, default='.',
                type=click.Path(exists=True, writable=True, dir_okay=True, file_okay=False))
def init(config: Config, init_path: str):
    click.echo(config.project_root.exists)
    click.echo(init_path)
    click.echo('Initialising new project')
