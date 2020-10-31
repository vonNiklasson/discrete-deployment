import os
import yaml

from discrete_deployment import settings


class FileHelper:

    @staticmethod
    def get_working_path():
        return os.getcwd()

    @staticmethod
    def traverse_up(path: str) -> str:
        return os.path.dirname(path)

    @staticmethod
    def file_exists(path: str):
        return os.path.isfile(path)

    @staticmethod
    def dir_exists(path: str):
        return os.path.isdir(path)

    @staticmethod
    def is_project_root(path: str):
        return FileHelper.file_exists(
            os.path.join(path, settings.DD_PATHS_FILE_NAME)
        )

    @staticmethod
    def has_config_file(path: str):
        return FileHelper.file_exists(
            os.path.join(path, settings.DD_CONFIG_FILE_NAME)
        )

    @staticmethod
    def is_system_root(path: str):
        return path == FileHelper.traverse_up(path)

    @staticmethod
    def compose_dd_config_path(path: str):
        return os.path.join(path, settings.DD_CONFIG_FILE_NAME)

    @staticmethod
    def compose_dd_paths_path(path: str):
        return os.path.join(path, settings.DD_PATHS_FILE_NAME)

    @staticmethod
    def read_yaml(path: str):
        with open(path, 'r') as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError:
                return None

    @staticmethod
    def read_paths_file(path: str):
        return FileHelper.read_yaml(
            FileHelper.compose_dd_paths_path(path)
        )

    @staticmethod
    def read_config_file(path: str):
        return FileHelper.read_yaml(
            FileHelper.compose_dd_config_path(path)
        )

    @staticmethod
    def find_project_root(current_path: str) -> (str, bool):
        """
        Finds the project root based on the current_path.

        @param current_path: The current path to traverse up from.
        @return: A tuple containing of the path and whether the project root was found or not.
        """
        current_path = FileHelper.get_working_path() if current_path is None else current_path
        while True:
            # Check if init file exists in the given path
            if FileHelper.is_project_root(current_path):
                return current_path, True

            # If not make sure we're not at system root and traverse up one directory
            if FileHelper.is_system_root(current_path):
                break
            current_path = FileHelper.traverse_up(current_path)

        return '', False