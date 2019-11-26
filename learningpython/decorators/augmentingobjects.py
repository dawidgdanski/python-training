# Augmenting decorated objects directly

def decorate(func):
    func.marked = True  # Assign function attribute for later use
    return func


@decorate
def spam1(a, b):
    return a + b


def annotate(text):  # Same, but value is decorator argument
    def decorate(func):
        func.label = text
        return func

    return decorate


@annotate('spam data')
def spam2(a, b):  # spam = annotate(...)(spam)
    return a + b


if __name__ == "__main__":
    print(spam1.marked)

    print(spam2(1, 2))

    print(spam2.label)
