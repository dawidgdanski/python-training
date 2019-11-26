from learningpython.decorators.commonusage.access2 import trace


def accessControl(failIf):
    def onDecorator(aClass):
        def getattributes(self, attr):
            trace('get:', attr)
            if failIf(attr):
                raise TypeError('private attribute fetch: ' + attr)
            else:
                return object.__getattribute__(self, attr)

        def setattributes(self, attr, value):
            trace('set:', attr)
            if failIf(attr):
                raise TypeError('private attribute change: ' + attr)
            else:
                return object.__setattr__(self, attr, value)

        aClass.__getattribute__ = getattributes
        aClass.__setattr__ = setattributes  # Insert accessors
        return aClass  # Return original class

    return onDecorator


def Private(*attributes):
    return accessControl(failIf=(lambda attr: attr in attributes))


def Public(*attributes):
    return accessControl(failIf=(lambda attr: attr not in attributes))


if __name__ == "__main__":
    # @Private('age')  # Person = Private('age')(Person)
    # class Person:  # Person = onInstance with state
    #     def __init__(self, name, age):
    #         self.name = name
    #         self.age = age  # Inside accesses run normally
    #
    #
    # X = Person('Bob', 40)
    # X.name  # Outside accesses validated
    # X.name = 'Sue'
    # X.name
    # X.age
    # X.age = 'Tom'

    @Public('name')
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age


    X = Person('bob', 40)  # X is an onInstance
    X.name  # onInstance embeds Person
    X.name = 'Sue'
    X.name
    X.age
    X.age = 'Tom'
