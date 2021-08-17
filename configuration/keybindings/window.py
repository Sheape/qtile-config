from libqtile.lazy import lazy
from libqtile.config import Key

from configuration.keybindings.mod import Keys


class Layout:
    def __init__():
        pass

    Keys([Keys.Modifier.mod_key], Keys.Modifier.space_key, lazy.next_layout())
