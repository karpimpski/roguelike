import tcod
from map_classes.map_constants import *

def render_all(con, entities, game_map, screen_width, screen_height):
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            draw_light_tile(con, x, y, game_map.tiles[x][y].img)

    for entity in entities:
        draw_entity(con, entity)
    tcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)
    clear_all(con, entities)

def clear_all(con, entities):
    for entity in entities:
        clear_entity(con, entity)

def draw_entity(con, entity):
    tcod.console_put_char(con, entity.x, entity.y, entity.tile, tcod.BKGND_NONE)

def clear_entity(con, entity):
    tcod.console_flush()

def draw_light_tile(con, x, y, tile):
    tcod.console_put_char_ex(con, x, y, tile, tcod.white, tcod.black)

def draw_dark_tile(con, x, y, tile):
    tcod.console_put_char_ex(con, x, y, tile, tcod.grey, tcod.black)