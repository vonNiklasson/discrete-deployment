import click

from discrete_deployment.decorators import pass_context, pass_config, Context, Config
from discrete_deployment.utils.file_helper import FileHelper
from discrete_deployment.utils.index_file_parser import IndexFileParser


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
    def command(context: Context, config: Config, path: str):
        context.project_path = path
        index_path = FileHelper.compose_index_path(path)
        IndexFileParser.save_index_from_configurations(context, index_path, [])
