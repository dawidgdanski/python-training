class Decorator:
    def __init__(self, C):  # On @ decoration
        self.C = C

    def __call__(self, *args):  # On instance creation
        self.wrapped = self.C(*args)
        return self

    def __getattr__(self, attrname):  # On atrribute fetch
        return getattr(self.wrapped, attrname)


@Decorator
class C:
    pass


if __name__ == "__main__":
    x = C()
    y = C()  # Overwrites x!
