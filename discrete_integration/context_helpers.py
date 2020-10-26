import os


class DirectoryHelper:

    @staticmethod
    def traverse_up(path):
        return os.path.dirname(path)

    @staticmethod
    def file_exists(file):
        return os.path.isfile(file)

    @staticmethod
    def init_file_exists(path):
        DirectoryHelper.file_exists(path + '.di_init.json')

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
