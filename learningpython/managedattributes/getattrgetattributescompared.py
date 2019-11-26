class GetAttr:
    attr1 = 1

    def __init__(self):
        self.attr2 = 2

    def __getattr__(self, attr):  # On undefined attrs only
        print('get: ' + attr)  # Not on attr1: inherited from class
        if attr == 'attr3':  # Not on attr2: stored on instance
            return 3
        else:
            raise AttributeError(attr)




class GetAttribute(object):  # (object) needed in 2.X only
    attr1 = 1

    def __init__(self):
        self.attr2 = 2

    def __getattribute__(self, attr):  # On all attr fetches
        print('get: ' + attr)  # Use superclass to avoid looping here
        if attr == 'attr3':
            return 3
        else:
            return object.__getattribute__(self, attr)


if __name__ == "__main__":
    X = GetAttr()
    print(X.attr1)
    print(X.attr2)
    print(X.attr3)
    print('-' * 20)

    X = GetAttribute()
    print(X.attr1)
    print(X.attr2)
    print(X.attr3)
