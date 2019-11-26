from learningpython.decorators.singleton3only import singleton3only

_instances = {}


def singleton(aClass):  # On @ decoration
    def onCall(*args, **kwargs):  # On instance creation
        if aClass not in _instances:  # One dict entry per class
            _instances[aClass] = aClass(*args, **kwargs)
        return _instances[aClass]

    return onCall


@singleton  # Person = singleton(Person)
class Person:  # Rebinds Person to onCall
    def __init__(self, name, hours, rate):  # onCall remembers Person
        self.name = name
        self.hours = hours
        self.rate = rate

    def pay(self):
        return self.hours * self.rate


@singleton3only  # Spam = singleton(Spam)
class Spam:  # Rebinds Spam to onCall
    def __init__(self, val):  # onCall remembers Spam
        self.attr = val


if __name__ == "__main__":
    bob = Person('Bob', 40, 10)  # Really calls onCall
    print(bob.name, bob.pay())
    
    sue = Person('Sue', 50, 20)  # Same, single object
    print(sue.name, sue.pay())

    X = Spam(val=42)  # One Person, one Spam
    Y = Spam(99)
    print(X.attr, Y.attr)
