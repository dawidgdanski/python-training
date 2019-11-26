class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self) -> str:
        return f'Vector({self.x}, {self.y}, {self.z})'


class Color:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def __repr__(self) -> str:
        return f'Color({self.red}, {self.green}, {self.blue})'


class Vertex:
    def __init__(self, vector, color):
        self.vector = vector
        self.color = color

    def __repr__(self) -> str:
        return f'Vertex({self.vector}, {self.color})'
