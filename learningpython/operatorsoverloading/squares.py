class Squares:
    def __init__(self, start, stop):  # Save state when created
        self.value = start - 1
        self.stop = stop

    def __iter__(self):  # Get iterator object on iter
        return self

    def __next__(self):  # Return a square on each iteration
        if self.value == self.stop:  # Also called by next built-in
            raise StopIteration
        self.value += 1
        return self.value ** 2


if __name__ == "__main__":
    for i in Squares(1, 5):
        print(i, end=' ')
    # or [x ** 2 for x in range(1, 6)]
    print()
    X = Squares(2, 7)
    print([x for x in X])  # Exhausts items: __iter__ returns self
    print([x for x in X])  # Now it's empty: __iter__ returns same self

    print([n for n in Squares(1, 5)])  # Make a new iterable object
    print(list(Squares(1, 3)))  # A new object for each new __iter__ call

    print(36 in Squares(1, 10))
    a, b, c = Squares(1, 3)  # Each calls __iter__ and then __next__
    print(a, b, c)
    print(':'.join(map(str, Squares(1, 5))))

    X = Squares(1, 5)
    print(tuple(X), tuple(X))

    X = list(Squares(1, 5))
    print(tuple(X), tuple(X))
