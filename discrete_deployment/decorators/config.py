from typing import Dict

from discrete_deployment.exceptions import NotInitialisedException
from discrete_deployment.utils.file_helper import FileHelper
from slugify import slugify

from discrete_deployment.utils.paths_file_parser import PathsFileParser


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

        paths_file_path = FileHelper.compose_paths_path(project_path)
        self.targets = PathsFileParser().load_paths(paths_file_path)
