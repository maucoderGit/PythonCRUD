clients = []

def list_clients():
    global clients
    
    print(clients)

def create_client(client_name):
    global clients
    clients.append(client_name)
    
def _add_comma(user_var):
    """Add a comma with space to a var string

    Args:
        user_var str: String with names, phares or content

    Returns:
        str: return a string with coma and space on the end
    """
    user_var += ", "
    
    return user_var

    
def run():
    global clients
    list_clients()
    
    request = True
    while request == True:
        name:str = input("Please, write client's name: ")
        create_client(name)
        
        request = input("Do you want to continue? Y/N: ")
        request = request.upper()
        
        if request == "Y" or request == "YES":
            request = True
        elif request == "N" or request == "NO":
            request = False
            print("-"*30)
            print("\nOk! Request Completed sucefully")
        else:
            request = False
            print("Stopping...")
        
    names = ""
    for i in clients:
        names += i
        names = _add_comma(names)
    
    print(names)

if __name__ == '__main__':
    run()