import click

from discrete_deployment.decorators import pass_context, pass_config, Context, Config
from discrete_deployment.utils.file_helper import FileHelper
from discrete_deployment.utils.paths_file_parser import PathsFileParser


class Init:

    @staticmethod
    @click.command()
    # Contexts
    @pass_config
    @pass_context
    # Argument for where to initialise
    @click.argument("path", required=False, default='.',
                    type=click.Path(exists=True, file_okay=False, writable=True, resolve_path=True)
                    )
    @click.option("--no-config-template", is_flag=True)
    def command(context: Context, config: Config, path: str, no_config_template):
        context.project_path = path

        if not no_config_template:
            # TODO: Create a config template file
            pass

        paths_path = FileHelper.compose_paths_path(path)
        PathsFileParser.save_paths(paths_path, {})
