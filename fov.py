import tcod
from map_classes.map_constants import *


class FOV:
    def __init__(self, game_map):
        self.algorithm = 0
        self.light_walls = True
        self.radius = 10
        self.recompute = True
        self.game_map = game_map
        self.map = self.initialize_map()

    def initialize_map(self):
        fov_map = tcod.map.Map(MAP_WIDTH, MAP_HEIGHT)
        for y in range(MAP_HEIGHT):
            for x in range(MAP_WIDTH):
                tcod.map_set_properties(
                    fov_map,
                    x,
                    y,
                    not self.game_map.tiles[x][y].block_sight,
                    not self.game_map.tiles[x][y].blocked,
                )
        return fov_map

    def compute(self, x, y):
        tcod.map_compute_fov(self.map, x, y, self.radius, self.light_walls, 0)

