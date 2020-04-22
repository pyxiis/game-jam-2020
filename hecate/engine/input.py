from arcade import key

KEYS = dict()
MODS = dict()

for k in dir(key):
    if "MOD_" in k:
        MODS[k[4:]] = eval(f'key.{k}')
    elif "__" not in k:
        KEYS[k] = eval(f'key.{k}')


class KeyManager:

    def __init__(self):
        self.keys = set()
        self.modifiers = set()
        self.loc = (0, 0)
        self.mouse_keys = set()

    def update_press(self, addkey, addmod):
        self.keys.add(addkey)
        self.modifiers = KeyManager.parse_modifiers(addmod)

    def update_release(self, relkey, relmod):
        self.keys.remove(relkey)
        self.modifiers = KeyManager.parse_modifiers(relmod)

    def update_mouse_press(self, x, y, button, mods):
        self.mouse_keys.add(button)
        self.modifiers = KeyManager.parse_modifiers(mods)
        self.loc = (x, y)

    def update_mouse_release(self, x, y, button, mods):
        self.mouse_keys.remove(button)
        self.modifiers = KeyManager.parse_modifiers(mods)
        self.loc = (x, y)

    def update_mouse(self, x, y):
        self.loc = (x, y)

    @staticmethod
    def parse_modifiers(modifiers):
        all = set()
        for m in MODS:
            if (MODS[m] & modifiers):
                all.add(MODS[m])

        return all
