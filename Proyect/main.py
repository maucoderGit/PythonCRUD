import sys
clients: list = []


def _create_client():
    request: bool = True
    while request:
        name: str = _get_client_name()
        if name not in clients:
            clients.append(name)
        else:
            print(f'Client "{name}" already is in the client\'s list')
        
        user_chose = input("Do you want to continue? Y/N: ")
        user_chose = user_chose.upper()
        
        if user_chose == "Y" or user_chose == "YES":
            request = True
        elif user_chose == "N" or user_chose == "NO":
            request = False
            print("-"*50)
            print("\nOk! Request Completed successfully")
        else:
            request = False
            print("Stopping...")


def _delete_client(client_id):
    if client_id in clients:
        clients.remove(client_id)
        list_clients()
    else:
        print('Client isn\'t in the client list.')


def _get_client_id():
    """
    Get a user id
    """
    client_id: str = input('- Write client id: ')
    return client_id


def _get_client_name():
    """
    Return a username
    """
    client_name = None

    while not client_name:
        print(f'{"-" * 20} # insert "exit" to break')
        client_name = str(input('Client\'s name: '))

        if client_name.lower() == 'exit':
            client_name = None
            break

    if not client_name:
        sys.exit()

    return client_name


def _update_client(client_id: str):
    if client_id in clients:
        new_client_name: str = input('\bUpdate client name: ')

        index = clients.index(client_id)
        clients[index] = new_client_name
    else:
        print('Client is not in the client list.')


def _read_clients():
    print('[s] to show this list')
    print('[f] to find a client')
    chose: str = input('Please, chose one: ').lower()

    if chose == 's':
        list_clients()
    elif chose == 'f':
        target = _get_client_name()
        if target in clients:
            print(f'The client {target} was found!')
        else:
            print(f'The client was not found')
    else:
        print('Ups! We don\'t have that option. \bPlease send feedback at @maucoder on twitter to more updates!')


def _print_welcome():
    print('Welcome to CMT POS')
    print('-'*50)
    print('What would you like to do today')
    print('Create clients - Write "C"')
    print('Show clients - Write "R"')
    print('Update clients - Write "U"')
    print('Delete clients - Write "D"')


def list_clients():
    for idx, client in enumerate(clients):
        print(f'{idx}: {client}')


def run():
    global clients
    _print_welcome()

    command = input("\nYour chose: ").lower()
    
    if command == 'c':
        _create_client()
        list_clients()
    elif command == 'r':
        _read_clients()
    elif command == 'd':
        client = _get_client_name()

        _delete_client(client)
    elif command == 'u':
        client = _get_client_name()
        _update_client(client)

        list_clients()
    else:
        print('Invalid command, please select an available option')


if __name__ == '__main__':
    run()
