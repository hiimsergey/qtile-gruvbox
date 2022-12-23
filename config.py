#     ██████     █████     ███  ████          
#   ███░░░░███  ░░███     ░░░  ░░███          
#  ███    ░░███ ███████   ████  ░███   ██████ 
# ░███     ░███░░░███░   ░░███  ░███  ███░░███
# ░███   ██░███  ░███     ░███  ░███ ░███████ 
# ░░███ ░░████   ░███ ███ ░███  ░███ ░███░░░  
#  ░░░██████░██  ░░█████  █████ █████░░██████ 
#    ░░░░░░ ░░    ░░░░░  ░░░░░ ░░░░░  ░░░░░░  
# ~/.config/qtile/config.py
# Qtile Configuration
# https://github.com/hiimsergey/qtile-examples

## IMPORTS
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

## VARIABLES
mod = "mod4"
terminal = "kitty"
browser = "chromium"
notes = "obsidian"
vm = "virt-manager"
minecraft = "prismlauncher"

## KEYS
keys = [
    # Launch applications
    Key([mod], "a", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "c", lazy.spawn(browser), desc="Launch browser"),
    Key([mod], "q", lazy.spawn(notes), desc="Launch notes"),
    Key([mod], "v", lazy.spawn(vm), desc="Launch virtual machines"),
    Key([mod], "g", lazy.spawn(minecraft), desc="Launch Minecraft"),

    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    # Move windows between columns
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Switch columns
    Key([mod, "mod1"], "h", lazy.layout.swap_column_left()),
    Key([mod, "mod1"], "l", lazy.layout.swap_column_right()),

    # Toggle between split and unsplit sides of stack.
    Key([mod], "return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),

    # Toggle between different layouts
    Key([mod], "tab", lazy.next_layout(), desc="Toggle next layout"),
    Key([mod, "shift"], "tab", lazy.prev_layout(), desc="Toggle previous layout"),

    # Toggle floating or fullscreen windows
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating window"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen window"),

    # Other basic actions
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    # Volume
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -c 0 -q set Master 2dB+")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -c 0 -q set Master 2dB-")),
    Key([], "XF86AudioMute", lazy.spawn("amixer -c 0 -q set Master toggle")),
]

## MOUSE
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

## GROUPS
groups = [Group(i) for i in "12345"]
for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key([mod], i.name, lazy.group[i.name].toscreen(), desc="Switch to group {}".format(i.name)),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True), desc="Switch to & move focused window to group {}".format(i.name)),
        ]
    )

## LAYOUTS
layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4, margin=6, margin_on_single=0),
    layout.Max(),
    # layout.Stack(num_stacks=2),
    layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="Cantarell",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

## COLORS
colo = [["#282828"], # bg
        ["#cc241d"], # red
        ["#d65d0e"], # orange
        ["#d79921"], # yellow
        ["#98971a"], # green
        ["#689d6a"], # aqua
        ["#458588"], # blue
        ["#b16286"]] # purple

### COLORS (soft versions)
cols = [["#928374"],
        ["#fb4934"],
        ["#fe8019"],
        ["#fabd2f"],
        ["#b8bb26"],
        ["#8ec07c"],
        ["#83a598"],
        ["#d3869b"]]
contrast = "#1d2021"   # darker bg

## SCREENS
# To achieve a Powerline effect without installing anything additionally, you insert Unicode characters ("" and "") between the widgets.
# Instead of copy-pasting the almost same lines over and over again, I used my limited Python skills to write this neat function.
def powerline(rl, fg, bg):
    if rl == 0:
        uc = ""
    else:
        uc = ""
    return widget.TextBox(text = uc, padding = 0, fontsize = 24, foreground=fg, background=bg)

screens = [
    Screen(
        wallpaper="~/.config/qtile/arch.png",
        wallpaper_mode="stretch",
        top=bar.Bar(
            [
                widget.CurrentLayoutIcon(
                    scale=0.75,
                    background=colo[3]
                ),
                powerline(0, colo[3], cols[3]),
                powerline(0, cols[3], colo[6]),
                widget.GroupBox(
                    highlight_method="block",
                    background=colo[6],
                    this_current_screen_border=cols[6]
                ),
                powerline(0, colo[6], cols[6]),
                powerline(0, cols[6], colo[7]),
                widget.WindowName(
                    background=colo[7],
                    empty_group_string="Gruvbox <3"
                ),
                powerline(0, colo[7], cols[7]),
                powerline(0, cols[7], contrast),
                powerline(0, contrast, colo[0]),
                widget.Prompt(),
                widget.Spacer(
                    length=800
                ),
                powerline(1, contrast, colo[0]),
                powerline(1, cols[5], contrast),
                powerline(1, colo[5], cols[5]),
                widget.Systray(
                    background=colo[5]
                ),
                widget.Volume(
                    emoji=True,
                    background=colo[5]
                ),
                widget.Volume(
                    background=colo[5]
                ),
                powerline(1, cols[4], colo[5]),
                powerline(1, colo[4], cols[4]),
                widget.BatteryIcon(
                    background=colo[4]
                ),
                widget.Battery(
                    charge_char="now ",
                    discharge_char="left",
                    format="{percent:2.0%} {char}",
                    background=colo[4]
                    ),
                powerline(1, cols[1], colo[4]),
                powerline(1, colo[1], cols[1]),
                widget.Clock(
                    format="%Y-%m-%d %a %I:%M %p",
                    background=colo[1]
                ),
            ],
            26,
            background=colo[0]
        ),
    ),
]

## ETC
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
