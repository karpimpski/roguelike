import tcod


def handle_keys(sym):
    print(sym)
    switch = {
        1073741920: {"move": (0, -1)},
        1073741914: {"move": (0, 1)},
        1073741916: {"move": (-1, 0)},
        1073741918: {"move": (1, 0)},
        27: {"exit": True},
    }
    return switch.get(sym)
