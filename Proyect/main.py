clients: list = ["Miguel", "Jose", "Carlos"]


def _get_client_name():
    """
    Return a username
    """
    return input("What is the client name: ")


def _get_client_id():
    """
    Get a user id
    """
    client_id: str = input('- Write client id: ')
    return client_id


def _create_client():
    global clients
    
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
    global clients

    if client_id in clients:
        clients.remove(client_id)
        list_clients()
    else:
        print('Client isn\'t in the client list.')


def _update_client(client_id: str):
    global clients
    if client_id in clients:
        new_client_name: str = input('\bUpdate client name: ')
        clients[clients.index(client_id)] = new_client_name
    else:
        print('Client is not in the client list.')


def _add_comma(user_var):
    """Add a comma with space to a var string

    Args:
        user_var str: String with names, phrases or content

    Returns:
        str: return a string with coma and space on the end
    """
    user_var += ", "
    
    return user_var


def list_clients():
    global clients
    
    print(clients)


def _print_welcome():
    print('Welcome to CMT POS')
    print('-'*50)
    print('What would you like to do today')
    print('Create clients - Write "C"')
    print('Update clients - Write "U"')
    print('Delete clients - Write "D"')


def run():
    _print_welcome()

    command = input("\nYour chose: ").lower()
    
    if command == 'c':
        _create_client()
        list_clients()
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