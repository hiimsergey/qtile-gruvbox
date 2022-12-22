from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

mod = "mod4"
terminal = "kitty"
browser = "chromium"
notes = "obsidian"
vm = "virt-manager"
minecraft = "prismlauncher"

keys = [
    Key([mod], "a", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "c", lazy.spawn(browser), desc="Launch browser"),
    Key([mod], "q", lazy.spawn(notes), desc="Launch notes"),
    Key([mod], "v", lazy.spawn(vm), desc="Launch virtual machines"),
    Key([mod], "g", lazy.spawn(minecraft), desc="Launch Minecraft"),
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Switch columns

    # Toggle between split and unsplit sides of stack.
    Key([mod], "return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
    # Toggle between different layouts as defined below
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating window"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen window"),
    Key([mod], "tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]

groups = [Group(i) for i in "12345"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4, margin=6, margin_on_single=0),
    layout.Max(),
    layout.Bsp(),
]

widget_defaults = dict(
    font="Cantarell",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

colors = [["#282828"], #bg
          ["#cc241d"], #red
          ["#d65d0e"], #orange
          ["#d79921"], #yellow
          ["#98971a"], #green
          ["#689d6a"], #aqua
          ["#458588"], #blue
          ["#b16286"], #purple
          ["#a89984"]] #gray
solors = [["#928374"],
          ["#fb4934"],
          ["#fe8019"],
          ["#fabd2f"],
          ["#b8bb26"],
          ["#8ec07c"],
          ["#83a598"],
          ["#d3869b"],
          ["#ebdbb2"]]
contrast = "#1d2021"

screens = [
    Screen(
        wallpaper="~/.config/qtile/arch.png",
        wallpaper_mode="stretch",
        top=bar.Bar(
            [
                widget.CurrentLayoutIcon(scale=0.75, background=colors[3]),
                widget.TextBox(
                       text = '',
                       padding = 0,
                       fontsize = 24,
                       foreground=colors[3],
                       background=solors[3]
                       ),    
                widget.TextBox(
                       text = '',
                       padding = 0,
                       fontsize = 24,
                       foreground=solors[3],
                       background=colors[6]
                       ),    
                widget.GroupBox(
                       highlight_method="block",
                       background=colors[6],
                       this_current_screen_border=solors[6]
                       ),
                widget.TextBox(
                       text = '',
                       padding = 0,
                       fontsize = 24,
                       foreground=colors[6],
                       background=solors[6]
                       ),    
                widget.TextBox(
                       text = '',
                       padding = 0,
                       fontsize = 24,
                       foreground=solors[6],
                       background=colors[7]
                       ),    
                widget.WindowName(background=colors[7], empty_group_string="Gruvbox <3"),
                widget.TextBox(
                       text = '',
                       padding = 0,
                       fontsize = 24,
                       foreground=colors[7],
                       background=solors[7]
                       ),    
                widget.TextBox(
                       text = '',
                       padding = 0,
                       fontsize = 24,
                       foreground=solors[7],
                       background=contrast
                       ),    
                widget.TextBox(
                       text = '',
                       padding = 0,
                       fontsize = 24,
                       foreground=contrast,
                       background=colors[0]
                       ),    
               widget.Prompt(),
               widget.Spacer(length=800),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.TextBox(
                       text = '',
                       padding = 0,
                       fontsize = 24,
                       foreground=contrast,
                       background=colors[0]
                       ),    
                widget.TextBox(
                       text = '',
                       padding = 0,
                       fontsize = 24,
                       foreground=solors[2],
                       background=contrast
                       ),    
                widget.TextBox(
                       text = '',
                       padding = 0,
                       fontsize = 24,
                       foreground=colors[2],
                       background=solors[2]
                       ),    
                widget.Systray(background=colors[2]),
                widget.BatteryIcon(background=colors[2]),
                widget.TextBox(
                       text = '',
                       padding = 0,
                       fontsize = 24,
                       foreground=solors[4],
                       background=colors[2]
                       ),    
                widget.TextBox(
                       text = '',
                       padding = 0,
                       fontsize = 24,
                       foreground=colors[4],
                       background=solors[4]
                       ),    
                widget.Battery(
                    charge_char="now ",
                    discharge_char="left",
                    format="{percent:2.0%} {char}",
                    background=colors[4]
                    ),
                widget.TextBox(
                       text = '',
                       padding = 0,
                       fontsize = 24,
                       foreground=solors[1],
                       background=colors[4]
                       ),    
                widget.TextBox(
                       text = '',
                       padding = 0,
                       fontsize = 24,
                       foreground=colors[1],
                       background=solors[1]
                       ),    
                widget.Clock(format="%Y-%m-%d %a %I:%M %p", background=colors[1]),
            ],
            26,
            background=colors[0]
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "Qtile"
