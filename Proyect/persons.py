class Persons:
    
    def __init__(self, name, birthday):
        self.name: str = name
        self.birthday: str = birthday
        
    
    def say_hello(self):
        print(f'Hello, my name is {self.name} and I born in {self.birthday}')


if __name__ == '__main__':
    person = Persons('Mauricio', '10-30-2003')
    
    person.say_hello()