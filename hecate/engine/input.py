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

    def update_press(self, addkey, addmod):
        self.keys.add(Key(v=addkey))
        self.modifiers = Modifier.parse_modifiers(addmod)

    def update_release(self, relkey, relmod):
        print('hello')
        for i in self.keys:
            if relkey == KEYS[str(i)]:
                self.keys.remove(i)
                break

        self.modifiers = Modifier.parse_modifiers(relmod)


class Key:
    def __init__(self, n=None, v=None):
        if n is None:
            if v is None:
                raise ValueError
            else:
                self.name = list(KEYS.keys())[list(KEYS.values()).index(v)]
        elif v is None:
            self.name = n
            self.value = KEYS[n]
        else:
            self.name = n
            self.value = v

    def __str__(self):
        return self.name


class Modifier:
    def __init__(self, n=None, v=None):
        if n is None:
            if v is None:
                raise ValueError
            else:
                self.name = list(MODS.keys())[list(MODS.values()).index(v)]
        elif v is None:
            self.name = n
            self.value = MODS[n]
        else:
            self.name = n
            self.value = v

    def __str__(self):
        return self.name

    @staticmethod
    def parse_modifiers(modifiers):
        all = set()
        for m in MODS:
            if (MODS[m] & modifiers):
                all.add(Modifier(v=MODS[m]))

        return all
