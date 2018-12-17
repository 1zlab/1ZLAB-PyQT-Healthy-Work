#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
import json 
import pwd

BASE_DIR = os.path.dirname("/home/%s/" % pwd.getpwuid(os.getuid())[0])

CONFIG_FILE_PATH = os.path.join(BASE_DIR, ".config/healthywork.json")
# print(CONFIG_FILE_PATH)

WALLPAPER_DIR = os.path.join(BASE_DIR, "Pictures")
MUSIC_DIR = os.path.join(BASE_DIR, "Music")

DEFALUT_CONFIG = {
    'label_stylesheet': "color: rgb(255, 0, 127);font: 30pt \"WenQuanYi Micro Hei Mono\";",
    'button_stylesheet': "background-color: rgba(182, 176, 171, 90);color: rgb(255, 0, 127);font: 30pt \"WenQuanYi Micro Hei Mono\";",
    'message': "喝杯水休息一下吧",
    'count': " "*16,
    'time_work': "2400000",
    'time_rest': "600000",
    'wallpapers_dir': WALLPAPER_DIR,
    'music_dir': MUSIC_DIR,
    'with_music': "1"
}


class Config():
    def __init__(self, *args, **kwargs):
        self.LABEL_STYLESHEET = self.read_config()['label_stylesheet']
        self.BUTTON_STYLESHEET = self.read_config()['button_stylesheet']
        self.MESSAGE = self.read_config()['message']
        self.COUNT = self.read_config()['count']
        self.TIME_WORK = self.read_config()['time_work']
        self.TIME_REST = self.read_config()['time_rest']
        self.DIR_WALLPAPERS = self.read_config()['wallpapers_dir']
        self.DIR_MUSIC = self.read_config()['music_dir']
        self.WITH_MUSIC = int(self.read_config()['with_music'])

    def read_config(self):

        if os.path.exists(CONFIG_FILE_PATH):
            with open(CONFIG_FILE_PATH, 'r') as file:
                config = file.read()
        else:
            with open(CONFIG_FILE_PATH, 'w') as file:
                config = json.dumps(DEFALUT_CONFIG)
                file.write(config)

        return json.loads(config)


CONFIG = Config()
