class A: pass


class B(A): pass  # Diamonds: order differs for newstyle


class C(A): pass  # Breadth-first across lower levels


class D(B, C): pass


if __name__ == "__main__":
    print(D.mro())
    print(D.__mro__)
    print(D.__bases__)