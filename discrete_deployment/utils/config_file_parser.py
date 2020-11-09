from typing import List, Dict, Set

import yaml
from slugify import slugify

from discrete_deployment.configurations.config_classes import ConfigClasses
from discrete_deployment.configurations.configurations import LazyConfiguration
from discrete_deployment.decorators import Context
from discrete_deployment.exceptions import ConfigurationAlreadyExistsException, MalformedConfigurationException
from discrete_deployment.utils.file_helper import FileHelper


class ConfigFileParser:

    @staticmethod
    def lazy_load_file_from_path(context: Context, path: str):
        """
        Loads a file containing the configurations into a Configuration class

        @param context: The path of the configuration file.
        @param path: The path of the configuration file.
        """
        lazy_configurations: List[LazyConfiguration] = []
        try:
            file_configs = FileHelper.read_yaml(path)
        except yaml.YAMLError:
            relative_path = FileHelper.make_path_relative(context.project_path, path)
            raise MalformedConfigurationException(relative_path)

        if file_configs is None:
            return lazy_configurations

        # Iterate over each type of configuration in the file
        for config_class_str, configurations in file_configs.items():
            # Make sure the config class is in the allowed values
            if config_class_str not in ConfigClasses.values():
                # If not, raise exception
                raise MalformedConfigurationException(
                    path, 'Config class "%s" not found. Must be one of %s.' %
                          (config_class_str, ", ".join(ConfigClasses.values()))
                )

            # Convert the config class to it's corresponding ConfigClass value
            config_class = ConfigClasses.from_str(config_class_str)
            # Iterate over all configurations in that specific type
            for configuration in configurations:
                # Add them to the list
                lazy_configurations.append(
                    LazyConfiguration.from_dict(path, config_class, configuration)
                )

        return lazy_configurations

    @staticmethod
    def lazy_load_files_from_paths(paths: List[str]):
        # Declare a set of names to keep track if we're loading duplicates
        config_names: Set[str] = set()
        # A dictionary of name: configuration
        configurations: Dict[str, LazyConfiguration] = {}
        # Iterate over all paths with configurations
        for path in paths:
            # Load the actual configuration into a temporarily dictionary
            lazy_configs = ConfigFileParser.lazy_load_file_from_path(path)
            # Iterate over each configuration
            for lazy_config in lazy_configs:
                # Slugify the config name to something unified
                config_name = slugify(lazy_config.name)
                # Check if the configuration has already been loaded, if so raise an exception
                if config_name in config_names:
                    raise ConfigurationAlreadyExistsException(config_name)

                configurations[config_name] = lazy_config
                # Store the config name to the set so we can make sure we dont' store duplicates
                config_names.add(config_name)

        return configurations

    @staticmethod
    def group_configurations_by_path(configurations: Dict[str, LazyConfiguration]):
        paths: Dict[str, List[str]] = {}
        for name, configuration in configurations.items():
            if configuration.path not in paths:
                paths[configuration.path] = []
            paths[configuration.path].append(name)
        return paths
