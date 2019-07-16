import tcod
from map_classes.map_constants import *

# Draws tiles, entities, then blits the console.
def render_all(con, entities, game_map, screen_width, screen_height, fov):
    if fov.recompute:
        draw_tiles(con, game_map, fov)
    draw_entities(con, entities, fov)
    tcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)
    tcod.console_flush()
    fov.recompute = False


# Draws all tiles.
def draw_tiles(con, game_map, fov):
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            if tcod.map_is_in_fov(fov.map, x, y):
                draw_light_tile(con, x, y, game_map.tiles[x][y].img)
                game_map.tiles[x][y].explored = True
            elif game_map.tiles[x][y].explored:
                draw_dark_tile(con, x, y, game_map.tiles[x][y].img)


# Draws all entities.
def draw_entities(con, entities, fov):
    for entity in entities:
        draw_entity(con, entity, fov)


# Draws a single entity.
def draw_entity(con, entity, fov):
    if tcod.map_is_in_fov(fov.map, entity.x, entity.y):
        tcod.console_put_char(con, entity.x, entity.y, entity.tile, tcod.BKGND_NONE)


# Draws tile with a light tint.
def draw_light_tile(con, x, y, tile):
    tcod.console_put_char_ex(con, x, y, tile, tcod.white, tcod.black)


# Draws tile with a dark tint.
def draw_dark_tile(con, x, y, tile):
    tcod.console_put_char_ex(con, x, y, tile, tcod.grey, tcod.black)
