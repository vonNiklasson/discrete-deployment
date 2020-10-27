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
            os.path.join(path, settings.DI_ROOT_CONFIG_DIR_NAME)
        )

    @staticmethod
    def is_system_root(path: str):
        return path == DirectoryHelper.traverse_up(path)

    @staticmethod
    def get_di_file_path(path: str):
        return os.path.join(path, settings.DI_FILE_NAME)

    @staticmethod
    def get_di_config_path(path: str):
        return os.path.join(path, settings.DI_ROOT_CONFIG_DIR_NAME)

    @staticmethod
    def create_di_config_dir(path: str):
        os.mkdir(DirectoryHelper.get_di_config_path(path), mode=0o755)
