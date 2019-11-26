class Descriptor:
    """docstring goes here"""

    def __get__(self, instance, owner):
        pass  # Return attr value

    def __set__(self, instance, value):
        pass  # Return nothing (None)

    def __delete__(self, instance):
        pass  # Return nothing (None)
