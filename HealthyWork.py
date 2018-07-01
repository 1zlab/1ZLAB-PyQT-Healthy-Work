#!/usr/bin/python3
# -*- coding: utf-8 -*-


from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QPainter, QPixmap, QGuiApplication
from PyQt5.QtCore import Qt, QTimer, QUrl, QDir, QCoreApplication
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from config import CONFIG
import sys
import os
import random


class HealthyWork(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.init_timer()
        self.player = QMediaPlayer(self)

    def init_ui(self):
        # TODO
        # set a window icon
        self.label_background = QLabel(self)
        self.button = QPushButton(self)
        self.button.setText('BACK TO WORK')
        self.button.setStyleSheet(CONFIG.BUTTON_STYLESHEET)
        self.button.resize(self.button.sizeHint())
        self.set_position(self.button, Label='Message')
        self.button.clicked.connect(self.start_work)
        self.button.hide()
        self.label_message = QLabel(self)
        self.label_count = QLabel(self)
        self.label_message.setText(CONFIG.MESSAGE)
        self.label_count.setText(CONFIG.COUNT)
        self.label_message.setStyleSheet(CONFIG.LABEL_STYLESHEET)
        self.label_count.setStyleSheet(CONFIG.LABEL_STYLESHEET)
        self.label_message.resize(self.label_message.sizeHint())
        self.label_count.resize(self.label_count.sizeHint())
        self.set_position(self.label_message, Label='Message')
        self.set_position(self.label_count, Label='Count')
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint |
                            Qt.WindowStaysOnTopHint | Qt.SubWindow)
        print('start healthywork ...')

    def init_timer(self):
        self.rest_time = int(CONFIG.TIME_REST)
        self.timer_work = QTimer()
        self.timer_rest = QTimer()
        self.timer_count = QTimer()
        self.timer_work.start(int(CONFIG.TIME_WORK))
        self.timer_work.timeout.connect(self.start_rest)
        self.timer_rest.timeout.connect(self.show_button)
        self.timer_count.timeout.connect(self.count_down)
        print('work timer start with %s millseconds' % CONFIG.TIME_WORK)

    def start_rest(self):
        self.with_music(CONFIG.WITH_MUSIC)
        self.show_background_picture()
        self.timer_work.stop()
        print('work timer stop')
        self.timer_rest.start(int(CONFIG.TIME_REST))
        self.rest_time = int(CONFIG.TIME_REST)
        print('rest timer start with %s millseconds' % CONFIG.TIME_REST)
        self.timer_count.start(1000)

    def start_work(self):
        self.button.hide()
        self.hide()
        self.timer_work.start(int(CONFIG.TIME_WORK))
        print('work timer start with %s millseconds' % CONFIG.TIME_WORK)
        self.player.stop()

    def count_down(self):
        def format_time(mseconds):
            m, s = divmod(mseconds / 1000, 60)
            h, m = divmod(m, 60)
            # print("%02d:%02d:%02d" % (h, m, s))
            return (h, m, s)
        self.label_count.setText("%02d:%02d:%02d" %
                                 format_time(self.rest_time - 1000))
        self.rest_time = self.rest_time - 1000

    def show_button(self):
        self.timer_rest.stop()
        print('rest timer stop')
        self.timer_count.stop()
        self.label_count.hide()
        self.label_message.hide()
        self.button.show()

    def with_music(self, is_music_on):
        # 随机播放音乐，单曲，无列表，只播放一次
        def media(url):
            return QMediaContent(
                QUrl.fromLocalFile(QDir.absolutePath(QDir(url))))
        if is_music_on and os.listdir(CONFIG.DIR_MUSIC):
            songs = [CONFIG.DIR_MUSIC + "/" +
                     song for song in os.listdir(CONFIG.DIR_MUSIC)]
            index = random.randint(0, len(songs) - 1)
            try:
                self.player.setMedia(media(songs[index]))
            except:
                pass
            self.player.play()

    def position(self, widget):
        # 计算label显示位置
        window_size = QApplication.desktop().screenGeometry()
        x = (window_size.width() - widget.width()) // 2
        y = (window_size.height() - widget.height()) // 2
        return (x, y, widget.width(), widget.height())

    def set_position(self, label, **kwargs):
        pos = self.position(label)
        if kwargs['Label'] == 'Message':
            label.setGeometry(pos[0], pos[1], pos[2], pos[3])
        else:
            label.setGeometry(pos[0], pos[1] + 80, pos[2], pos[3])

    def show_background_picture(self):
        # 随机一张壁纸全屏显示
        self.showFullScreen()

        if os.listdir(CONFIG.DIR_WALLPAPERS):
            window_size = QApplication.desktop().screenGeometry()
            self.label_background.setGeometry(
                0, 0, window_size.width(), window_size.height())
            wallpapers = [CONFIG.DIR_WALLPAPERS + "/" +
                          wallpaper for wallpaper in os.listdir(CONFIG.DIR_WALLPAPERS)]
            # print(wallpapers)
            index = random.randint(0, len(wallpapers) - 1)
            self.label_background.setPixmap(QPixmap(QDir.absolutePath(QDir(wallpapers[index])))
                                            .scaled(window_size.width(), window_size.height()))
        self.label_message.show()
        self.label_count.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    QCoreApplication.setApplicationName("HealthyWork")
    QGuiApplication.setApplicationDisplayName("HealthyWork")
    w = HealthyWork()
    sys.exit(app.exec_())
