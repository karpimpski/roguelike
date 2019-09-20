"""Interprets input."""


def handle_keys(sym):
    """Reads input symbol and returns appropriate command."""
    print('Debug: ' + str(sym))
    switch = {
        1073741920: {"move": (0, -1)},
        1073741906: {"move": (0, -1)},
        1073741914: {"move": (0, 1)},
        1073741905: {"move": (0, 1)},
        1073741916: {"move": (-1, 0)},
        1073741904: {"move": (-1, 0)},
        1073741918: {"move": (1, 0)},
        1073741903: {"move": (1, 0)},
        27: {"exit": True},
    }
    return switch.get(sym)
