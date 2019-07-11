from map_classes.tile import Tile
import imgs

class Wall(Tile):
    def __init__(self):
        Tile.__init__(self, imgs.wall, True)

class Floor(Tile):
    def __init__(self):
        Tile.__init__(self, imgs.floor, False)