import random

import arcade

from ...assets.sprites import FLOOR, ALTAR, FLOOR_DECO


class Floor(arcade.Sprite):
    def __init__(self, direction):
        super().__init__(scale=1)

        # For readability
        self.wall_directions = []
        if 1 & direction == 1:
            self.wall_directions.append('e')
        if 2 & direction == 2:
            self.wall_directions.append('se')
        if 4 & direction == 4:
            self.wall_directions.append('s')
        if 8 & direction == 8:
            self.wall_directions.append('sw')
        if 16 & direction == 16:
            self.wall_directions.append('w')
        if 32 & direction == 32:
            self.wall_directions.append('nw')
        if 64 & direction == 64:
            self.wall_directions.append('n')
        if 128 & direction == 128:
            self.wall_directions.append('ne')

        if 'e' in self.wall_directions and 'w' in self.wall_directions:
            self.texture = random.choice(FLOOR[23:25])
        elif 'n' in self.wall_directions and 's' in self.wall_directions:
            self.texture = random.choice(FLOOR[21:23])
        elif 'n' in self.wall_directions and 'w' in self.wall_directions:
            self.texture = random.choice([FLOOR[1], FLOOR[60]])
        elif 's' in self.wall_directions and 'w' in self.wall_directions:
            self.texture = random.choice([FLOOR[3], FLOOR[58]])
        elif 's' in self.wall_directions and 'e' in self.wall_directions:
            self.texture = random.choice([FLOOR[4], FLOOR[57]])
        elif 'n' in self.wall_directions and 'e' in self.wall_directions:
            self.texture = random.choice([FLOOR[2], FLOOR[59]])

        else:
            if len(self.wall_directions) == 3:
                if 'n' in self.wall_directions:
                    self.texture = random.choice(FLOOR[8:11])
                elif 'w' in self.wall_directions:
                    self.texture = random.choice(FLOOR[5:8])
                elif 's' in self.wall_directions:
                    self.texture = random.choice(FLOOR[11:14])
                else:
                    self.texture = random.choice(FLOOR[14:17])
            elif len(self.wall_directions) == 2:
                if 'n' in self.wall_directions:
                    self.texture = random.choice(FLOOR[8:11])
                elif 'w' in self.wall_directions:
                    self.texture = random.choice(FLOOR[5:8])
                elif 's' in self.wall_directions:
                    self.texture = random.choice(FLOOR[11:14])
                elif 'e' in self.wall_directions:
                    self.texture = random.choice(FLOOR[14:17])
                else:
                    if 'nw' in self.wall_directions and 'ne' in self.wall_directions:
                        self.texture = FLOOR[53]
                    elif 'nw' in self.wall_directions and 'sw' in self.wall_directions:
                        self.texture = FLOOR[54]
                    elif 'se' in self.wall_directions and 'ne' in self.wall_directions:
                        self.texture = FLOOR[55]
                    else:
                        self.texture = FLOOR[56]
            elif len(self.wall_directions) == 5:
                if 'n' in self.wall_directions:
                    self.texture = FLOOR[38]
                elif 'w' in self.wall_directions:
                    self.texture = FLOOR[39]
                elif 's' in self.wall_directions:
                    self.texture = FLOOR[41]
                else:
                    self.texture = FLOOR[40]
            elif len(self.wall_directions) == 0:
                self.texture = random.choice(FLOOR[-11:-3])
            else:
                if 'n' in self.wall_directions:
                    if 'sw' in self.wall_directions:
                        self.texture = FLOOR[37]
                    else:
                        self.texture = FLOOR[36]
                elif 'w' in self.wall_directions:
                    if 'ne' in self.wall_directions:
                        self.texture = FLOOR[32]
                    else:
                        self.texture = FLOOR[30]
                elif 's' in self.wall_directions:
                    if 'nw' in self.wall_directions:
                        self.texture = FLOOR[35]
                    else:
                        self.texture = FLOOR[34]
                else:
                    if 'nw' in self.wall_directions:
                        self.texture = FLOOR[33]
                    else:
                        self.texture = FLOOR[31]


class FloorDecor(arcade.Sprite):
    def __init__(self, altar):
        super().__init__(scale=1)
        if altar:
            print(ALTAR)
            self.texture = random.choice(ALTAR)
        else:
            print(FLOOR_DECO)
            self.texture = random.choice(FLOOR_DECO)
