from libqtile.lazy import lazy
from libqtile.config import Key

from configuration.keybindings.mod import Keys


class Rofi:
    keys = [
        Key([Keys.Modifier.mod_key],
            'r',
            lazy.spawn("rofi -show run -display-run ' '"),
            desc="Spawn a command using a prompt widget"),

    ]
