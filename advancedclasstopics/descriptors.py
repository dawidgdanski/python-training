class AgeDesc(object):
    def __get__(self, instance, owner): return 40

    def __set__(self, instance, value): instance._age = value


class Descriptors(object):
    age = AgeDesc()


if __name__ == "__main__":
    x = Descriptors()
    print(x.age)

    x.age = 42
    print(x._age)
