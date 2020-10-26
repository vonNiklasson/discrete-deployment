import os

from discrete_integration.decorators.context_helpers import ProjectRoot, DirectoryHelper


class Config:

    def __init__(self):
        self.project_root: ProjectRoot = ProjectRoot('', False, False)
        self.working_dir: str = DirectoryHelper.get_working_dir()

    def assume_project_root(self, current_path: str = None):
        current_path = self.working_dir if current_path is None else current_path
        while True:
            # Check if init file exists in the given path
            if DirectoryHelper.root_file_exists(current_path):
                self.project_root.path = current_path
                self.project_root.is_assumed = True
                self.project_root.exists = True

            # If not make sure we're not at system root and traverse up one directory
            if DirectoryHelper.is_system_root(current_path):
                break
            current_path = DirectoryHelper.traverse_up(current_path)