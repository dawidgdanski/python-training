from abc import ABC, abstractmethod


class SwordMeta(type):

    def __instancecheck__(self, instance):
        return self.__subclasscheck__(type(instance))

    def __subclasscheck__(self, subclass):
        return (hasattr(subclass, 'swipe') and callable(subclass.swipe) and
                hasattr(subclass, 'sharpen') and callable(subclass.sharpen))


class Sword(ABC):

    @classmethod
    def __subclasshook__(cls, subclass):
        return ((hasattr(subclass, 'swipe') and callable(subclass.swipe) and
                 hasattr(subclass, 'sharpen') and callable(subclass.sharpen))
                or
                NotImplemented)

    @abstractmethod
    def thrust(self):
        print('Thrust...')


class BoardSword(Sword):
    def thrust(self):
        super().thrust()

    def swipe(self):
        print('Swoosh')

    def sharpen(self):
        print('Shink')


@Sword.register
class LightSaber:
    def swipe(self):
        print('Light saber swipe')


class SamuraiSword:
    def swipe(self):
        print('Swoosh')

    def sharpen(self):
        print('Shink')


if __name__ == "__main__":
    print(issubclass(SamuraiSword, Sword))
    print(isinstance(BoardSword(), Sword))
    print(issubclass(LightSaber, Sword))
