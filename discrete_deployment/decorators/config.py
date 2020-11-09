from typing import Dict

from slugify import slugify

from discrete_deployment.exceptions import NotInitialisedException
from discrete_deployment.utils.file_helper import FileHelper
from discrete_deployment.utils.index_file_parser import IndexFileParser


class Config:
    def __init__(self):
        self.is_initialised: bool = False
        self.names: Dict[str, str] = {}

    def load_index(self, project_path):
        """
        Loads the file containing the names and their paths into the config class

        @raise NotInitialisedException: If Configuration is not initialised.
        @param project_path: The path of the project root.
        """
        # If there's no project initialised, raise an exception
        if not self.is_initialised:
            raise NotInitialisedException()

        index_file_path = FileHelper.compose_index_path(project_path)
        self.names = IndexFileParser().lazy_load_index_by_names(index_file_path)
