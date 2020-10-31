import click

from discrete_deployment.decorators import pass_context, pass_config, Context, Config


class Init:

    @staticmethod
    @click.command()
    # Contexts
    @pass_config
    @pass_context
    def command(context: Context, config: Config):
        pass
