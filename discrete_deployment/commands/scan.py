import glob
from typing import List, Dict

import click
from slugify import slugify

from discrete_deployment.configurations.configurations import LazyConfiguration
from discrete_deployment.decorators import pass_context, pass_config, Context, Config
from discrete_deployment.exceptions import ConfigurationAlreadyExistsException
from discrete_deployment.utils.config_file_parser import ConfigFileParser
from discrete_deployment.utils.file_helper import FileHelper
from discrete_deployment.utils.paths_file_parser import PathsFileParser


class Scan:

    @staticmethod
    @click.command()
    # Contexts
    @pass_config
    @pass_context
    def command(context: Context, config: Config):
        # Find all ddep.yaml files
        file_paths = FileHelper.find_configs_paths(context.project_path)
        # Parse all ddep.yaml files into a Dict[str, LazyConfiguration] dictionary
        configurations = ConfigFileParser.lazy_load_configurations_from_paths(file_paths)
        # Save all targets into the paths file and overwrite it
        PathsFileParser.save_paths(
            FileHelper.compose_paths_path(context.project_path),
            configurations
        )
