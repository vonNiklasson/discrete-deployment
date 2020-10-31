from typing import Dict

from slugify import slugify
from discrete_deployment.utils.file_helper import FileHelper


class PathsFileParser:

    @staticmethod
    def load_paths(path: str):
        """
        Loads the file containing the paths with it's corresponding names/targets

        @param path: The path of the paths file.
        """
        # Open the yaml file of paths
        file_paths = FileHelper.read_yaml(path)

        targets: Dict[str, str] = {}

        # Read the list of targets
        for file_path in file_paths['paths']:
            # Make sure the name is a list. If it's a string, convert it to a list
            names = [file_path['name']] if isinstance(file_path['name'], str) else file_path['name']
            for name in names:
                # Store it in a dictionary based on the name for quick access
                targets[slugify(name)] = file_path['path']

        return targets
