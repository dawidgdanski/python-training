class Truth:
    def __bool__(self):
        print('__bool__')
        return True  # 3.X tries __bool__ first if not defined, then tries __len__

    def __len__(self):
        print('__len__')
        return 0  # 2.X tries __len__ first


if __name__ == "__main__":
    X = Truth()
    if X:
        print('SUCCESS')
    else:
        print('FAILURE')
