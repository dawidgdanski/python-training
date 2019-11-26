class SkipObject:  # Another __iter__ + yield generator
    def __init__(self, wrapped):  # Instance scope retained normally
        self.wrapped = wrapped  # Local scope state saved auto

    def __iter__(self):
        offset = 0
        while offset < len(self.wrapped):
            item = self.wrapped[offset]
            offset += 2
            yield item


if __name__ == "__main__":
    skipper = SkipObject('abcdef')
    I = iter(skipper)
    next(I)
    next(I)
    next(I)
    for x in skipper:  # Each for calls __iter__: new auto generator
        for y in skipper:
            print(x + y, end=' ')
