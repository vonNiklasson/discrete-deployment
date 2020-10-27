import click

from discrete_integration import settings
from discrete_integration.decorators.config import Config, di_config
from discrete_integration.utils.directory_helper import DirectoryHelper


class Init:

    @staticmethod
    def assert_current_path_compatibility(config: Config, init_path: str):
        # Check if a project root already exists in the current directory
        if config.project_root.exists and config.project_root.path == init_path:
            # If so, just abort. We don't want to re-initialise this way.
            click.secho('Error: Discrete Integration root already exists in current path.',
                        fg='red')
            return False
        return True

    @staticmethod
    def assert_parent_path_compatibility(config: Config, init_path: str):
        # Check if a project root already exists in the parent directory
        if config.project_root.exists and config.project_root.path != init_path:
            # There is a root init file in a parent directory.
            # Prompt the user tp make sure the still want to create a new init file.
            try:
                initialise_again = click.prompt(
                    'Found parent Discrete Integration root at %s\n'
                    'Do you want to initialise anyway?' % DirectoryHelper.get_di_config_path(config.project_root.path),
                    type=click.Choice(choices=['Y', 'n'], case_sensitive=False),
                    default='n'
                )
            except click.Abort as e:
                # If user aborted, stop the script
                return False
            if initialise_again == 'n':
                # If user answered No, stop the script
                return False
        return True

    @staticmethod
    def create_init_structure(config: Config, init_path: str):
        # Creating .di directory
        DirectoryHelper.create_di_config_dir(init_path)
        click.secho('Creating project config directory .di/', fg='yellow')
        # Creating initial di.json file in project root
        if not DirectoryHelper.file_exists(DirectoryHelper.get_di_file_path(init_path)):
            open(DirectoryHelper.get_di_file_path(init_path), "x")
            click.secho('Creating initial Discrete Integration file di.json in project root', fg='yellow')
        else:
            click.secho('Skipping initial Discrete Integration file di.json (already exists)', fg='yellow')


    @staticmethod
    @click.command()
    @click.argument('init_path', required=False, default='.',
                    type=click.Path(exists=True, writable=True, file_okay=False, resolve_path=True))
    @di_config
    def command(config: Config, init_path: str):
        # Check if a project root already exists
        if not Init.assert_current_path_compatibility(config, init_path):
            return
        if not Init.assert_parent_path_compatibility(config, init_path):
            return

        click.secho('Initialising Discrete Integration', fg='cyan')
        Init.create_init_structure(config, init_path)
