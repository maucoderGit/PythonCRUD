import click


@click.group()
def clients():
    """Manages the clients lifecycle"""
    pass


@clients.command()
@click.pass_context
def create(context, name, company, email, position):
    """Creates a new client

    Args:
        context (object): _description_
        name (str): user's name
        company (str): user's work
        email (str): user's email
        position (str): user's position
    """
    pass


@clients.command()
@click.pass_context
def lists(context):
    """List all clients

    Args:
        context (_type_): _description_
    """
    pass


@clients.command()
@click.pass_context
def update(context, client_uid):
    """Updates a client"""
    pass


@clients.command()
@click.pass_context
def delete(context, client_uid):
    """Deletes a client"""
    pass


all = clients
