class Properties(object):  # Need object in 2.X for setters
    def getage(self):
        return 40

    def setage(self, value):
        print('set age: %s' % value)
        self._age = value

    age = property(getage, setage, None, None)


class Operators:
    def __getattr__(self, name):  # On undefined reference
        if name == 'age':
            return 40
        else:
            raise AttributeError(name)

    def __setattr__(self, name, value):  # On all assignments
        print('set: %s %s' % (name, value))
        if name == 'age':
            self.__dict__['_age'] = value  # Or object.__setattr__()
        else:
            self.__dict__[name] = value


if __name__ == "__main__":
    x = Properties()
    x.age = 1
    print(x.age)

    y = Operators()

    y.age = 12
    print(y.age)

    y.job = 'trainer'
    print(y.job)
