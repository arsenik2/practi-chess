class Square:

    def __init__(self, x_coord, y_coord):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.color = (ord(x_coord) + y_coord) % 2 == 1
        self.piece = None

    def get_color(self):
        return ["X", " "][self.color]

    def __repr__(self):
        if self.piece and self.piece.short:
            return f"{self.piece.short}{self.x_coord}{self.y_coord}"
        return f"{self.x_coord}{self.y_coord}"
