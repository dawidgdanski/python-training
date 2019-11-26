class C:
    def __index__(self):
        return 255


if __name__ == "__main__":
    X = C()
    print(hex(X))
    print(bin(X))
    print(oct(X))
    # noinspection PyTypeChecker
    print(('C' * 256)[X:])
