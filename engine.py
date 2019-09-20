"""Starts application and contains the Game class."""

import tcod
import tcod.event

import settings
import input_handler
import imgs
from entity import Entity
from renderer import Renderer
from map_classes.game_map import GameMap


class Game:
    def __init__(self):
        """Initializes game variables then begins game loop."""
        self.game_map = GameMap()
        self.console = self.create_console()
        self.entities = self.create_entities()
        self.player = self.entities[0]
        self.renderer = Renderer(self.console, self.game_map)
        self.game_loop()

    def create_console(self):
        """Creates and initializes the console, including font mapping."""
        tcod.console_set_custom_font(
            "sprites.png", tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD, 32, 10
        )
        console = tcod.console_init_root(
            settings.SCREEN_WIDTH,
            settings.SCREEN_HEIGHT,
            "Roguelike",
            False,
            tcod.RENDERER_OPENGL2,
            "F",
            True,
        )
        self.map_ascii_codes()
        return console

    def map_ascii_codes(self):
        """Maps ASCII codes to font, allowing the game to use sprites stored in sprites.png."""
        a = 256
        for y in range(5, 6):
            tcod.console_map_ascii_codes_to_font(a, 32, 0, y)
            a += 32

    def create_entities(self):
        """Creates and returns all entities in game (PLAYER MUST BE FIRST ENTITY - TEMP)."""
        (player_x, player_y) = self.game_map.rooms[0].center()
        player = Entity(player_x, player_y, imgs.PLAYER)
        orc = Entity(player_x + 2, player_y + 2, imgs.ORC)
        return [player, orc]

    def game_loop(self):
        """Renders game, checks for input, then performs an action based on input while running."""
        while True:
            self.renderer.render_all(
                self.entities, settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT,
                self.player.x, self.player.y
            )
            action = self.check_for_input()
            if action is not None:
                self.perform(action)

    def check_for_input(self):
        """Checks for window events and passes key events to input handler."""
        for event in tcod.event.get():
            if event.type == "QUIT":
                raise SystemExit
            if event.type == "KEYDOWN":
                return input_handler.handle_keys(event.sym)

    def perform(self, action):
        """Interperets and performs an action."""
        if action.get("move"):
            dx, dy = action.get("move")
            if not self.game_map.is_blocked(self.player.x + dx, self.player.y + dy):
                self.player.move(dx, dy)
        if action.get("exit"):
            raise SystemExit()
        if action.get("fullscreen"):
            print("I am learning how to go full-screen without crashing the desktop!")


if __name__ == "__main__":
    Game()
