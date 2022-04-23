CLIENTS = ["Juan", "Jose", "Pedro"]

def run():
    counter = 0
    for i in CLIENTS:
        print(f'{counter}. {CLIENTS[counter]}')
        counter += 1

if __name__ == '__main__':
    run()