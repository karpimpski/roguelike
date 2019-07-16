import tcod
from fov import FOV
from map_classes.map_constants import *


class Renderer:
    def __init__(self, console, game_map):
        self.console = console
        self.game_map = game_map
        self.fov = FOV(game_map)

    def render_all(self, entities, screen_width, screen_height, x, y):
        """Recomputes FOV and draws all tiles/entities."""
        self.fov.compute(x, y)
        self.draw_tiles(self.fov)
        self.draw_entities(entities, self.fov)
        tcod.console_blit(self.console, 0, 0, screen_width, screen_height, 0, 0, 0)
        tcod.console_flush()

    def draw_tiles(self, fov):
        """Draws all tiles in list."""
        for y in range(MAP_HEIGHT):
            for x in range(MAP_WIDTH):
                if tcod.map_is_in_fov(fov.map, x, y):
                    self.draw_light_tile(
                        self.console, x, y, self.game_map.tiles[x][y].img
                    )
                    self.game_map.tiles[x][y].explored = True
                elif self.game_map.tiles[x][y].explored:
                    self.draw_dark_tile(
                        self.console, x, y, self.game_map.tiles[x][y].img
                    )

    def draw_entities(self, entities, fov):
        """Draws all entities in list."""
        for entity in entities:
            self.draw_entity(self.console, entity, fov)

    def draw_entity(self, con, entity, fov):
        """Draws a single entity."""
        if tcod.map_is_in_fov(fov.map, entity.x, entity.y):
            tcod.console_put_char(con, entity.x, entity.y, entity.tile, tcod.BKGND_NONE)

    def draw_light_tile(self, con, x, y, tile):
        """Draws tile with a light tint."""
        tcod.console_put_char_ex(con, x, y, tile, tcod.white, tcod.black)

    def draw_dark_tile(self, con, x, y, tile):
        """Draws tile with a dark tint."""
        tcod.console_put_char_ex(con, x, y, tile, tcod.grey, tcod.black)
