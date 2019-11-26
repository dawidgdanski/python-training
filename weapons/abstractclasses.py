from abc import ABC, abstractmethod


class AbstractBaseClass(ABC):

    @staticmethod
    @abstractmethod
    def an_abstract_static_method():
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def an_abstract_class_method(cls):
        raise NotImplementedError

    @property
    @abstractmethod
    def an_abstract_property(self):
        raise NotImplementedError

    @an_abstract_property.setter
    @abstractmethod
    def an_abstract_property(self, value):
        raise NotImplementedError


class MyDataDescriptor(ABC):

    @abstractmethod
    def __get__(self, instance, owner):
        pass

    @abstractmethod
    def __set__(self, instance, value):
        pass

    @abstractmethod
    def __delete__(self, instance):
        pass

    @property
    def __isabstractmethod__(self):
        return True
