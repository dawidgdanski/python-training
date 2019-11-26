class tracerwithwrapperclass(object):  # A decorator+descriptor
    def __init__(self, func):  # On @ decorator
        self.calls = 0  # Save func for later call
        self.func = func

    def __call__(self, *args, **kwargs):  # On call to original func
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)

    def __get__(self, instance, owner):  # On method attribute fetch
        return wrapper(self, instance)


class tracerwithwrappernestedfunction(object):
    def __init__(self, func):  # On @ decorator
        self.calls = 0  # Save func for later call
        self.func = func

    def __call__(self, *args, **kwargs):  # On call to original func
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)

    def __get__(self, instance, owner):  # On method fetch
        def wrapper(*args, **kwargs):  # Retain both inst
            return self(instance, *args, **kwargs)  # Runs __call__

        return wrapper


class wrapper:
    def __init__(self, desc, subj):  # Save both instances
        self.desc = desc  # Route calls back to deco/desc
        self.subj = subj

    def __call__(self, *args, **kwargs):
        return self.desc(self.subj, *args, **kwargs)  # Runs tracer.__call__


@tracerwithwrapperclass
def spam(a, b, c):  # spam = tracer(spam)
    print(a, b, c)


class Person:
    @tracerwithwrapperclass
    def giveRaise(self, percent):  # giveRaise = tracer(giveRaise)
        print('giveRaise ', percent, sep=' ')


if __name__ == "__main__":
    spam(3, 6, 8)
    Person().giveRaise(.10)
