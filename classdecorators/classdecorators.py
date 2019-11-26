import functools
from abc import ABC, abstractmethod


def my_class_decorator(cls):
    for name, attr in vars(cls).items():
        print(name)
    return cls


def _wrap_method_with_invariant_checking_proxy(cls, name, predicate):
    method = getattr(cls, name)
    assert callable(method)

    @functools.wraps(method)
    def invariant_checking_method_decorator(self, *args, **kwargs):
        result = method(self, *args, **kwargs)
        if not predicate(self):
            raise RuntimeError('Class invariant {!r} violated for {!r}'.format(predicate.__doc__, self))
        return result

    setattr(cls, name, invariant_checking_method_decorator)


def _wrap_property_with_invariant_checking_proxy(cls, name, predicate):
    prop = getattr(cls, name)
    assert isinstance(prop, property)
    invariant_checking_proxy = InvariantCheckingPropertyProxy(prop, predicate)
    setattr(cls, name, invariant_checking_proxy)


def invariant(predicate):
    def invariant_checking_class_decorator(cls):
        method_names = [name for name, attr in vars(cls).items() if callable(attr)]
        for name in method_names:
            _wrap_method_with_invariant_checking_proxy(cls, name, predicate)
        property_names = [name for name, attr in vars(cls).items() if isinstance(attr, PropertyDataDescriptor)]
        for name in property_names:
            _wrap_property_with_invariant_checking_proxy(cls, name, predicate)
        return cls

    return invariant_checking_class_decorator


def not_below_absolute_zero(temperature):
    """
    Checks whether temperature is not below zero
    """
    return temperature._kelvin > 0


def below_absolute_hot(temperature):
    """
    Temperature below absolute hot
    """
    return temperature._kelvin <= 1.416785e32


class PropertyDataDescriptor(ABC):

    @abstractmethod
    def __get__(self, instance, owner):
        raise NotImplementedError

    @abstractmethod
    def __set__(self, instance, value):
        raise NotImplementedError

    @abstractmethod
    def __delete__(self, instance):
        raise NotImplementedError

    @property
    @abstractmethod
    def __isabstractmethod__(self):
        raise NotImplementedError


PropertyDataDescriptor.register(property)


class InvariantCheckingPropertyProxy(PropertyDataDescriptor):

    def __init__(self, referent, predicate):
        self.predicate = predicate
        self.referent = referent

    def __get__(self, instance, owner):
        if instance is None:
            return self.referent
        result = self.referent.__get__(instance, owner)
        if not self.predicate(instance):
            raise RuntimeError("Class invariant {!r} violated for {!r}".format(self.predicate.__doc__, instance))
        return result

    def __set__(self, instance, value):
        result = self.referent.__set__(instance, value)
        if not self.predicate(instance):
            raise RuntimeError("Class invariant {!r} violated for {!r}".format(self.predicate.__doc__, instance))
        return result

    def __delete__(self, instance):
        result = self.referent.__delete(instance)
        if not self.predicate(instance):
            raise RuntimeError("Class invariant {!r} violated for {!r}".format(self.predicate.__doc__, instance))
        return result

    @property
    def __isabstractmethod__(self):
        return self.referent.__isabstractmethod__


# @my_class_decorator
@invariant(below_absolute_hot)
@invariant(not_below_absolute_zero)
class Temperature:

    def __init__(self, kelvin):
        self._kelvin = kelvin

    def get_kelvin(self):
        return self._kelvin

    def set_kelvin(self, kelvin):
        self._kelvin = kelvin

    @property
    def celsius(self):
        return self._kelvin - 273.15

    @celsius.setter
    def celsius(self, value):
        self._kelvin = value + 273.15


if __name__ == "__main__":
    temperature = Temperature(123)
    temperature.celsius = -400
    temperature.set_kelvin(1e33)
