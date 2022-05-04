import click

from clients import commands as clients_commands


@click.group()
@click.pass_context
def cli(context):
    context.object = {}


cli.add_command(clients_commands.all)