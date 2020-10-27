from discrete_integration.utils.directory_helper import DirectoryHelper


class RootConfig:

    def __init__(self, project_root: str):
        self.project_root = project_root
        self.di_root = DirectoryHelper.get_di_root(self.project_root)
