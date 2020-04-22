import math

import arcade


def attack(player: arcade.Sprite, mobs: arcade.SpriteList, angle: int, angle_sweep: int,
           dist: int) -> arcade.SpriteList:
    attackable = arcade.SpriteList()
    angles = [angle - angle_sweep, angle + angle_sweep]
    corrected = False
    if angles[0] < 0:
        corrected = True
        if angles[1] > 270:
            angles = [angles[0] + 90, angles[1] - 270]
        else:
            angles = [angles[0] + 90, angles[1] + 90]
    for mob in mobs:
        if (mob.center_x - player.center_x) ** 2 + (
                mob.center_y - player.center_y) ** 2 <= dist ** 2:
            attack_angle = math.atan2(mob.center_x - player.center_x,
                                      mob.center_y - player.center_y)
            attack_angle *= 360 / (2 * math.pi)
            if corrected:
                if attack_angle > 270:
                    attack_angle -= 270
                else:
                    attack_angle += 90

            if attack_angle < angles[1] and attack_angle > angles[0]:
                attackable.append(mob)

    return attackable
