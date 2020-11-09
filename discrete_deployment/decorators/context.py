from os.path import relpath

from discrete_deployment.exceptions import NotInitialisedException


class Context:

    def __init__(self):
        self.working_path: str = ''
        self.project_path: str = ''
        self.project_exists: bool = False

    def get_project_relpath(self, path):
        if not self.project_exists:
            raise NotInitialisedException()
        return relpath(path, self.project_path)

    def get_working_relpath(self, path):
        return relpath(path, self.working_path)
