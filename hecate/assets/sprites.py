import time

import PIL
import arcade

CEILING = arcade.load_spritesheet('./assets/ceiling.png', 16, 16, 30, 57)
WALL = arcade.load_spritesheet('./assets/wall.png', 16, 32, 9, 9)
FLOOR = arcade.load_spritesheet('./assets/floor.png', 16, 16, 30, 72)
WALL_DECO = arcade.load_spritesheet('./assets/walldeco.png', 16, 32, 12, 12)
ALTAR = arcade.load_spritesheet('./assets/altar.png', 16, 32, 4, 4)
FLOOR_DECO = arcade.load_spritesheet('./assets/floordeco.png', 16, 16, 3, 3)

ROGUE = arcade.load_spritesheet('./assets/rogue.png', 32, 32, 10, 100)
ANTIROGUE = [arcade.Texture(f'antirogue{time.time()}', PIL.ImageOps.mirror(texture.image)) for
             texture in ROGUE]
WARRIOR = arcade.load_spritesheet('./assets/warrior.png', 32, 32, 10, 100)
ANTIWARRIOR = [arcade.Texture(f'antiwarrior{time.time()}', PIL.ImageOps.mirror(texture.image)) for
               texture in WARRIOR]
WIZARD = arcade.load_spritesheet('./assets/wizard.png', 32, 32, 10, 100)
ANTIWIZARD = [arcade.Texture(f'antiwizard{time.time()}', PIL.ImageOps.mirror(texture.image)) for
              texture in WIZARD]
