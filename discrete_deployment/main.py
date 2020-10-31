import click

from discrete_deployment.commands import Init, Scan
from discrete_deployment.decorators import pass_context, pass_config, Context, Config
from discrete_deployment.utils.file_helper import FileHelper


@click.group()
# Contexts
@pass_config
@pass_context
# Options
@click.option("-wp", "--working-path", required=False, default='.',
              type=click.Path(exists=True, file_okay=False, writable=True, resolve_path=True)
              )
def cli(context: Context, config: Config, working_path: str):
    context.working_path = working_path
    context.project_path, context.project_exists = FileHelper.find_project_root(working_path)
    # IF there's a project root, load the targets into the config
    if context.project_exists:
        config.is_initialised = True
        config.load_paths(context.project_path)


cli.add_command(Init.command, 'init')
cli.add_command(Scan.command, 'scan')
