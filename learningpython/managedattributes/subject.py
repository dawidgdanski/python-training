class Descriptor:  # Add "(object)" in 2.X
    def __get__(self, instance, owner):
        print(self, instance, owner, sep='\n')


class Subject:  # Add "(object)" in 2.X
    attr = Descriptor()  # Descriptor instance is class attr


if __name__ == "__main__":
    print('-' * 50)
    X = Subject()
    X.attr
    print('-' * 50)
    Subject.attr
    print('-' * 50)