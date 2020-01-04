

class User:

    def __init__(self, name=None):
        self.name = name

    def __str__(self):
        return '' if self.name is None else self.name
