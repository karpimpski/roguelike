from random import randint

from map_classes.tile import Tile
from map_classes.room import Room
from map_classes.generic_tiles import Wall, Floor
from map_classes.map_constants import *
import imgs


class GameMap:
    def __init__(self):
        self.tiles = self.initialize_tiles()
        self.rooms = []
        self.create_map()

    # MAP CREATION METHODS.

    # Initializes all tiles as walls.
    def initialize_tiles(self):
        return [[Wall() for y in range(MAP_HEIGHT)] for x in range(MAP_WIDTH)]

    # Generates and connect a limited number of rooms to create a random dungeon.
    def create_map(self):
        for _ in range(MAX_ROOMS):
            new_room = self.create_room()
            if self.valid_room(new_room):
                self.draw_room(new_room)
                if len(self.rooms) > 0:
                    self.connect_rooms(self.rooms[len(self.rooms) - 1], new_room)
                self.rooms.append(new_room)

    # Creates a room with a random size and location.
    def create_room(self):
        w = randint(MIN_ROOM_SIZE, MAX_ROOM_SIZE)
        h = randint(MIN_ROOM_SIZE, MAX_ROOM_SIZE)
        return Room(randint(0, MAP_WIDTH - w - 1), randint(0, MAP_HEIGHT - h - 1), w, h)

    # Checks whether a potential room would intersect any existing rooms.
    def valid_room(self, room):
        for other_room in self.rooms:
            if room.intersect(other_room):
                return False
        return True

    # Creates tunnels between two given rooms.
    def connect_rooms(self, room1, room2):
        (x1, y1) = room1.center()
        (x2, y2) = room2.center()
        if randint(0, 1) == 1:
            self.draw_h_tunnel(x1, x2, y1)
            self.draw_v_tunnel(y1, y2, x2)
        else:
            self.draw_v_tunnel(y1, y2, x1)
            self.draw_h_tunnel(x1, x2, y2)

    # Draws floor tiles in a horizontal line.
    def draw_h_tunnel(self, x1, x2, y):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            self.tiles[x][y] = Floor()

    # Draws floor tiles in a vertical line.
    def draw_v_tunnel(self, y1, y2, x):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            self.tiles[x][y] = Floor()

    # Draws a room.
    def draw_room(self, room):
        for x in range(room.x1 + 1, room.x2):
            for y in range(room.y1 + 1, room.y2):
                self.tiles[x][y] = Floor()

    # GAME LOGIC METHODS.

    # Checks whether a tile blocks movement.
    def is_blocked(self, x, y):
        if self.tiles[x][y].blocked:
            return True
        return False
