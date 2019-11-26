class ChessCoordinate:
    _interned = dict()  # _interned is a static property that can be shared among classes

    def __new__(cls, file, rank):
        key = (file, rank)
        if key not in cls._interned:
            obj = super().__new__(cls)
            obj._file = file
            obj._rank = rank
            cls._interned[key] = obj
        return cls._interned[key]

    @property
    def file(self):
        return self._file


    @property
    def rank(self):
        return self._rank


if __name__ == "__main__":
    print(id(ChessCoordinate('A', '8')._interned))
    print(id(ChessCoordinate('B', '8')._interned))

    print(id(ChessCoordinate('B', '1')))
    print(id(ChessCoordinate('B', '1')))
