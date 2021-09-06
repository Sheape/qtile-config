from libqtile.lazy import lazy
from libqtile.config import Key

from configuration.keybindings.mod import Keys

class Apps:
    keys = [
            Key([Keys.Modifier.mod_key],
                'b',
                lazy.spawn('brave'),
                desc="Launch Default browser"),

            Key([Keys.Modifier.mod_key],
                'e',
                lazy.spawn('emacsclient -c'),
                desc="Launch emacs as a client"),

            Key([Keys.Modifier.mod_key],
                't',
                lazy.spawn('pomotroid'),
                desc="Launch pomotroid"),

            # Key([Keys.Modifier.mod_key],
            #     'm',
            #     lazy.spawn(),
            #     desc="Toggle music player"),

            # Key([Keys.Modifier.mod_key],
            #     'd',
            #     lazy.spawn(),
            #     desc="Toggle Date"),
            ]
