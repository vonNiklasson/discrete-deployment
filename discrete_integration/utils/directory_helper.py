import os

from discrete_integration import settings


class DirectoryHelper:

    @staticmethod
    def get_working_dir():
        return os.getcwd()

    @staticmethod
    def traverse_up(path):
        return os.path.dirname(path)

    @staticmethod
    def file_exists(path: str):
        return os.path.isfile(path)

    @staticmethod
    def dir_exists(path: str):
        return os.path.isdir(path)

    @staticmethod
    def is_project_root(path: str):
        return DirectoryHelper.dir_exists(
            os.path.join(path, settings.DI_CONFIG_FILE_NAME)
        )

    @staticmethod
    def is_system_root(path: str):
        return path == DirectoryHelper.traverse_up(path)

    @staticmethod
    def compose_di_config_path(path: str):
        return os.path.join(path, settings.DI_CONFIG_FILE_NAME)

    @staticmethod
    def compose_di_paths_path(path: str):
        return os.path.join(path, settings.DI_PATHS_FILE_NAME)
