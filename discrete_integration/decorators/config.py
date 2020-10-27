import os

import click

from discrete_integration.utils.project_root_helper import ProjectRootHelper
from discrete_integration.utils.directory_helper import DirectoryHelper


class Config:

    def __init__(self):
        self.project_root: ProjectRootHelper = ProjectRootHelper()
        self.working_dir: str = DirectoryHelper.get_working_dir()


di_config = click.make_pass_decorator(Config, ensure=True)

__all__ = [
    Config,
    di_config
]
