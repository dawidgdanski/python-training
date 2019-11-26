class Eggs:  # Inherited names here
    pass


class Spam(Eggs):  # Inherits from Eggs
    data = 1  # Class data attribute

    def meth(self, arg):  # Class method attribute
        return self.data + arg


# Alternative form of definining a Spam class
Spam2 = type('Spam', (Eggs,), {'data': 1, 'meth': lambda self, arg: self.data + arg, '__module__': '__main__'})

if __name__ == "__main__":
    print(Spam().meth(1))
    print(Spam2().meth(1))
