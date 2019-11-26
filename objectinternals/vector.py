from typing import Any


class Vector:

    def __init__(self, **coords):
        private_coords = {f'_{k}': v for k, v in coords.items()}
        self.__dict__.update(private_coords)

    def __getattr__(self, name: str) -> Any:
        private_name = f'_{name}'
        if private_name not in self.__dict__:
            raise AssertionError('{!r} object has no attribute {!r}'.format(self.__class__, name))
        return getattr(self, private_name)

    def __setattr__(self, name: str, value: Any) -> None:
        raise AssertionError('Cannot set attribute {!r}'.format(name))

    def __delattr__(self, name: str) -> None:
        raise AssertionError('Cannot delete attribute {!r}'.format(name))

    def __repr__(self) -> str:
        return f'{self.__class__}({", ".join(("{k}={v}".format(k=k, v=self.__dict__[k]) for k in sorted(self.__dict__.keys())))})'


if __name__ == "__main__":
    vector = Vector(p=1, q=5)
    print(vector)
    del vector._p
