import os
import random
import timeit

import arcade
import yaml
from pyglet.gl import GL_NEAREST

from hecate.engine.input import KeyManager
from hecate.engine.world.binary_space_partitioning import RLDungeonGenerator
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

        self.processing_time = 0
        self.draw_time = 0

        self.dungeon = Dungeon(GRID_WIDTH, GRID_HEIGHT, 15)
        arcade.set_background_color(arcade.color.BLACK)
        self.km = KeyManager()

    def setup(self):
        """ Set up the game """
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)
        self.player_list = arcade.SpriteList()

        # Create cave system using a 2D grid
        dg = RLDungeonGenerator(GRID_WIDTH, GRID_HEIGHT, 15)
        dg.generate_map()
        # Create sprites based on 2D grid

        # for row in range(dg.height):
        #     for column in range(dg.width):
        #         value = dg.dungeon[row][column]
        #         if value == '#':
        #             wall = arcade.Sprite(":resources:images/tiles/grassCenter.png",
        #                                  WALL_SPRITE_SCALING)
        #             wall.center_x = column * WALL_SPRITE_SIZE + WALL_SPRITE_SIZE / 2
        #             wall.center_y = row * WALL_SPRITE_SIZE + WALL_SPRITE_SIZE / 2
        #             self.wall_list.append(wall)
        self.wall_list = self.dungeon.ceiling_list
        self.floor_list = self.dungeon.floor_list
        self.facade_list = self.dungeon.facade_list
        self.wall_decor = self.dungeon.wall_decor_list
        self.floor_decor = self.dungeon.decor_list
        # for wall in self.wall_list:
        # wall.center_x = column * WALL_SPRITE_SIZE + WALL_SPRITE_SIZE / 2
        # wall.center_y = row * WALL_SPRITE_SIZE + WALL_SPRITE_SIZE / 2

        # Set up the player
        self.player_sprite = arcade.Sprite(
            "/Users/ethanji/PycharmProjects/hecate/venv/hecate/hecate/assets/rogue.png",
            0.25)
        self.player_list.append(self.player_sprite)

        # Randomly place the player. If we are in a wall, repeat until we aren't.
        placed = False
        while not placed:
            # Randomly position
            self.player_sprite.center_x = random.randrange(AREA_WIDTH)
            self.player_sprite.center_y = random.randrange(AREA_HEIGHT)

            # Are we in a wall?
            # walls_hit = arcade.check_for_collision_with_list(self.player_sprite,
            #                                                  self.wall_list)
            # if len(walls_hit) == 0:
            #     # Not in a wall! Success!
            placed = True

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                         self.wall_list)

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
        self.wall_list.draw(filter=GL_NEAREST)
        self.player_list.draw(filter=GL_NEAREST)

        # Draw info on the screen
        sprite_count = len(self.wall_list)

        self.draw_time = timeit.default_timer() - draw_start_time

    def update(self, delta_time):
        pass

    def on_key_press(self, key, modifiers):
        self.km.update_press(key, modifiers)


    def on_key_release(self, key, modifiers):
        self.km.update_release(key, modifiers)


def main():
    game = Hecate(SETTINGS['window']['width'], SETTINGS['window']['height'], 'Hecate')
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
