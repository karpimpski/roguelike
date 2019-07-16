class Tile:
    def __init__(self, img, blocked, block_sight=None):
        self.img = img
        self.blocked = blocked
        if block_sight is None:
            block_sight = blocked
        self.block_sight = block_sight
