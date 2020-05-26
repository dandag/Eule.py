import win32gui
from utils import transform_coordinates
from sends import send_mouse, send_key
import macros
import os
import sys

try:
    wd = sys._MEIPASS
except AttributeError:
    wd = ''


def start_game(ahk, handle):
    x1, y1, x2, y2 = win32gui.GetWindowRect(handle)
    image_path = os.path.join(wd, f'./images/{x2 - x1}_{y2 - y1}/start_game.png')
    x1, y1 = transform_coordinates(handle, 160, 500)
    x2, y2 = transform_coordinates(handle, 320, 540)
    found = ahk.image_search(image_path, (x1, y1), (x2, y2), 30)
    if found:
        print('FOUND START GAME!')
        send_mouse(handle, 'LM', x1, y1)


def open_rift(ahk, handle, rift_type):
    x1, y1, x2, y2 = win32gui.GetWindowRect(handle)
    image_path = os.path.join(wd, f'./images/{x2 - x1}_{y2 - y1}/obelisk.png')
    x1, y1 = transform_coordinates(handle, 220, 30)
    x2, y2 = transform_coordinates(handle, 300, 100)
    found = ahk.image_search(image_path, (x1, y1), (x2, y2), 30)
    if found:
        print('FOUND OPEN RIFT!')
        if rift_type == 'grift':
            macros.open_gr()
        else:
            macros.open_rift()


def gamble(ahk, handle, item):
    x1, y1, x2, y2 = win32gui.GetWindowRect(handle)
    image_path = os.path.join(wd, f'./images/{x2 - x1}_{y2 - y1}/kadala.png')
    x1, y1 = transform_coordinates(handle, 220, 30)
    x2, y2 = transform_coordinates(handle, 300, 100)
    found = ahk.image_search(image_path, (x1, y1), (x2, y2), 30)
    if found:
        print('FOUND Kadala!')
        macros.gamble(item)


def accept_gr(ahk, handle):
    x1, y1, x2, y2 = win32gui.GetWindowRect(handle)
    image_path = os.path.join(wd, f'./images/{x2 - x1}_{y2 - y1}/keystone.png')
    x1, y1 = transform_coordinates(handle, 705, 755)
    x2, y2 = transform_coordinates(handle, 790, 815)
    accept = transform_coordinates(handle, 800, 900)
    found = ahk.image_search(image_path, (x1, y1), (x2, y2), 30)
    if found:
        print('FOUND accept GR')
        send_mouse(handle, 'LM', accept[0], accept[1])


def upgrade_gem(ahk, handle):
    x1, y1, x2, y2 = win32gui.GetWindowRect(handle)
    image_paths = [
        os.path.join(wd, f'./images/{x2 - x1}_{y2 - y1}/urhsi_upgrade_{i}.png')
        for i in range(1, 6)
    ]
    x1, y1 = transform_coordinates(handle, 200, 530)
    x2, y2 = transform_coordinates(handle, 335, 560)
    upgrade = transform_coordinates(handle, 280, 550)
    if ahk.image_search(image_paths[0], (x1, y1), (x2, y2), 30):  # 1 upgrade left
        send_mouse(handle, 'LM', upgrade[0], upgrade[1])
        send_key(handle, 't')
        print('Found 1 Upgrades Left!')
    elif ahk.image_search(image_paths[1], (x1, y1), (x2, y2), 30):  # 2 upgrades left
        send_mouse(handle, 'LM', upgrade[0], upgrade[1])
        send_key(handle, 't')
        print('Found 2 Upgrades Left!')
    elif ahk.image_search(image_paths[2], (x1, y1), (x2, y2), 30):  # 3 upgrade left
        send_mouse(handle, 'LM', upgrade[0], upgrade[1])
        send_key(handle, 't')
        print('Found 3 Upgrades Left!')
    elif ahk.image_search(image_paths[3], (x1, y1), (x2, y2), 30):  # 4 upgrade left
        send_mouse(handle, 'LM', upgrade[0], upgrade[1])
        print('Found 4 Upgrades Left!')
    elif ahk.image_search(image_paths[4], (x1, y1), (x2, y2), 30):  # 5 upgrade left
        send_mouse(handle, 'LM', upgrade[0], upgrade[1])
        print('Found 5 Upgrades Left!')