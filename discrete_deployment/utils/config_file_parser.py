from typing import List, Dict, Set

import yaml
from slugify import slugify

from discrete_deployment.configurations.configurations import LazyConfiguration
from discrete_deployment.exceptions import ConfigurationAlreadyExistsException
from discrete_deployment.utils.file_helper import FileHelper


class ConfigFileParser:

    @staticmethod
    def lazy_load_config_file(path: str):
        """
        Loads a file containing the configurations into a Configuration class

        @param path: The path of the configuration file.
        """
        parsed_configurations: List[LazyConfiguration] = []
        try:
            file_configs = FileHelper.read_yaml(path)
        except yaml.YAMLError as e:
            # TODO: Catch this error somehow
            return parsed_configurations

        if file_configs is None:
            return parsed_configurations

        # Iterate over each type of configuration in the file
        for config_class, configurations in file_configs.items():
            # Iterate over all configurations in that specific type
            for configuration in configurations:
                # Add them to the list
                parsed_configurations.append(
                    LazyConfiguration.from_dict(path, config_class, configuration)
                )

        return parsed_configurations

    @staticmethod
    def lazy_load_configurations_from_paths(paths: List[str]):
        # Declare a set of names to keep track if we're loading duplicates
        config_names: Set[str] = set()
        # A dictionary of name: configuration
        configurations: Dict[str, LazyConfiguration] = {}
        # Iterate over all paths with configurations
        for path in paths:
            # Load the actual configuration into a temporarily dictionary
            lazy_configs = ConfigFileParser.lazy_load_config_file(path)
            # Iterate over each configuration
            for lazy_config in lazy_configs:
                # Slugify the config name to something unified
                config_name = slugify(lazy_config.name)
                # Check if the configuration has already been loaded, if so throw an exception
                if config_name in config_names:
                    raise ConfigurationAlreadyExistsException(config_name)

                configurations[config_name] = lazy_config
                # Store the config name to the set so we can make sure we dont' store duplicates
                config_names.add(config_name)

        return configurations
