from typing import List

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

from configuration.keybindings.mod import Keys
from configuration.keybindings.keys import Keybindings

mod = Keys.Modifier.mod_key
terminal = "kitty"

keys = Keybindings.keys

groups = [Group("1", exclusive=False, label=""),
          Group("2", exclusive=False, label=""),
          Group("3", exclusive=False, label=""),
          Group("4", exclusive=False, label=""),
          Group("5", exclusive=False, label=""),
          Group("6", exclusive=False, persist=False, init=False, label=""),
          Group("7", exclusive=False, persist=False, init=False, label=""),
          Group("8", exclusive=False, persist=False, init=False, label=""),
          Group("9", exclusive=False, persist=False, init=False, label="")
          ]

layouts = [
   layout.Columns(border_focus='#ef7981',
                   border_normal='#122125',
                   border_width=3,
                   margin=4,
                   ),
    layout.Floating(border_focus_active='a4d8d8'),

    layout.Max()
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='JetBrains Mono Nerd Font',
    fontsize=13,
    padding=10,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.TextBox('',
                               font='Roboto Mono Nerd Font',
                               fontsize=14,
                               padding=15,
                               foreground="#a4d8d8"),
                widget.Sep(padding=1, linewidth=0, size_percent=5),
                widget.TextBox('', padding=0, foreground="#a4d8d8", fontsize=17),
                widget.Sep(padding=7, linewidth=0, size_percent=5),
                # widget.CurrentLayout(),
                widget.GroupBox(active='#af93b9',
                                fontsize=14,
                                disable_drag=True,
                                highlight_method='text',
                                inactive='#4f4f4b',
                                this_current_screen_border='#ef7981',
                                padding_x=6),
                widget.Prompt(),
                widget.Spacer(),
                widget.WindowName(format=" {state}{name}",
                                  width=bar.CALCULATED,
                                  max_chars=60,
                                  foreground="ecb09a",
                                  padding=0,
                                  empty_group_string=" Desktop"),
                widget.Spacer(),
                widget.TextBox('奔', foreground="#ddc3cd", fontsize=16),
                widget.Spacer(length=3),
                widget.PulseVolume(padding=0, 
                                   foreground="#ddc3cd",
                                   limit_max_volume=True),
                widget.Spacer(length=20),
                widget.Clock(format='%a %I:%M %p', padding=0, foreground="#ddc3cd"),
                widget.Spacer(length=20)
            ],
            35,
            background='#122125',
            margin=[10, 10, 2, 10]
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    Match(wm_class='galculator')
], border_focus="#122125")
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "I use arch btw."
