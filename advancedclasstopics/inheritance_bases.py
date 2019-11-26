class X:
    def m(self): print('X.m')


class Y:
    def m(self): print('Y.m')


class C(X):  # Start out inheriting from X
    def m(self): super().m()


if __name__ == "__main__":
    i = C()
    i.m()
    C.__bases__ = (Y,)  # Change superclass at runtime!
    i.m()
