import click

from discrete_integration import settings
from discrete_integration.decorators.config import Config


di_config = click.make_pass_decorator(Config, ensure=True)


@click.group()
@di_config
def cli(config: Config):
    config.assume_project_root()


@cli.command()
@click.argument('init_path', required=False, default='.',
                type=click.Path(exists=True, writable=True, file_okay=False, resolve_path=True))
@di_config
def init(config: Config, init_path: str):
    # Check if a project root already exists
    if config.project_root.exists:
        # Check if it exists in the given directory
        if config.project_root.path == init_path:
            # If so, just abort. We don't want to re-initialise this way.
            click.secho('Error: Discrete Integration root %s already exists in path.' % settings.INIT_FILE_NAME, fg='red')
            return

        # There is a root init file in a parent directory.
        # Prompt the user tp make sure the still want to create a new init file.
        try:
            initialise_again = click.prompt(
                'Found parent Discrete Integration root at %s/%s\n'
                'Do you want to initialise anyway?' % (config.project_root.path, settings.INIT_FILE_NAME),
                type=click.Choice(choices=['Y', 'n'], case_sensitive=False),
                default='n'
            )
        except click.Abort as e:
            # If user aborted, stop the script
            return
        if initialise_again == 'n':
            # If user answered No, stop the script
            return
    click.secho('Initialising Discrete Integration', fg='cyan')
