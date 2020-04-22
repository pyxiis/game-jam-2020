import arcade

from ...assets.sprites import ROGUE, ANTIROGUE, WARRIOR, ANTIWARRIOR, WIZARD, ANTIWIZARD

STATES = [ROGUE, WARRIOR, WIZARD]
ANTISTATES = [ANTIROGUE, ANTIWARRIOR, ANTIWIZARD]

LEFT = (arcade.key.A, arcade.key.J, arcade.key.LEFT)
RIGHT = (arcade.key.D, arcade.key.L, arcade.key.RIGHT)
UP = (arcade.key.W, arcade.key.I, arcade.key.UP)
DOWN = (arcade.key.S, arcade.key.K, arcade.key.DOWN)


class Player(arcade.Sprite):
    def __init__(self, km):
        super().__init__(scale=1)
        self.key_manager = km
        self.hp0 = 20  # rogue hp
        self.hp1 = 50  # warrior hp
        self.hp2 = 10  # wizard hp
        self.points = [(-6, 16), (6, 16), (6, 14), (-6, 14)]
        self.moving_x = False
        self.moving_y = False
        self.attacking = False
        self.texture = ROGUE[0]
        self.frame = 0
        self.time = 0
        self.state = 0  # 0 is rogue, 1 is warrior, 2 is wizard
        self.shifting = False
        self.shift_from = 0  # hacky variable with various purposes
        print('player made!')

    def update(self):
        self.change_x = 0
        self.change_y = 0
        self.time += 1
        if self.time == 10:
            self.time = 0
        if self.attacking:
            self.change_x = 0
            self.change_y = 0
            self.moving_x = False
            self.moving_y = False
        else:
            if arcade.key.LSHIFT in self.key_manager.keys and not self.shifting:
                self.state -= 1
                self.state %= 3
                self.shifting = True
                self.shift_from = 1
            elif arcade.key.RSHIFT in self.key_manager.keys and not self.shifting:
                self.state += 1
                self.state %= 3
                self.shifting = True
                self.shift_from = -1
            elif not self.shifting:
                if arcade.key.LEFT in self.key_manager.keys:
                    self.moving_x = True
                    self.change_x = -1
                elif arcade.key.RIGHT in self.key_manager.keys:
                    self.moving_x = True
                    self.change_x = 1
                else:
                    self.moving_x = False
                    self.change_x = 0
                if arcade.key.UP in self.key_manager.keys:
                    self.moving_y = True
                    self.change_y = 1
                elif arcade.key.DOWN in self.key_manager.keys:
                    self.moving_y = True
                    self.change_y = -1
                else:
                    self.moving_y = False
                    self.change_y = 0

        if self.shifting:
            if self.frame >= 50 or self.frame < 40:
                self.frame = 40
            if self.frame == 49:
                self.shift_from = 0
            self.texture = STATES[(self.state + self.shift_from) % 3][self.frame]
            if self.time == 0:
                if self.shift_from == 0:
                    if self.frame == 40:
                        self.shifting = False
                    self.frame -= 1
                else:
                    self.frame += 1
        else:
            if not self.moving_x and not self.moving_y:
                if self.frame >= 10:
                    self.frame = 0
                self.texture = STATES[self.state][self.frame]
                if self.time == 0:
                    self.frame += 1

            else:
                if self.frame >= 30 or self.frame < 20:
                    self.frame = 20
                if self.change_x < 0:
                    self.texture = ANTISTATES[self.state][self.frame]
                else:
                    self.texture = STATES[self.state][self.frame]
                if self.time == 0:
                    self.frame += 1
