def d1(F): return lambda: 'X' + F()


def d2(F): return lambda: 'Y' + F()


def d3(F): return lambda: 'Z' + F()


@d1
@d2
@d3
def func():  # func = d1(d2(d3(func)))
    return 'spam'


if __name__ == "__main__":
    print(func())  # Prints "XYZspam"
