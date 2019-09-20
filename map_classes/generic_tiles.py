"""Selection of common tiles."""

from map_classes.tile import Tile
import imgs


class Wall(Tile):
    """Wall that blocks movement and vision."""

    def __init__(self):
        Tile.__init__(self, imgs.WALL, True)


class Floor(Tile):
    """Stone floor."""

    def __init__(self):
        Tile.__init__(self, imgs.FLOOR, False)
