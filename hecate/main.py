import os
import time
import timeit

import arcade
import yaml
from pyglet.gl import GL_NEAREST

from hecate.engine.input import KeyManager
from hecate.engine.world.tile_display import Dungeon

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

SETTINGS = yaml.load(open('settings.yaml', 'r'), Loader=Loader)
WALL_SPRITE_SCALING = SETTINGS['scaling']['tile']
WALL_SPRITE_SIZE = 128 * WALL_SPRITE_SCALING
GRID_WIDTH = SETTINGS['world']['bin']['width']
GRID_HEIGHT = SETTINGS['world']['bin']['height']
AREA_WIDTH = GRID_WIDTH * WALL_SPRITE_SIZE
AREA_HEIGHT = GRID_HEIGHT * WALL_SPRITE_SIZE
MUSIC_VOLUME = 0.5


class Hecate(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        self.grid = None
        self.wall_list = None
        self.player_list = None
        self.floor_list = None
        self.floor_decor = None
        self.facade_list = None
        self.wall_decor = None
        self.player_sprite = None
        self.view_bottom = 0
        self.view_left = 0
        self.physics_engine = None

        self.music_list = []
        self.current_song = 0
        self.music = None

        self.processing_time = 0
        self.draw_time = 0
        self.km = KeyManager()
        self.dungeon = Dungeon(GRID_WIDTH, GRID_HEIGHT, 15, self.km)
        arcade.set_background_color(arcade.color.BLACK)

        self.current_vista = 192


    def setup(self):
        """ Set up the game """
        self.player_list = self.dungeon.player_list
        self.player_sprite = self.player_list[0]
        print('list made')
        self.wall_list = self.dungeon.ceiling_list
        self.floor_list = self.dungeon.floor_list
        self.facade_list = self.dungeon.facade_list
        self.wall_decor = self.dungeon.wall_decor_list
        self.floor_decor = self.dungeon.decor_list
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                         self.wall_list)

        # List of music
        self.music_list = ['assets/background.mp3']
        # Array index of what to play
        self.current_song = 0
        # Play the song
        self.play_song()

        # Set up the player
        # self.player_sprite = Player()
        # self.player_sprite.center_x = 6400
        # self.player_sprite.center_y = 3200
        # print(ROGUE[0])
        #
        # placed = False
        # while not placed:
        #     # Randomly position
        #     # Are we in a wall?
        #     walls_hit = arcade.check_for_collision_with_list(self.player_sprite,
        #                                                      self.wall_list)
        #     if len(walls_hit) == 0:
        #         print(self.player_sprite.center_x)
        #         print(AREA_WIDTH)
        #         print(self.player_sprite.center_y)
        #         print(AREA_HEIGHT)
        #         #     # Not in a wall! Success!
        #         placed = True

        # self.player_list = self.dungeon.player_list

        # Randomly place the player. If we are in a wall, repeat until we aren't.

        # self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
        #                                                  self.wall_list)

        self.set_fullscreen(not self.fullscreen)
        width, height = self.get_size()
        self.set_fullscreen(not self.fullscreen)
        self.set_size(width, height)

    def on_draw(self):
        """ Render the screen. """

        # Start timing how long this takes
        draw_start_time = timeit.default_timer()

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        # Draw the sprites
        self.floor_list.draw(filter=GL_NEAREST)
        self.facade_list.draw(filter=GL_NEAREST)
        self.wall_decor.draw(filter=GL_NEAREST)
        self.floor_decor.draw(filter=GL_NEAREST)
        self.player_list.draw(filter=GL_NEAREST)
        self.wall_list.draw(filter=GL_NEAREST)

    def update(self, delta_time):
        # for key in self.km.keys:
        #     if str(key) == 'LEFT':

        # pass
        self.player_sprite.update()
        self.physics_engine.update()
        position = self.music.get_stream_position()

        # The position pointer is reset to 0 right after we finish the song.
        # This makes it very difficult to figure out if we just started playing
        # or if we are doing playing.
        if position == 0.0:
            self.advance_song()
            self.play_song()

        arcade.set_viewport(self.player_sprite.center_x - self.current_vista,
                            self.player_sprite.center_x + self.current_vista,
                            self.player_sprite.center_y - self.current_vista * 108 / 192,
                            self.player_sprite.center_y + self.current_vista * 108 / 192)

    def on_key_press(self, key, modifiers):
        self.km.update_press(key, modifiers)

    def on_key_release(self, key, modifiers):
        self.km.update_release(key, modifiers)

    def advance_song(self):
        """ Advance our pointer to the next song. This does NOT start the song. """
        self.current_song += 1
        if self.current_song >= len(self.music_list):
            self.current_song = 0

    def play_song(self):
        """ Play the song. """
        # Stop what is currently playing.
        if self.music:
            self.music.stop()

        # Play the next song
        print(f"Playing {self.music_list[self.current_song]}")
        self.music = arcade.Sound(self.music_list[self.current_song], streaming=True)
        self.music.play(MUSIC_VOLUME)
        # This is a quick delay. If we don't do this, our elapsed time is 0.0
        # and on_update will think the music is over and advance us to the next
        # song before starting this one.
        time.sleep(0.03)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        self.km.update_mouse_press(x, y, button, modifiers)

    def on_mouse_release(self, x: float, y: float, button: int,
                         modifiers: int):
        self.km.update_mouse_release(x, y, button, modifiers)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.km.update_mouse(x, y)

    def on_mouse_scroll(self, x: int, y: int, scroll_x: int, scroll_y: int):
        # not managed by keymanager because scrolling relies on deltas rather than absolute data
        if scroll_y > 0:
            self.current_vista += (scroll_x ** 2 + scroll_y ** 2) ** 0.5
            if self.current_vista > 192:
                self.current_vista = 192
        elif scroll_y < 0:
            self.current_vista -= (scroll_x ** 2 + scroll_y ** 2) ** 0.5
            if self.current_vista < 19.2:
                self.current_vista = 19.2


def main():
    game = Hecate(SETTINGS['window']['width'], SETTINGS['window']['height'], 'Hecate')
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
