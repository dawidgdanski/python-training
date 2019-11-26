class TracingMeta(type):

    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        print('TracingMeta.__prepare__(name, bases, **kwargs)')
        print(' mcs = ', mcs)
        print(' name = ', name)
        print(' bases = ', bases)
        print(' kwargs = ', kwargs)
        namespace = super().__prepare__(name, bases)
        print(' namespace = ', namespace)
        print()
        return namespace

    def __init__(cls, name, bases, namespace, **kwargs):
        print('TracingMeta.__init__(cls, name, bases, namespace, **kwargs)')
        print(' cls = ', cls)
        print(' name = ', name)
        print(' bases = ', bases)
        print(' namespace = ', namespace)
        print(' kwargs = ', kwargs)
        super().__init__(name, bases, namespace)
        print()

    def metamethod(cls):
        print('TracingMeta.metamethod(cls)')
        print(' cls = ', cls)

    def __call__(cls, *args, **kwds):
        print('TracingMeta.__call__(cls, *args, **kwargs)')
        print(' cls = ', cls)
        print(' args = ', args)
        print(' kwargs = ', kwds)
        print('calling type.__call__()')
        obj = super().__call__(*args, **kwds)
        print(' type.__call__() result = ', obj)
        print('Returned from type.__call__()')
        print()
        return obj


class TracingClass(metaclass=TracingMeta):

    def __new__(cls, *args, **kwargs):
        print('TracingClass.__new__(cls, args, kwargs)')
        print(' cls = ', cls)
        print(' args = ', args)
        print(' kwargs = ', kwargs)
        obj = super().__new__(cls)
        print('type.__new__() result = ', obj)
        print()
        return obj

    def __init__(self, *args, **kwargs):
        print('TracingClass.__init__(self, *args, **kwargs)')
        print(' self = ', self)
        print(' args = ', args)
        print(' kwars = ', kwargs)
        print()


if __name__ == "__main__":
    print(TracingClass())
