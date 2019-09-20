"""Tile class."""


class Tile:
    """Tile class. Contains image code as well as sight-blocking and explored flags."""

    def __init__(self, img, blocked, block_sight=None):
        self.img = img
        self.blocked = blocked
        if block_sight is None:
            block_sight = blocked
        self.block_sight = block_sight
        self.explored = False
