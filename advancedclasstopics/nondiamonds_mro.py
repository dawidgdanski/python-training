class A:
    pass


class B:
    pass  # Another nondiamond: DFLR


class C(A):
    pass


class D(B, C):
    pass


if __name__ == "__main__":
    print(D.__mro__)
    print(D.mro())
    print(D.__bases__)
