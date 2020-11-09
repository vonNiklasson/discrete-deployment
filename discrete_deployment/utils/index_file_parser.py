from typing import Dict, Union, List

import yaml
from slugify import slugify

from discrete_deployment.configurations.configurations import LazyConfiguration, Configuration
from discrete_deployment.utils.file_helper import FileHelper


class IndexFileParser:

    @staticmethod
    def lazy_load_index_by_names(path: str):
        """
        Loads the file containing the paths with it's corresponding names

        @param path: The path of the index file.
        """
        names: Dict[str, str] = {}
        # Open the yaml file of paths
        try:
            index_file = FileHelper.read_yaml(path)
        except yaml.YAMLError as e:
            # TODO: Catch this error somehow
            return names

        if index_file is None or index_file['paths'] is None:
            return names

        # Read the list of names
        for file_path in index_file['paths']:
            # Make sure the name is a list. If it's a string, convert it to a list
            file_names = [file_path['names']] if isinstance(file_path['names'], str) else file_path['names']
            for name in file_names:
                # Store it in a dictionary based on the name for quick access
                names[slugify(name)] = file_path['path']

        return names

    @staticmethod
    def save_index_from_configurations(context, path: str, configurations: Union[LazyConfiguration, List[LazyConfiguration]]):
        # Make sure the configurations is of type list (but allow single object as well)
        configurations = [configurations] if isinstance(configurations, LazyConfiguration) else configurations

        # Group the names by its path
        grouped_names = IndexFileParser.group_names_by_paths(configurations)

        # Format the grouped names into an dictionary
        formatted_grouped_names = [
            {
                'path': FileHelper.make_path_relative(context.project_path, file_path),
                'names': file_names
            } for file_path, file_names in grouped_names.items()
        ]

        FileHelper.write_yaml(path, {'paths': formatted_grouped_names})

    @staticmethod
    def group_names_by_paths(configurations: List[LazyConfiguration]):
        paths = {}
        for config in configurations:
            if config.path not in paths:
                paths[config.path] = []
            paths[config.path].append(config.get_key())

        return paths
