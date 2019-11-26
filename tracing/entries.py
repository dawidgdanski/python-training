class EntriesMeta(type):

    def __new__(cls, name, bases, namespace, **kwargs):
        print('Entries.__new__(mcs, name, bases, namespace, **kwargs)')
        print(' kwargs = ', kwargs)
        num_entries = kwargs['num_entries']
        print('num_entries = ', num_entries)
        namespace.update({chr(i): i for i in range(ord('a'), ord('a') + num_entries)})
        return super().__new__(cls, name, bases, namespace)

    def __init__(self, name, bases, namespace, **kwargs):
        super().__init__(name, bases, namespace)


if __name__ == "__main__":
    class AtoZ(metaclass=EntriesMeta, num_entries=26): pass


    print(AtoZ)
    print(AtoZ.a)
    print(AtoZ.b)
    print(AtoZ.c)
