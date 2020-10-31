from typing import Dict

from discrete_deployment.exceptions import NotInitialisedException
from discrete_deployment.utils.file_helper import FileHelper
from slugify import slugify


class Config:

    def __init__(self):
        self.is_initialised: bool = False
        self.targets: Dict[str, str] = {}
        self.configs: Dict[str, str] = {}

    def load_paths(self, project_path):
        """
        Loads the file containing the targets into the config class

        @raise NotInitialisedException: If Configuration is not initialised.
        @param project_path: The path of the project root.
        """
        # If there's no project initialised, throw an exception
        if not self.is_initialised:
            raise NotInitialisedException()

        # Open the yaml file of paths
        file_paths = FileHelper.read_paths_file(project_path)

        # Read the list of targets
        for file_target in file_paths['targets']:
            # Store it in a dictionary based on the name for quick access
            self.targets[slugify(file_target['name'])] = file_target['path']

        # Read the list of configs
        for file_config in file_paths['configs']:
            # Store it in a dictionary based on the name for quick access
            self.configs[slugify(file_config['name'])] = file_config['path']


class DdFile:

    TYPE_TARGET = 'target'
    TYPE_CONFIG = 'config'

    name: str
    path: str
    dd_type: str

    @classmethod
    def from_path(cls, path):
        file_contents = FileHelper.read_yaml(path)


class DdTarget(DdFile):
    pass