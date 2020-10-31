import glob
from typing import List, Dict

import click
from slugify import slugify

from discrete_deployment.configurations.configurations import LazyConfiguration
from discrete_deployment.decorators import pass_context, pass_config, Context, Config
from discrete_deployment.exceptions import ConfigurationAlreadyExistsException
from discrete_deployment.utils.config_file_parser import ConfigFileParser


class Scan:

    @staticmethod
    @click.command()
    # Contexts
    @pass_config
    @pass_context
    def command(context: Context, config: Config):
        file_paths = Scan.find_ddep_configs_paths(context.project_path)
        configurations = Scan.load_configurations_from_paths(file_paths)

    @staticmethod
    def find_ddep_configs_paths(path: str):
        file_paths = []
        file_names = glob.iglob(path + '/**/ddep.yaml', recursive=True)
        for file_name in file_names:
            file_paths.append(file_name)

        return file_paths

    @staticmethod
    def load_configurations_from_paths(paths: List[str]):
        # Declare a set of names to keep track if we're loading duplicates
        config_names = set()
        # A dictionary of name: configuration
        configurations: Dict[str, LazyConfiguration] = {}
        # Iterate over all paths with configurations
        for path in paths:
            # Load the actual configuration into a temporarily dictionary
            lazy_configs = ConfigFileParser.load_configurations_lazy(path)
            # Iterate over each configuration
            for lazy_config in lazy_configs:
                # Slugify the config name to something unified
                config_name = slugify(lazy_config.name)
                # Check if the configuration has already been loaded, if so throw an exception
                if config_name in config_names:
                    raise ConfigurationAlreadyExistsException(config_name)

                configurations[config_name] = lazy_config
                config_names.add(config_name)

        return configurations
