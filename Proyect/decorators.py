PASSWORD = 'MySecurePassword1234!"#$'


def password_required(func):
    def wrapper():
        password = input('password: ')
        
        if password == PASSWORD:
            return func()
        else:
            print('password isn\'t valid')
                  
    return wrapper


@password_required
def need_password():
    print('The password is correct!')


def upper(func) -> str:
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        
        return result.upper()
    return wrapper


@upper
def say_my_name(name: str) -> str:
    return f'Hola, {name}'


def run():
    print(say_my_name('Mau'))
    need_password()


if __name__ == '__main__':
    run()