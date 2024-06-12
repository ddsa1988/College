class Person:
    def __init__(self, name, cpf):
        self.name = name
        self.cpf = cpf

    def __lt__(self, other):
        if isinstance(other, type(self)):
            return self.name < other.name

    def __gt__(self, other):
        if isinstance(other, type(self)):
            return self.name > other.name

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.name == other.name

        return False

    def __repr__(self):
        return f"Name: {self.name} CPF: {self.cpf}"
