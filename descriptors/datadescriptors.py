class DataDescriptor:

    def __get__(self, instance, owner):
        print("{!r}.__get__({!r}, {!r})".format(self.__class__.__name__, instance, owner))

    def __set__(self, instance, value):
        print("{!r}.__set__({!r}, {!r})".format(self.__class__.__name__, instance, value))


class NonDataDescriptor:

    def __get__(self, instance, owner):
        print("{!r}.__get__({!r}, {!r})".format(self.__class__.__name__, instance, owner))


class Owner:
    a = DataDescriptor()
    b = NonDataDescriptor()


if __name__ == "__main__":
    obj = Owner()
    obj.a
    obj.__dict__['a'] = 123456
    obj.a  # Data descriptor takes precedence over the attribute stored in __dict__ dictionary

    obj.b
    obj.__dict__['b'] = 'asdf'
    print(obj.b)  # Attribute in __dict__ takes precedence over the non-data descriptor
