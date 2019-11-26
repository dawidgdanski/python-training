class Number:
    def __init__(self, start):  # On Number(start)
        self.data = start

    def __sub__(self, other):  # On instance - other
        if isinstance(other, Number):
            return Number(self.data - other.data)
        elif isinstance(other, int):
            return Number(self.data - other)
        else:
            raise ValueError(f'Incorrect value to subtract: {other}')

    def __repr__(self):
        return f'{self.data}'


if __name__ == "__main__":
    X = Number(6)
    Y = X - 2
    print(Y.data)
    Z = Number(5)
    print(X - Z)
    # print(X - '')
