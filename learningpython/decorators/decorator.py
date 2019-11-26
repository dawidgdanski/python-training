def decorator(F):
    print('WRAPPING F')
    return F


@decorator
def func(arg):
    print(arg)


def decorator2(F):  # On @ decoration
    def wrapper(*args):  # On wrapped function call
        F(*args)
        print('SIEMA', args)

    # Use F and args
    # F(*args) calls original function
    return wrapper


@decorator2  # func = decorator(func)
def func2(x, y):  # func is passed to decorator's F
    print('IN func2: ', x, y)


if __name__ == "__main__":
    func('asdf')
    func2(2, 6)
