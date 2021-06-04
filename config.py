# # # The configurationg is still incomplete.
# # # The following tasks  are still left.
# # #   *   Notifications
# #     *   Lockscreen 
# #     *   custom rofi scripts
# #     *   auto mounting




# import os
# import re
# import socket
# import subprocess
# from libqtile import qtile
# from libqtile.config import Click, Drag, Group, KeyChord, Key, Match, Screen
# from libqtile.command import lazy
# from libqtile import layout, bar, widget, hook
# from libqtile.lazy import lazy
# from typing import List  # noqa: F401
# from settings.layouts import layouts, floating_layout
# from settings.keys import mod, alt, keys
# from settings.groups import groups
# from settings.mouse import mouse
# from settings.widgets import widget_list, extension_defaults, widget_defaults, secondary_list
# #from settings.path import qtile_path


# screens = [Screen(top=bar.Bar(widgets=widget_list, opacity=1.0, size=20)),
#            Screen(top=bar.Bar(widgets=secondary_list, opacity=1.0, size=20))
#             ]


# dgroups_key_binder = None
# dgroups_app_rules = []  # type: List
# main = None  # WARNING: this is deprecated and will be removed soon
# follow_mouse_focus = True
# bring_front_click = False
# cursor_warp = False

# auto_fullscreen = True
# focus_on_window_activation = "smart"


# def window_to_prev_group(qtile):
#     if qtile.currentWindow is not None:
#         i = qtile.groups.index(qtile.currentGroup)
#         qtile.currentWindow.togroup(qtile.groups[i - 1].name)

# def window_to_next_group(qtile):
#     if qtile.currentWindow is not None:
#         i = qtile.groups.index(qtile.currentGroup)
#         qtile.currentWindow.togroup(qtile.groups[i + 1].name)

# def window_to_previous_screen(qtile):
#     i = qtile.screens.index(qtile.current_screen)
#     if i != 0:
#         group = qtile.screens[i - 1].group.name
#         qtile.current_window.togroup(group)

# def window_to_next_screen(qtile):
#     i = qtile.screens.index(qtile.current_screen)
#     if i + 1 != len(qtile.screens):
#         group = qtile.screens[i + 1].group.name
#         qtile.current_window.togroup(group)

# def switch_screens(qtile):
#     i = qtile.screens.index(qtile.current_screen)
#     group = qtile.screens[i - 1].group
#     qtile.current_screen.set_group(group)

# @hook.subscribe.startup_once
# def autostart():
#     home = os.path.expanduser('~/.config/qtile/autostart.sh')
#     subprocess.call([home])

# # Long story this is done so that Java UI toolkits are not a pain in the ass.
# wmname = "LG3D"

import os
import re
import socket
import subprocess
from libqtile import qtile
from libqtile.config import Click, Drag, Group, KeyChord, Key, Match, Screen
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.lazy import lazy
from typing import List  # noqa: F401


mod = "mod4"
terminal = "alacritty"
default_browser = "brave"
alt = "mod1"







## Key bindidings ------------------------------------------------------------------------------------------------------------
keys = [

    # Read the desc arg  to know what the keybingdings do...
    Key([mod], "j", lazy.layout.down(),
        desc="Move focus down"),

    Key([mod], "k", lazy.layout.up(),
        desc="Move focus up"),

    Key([mod], "h", lazy.layout.shrink(), lazy.layout.decrease_nmaster(),
       desc='Shrink window (MonadTall), decrease number in master pane (Tile)'),

    Key([mod], "l", lazy.layout.grow(), lazy.layout.increase_nmaster(),
        desc='Expand window (MonadTall), increase number in master pane (Tile)'),

    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    Key([mod], "n", lazy.layout.normalize(),
        desc='normalize window size ratios'),

    Key([mod], "m", lazy.layout.maximize(),
        desc='toggle window between minimum and maximum sizes'),

    Key([mod, alt], "space", lazy.window.toggle_floating(),
        desc='toggle floating'),

    Key([mod], "i", lazy.window.toggle_fullscreen(),
        desc='toggle fullscreen'),

    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        lazy.layout.section_down(),
        desc="Move window down"),

    Key([mod, "shift"], "k", lazy.layout.shuffle_up(),
        lazy.layout.section_up(),
        desc="Move window up"),

    Key([mod, "shift"], "Tab", lazy.layout.rotate(), lazy.layout.flip(),
        desc="Toggle between split and unsplit sides of stack"),


    Key([mod], "Return", lazy.spawn(terminal),
        desc="Launch terminal"),

    Key([mod], "w", lazy.spawn(default_browser),
        desc="Launch default_browser"),


    Key([mod], "Tab", lazy.next_layout(),
        desc="Toggle between layouts"),


    Key([mod], "q", lazy.window.kill(),
        desc="Kill focused window"),

    # Keychord for applications 
    KeyChord([mod], "p",[

        Key([], "o", 
            lazy.spawn("obsidian"),
            desc="Launching Obsidian"),

        Key([], "m", 
            lazy.spawn("vmplayer"),
            desc="Launching vmplayer"),

        Key([], "t", 
            lazy.spawn("thunar"),
            desc="Launching thunar file manager")

        ]),


    Key([mod, "shift"], "r", lazy.restart(),
        desc="Restart Qtile"),


    Key([mod, "control"], "q", lazy.shutdown(),
        desc="Shutdown Qtile"),

    # Switch focus to next monitor
    Key([mod], "space", lazy.next_screen(),
        desc='Move focus to next monitor'),

    # Sound
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -c 0 sset Master 1- unmute")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -c 0 sset Master 1+ unmute")),

    Key([mod], "r", lazy.spawn("rofi  -show run -p 'Run :'"),
        desc="Spawn rofi run launcher")


    # Switch focus to previous monitor
    #Key([mod], "comma", lazy.prev_screen(), desc='Move focus to previous monitor')

    # Switch focus to the Primary Monitor (First Display)
    #Key([mod], ";", lazy.to_screen(0), desc='Keyboard focus to monitor 1'),


    # Switch focus to the Secondary Monitor (Second Display)
    #Key([mod], "'", lazy.to_screen(0), desc='Keyboard focus to monitor 2'),

]
## ------------------------------------------------------------------------------------------------------------------------------


## Groups and their Key bindings ------------------------------------------------------------------------------------------------

group_names = [("1", {'layout': 'monadtall'}),
               ("2", {'layout': 'monadtall'}),
               ("3", {'layout': 'monadtall'}),
               ("4", {'layout': 'monadtall'}),
               ("5", {'layout': 'monadtall'}),
               ("6", {'layout': 'monadtall'}),
               ("7", {'layout': 'monadtall'}),
               ("8", {'layout': 'monadtall'}),
               ("9", {'layout': 'floating'})]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group

## ------------------------------------------------------------------------------------------------------------------------------


layout_theme = {
    
    "border_width" : 2,
    "margin": 8,
    "border_focus": "dc322f",
    "border_normal": "073642"
}

## Layouts
layouts = [
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.Max(),
    layout.Floating(**layout_theme)

]
## ------------------------------------------------------------------------------------------------------------------------------


widget_defaults = dict(
    font='Roboto Medium',
    fontsize=12,
    padding=3,
    background="002b36",
    foreground="93a1a1"
    
    
)

sep = widget.TextBox(
        font="Roboto Medium Bold",
        text="",
        foreground="b58900"
    )

groupbox = widget.GroupBox(
                font="Roboto Medium",
                highlight_method="block",
                rounded=False,
                padding_x=5,
                padding_y=5,
                active="#ffffff",
                inactive="#959595",
               # other_screen_border="ac5e5e",
               # this_current_screen_border="",
                this_screen_border="ac5e5e",
                this_current_screen_border="c91212",
                urgent_border="bf616a",
                disable_drag=True
            )
windowname = widget.WindowName(
                font="Roboto Medium",
                foreground="eee8d5"
            )
day = widget.Clock(format='%Y-%m-%d')
time = widget.Clock(format='%I:%M %p %a ')
currentLayout = widget.CurrentLayout()
vol = widget.Volume()
mem =widget.Memory()
systray = widget.Systray()

extension_defaults = widget_defaults.copy()

bar1_widgets = [
                
                groupbox,
                widget.Prompt(),
                windowname,
                sep,
                systray,
                sep,
                vol,
                sep,
                mem,
                sep,
                currentLayout,
                sep,
                day,
                sep,
                time
                
            ]

bar2_widgets = [
                
                widget.GroupBox(
                    font="Roboto Medium",
                    highlight_method="block",
                    rounded=False,
                    padding_x=5,
                    padding_y=5,
                    active="#ffffff",
                    inactive="#959595",
                    # other_screen_border="ac5e5e",
                    # this_current_screen_border="",
                    this_screen_border="ac5e5e",
                    this_current_screen_border="c91212",
                    urgent_border="bf616a",
                    disable_drag=True
            ),
                
                widget.WindowName(),
                sep,
                
                
                vol,
                sep,
                mem,
                sep,
                currentLayout,
                sep,
                day,
                sep,
                time
                
            ]

screens = [
    Screen(
        top=bar.Bar(bar1_widgets,24)
    ),
    Screen(
        top=bar.Bar(bar2_widgets,24)
    )
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
main = None  # WARNING: this is deprecated and will be removed soon
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
])
auto_fullscreen = True
focus_on_window_activation = "smart"


def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

def window_to_previous_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group)

def window_to_next_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group)

def switch_screens(qtile):
    i = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[i - 1].group
    qtile.current_screen.set_group(group)






@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])

# Long story this is done so that Java UI toolkits are not a pain in the ass.
wmname = "LG3D"

