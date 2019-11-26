class simplelogger:
    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        print('Logging function call ')
        self._func(*args)


@simplelogger
def func(x, y):
    print('IN FUNC HERE: ', x, y)


if __name__ == "__main__":
    func(5, 10)
