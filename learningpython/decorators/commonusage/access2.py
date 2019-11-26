"""
File access2.py (3.X + 2.X)
Class decorator with Private and Public attribute declarations.

Controls external access to attributes stored on an instance, or
Inherited by it from its classes. Private declares attribute names
that cannot be fetched or assigned outside the decorated class,
and Public declares all the names that can.

Caveat: this works in 3.X for explicitly named attributes only: __X__
operator overloading methods implicitly run for built-in operations
do not trigger either __getattr__ or __getattribute__ in new-style
classes.  Add __X__ methods here to intercept and delegate built-ins.
"""

traceMe = False


def trace(*args):
    if traceMe: print('[' + ' '.join(map(str, args)) + ']')


def accessControl(failIf):
    def onDecorator(aClass):
        class onInstance:
            def __init__(self, *args, **kargs):
                self.__wrapped = aClass(*args, **kargs)

            def __getattr__(self, attr):
                trace('get:', attr)
                if failIf(attr):
                    raise TypeError('private attribute fetch: ' + attr)
                else:
                    return getattr(self.__wrapped, attr)

            def __setattr__(self, attr, value):
                trace('set:', attr, value)
                if attr == '_onInstance__wrapped':
                    self.__dict__[attr] = value
                elif failIf(attr):
                    raise TypeError('private attribute change: ' + attr)
                else:
                    setattr(self.__wrapped, attr, value)

        return onInstance

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
