"""Entity class."""


class Entity:
    """Generic entity class containing location, tile code, and move method."""

    def __init__(self, x, y, tile):
        self.x = x
        self.y = y
        self.tile = tile

    def move(self, x, y):
        """Adjusts location."""
        self.x += x
        self.y += y
