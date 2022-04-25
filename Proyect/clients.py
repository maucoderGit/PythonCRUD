class Client:
    """
    Create client's object
    """
    def __init__(self):
        self._name: str
    
    # returns atribute's name
    @property
    def name(self):
        return self._name
    
    # Set value to atribute name
    @name.setter
    def name(self, name):
        self._name = name