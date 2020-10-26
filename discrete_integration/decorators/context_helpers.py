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
    def file_exists(file):
        return os.path.isfile(file)

    @staticmethod
    def root_file_exists(path: str):
        if not path.endswith('/'):
            path = path + '/'
        return DirectoryHelper.file_exists(path + settings.INIT_FILE_NAME)

    @staticmethod
    def is_system_root(path):
        return path == DirectoryHelper.traverse_up(path)


class ProjectRoot:

    def __init__(self, path: str, exists: bool, is_assumed: bool):
        self.path = path
        self.exists = exists
        self.is_assumed = is_assumed

    def __str__(self):
        return self.path
