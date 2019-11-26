import traceback


def inverse(x):
    return 1 / x


if __name__ == "__main__":
    try:
        inverse(0)
    except Exception:
        traceback.print_exc(file=open('badly.exc', 'w'))
