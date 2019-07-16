class Entity:
    def __init__(self, x, y, tile):
        self.x = x
        self.y = y
        self.tile = tile

    def move(self, x, y):
        self.x += x
        self.y += y
