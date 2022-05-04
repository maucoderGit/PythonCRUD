import csv

from clients.models import Clients

class ClientService:

    def __init__(self, table_name):
        self.table_name = table_name

        
    def create_client(self, client):
        with open(self.table_name, mode='a') as f:
            writer =csv.DictWriter(f, fieldnames=Clients.schema())
            writer.writerow(client.to_dict())
            
    def list_clients(self):
        with open(self.table_name, mode='r') as f:
            reader = csv.DictReader(f, fieldnames=Clients.schema())

            return list(reader)