class tracer:
    def __init__(self, func):  # On @ decoration: save original func
        self.calls = 0
        self.func = func

    def __call__(self, *args):  # On later calls: run original func
        self.calls += 1
        print('call %s to %s : args = %s' % (self.calls, self.func.__name__, args))
        self.func(*args)


@tracer
def spam(a, b, c):  # spam = tracer(spam)
    print(a + b + c)  # Wraps spam in a decorator object


if __name__ == "__main__":
    spam(1, 2, 3)
    spam(2, 3, 4)
    spam(3, 4, 5)
