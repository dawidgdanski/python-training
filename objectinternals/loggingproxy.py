from typing import Any

_TARGET = 'target'


class LoggingProxy:
    def __init__(self, target):
        super().__setattr__('target', target)

    def __getattribute__(self, name: str) -> Any:
        target = super().__getattribute__(_TARGET)
        try:
            value = getattr(target, name)
        except AttributeError as e:
            raise AttributeError("{} could not forward request {} to {}".format(
                super().__getattribute__('__class__').__name__, name, target)) \
                from e
        print('Retrieved attribute {!r} = {!r} from {!r}'.format(name, value, target))
        return value

    def __setattr__(self, name, value):
        target = super().__getattribute__(_TARGET)
        try:
            setattr(target, name, value)
        except AttributeError as e:
            raise AttributeError("{} could not forward request {} to {}".format(
                super().__getattribute__('__class__').__name__, name, target)) \
                from e
        print('Set attribute {!r} = {!r} from {!r}'.format(name, value, target))

    def __repr__(self):
        target = super().__getattribute__(_TARGET)
        repr_callable = getattr(target, '__repr__')
        return repr_callable()


if __name__ == "__main__":
    class TestTarget:

        def __repr__(self):
            return "TestTarget"

    logging_vector = LoggingProxy(TestTarget())
    logging_vector.k = 8
    print(logging_vector.k)
    repr(logging_vector)
