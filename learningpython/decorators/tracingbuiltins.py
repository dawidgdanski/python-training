from learningpython.decorators.tracerclasswrapper import Tracer


@Tracer
class MyList(list): pass  # MyList = Tracer(MyList)


if __name__ == "__main__":
    x = MyList([1, 2, 3])  # Triggers Wrapper()
    x.append(4)  # Triggers __getattr__, append
    x.wrapped

    WrapList = Tracer(list)  # Or perform decoration manually
    x = WrapList([4, 5, 6])  # Else subclass statement required
    x.append(7)
    x.wrapped
