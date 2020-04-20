import arcade

from ...assets.sprites import ROGUE


class Player(arcade.Sprite):
    def __init__(self):
        super().__init__(scale=1)
        self.hp0 = 20  # rogue hp
        self.hp1 = 50  # warrior hp
        self.hp2 = 10  # wizard hp
        self.texture = ROGUE[10]
        print('player made!')
