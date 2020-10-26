import click
import os

class DirectoryHelper:

    @staticmethod
    def traverse_up(path):
        return os.path.dirname(path)

    @staticmethod
    def file_exists(file):
        return os.path.isfile(file)

    @staticmethod
    def init_file_exists(path):
        DirectoryHelper.file_exists(path + '.di_init.json')

    @staticmethod
    def is_system_root(path):
        return path == DirectoryHelper.traverse_up(path)


class ProjectRoot:

    def __init__(self, path: str, exists: bool, is_assumed: bool):
        self.path = path
        self.exists = exists
        self.is_assumed = is_assumed

    def __str__(self):
        return self.path


class Config:

    def __init__(self):
        self.project_root: ProjectRoot = ProjectRoot(None, False, False)
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
