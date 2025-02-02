from vector import Vector


class Color(Vector):
    @classmethod
    def from_hex(cls, hexcolor="#FFFFFF"):
        if hexcolor[0] != "#":
            raise ValueError("Hex color must start with #")
        elif len(hexcolor) != 7:
            raise ValueError("Hex color must be 7 characters long")
        elif not all([c in "0123456789ABCDEF" for c in hexcolor[1:]]):
            raise ValueError("Hex color must be in the format #RRGGBB")
        x = int(hexcolor[1:3], 16) / 255.0
        y = int(hexcolor[3:5], 16) / 255.0
        z = int(hexcolor[5:7], 16) / 255.0
        return cls(x, y, z)
