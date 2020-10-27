from discrete_integration.utils.directory_helper import DirectoryHelper


class ProjectRootHelper:

    def __init__(self, path: str = '', exists: bool = False, is_assumed: bool = False):
        self.path = path
        self.exists = exists
        self.is_assumed = is_assumed

    def assume_project_root(self, current_path: str = None):
        current_path = DirectoryHelper.get_working_dir() if current_path is None else current_path
        while True:
            # Check if init file exists in the given path
            if DirectoryHelper.is_project_root(current_path):
                self.path = current_path
                self.is_assumed = True
                self.exists = True

            # If not make sure we're not at system root and traverse up one directory
            if DirectoryHelper.is_system_root(current_path):
                break
            current_path = DirectoryHelper.traverse_up(current_path)

    def __str__(self):
        return self.path
