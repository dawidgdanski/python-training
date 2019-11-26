import code
import struct
from binascii import hexlify
from pprint import pprint

from binary.colorprints import Vertex, Vector, Color


def _make_colored_vertex(x, y, z, red, green, blue):
    return Vertex(Vector(x, y, z), Color(red, green, blue))


def main():
    with open('colors.bin', 'rb') as f:
        buffer = f.read()

    print(f'buffer: {len(buffer)} bytes')

    indexes = ' '.join(str(n).zfill(2) for n in range(len(buffer)))
    print(f'indexes: {indexes}')

    hex_buffer = hexlify(buffer).decode('ascii')
    hex_pairs = ' '.join(hex_buffer[i:i + 2] for i in range(0, len(hex_buffer), 2))
    print(f'hex pairs: {hex_pairs}')

    vertices = [_make_colored_vertex(*fields) for fields in struct.iter_unpack('@3f3Hxx', buffer)]
    pprint(vertices)


if __name__ == '__main__':
    main()
