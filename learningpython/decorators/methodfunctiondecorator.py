def decorator(F):  # F is func or method without instance
    def wrapper(*args):  # class instance in args[0] for method
        print('Function wrapper call: ', *args)
        F(*args)

    return wrapper


@decorator
def func(x, y):  # func = decorator(func)
    print('Actual function call: ', x, y)


class C:
    @decorator
    def method(self, x, y):  # method = decorator(method)
        print('Actual method call: ', x, y)


if __name__ == "__main__":
    func(6, 7)  # Really calls wrapper(6, 7)

    X = C()
    X.method(4, 6)  # Really calls wrapper(X, 6, 7)
