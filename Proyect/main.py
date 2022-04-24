clients = ["Miguel", "Jose", "Carlos"]

def _create_client():
    global clients
    
    request = True
    while request == True:
        name:str = input("Please, write client's name: ")
        if name not in clients:
            clients.append(name)
        else:
            print(f'Client "{name}" already is in the client\'s list')
        
        request = input("Do you want to continue? Y/N: ")
        request = request.upper()
        
        if request == "Y" or request == "YES":
            request = True
        elif request == "N" or request == "NO":
            request = False
            print("-"*50)
            print("\nOk! Request Completed sucefully")
        else:
            request = False
            print("Stopping...")
            
            
def _add_comma(user_var):
    """Add a comma with space to a var string

    Args:
        user_var str: String with names, phares or content

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
    print('[C]reate clients - write "C"')
    print('[D]elete clients - write "D"')
    
def run():
    _print_welcome()

    command = input("\nYour chose: ").lower()
    
    if command == 'c':
        _create_client()
        list_clients()
    elif command == 'd':
        print('We are on BETA version, more updates soon!')
    else:
        print('Invalid command, please select an avalible option')

if __name__ == '__main__':
    run()