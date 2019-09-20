"""Game Map class."""

from random import randint

from map_classes.room import Room
from map_classes.generic_tiles import Wall, Floor
import map_classes.settings as map_settings


class GameMap:
    """Represents the game map; includes map creation and logic methods."""

    def __init__(self):
        self.width = map_settings.MAP_WIDTH
        self.height = map_settings.MAP_HEIGHT
        self.tiles = self.initialize_tiles()
        self.rooms = []
        self.create_map()

    # MAP CREATION METHODS.
    def initialize_tiles(self):
        """Initializes all tiles as walls."""
        return [[Wall() for y in range(self.height)] for x in range(self.width)]

    def create_map(self):
        """Initializes all tiles as walls."""
        for _ in range(map_settings.MAX_ROOMS):
            new_room = self.create_room()
            if self.valid_room(new_room):
                self.draw_room(new_room)
                if len(self.rooms) > 0:
                    self.connect_rooms(
                        self.rooms[len(self.rooms) - 1], new_room)
                self.rooms.append(new_room)

    def create_room(self):
        """Creates a room with a random size and location."""
        w = randint(map_settings.MIN_ROOM_SIZE, map_settings.MAX_ROOM_SIZE)
        h = randint(map_settings.MIN_ROOM_SIZE, map_settings.MAX_ROOM_SIZE)
        return Room(randint(0, self.width - w - 1), randint(0, self.height - h - 1), w, h)

    def valid_room(self, room):
        """Checks whether a potential room would intersect any existing rooms."""
        for other_room in self.rooms:
            if room.intersect(other_room):
                return False
        return True

    def connect_rooms(self, room1, room2):
        """Creates tunnels between two given rooms."""
        (x1, y1) = room1.center()
        (x2, y2) = room2.center()
        if randint(0, 1) == 1:
            self.draw_h_tunnel(x1, x2, y1)
            self.draw_v_tunnel(y1, y2, x2)
        else:
            self.draw_v_tunnel(y1, y2, x1)
            self.draw_h_tunnel(x1, x2, y2)

    def draw_h_tunnel(self, x1, x2, y):
        """Draws floor tiles in a horizontal line."""
        for x in range(min(x1, x2), max(x1, x2) + 1):
            self.tiles[x][y] = Floor()

    def draw_v_tunnel(self, y1, y2, x):
        """Draws floor tiles in a vertical line."""
        for y in range(min(y1, y2), max(y1, y2) + 1):
            self.tiles[x][y] = Floor()

    def draw_room(self, room):
        """Draws a room."""
        for x in range(room.x1 + 1, room.x2):
            for y in range(room.y1 + 1, room.y2):
                self.tiles[x][y] = Floor()

    # GAME LOGIC METHODS.
    def is_blocked(self, x, y):
        """Checks whether a tile blocks movement."""
        if self.tiles[x][y].blocked:
            return True
        return False
