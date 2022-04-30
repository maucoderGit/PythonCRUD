import sys
clients: list = [
    {
        'name': 'Pablo',
        'company': 'Google',
        'email': 'pablo@google.com',
        'position': 'Software engineer',
    },
    {
        'name': 'Mauricio',
        'company': 'Reserve',
        'email': 'mauricio@reserve.com',
        'position': 'Backend developer',
    }
]


def _get_client_data():
    client: dict = {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'position': _get_client_field('position')
    }

    return client


def _create_client():
    request: bool = True
    while request:
        client = _get_client_data()

        if client not in clients:
            clients.append(client)
        else:
            print(f'Client "{client["name"]}" already is in the client\'s list')
        
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
    is_valid, index = client_id

    if is_valid:
        client = clients[index]
        while True:
            confirm = input(f"Are you secure to remove {client['name']} from client\'s data?: ").upper()
            if confirm == "YES":
                print(f'{index}: {clients[index]} was delete')

                del(clients[index])
                list_clients()
                break
            elif confirm == "NO":
                print("Stopping...")
                break
            else:
                print('Print Yes or No to continue')
    else:
        print('Client isn\'t in the client list.')


def _get_client_id() -> list[bool, int]:
    """
    Get a user integer id
    """
    is_logic: bool = False

    while not is_logic:
        try:
            # If the user sent a not valid value, use exception for error's prevention
            client_id: int = int(input('- Write client id: '))
            is_valid = True

            if clients[client_id] not in clients:
                print('Sorry, that index is out of range or was not found')
                is_valid = False

            return [is_valid, client_id]

        except IndexError:
            print('Please write a valid index')

        except ValueError:
            print('Please write a number.\n')


def _get_client_field(data):
    """
    Return a username
    """
    client_info = None

    while not client_info:
        print(f'{"-" * 20} # insert "exit" to break')
        client_info = str(input(f'Client\'s {data}: '))

        if client_info.lower() == 'exit':
            client_info = None
            break

    if not client_info:
        sys.exit()

    return client_info


def _update_client(client_id: list):
    validator = client_id[0]
    index = client_id[1]

    if validator:
        new_client: dict = _get_client_data()

        clients[index] = new_client
    else:
        print('Client is not in the client list.')


def _read_clients():
    print('[s] to show this list')
    print('[f] to find a client')
    chose: str = input('Please, chose one: ').lower()

    if chose == 's':
        list_clients()
    elif chose == 'f':
        target, index = _get_client_id()

        if target:
            client = clients[index]
            print(f'The client {client["name"]} was found!')
        else:
            print(f'The client was not found')
    else:
        print('Ups! We don\'t have that option.\nPlease send feedback at @maucoder on twitter to more updates!')


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
        print(f'{idx}: {client["name"]} | {client["company"]} | {client["email"]} | {client["position"]}')


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
        client = _get_client_id()

        _delete_client(client)
    elif command == 'u':
        client = _get_client_id()
        _update_client(client)

        list_clients()
    else:
        print('Invalid command, please select an available option')


if __name__ == '__main__':
    run()
