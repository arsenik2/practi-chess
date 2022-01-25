class Piece:

    def __init__(self, name, short, color):
        self.name = name
        self.short = short
        self.color = color

    def get_color(self):
        return ["W", "B"][self.color]
