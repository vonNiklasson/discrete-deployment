from typing import Dict

from discrete_integration.exceptions import NotInitialisedException
from discrete_integration.utils.file_helper import FileHelper
from slugify import slugify


class Config:

    def __init__(self):
        self.is_initialised: bool = False
        self.targets: Dict[str, Target] = {}

    def load_targets(self, project_path):
        """
        Loads the file containing the targets into the config class

        @raise NotInitialisedException: If Configuration is not initialised.
        @param project_path: The path of the project root.
        """
        # If there's no project initialised, throw an exception
        if not self.is_initialised:
            raise NotInitialisedException()

        # Open the yaml file of targets
        file_targets = FileHelper.read_targets(project_path)
        for file_target in file_targets['targets']:
            # Create a temporarily target object
            temp_target = Target(
                name=file_target['name'],
                path=file_target['path']
            )
            # Store it in a dictionary based on the name for quick access
            self.targets[temp_target.name] = temp_target


class Target:

    def __init__(self, name: str, path: str):
        self.name: str = slugify(name)
        self.path: str = path
