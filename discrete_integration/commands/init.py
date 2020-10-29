import click

from discrete_integration.decorators import pass_context, pass_config


class Init:

    @staticmethod
    @click.command()
    @pass_context
    @pass_config
    def command(context, config):
        pass
