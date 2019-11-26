class Callee:
    def __call__(self, *pargs, **kargs):  # Intercept instance calls
        print('Called:', pargs, kargs)


if __name__ == "__main__":
    C = Callee()
    C(1, 2, 3)
    C(1, 2, x=3, y=5)
