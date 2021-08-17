from libqtile.config import Key
from libqtile.lazy import lazy

from configuration.keybindings.mod import Keys
# from configuration.keybindings.window import


class Keybindings:
    keys = [
        Key([Keys.Modifier.mod_key], Keys.Vim.left,
            lazy.layout.left(), desc="Move focus to left"),

        Key([Keys.Modifier.mod_key], Keys.Vim.right,
            lazy.layout.right(), desc="Move focus to right"),
        Key([Keys.Modifier.mod_key], Keys.Vim.down,
            lazy.layout.down(), desc="Move focus down"),
        Key([Keys.Modifier.mod_key], Keys.Vim.up,
            lazy.layout.up(), desc="Move focus up"),

        # TODO: Change this to switch tiling layouts
        Key([Keys.Modifier.mod_key], Keys.Modifier.space_key, lazy.next_layout(),
            desc="Move window focus to other window"),
        Key([Keys.Modifier.mod_key, Keys.Modifier.shift_key], Keys.Vim.left, lazy.layout.shuffle_left(),
            desc="Move window to the left"),
        Key([Keys.Modifier.mod_key, Keys.Modifier.shift_key], Keys.Vim.right, lazy.layout.shuffle_right(),
            desc="Move window to the right"),
        Key([Keys.Modifier.mod_key, Keys.Modifier.shift_key], Keys.Vim.down, lazy.layout.shuffle_down(),
            desc="Move window down"),
        Key([Keys.Modifier.mod_key, Keys.Modifier.shift_key], Keys.Vim.up,
            lazy.layout.shuffle_up(), desc="Move window up"),

        # Grow windows. If current window is on the edge of screen and direction
        # will be to screen edge - window would shrink.
        Key([Keys.Modifier.mod_key, Keys.Modifier.control_key], Keys.Vim.left, lazy.layout.grow_left(),
            desc="Grow window to the left"),
        Key([Keys.Modifier.mod_key, Keys.Modifier.control_key], Keys.Vim.right, lazy.layout.grow_right(),
            desc="Grow window to the right"),
        Key([Keys.Modifier.mod_key, Keys.Modifier.control_key], Keys.Vim.down, lazy.layout.grow_down(),
            desc="Grow window down"),
        Key([Keys.Modifier.mod_key, Keys.Modifier.control_key], Keys.Vim.up,
            lazy.layout.grow_up(), desc="Grow window up"),
        Key([Keys.Modifier.mod_key], 'j', lazy.layout.normalize(),
            desc="Reset all window sizes"),

        # Toggle between split and unsplit sides of stack.
        # Split = all windows displayed
        # Unsplit = 1 window displayed, like Max layout, but still with
        # multiple stack panes
        Key([Keys.Modifier.mod_key, Keys.Modifier.shift_key], Keys.Modifier.enter, lazy.layout.toggle_split(),
            desc="Toggle between split and unsplit sides of stack"),
        Key([Keys.Modifier.mod_key], Keys.Modifier.enter,
            lazy.spawn("kitty"), desc="Launch terminal"),
        Key([Keys.Modifier.mod_key], 'q',
            lazy.window.kill(), desc="Kill focused window"),
        Key([Keys.Modifier.mod_key], 's', lazy.spawn(
            "maim -s -u | xclip -selection clipboard -t image/png -i")),
        Key([Keys.Modifier.mod_key, Keys.Modifier.control_key], "r",
            lazy.restart(), desc="Restart Qtile"),
        Key([Keys.Modifier.mod_key, Keys.Modifier.control_key], 'q',
            lazy.shutdown(), desc="Shutdown Qtile"),
        Key([Keys.Modifier.mod_key], 'r', lazy.spawncmd(),
            desc="Spawn a command using a prompt widget")
    ]
