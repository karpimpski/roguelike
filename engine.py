import tcod
import tcod.event
import input_handler
import renderer
import imgs

from entity import Entity
from map_classes.game_map import GameMap

# Constants.
screen_width = 80
screen_height = 50

class Game:
    def __init__(self):
        self.screen_width = 80
        self.screen_height = 50
        self.console = self.create_console()
        self.game_map = GameMap()
        self.entities = self.create_entities()
        self.player = self.entities[0]
        self.game_loop()
    
    # Creates and initializes the console.
    def create_console(self):
        tcod.console_set_custom_font('sprites.png', tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD, 32, 10)
        console = tcod.console_init_root(screen_width, screen_height, 'Roguelike', False)
        self.map_ascii_codes()
        return console
    
    # Maps ASCII codes to font, allowing the game to use sprites stored in sprites.png.
    def map_ascii_codes(self):
        a = 256
        for y in range(5,6):
            tcod.console_map_ascii_codes_to_font(a, 32, 0, y)
            a += 32
        
    # Creates and returns all entities in game (PLAYER MUST BE FIRST ENTITY - TEMP).
    def create_entities(self):
        (player_x, player_y) = self.game_map.rooms[0].center()
        player = Entity(player_x, player_y, imgs.player)
        return [player]
    
    # Renders the game map and entities, checks for input, then performs an action based on input. Loops while window is open.
    def game_loop(self):
        while not tcod.console_is_window_closed():
            renderer.render_all(self.console, self.entities, self.game_map, self.screen_width, self.screen_height)
            action = self.check_for_input()
            if action is not None:
                self.perform(action)
    
    # Checks for input and returns an object containing instructions (e.g. { 'move': (0, 1) } or { 'exit': True }).
    def check_for_input(self):
        key = tcod.Key()
        mouse = tcod.Mouse()
        tcod.sys_check_for_event(tcod.EVENT_KEY_PRESS, key, mouse)
        return input_handler.handle_keys(key)
    
    # Interperets and performs an action.
    def perform(self, action):
        if action.get('move'):
            dx, dy = action.get('move')
            if not self.game_map.is_blocked(self.player.x + dx, self.player.y + dy):
                self.player.move(dx, dy)
        if action.get('exit'):
            raise SystemExit()
        if action.get('fullscreen'):
            print('I am learning how to go full-screen without crashing the desktop!')


if __name__ == '__main__':
    game = Game()