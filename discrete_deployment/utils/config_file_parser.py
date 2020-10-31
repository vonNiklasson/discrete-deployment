from typing import List

from discrete_deployment.configurations.configurations import LazyConfiguration
from discrete_deployment.utils.file_helper import FileHelper


class ConfigFileParser:

    @staticmethod
    def lazy_load_config_file(path: str):
        """
        Loads a file containing the configurations into a Configuration class

        @param path: The path of the configuration file.
        """
        parsed_configurations: List[LazyConfiguration] = []
        file_configs = FileHelper.read_yaml(path)

        # Iterate over each type of configuration in the file
        for config_type, configurations in file_configs.items():
            # Iterate over all configurations in that specific type
            for configuration in configurations:
                # Add them to the list
                parsed_configurations.append(
                    LazyConfiguration.from_dict(config_type, configuration)
                )

        return parsed_configurations
