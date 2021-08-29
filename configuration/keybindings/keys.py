from libqtile.config import Key
from libqtile.lazy import lazy

# Keybindings
from configuration.keybindings.mod import Keys
from configuration.keybindings.window import Window
from configuration.keybindings.workspace import Workspace
from configuration.keybindings.system import System
from configuration.keybindings.layout import Layout
from configuration.keybindings.rofi import Rofi

class Keybindings:
    # This class is only here to combine all the
    # keybindings from other modules inside this package.

    keys = [
        Key([Keys.Modifier.mod_key], Keys.Modifier.enter,
            lazy.spawn("alacritty"), desc="Launch terminal"),
        Key([Keys.Modifier.mod_key], 's', lazy.spawn(
            "scrot '%Y_%m_%d___%I:%M%p.png' -select -e 'mv $f ~/Pictures/Screenshots/'")),
    ]

keybindings = Keybindings.keys

keybindings.extend(Window.keys)
keybindings.extend(Workspace.keys)
keybindings.extend(System.keys)
keybindings.extend(Layout.keys)
keybindings.extend(Rofi.keys)
