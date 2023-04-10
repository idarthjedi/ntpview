#!/usr/bin/env python3
# Visual tool for review and interpretation of NTP Peer and Loop Stats logs.
# Copyright (C) 2023 Jediah Logiodice <jediah@logiodice.com> (iDarthJedi)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
from PyQt6 import QtCore, QtGui, QtWidgets
import src.ntpview
import sys
import os


def show_main_window(loadfile: str):
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = QtWidgets.QMainWindow()
    ui = src.ntpview.Ui_MainWindow()
    ui.setupUi(mainwindow, loadfile)
    mainwindow.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if os.path.isfile(sys.argv[1]):
            show_main_window(sys.argv[1])
        else:
            show_main_window(None)
    else:
        show_main_window(None)