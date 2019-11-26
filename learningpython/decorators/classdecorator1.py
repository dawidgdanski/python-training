def decorator(cls):  # On @ decoration
    class Wrapper:
        def __init__(self, *args):  # On instance creation
            self.wrapped = cls(*args)

        def __getattr__(self, name):  # On attribute fetch
            return getattr(self.wrapped, name)

    return Wrapper


@decorator
class C:  # C = decorator(C)
    def __init__(self, x, y):  # Run by Wrapper.__init__
        self.attr = 'spam'


if __name__ == "__main__":
    x = C(6, 7)  # Really calls Wrapper(6, 7)
    print(x.attr)  # Runs Wrapper.__getattr__, prints "spam"
