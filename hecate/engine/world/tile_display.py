import arcade

from .binary_space_partitioning import RLDungeonGenerator
from .floor import Floor
from .wall import Ceiling

WALL_SPRITE_SCALING = 1
WALL_SPRITE_SIZE = 16 * WALL_SPRITE_SCALING


class Dungeon():
    def __init__(self, width, height, cutoff):
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)
        self.facade_list = arcade.SpriteList(use_spatial_hash=True)
        self.floor_list = arcade.SpriteList(use_spatial_hash=True)
        self.decor_list = arcade.SpriteList(use_spatial_hash=True)
        self.ceiling_list = arcade.SpriteList(use_spatial_hash=True)
        self.layout = RLDungeonGenerator(width, height, cutoff)
        self.add_context()
        self._fill_lists()

    def add_context(self):
        for r in range(self.layout.height):
            for c in range(self.layout.width):
                self.layout.dungeon[r][c] = [self.layout.dungeon[r][c], 0]
        for r in range(self.layout.height):
            for c in range(self.layout.width):

                '''Use bitwise operators to determine where there are walls
                    8  4  2
                     \ | /
                16 --- x --- 1
                     / | \
                   32  64 128
                '''

                # I'm a noob but there has to be some better way to do this
                try:
                    if '#' in self.layout.dungeon[r][c - 1]:
                        self.layout.dungeon[r][c][1] += 16
                except Exception:
                    self.layout.dungeon[r][c][1] += 16
                try:
                    if '#' in self.layout.dungeon[r][c + 1]:
                        self.layout.dungeon[r][c][1] += 1
                except Exception:
                    self.layout.dungeon[r][c][1] += 1
                try:
                    if '#' in self.layout.dungeon[r - 1][c]:
                        self.layout.dungeon[r][c][1] += 4
                except Exception:
                    self.layout.dungeon[r][c][1] += 4
                try:
                    if '#' in self.layout.dungeon[r + 1][c]:
                        self.layout.dungeon[r][c][1] += 64
                except Exception:
                    self.layout.dungeon[r][c][1] += 64
                try:
                    if '#' in self.layout.dungeon[r + 1][c - 1]:
                        self.layout.dungeon[r][c][1] += 32
                except Exception:
                    self.layout.dungeon[r][c][1] += 32
                try:
                    if '#' in self.layout.dungeon[r - 1][c - 1]:
                        self.layout.dungeon[r][c][1] += 8
                except Exception:
                    self.layout.dungeon[r][c][1] += 8
                try:
                    if '#' in self.layout.dungeon[r + 1][c + 1]:
                        self.layout.dungeon[r][c][1] += 128
                except Exception:
                    self.layout.dungeon[r][c][1] += 128
                try:
                    if '#' in self.layout.dungeon[r - 1][c + 1]:
                        self.layout.dungeon[r][c][1] += 2
                except Exception:
                    self.layout.dungeon[r][c][1] += 2

    def _fill_lists(self):
        for r in range(self.layout.height):
            for c in range(self.layout.width):
                value = self.layout.dungeon[r][c]
                if value[0] == '#':
                    wall = Ceiling(value[1])
                    wall.center_x = c * WALL_SPRITE_SIZE + WALL_SPRITE_SIZE / 2
                    wall.center_y = r * WALL_SPRITE_SIZE + WALL_SPRITE_SIZE / 2
                    self.ceiling_list.append(wall)
                else:
                    floor = Floor(value[1])
                    floor.center_x = c * WALL_SPRITE_SIZE + WALL_SPRITE_SIZE / 2
                    floor.center_y = r * WALL_SPRITE_SIZE + WALL_SPRITE_SIZE / 2
                    self.floor_list.append(floor)
