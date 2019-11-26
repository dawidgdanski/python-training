class Indexer:
    data = [5, 6, 7, 8, 9]

    def __getitem__(self, index):  # Called for index or slice
        if isinstance(index, int):  # Test usage mode
            print('indexing', index)
        else:
            print('slicing', index.start, index.stop, index.step)
        return self.data[index]  # Perform index or slice

    def __setitem__(self, index, value):  # Intercept index or slice assignment
        print('setting', index, value)
        self.data[index] = value  # Assign index or slice


if __name__ == "__main__":
    X = Indexer()

    print(X[0])
    print(X[-1])
    print(X[2:4])
    print(X[1:])
    print(X[:-1])
    print(X[::2])

    X[2:4] = 1, 2, 3
    print(X.data)
