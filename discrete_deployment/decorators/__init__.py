from discrete_deployment.decorators.config import Config
from discrete_deployment.decorators.context import Context
import click

pass_context = click.make_pass_decorator(Context, ensure=True)
pass_config = click.make_pass_decorator(Config, ensure=True)

__all__ = [pass_context, pass_config]
