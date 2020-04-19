import arcade
import yaml
from engine.input import KeyManager

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

SETTINGS = yaml.load(open('settings.yaml', 'r'), Loader=Loader)

class Hecate(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        super().__init__(width, height)
        self.km = KeyManager()
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        # Set up your game here
        pass

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        # Your drawing code goes here

    def update(self, delta_time):
        pass

    def on_key_press(self, key, modifiers):
        self.km.update_press(key, modifiers)

    def on_key_release(self, key, modifiers):
        self.km.update_release(key, modifiers)


def main():
    game = Hecate(SETTINGS['window']['width'], SETTINGS['window']['height'])
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
