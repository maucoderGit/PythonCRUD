import click
from tabulate import tabulate

from clients.services import ClientService
from clients.models import Clients

@click.group()
def clients():
    """Manages the clients lifecycle"""
    pass


@clients.command()
@click.option('-n', '--name',
              type=str,
              prompt= True,
              help='The client name')
@click.option('-n', '--company',
              type=str,
              prompt= True,
              help='The client company')
@click.option('-n', '--email',
              type=str,
              prompt= True,
              help='The client email')
@click.option('-n', '--position',
              type=str,
              prompt= True,
              help='The client position')
@click.pass_context
def create(ctx, name, company, email, position):
    """Creates a new client

    Args:
        context (object): _description_
        name (str): user's name
        company (str): user's work
        email (str): user's email
        position (str): user's position
    """
    client = Clients(name, company, email, position)
    client_service = ClientService(ctx.obj['clients_table'])
    
    client_service.create_client(client)


@clients.command()
@click.pass_context
def lists(ctx):
    """List all clients"""
    client_service = ClientService(ctx.obj['clients_table'])
    clients_list = client_service.list_clients()

    headers = [field.capitalize() for field in Clients.schema()]
    table = []

    for client in clients_list:
        table.append(
            [client['name'],
             client['company'],
             client['email'],
             client['position'],
             client['uid']])

    print(tabulate(table, headers))
    

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
