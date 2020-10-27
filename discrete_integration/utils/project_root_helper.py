class ProjectRootHelper:

    def __init__(self, path: str = '', exists: bool = False, is_assumed: bool = False):
        self.path = path
        self.exists = exists
        self.is_assumed = is_assumed

    def __str__(self):
        return self.path
