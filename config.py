#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
import json
import pwd

# BASE_DIR = "/home/" + pwd.getpwuid(os.getuid())[0] + "/.config/healthywork"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# print(BASE_DIR)
CONFIG_FILE = BASE_DIR + "/config.json"
# print(CONFIG_FILE)
DEFALUT_CONFIG = {
    'label_stylesheet': "color: rgb(255, 0, 127);font: 30pt \"WenQuanYi Micro Hei Mono\";",
    'button_stylesheet': "background-color: rgba(182, 176, 171, 90);color: rgb(255, 0, 127);font: 30pt \"WenQuanYi Micro Hei Mono\";",
    'message': "喝杯水休息一下吧",
    'count': "        ",
    'time_work': "1800000",
    'time_rest': "300000",
    'wallpapers_dir': "./wallpapers",
    'music_dir': "./music",
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

        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, 'r') as file:
                config = file.read()
        else:
            with open(CONFIG_FILE, 'w') as file:
                config = json.dumps(DEFALUT_CONFIG)
                file.write(config)
                
        return json.loads(config)


CONFIG = Config()
