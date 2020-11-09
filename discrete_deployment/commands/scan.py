import glob
from typing import List, Dict

import click
from slugify import slugify
from os.path import relpath

from discrete_deployment.configurations.configurations import LazyConfiguration
from discrete_deployment.decorators import pass_context, pass_config, Context, Config
from discrete_deployment.exceptions import ConfigurationAlreadyExistsException
from discrete_deployment.utils.config_file_parser import ConfigFileParser
from discrete_deployment.utils.file_helper import FileHelper
from discrete_deployment.utils.index_file_parser import IndexFileParser


class Scan:

    @staticmethod
    @click.command()
    # Contexts
    @pass_config
    @pass_context
    def command(context: Context, config: Config):
        # Make sure the project is initialised before trying to scan for files
        if not context.project_exists:
            click.echo("Project not initialised. Please run \"ddep init\" from your project root folder first.")
            return

        # Find all ddep.yaml files
        config_paths_iglob = FileHelper.find_config_paths(context.project_path)
        config_paths = [path for path in config_paths_iglob]

        configurations = []
        # Read all the configuration into one list based on the paths
        for config_path in config_paths:
            # Print the file name based on the relative path
            click.echo(" - Found ", nl=False)
            click.echo(click.style("%s" % relpath(config_path, context.working_path), fg='cyan'))
            configurations += ConfigFileParser.lazy_load_file_from_path(context, config_path)

        # Save all names into the paths file and overwrite it
        IndexFileParser.save_index_from_configurations(
            context,
            FileHelper.compose_index_path(context.project_path),
            configurations
        )
