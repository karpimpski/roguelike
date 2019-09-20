import tcod
import map_classes.settings as map_settings


class FOV:
    """Class in charge of computing FOV."""

    def __init__(self, game_map):
        self.algorithm = 0
        self.light_walls = True
        self.radius = 10
        self.recompute = True
        self.game_map = game_map
        self.map = self.initialize_map()

    def initialize_map(self):
        """Creates TCOD map with data from the game map."""
        fov_map = tcod.map.Map(map_settings.MAP_WIDTH, map_settings.MAP_HEIGHT)
        for y in range(map_settings.MAP_HEIGHT):
            for x in range(map_settings.MAP_WIDTH):
                tcod.map_set_properties(
                    fov_map,
                    x,
                    y,
                    not self.game_map.tiles[x][y].block_sight,
                    not self.game_map.tiles[x][y].blocked,
                )
        return fov_map

    def compute(self, x, y):
        """Recompute TCOD map's FOV."""
        tcod.map_compute_fov(self.map, x, y, self.radius, self.light_walls, 0)
