# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the 'Software'), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import re
import subprocess
from typing import List  # noqa: F401

from libqtile import bar, hook, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

# mod4 is Super, mod1 is Alt
mod = 'mod1'
terminal = 'alacritty'
file_explorer = 'nautilus'


def switch_screens(qtile):
    i = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[i - 1].group
    qtile.current_screen.set_group(group)


def switch_keyboard_layout(qtile):
    qtile.widgets_map['keyboardlayout'].next_keyboard()
    subprocess.call('sleep 0.5; xmodmap ~/.Xmodmap', shell=True)


@lazy.function
def toggle_layouts(qtile):
    qtile.cmd_next_layout()


def where_am_i():
    try:
        ssid = subprocess.check_output(['iw', 'dev', 'wlp9s0', 'link']).decode('utf-8')
        if 'Eytan' in ssid:
            return 'Home'
        if 'Ohad' in ssid:
            return 'Migdal'
        else:
            return None
    except e:
        return None


my_place = where_am_i()
# my_place = 'Home'

keys = [
    # Switch between windows
    Key([mod], 'Left', lazy.layout.left(), desc='Move focus to left'),
    Key([mod], 'Right', lazy.layout.right(), desc='Move focus to right'),
    Key([mod], 'Down', lazy.layout.down(), desc='Move focus down'),
    Key([mod], 'Up', lazy.layout.up(), desc='Move focus up'),
    # Key([mod], 'space', lazy.layout.next(), desc='Move window focus to other window'),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, 'shift'],
        'Left',
        lazy.layout.shuffle_left(),
        desc='Move window to the left',
    ),
    Key(
        [mod, 'shift'],
        'Right',
        lazy.layout.shuffle_right(),
        desc='Move window to the right',
    ),
    Key([mod, 'shift'], 'Down', lazy.layout.shuffle_down(), desc='Move window down'),
    Key([mod, 'shift'], 'Up', lazy.layout.shuffle_up(), desc='Move window up'),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key(
        [mod, 'control'],
        'Left',
        lazy.layout.grow_left(),
        desc='Grow window to the left',
    ),
    Key(
        [mod, 'control'],
        'Right',
        lazy.layout.grow_right(),
        desc='Grow window to the right',
    ),
    Key([mod, 'control'], 'Down', lazy.layout.grow_down(), desc='Grow window down'),
    Key([mod, 'control'], 'Up', lazy.layout.grow_up(), desc='Grow window up'),
    Key([mod], 'n', lazy.layout.normalize(), desc='Reset all window sizes'),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, 'shift'],
        'Return',
        lazy.layout.toggle_split(),
        desc='Toggle between split and unsplit sides of stack',
    ),
    Key(
        [mod],
        'Return',
        lazy.spawn(terminal).when(
            focused=Match(wm_class=re.compile('^(?!.*?jetbrains\\-idea).*'))
        ),
        desc='Launch terminal',
    ),
    Key([mod], 'f', lazy.spawn(file_explorer), desc='Launch file explorer'),
    # Toggle between different layouts as defined below
    Key([mod, 'control'], 'Tab', lazy.next_layout(), desc='Toggle between layouts'),
    Key([mod], 'w', lazy.window.kill(), desc='Kill focused window'),
    Key([mod, 'control'], 'r', lazy.restart(), desc='Restart Qtile'),
    Key([mod, 'control'], 'c', lazy.reload_config(), desc='Reload Qtile Config'),
    Key([mod, 'control'], 'q', lazy.shutdown(), desc='Shutdown Qtile'),
    Key([mod], 'r', lazy.spawn('rofi -show drun'), desc='Spawn a command using rofi'),
    Key(
        [mod, 'control'],
        'e',
        lazy.spawn('rofimoji --files emojis hebrew superscripts_and_subscripts math'),
        desc='Insert Emojies',
    ),
    Key(
        [mod],
        'space',
        lazy.function(switch_keyboard_layout),
        desc='Next keyboard layout.',
    ),
    Key([mod], 's', lazy.function(switch_screens), desc='Switch between screens'),
    Key(
        [mod],
        'Tab',
        lazy.spawn('rofi -show window'),
        desc='Toggle between windows with rofi',
    ),
    # dunst shortcuts
    Key(['shift'], 'space', lazy.spawn('dunstctl close'), desc='Close notification'),
    Key(
        ['control', 'shift'],
        'space',
        lazy.spawn('dunstctl history-pop'),
        desc='Redisplay notification',
    ),
    # Toggle between layouts
    Key([mod], 't', toggle_layouts, desc='Toggle layouts'),
]

translation = {
    'e': 'hebrew_kuf',
    'f': 'hebrew_kaph',
    'n': 'hebrew_nun',
    'r': 'hebrew_resh',
    'c': 'hebrew_bet',
    's': 'hebrew_dalet',
    'q': 'slash',
    'w': 'apostrophe',
    't': 'hebrew_aleph',
}

import copy


def translate_key(key):
    key = copy.copy(key)
    key.key = translation[key.key]
    return key


keys += [translate_key(key) for key in keys if key.key in translation]

groups_conf = {
    'FF': {'spawn': 'firefox', 'exclusive': False, 'label': '🦊'},
    'TER': {'spawn': 'alacritty', 'exclusive': False, 'label': '💻'},
    'CHR': {'spawn': 'google-chrome-stable', 'exclusive': False, 'label': '🌐'},
    'TEL': {'spawn': '/opt/Telegram/Telegram', 'exclusive': False, 'label': '💬'},
    'OBS': {'spawn': 'obsidian', 'exclusive': False, 'label': '🪨 '},
    'MLC': {'spawn': 'nautilus', 'exclusive': False, 'label': '📂'},
    '7': {},
    '8': {},
    '9': {},
    '0': {},
}

groups = [Group(name, **kwargs) for name, kwargs in groups_conf.items()]

for i, (name, kwargs) in enumerate(groups_conf.items(), 1):
    keys.append(
        Key([mod], str(i % 10), lazy.group[name].toscreen())
    )  # Switch to another group
    keys.append(
        Key([mod, 'shift'], str(i % 10), lazy.window.togroup(name))
    )  # Send current window to another group

layouts = [
    layout.Columns(border_focus_stack='#d75f5f', margin=5),
    layout.Max(),
    layout.Floating(),
]

widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

import datetime

import hdate


def get_heb_date():
    return str(hdate.HDate(datetime.datetime.now()).hebrew_date)


import requests

heaterHomeUrl = 'http://192.168.1.2:8888/rest/items/heater'
heaterMigdalUrl = 'http://192.168.1.8/cm'


def get_heater_state():
    if my_place == 'Migdal':
        r = requests.get(heaterMigdalUrl, params={'cmnd': 'power'})
        return '🔥' if r.json()['POWER'] == 'ON' else '💧'
    elif my_place == 'Home':
        r = requests.get(heaterHomeUrl)
        return '🔥' if r.json()['state'] == 'ON' else '💧'
    else:
        return ''


def toggle_heater():
    if my_place == 'Migdal':
        requests.post(heaterMigdalUrl, params={'cmnd': 'power toggle'})
    elif my_place == 'Home':
        requests.post(
            heaterHomeUrl,
            headers={'Content-Type': 'text/plain', 'Accept': 'application/json'},
            data='toggle',
        )


from itertools import cycle

from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration

colors = cycle(['#002b36', '#073642'])

powerline = {'decorations': [PowerLineDecoration(path='forward_slash')]}

screens = [
    Screen(
        wallpaper='~/.config/qtile/wallpaper.png',
        wallpaper_mode='fill',
        top=bar.Bar(
            [
                widget.GroupBox(
                    background=next(colors), disable_drag=True, **powerline
                ),
                widget.WindowName(background=next(colors), **powerline),
                # widget.Wttr(location={'Karmei Katif':'Home'}, format=1, background=next(colors), **powerline),
                widget.CurrentLayout(background=next(colors), **powerline),
                widget.KeyboardLayout(
                    configured_keyboards=['us', 'il lyx'],
                    display_map={'us': 'En', 'il lyx': 'He'},
                    background=next(colors),
                    **powerline
                ),
                widget.Volume(
                    background=next(colors),
                    **powerline,
                    mouse_callbacks={'Button3': lambda: qtile.cmd_spawn('pavucontrol')}
                ),
                widget.Systray(background=next(colors), **powerline),
                widget.GenPollText(
                    background=next(colors),
                    **powerline,
                    func=get_heb_date,
                    update_interval=600
                ),
                widget.Clock(
                    format='%Y-%m-%d %a %I:%M %p', background=next(colors), **powerline
                ),
                widget.GenPollText(
                    func=get_heater_state,
                    update_interval=5,
                    mouse_callbacks={'Button1': toggle_heater},
                    background=next(colors),
                    **powerline
                ),
                widget.TextBox(
                    mouse_callbacks={'Button1': lazy.restart()},
                    text='🧹',
                    background=next(colors),
                    **powerline
                ),
                widget.LaunchBar(
                    progs=[('🔒 ', 'systemctl suspend', 'suspend system')],
                    background=next(colors),
                ),
            ],
            30,
        ),
    ),
    Screen(
        wallpaper='~/.config/qtile/wallpaper.png',
        wallpaper_mode='fill',
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod, 'shift'],
        'Button1',
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod, 'shift'],
        'Button3',
        lazy.window.set_size_floating(),
        start=lazy.window.get_size(),
    ),
    Click([mod, 'shift'], 'Button2', lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),  # gitk
        Match(wm_class='makebranch'),  # gitk
        Match(wm_class='maketag'),  # gitk
        Match(wm_class='ssh-askpass'),  # ssh-askpass
        Match(wm_class='pypeek'),  # pypeek
        Match(title='branchdialog'),  # gitk
        Match(title='pinentry'),  # GPG key password entry
    ],
    border_width=0,
)
auto_fullscreen = True
focus_on_window_activation = 'smart'

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = 'LG3D'


@hook.subscribe.startup_once
def autostart():
    mouse = os.path.expanduser('~/.config/qtile/mouse.sh')
    subprocess.call([mouse])
    apps = os.path.expanduser('~/.config/qtile/apps.sh')
    subprocess.call([apps])
