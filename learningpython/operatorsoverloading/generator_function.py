# any function that contains a yield statement is turned into a generator function
def gen(x):
    for i in range(x):
        yield i ** 2


if __name__ == "__main__":
    G = gen(5)
    print(G)
    print(G.__iter__() == G)

    I = iter(G)
    print(next(I), next(I))

    print(list(gen(5)))
