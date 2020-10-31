import glob

import click

from discrete_deployment.decorators import pass_context, pass_config, Context, Config


class Scan:

    @staticmethod
    @click.command()
    # Contexts
    @pass_config
    @pass_context
    def command(context: Context, config: Config):
        Scan.find_ddep_configs_paths(context.project_path)

    @staticmethod
    def find_ddep_configs_paths(path: str):
        file_paths = []
        file_names = glob.iglob(path + '/**/ddep.yaml', recursive=True)
        for file_name in file_names:
            file_paths.append(file_name)

