import random

import arcade

from ...assets.sprites import CEILING as WALL
from ...assets.sprites import WALL as FACADE
from ...assets.sprites import WALL_DECO as WD


class Ceiling(arcade.Sprite):
    def __init__(self, direction):
        super().__init__(scale=1)

        # For readability

        # This part is a bit wonky since arcade has 0 at bottom instead of top,
        # but flooring cardinality is good
        self.wall_directions = []
        if 1 & direction == 1:
            self.wall_directions.append('e')
        if 2 & direction == 2:
            self.wall_directions.append('ne')
        if 4 & direction == 4:
            self.wall_directions.append('n')
        if 8 & direction == 8:
            self.wall_directions.append('nw')
        if 16 & direction == 16:
            self.wall_directions.append('w')
        if 32 & direction == 32:
            self.wall_directions.append('sw')
        if 64 & direction == 64:
            self.wall_directions.append('s')
        if 128 & direction == 128:
            self.wall_directions.append('se')

        if len(self.wall_directions) == 8:
            # untextured block
            self.texture = WALL[0]



        elif len(self.wall_directions) == 7:
            # concave corner piece
            if 'ne' not in self.wall_directions:
                self.texture = WALL[-5]
            elif 'nw' not in self.wall_directions:
                self.texture = WALL[-6]
            elif 'se' not in self.wall_directions:
                self.texture = WALL[-7]
            else:
                self.texture = WALL[-8]

        elif len(self.wall_directions) == 6:
            # side piece or edge case double corner
            if 'n' not in self.wall_directions:
                self.texture = random.choice(WALL[11:14])
            elif 'w' not in self.wall_directions:
                self.texture = random.choice(WALL[5:8])
            elif 's' not in self.wall_directions:
                self.texture = random.choice(WALL[8:11])
            elif 'e' not in self.wall_directions:
                self.texture = random.choice(WALL[14:17])
            elif 'ne' not in self.wall_directions and 'sw' not in self.wall_directions:
                self.texture = WALL[-14]
            elif 'nw' not in self.wall_directions and 'se' not in self.wall_directions:
                self.texture = WALL[-15]
            elif 'ne' not in self.wall_directions:
                if 'nw' not in self.wall_directions:
                    self.texture = WALL[-1]
                else:
                    self.texture = WALL[-3]
            else:
                if 'se' not in self.wall_directions:
                    self.texture = WALL[-4]
                else:
                    self.texture = WALL[-2]

        elif len(self.wall_directions) == 5:
            # side piece or edge case double corner
            if 'n' not in self.wall_directions:
                self.texture = random.choice(WALL[11:14])
            elif 'w' not in self.wall_directions:
                self.texture = random.choice(WALL[5:8])
            elif 's' not in self.wall_directions:
                self.texture = random.choice(WALL[8:11])
            else:
                self.texture = random.choice(WALL[14:17])

        elif len(self.wall_directions) == 4:
            if 'n' in self.wall_directions and 'w' in self.wall_directions and 's' in self.wall_directions and 'e' in self.wall_directions:
                self.texture = WALL[-9]
            elif 'sw' not in self.wall_directions and 's' not in self.wall_directions and 'w' not in self.wall_directions:
                self.texture = WALL[1]
            elif 'se' not in self.wall_directions and 's' not in self.wall_directions and 'e' not in self.wall_directions:
                self.texture = WALL[2]
            elif 'nw' not in self.wall_directions and 'n' not in self.wall_directions and 'w' not in self.wall_directions:
                self.texture = WALL[3]
            elif 'ne' not in self.wall_directions and 'n' not in self.wall_directions and 'e' not in self.wall_directions:
                self.texture = WALL[4]
            elif 'e' in self.wall_directions and 'w' in self.wall_directions:
                if 'n' not in self.wall_directions and 's' not in self.wall_directions:
                    self.texture = random.choice(WALL[21:23])
                elif 'ne' in self.wall_directions and 'n' in self.wall_directions:
                    self.texture = WALL[37]
                elif 'nw' in self.wall_directions and 'n' in self.wall_directions:
                    self.texture = WALL[36]
                elif 'se' in self.wall_directions and 's' in self.wall_directions:
                    self.texture = WALL[34]
                elif 'sw' in self.wall_directions and 's' in self.wall_directions:
                    self.texture = WALL[35]
                else:
                    if 'n' in self.wall_directions:
                        self.texture = WALL[41]
                    else:
                        self.texture = WALL[38]
            else:
                if 'e' not in self.wall_directions and 'w' not in self.wall_directions:
                    self.texture = random.choice(WALL[23:25])
                elif 'ne' in self.wall_directions and 'e' in self.wall_directions:
                    self.texture = WALL[32]
                elif 'nw' in self.wall_directions and 'w' in self.wall_directions:
                    self.texture = WALL[33]
                elif 'se' in self.wall_directions and 'e' in self.wall_directions:
                    self.texture = WALL[30]
                elif 'sw' in self.wall_directions and 'w' in self.wall_directions:
                    self.texture = WALL[31]
                else:
                    if 'w' in self.wall_directions:
                        self.texture = WALL[40]
                    else:
                        self.texture = WALL[39]

        elif len(self.wall_directions) == 3:
            # corner piece or edge case double sided piece or edge case corner/side piece
            if 'ne' in self.wall_directions and 'n' in self.wall_directions and 'e' in self.wall_directions:
                self.texture = WALL[1]
            elif 'nw' in self.wall_directions and 'n' in self.wall_directions and 'w' in self.wall_directions:
                self.texture = WALL[2]
            elif 'se' in self.wall_directions and 's' in self.wall_directions and 'e' in self.wall_directions:
                self.texture = WALL[3]
            elif 'sw' in self.wall_directions and 's' in self.wall_directions and 'w' in self.wall_directions:
                self.texture = WALL[4]
            elif 'n' not in self.wall_directions and 'w' not in self.wall_directions and 's' not in self.wall_directions:
                self.texture = WALL[17]
            elif 'e' not in self.wall_directions and 'w' not in self.wall_directions and 's' not in self.wall_directions:
                self.texture = WALL[18]
            elif 'e' not in self.wall_directions and 'n' not in self.wall_directions and 's' not in self.wall_directions:
                self.texture = WALL[19]
            elif 'e' not in self.wall_directions and 'n' not in self.wall_directions and 'w' not in self.wall_directions:
                self.texture = WALL[16]
            elif 'w' not in self.wall_directions and 'e' not in self.wall_directions:
                self.texture = random.choice(WALL[23:25])
            elif 'n' not in self.wall_directions and 's' not in self.wall_directions:
                self.texture = random.choice(WALL[21:23])
            else:
                if 'n' not in self.wall_directions:
                    self.texture = WALL[41]
                elif 'w' not in self.wall_directions:
                    self.texture = WALL[40]
                elif 's' not in self.wall_directions:
                    self.texture = WALL[38]
                else:
                    self.texture = WALL[39]

        elif len(self.wall_directions) == 2:
            if 'n' in self.wall_directions and 's' in self.wall_directions:
                self.texture = random.choice(WALL[23:25])
            elif 'w' in self.wall_directions and 'e' in self.wall_directions:
                self.texture = random.choice(WALL[21:23])
            elif 'n' in self.wall_directions:
                self.texture = WALL[18]
            elif 'w' in self.wall_directions:
                self.texture = WALL[19]
            elif 's' in self.wall_directions:
                self.texture = WALL[20]
            else:
                self.texture = WALL[17]
        else:
            # peninsula piece
            if 'n' in self.wall_directions:
                self.texture = WALL[18]
            elif 'w' in self.wall_directions:
                self.texture = WALL[19]
            elif 's' in self.wall_directions:
                self.texture = WALL[16]
            else:
                self.texture = WALL[17]


class Wall(arcade.Sprite):
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

        if 'se' in self.wall_directions and 'sw' in self.wall_directions:
            self.texture = FACADE[-3]
        elif 'se' in self.wall_directions:
            self.texture = FACADE[-4]
        elif 'sw' in self.wall_directions:
            self.texture = FACADE[0]
        else:
            self.texture = random.choice(FACADE[1:5])


class WallDecor(arcade.Sprite):
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

        if 's' not in self.wall_directions:
            self.texture = random.choice(WD[0:6])
        elif 'w' not in self.wall_directions:
            self.texture = random.choice(WD[7:12:2])
        elif 'e' not in self.wall_directions:
            self.texture = random.choice(WD[6:12:2])
