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
import os

from PyQt6 import QtCore, QtGui, QtWidgets

# TODO: Add additional imports, and update above copyright details
from PyQt6.QtWidgets import QMainWindow, QFileDialog
from src.ntp_enums import FileType
from pathlib import Path
import datetime
import math
import juliandate

class Ui_MainWindow(QMainWindow):
    # TODO: Changed Object to QMainWindow

    # TODO: Adding __init__ for initialization
    def __init__(self):
        self._start_file = None
        QMainWindow.__init__(self, parent=None)

    # TODO: Changed setupUI to pass an optional filename
    def setupUi(self, MainWindow, start_file: str = None):
        self._start_file = start_file
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(997, 895)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tabPeerStats = QtWidgets.QWidget()
        self.tabPeerStats.setObjectName("tabPeerStats")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.tabPeerStats)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.listNTPLog = QtWidgets.QListWidget(parent=self.tabPeerStats)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listNTPLog.sizePolicy().hasHeightForWidth())
        self.listNTPLog.setSizePolicy(sizePolicy)
        self.listNTPLog.setMinimumSize(QtCore.QSize(0, 200))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.listNTPLog.setFont(font)
        self.listNTPLog.setSpacing(0)
        self.listNTPLog.setObjectName("listNTPLog")
        self.horizontalLayout_8.addWidget(self.listNTPLog)
        self.tabWidget.addTab(self.tabPeerStats, "")
        self.tabLoopStats = QtWidgets.QWidget()
        self.tabLoopStats.setObjectName("tabLoopStats")
        self.tabWidget.addTab(self.tabLoopStats, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.comboSearchItem = QtWidgets.QComboBox(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboSearchItem.sizePolicy().hasHeightForWidth())
        self.comboSearchItem.setSizePolicy(sizePolicy)
        self.comboSearchItem.setObjectName("comboSearchItem")
        self.comboSearchItem.addItem("")
        self.comboSearchItem.addItem("")
        self.comboSearchItem.addItem("")
        self.comboSearchItem.addItem("")
        self.comboSearchItem.addItem("")
        self.comboSearchItem.addItem("")
        self.horizontalLayout_5.addWidget(self.comboSearchItem)
        self.comboComparator = QtWidgets.QComboBox(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboComparator.sizePolicy().hasHeightForWidth())
        self.comboComparator.setSizePolicy(sizePolicy)
        self.comboComparator.setObjectName("comboComparator")
        self.comboComparator.addItem("")
        self.comboComparator.addItem("")
        self.comboComparator.addItem("")
        self.comboComparator.addItem("")
        self.comboComparator.addItem("")
        self.comboComparator.addItem("")
        self.horizontalLayout_5.addWidget(self.comboComparator)
        self.textSearchFirstItem = QtWidgets.QTextEdit(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textSearchFirstItem.sizePolicy().hasHeightForWidth())
        self.textSearchFirstItem.setSizePolicy(sizePolicy)
        self.textSearchFirstItem.setMinimumSize(QtCore.QSize(0, 26))
        self.textSearchFirstItem.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textSearchFirstItem.setObjectName("textSearchFirstItem")
        self.horizontalLayout_5.addWidget(self.textSearchFirstItem)
        self.comboConjunction = QtWidgets.QComboBox(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboConjunction.sizePolicy().hasHeightForWidth())
        self.comboConjunction.setSizePolicy(sizePolicy)
        self.comboConjunction.setObjectName("comboConjunction")
        self.comboConjunction.addItem("")
        self.horizontalLayout_5.addWidget(self.comboConjunction)
        self.textSearchSecondItem = QtWidgets.QTextEdit(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textSearchSecondItem.sizePolicy().hasHeightForWidth())
        self.textSearchSecondItem.setSizePolicy(sizePolicy)
        self.textSearchSecondItem.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textSearchSecondItem.setObjectName("textSearchSecondItem")
        self.horizontalLayout_5.addWidget(self.textSearchSecondItem)
        self.pushSearch = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushSearch.sizePolicy().hasHeightForWidth())
        self.pushSearch.setSizePolicy(sizePolicy)
        self.pushSearch.setObjectName("pushSearch")
        self.horizontalLayout_5.addWidget(self.pushSearch)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.textTime = QtWidgets.QTextEdit(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.textTime.sizePolicy().hasHeightForWidth())
        self.textTime.setSizePolicy(sizePolicy)
        self.textTime.setMinimumSize(QtCore.QSize(0, 0))
        self.textTime.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textTime.setObjectName("textTime")
        self.verticalLayout_4.addWidget(self.textTime)
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.textOffset = QtWidgets.QTextEdit(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.textOffset.sizePolicy().hasHeightForWidth())
        self.textOffset.setSizePolicy(sizePolicy)
        self.textOffset.setMinimumSize(QtCore.QSize(0, 0))
        self.textOffset.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textOffset.setObjectName("textOffset")
        self.verticalLayout_4.addWidget(self.textOffset)
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.textDispersion = QtWidgets.QTextEdit(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.textDispersion.sizePolicy().hasHeightForWidth())
        self.textDispersion.setSizePolicy(sizePolicy)
        self.textDispersion.setMinimumSize(QtCore.QSize(0, 0))
        self.textDispersion.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textDispersion.setObjectName("textDispersion")
        self.verticalLayout_4.addWidget(self.textDispersion)
        self.horizontalLayout_6.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.textPeerIP = QtWidgets.QTextEdit(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.textPeerIP.sizePolicy().hasHeightForWidth())
        self.textPeerIP.setSizePolicy(sizePolicy)
        self.textPeerIP.setMinimumSize(QtCore.QSize(0, 0))
        self.textPeerIP.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textPeerIP.setObjectName("textPeerIP")
        self.verticalLayout_5.addWidget(self.textPeerIP)
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_5.addWidget(self.label_6)
        self.textDelay = QtWidgets.QTextEdit(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textDelay.sizePolicy().hasHeightForWidth())
        self.textDelay.setSizePolicy(sizePolicy)
        self.textDelay.setMinimumSize(QtCore.QSize(0, 0))
        self.textDelay.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textDelay.setObjectName("textDelay")
        self.verticalLayout_5.addWidget(self.textDelay)
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_5.addWidget(self.label_8)
        self.textSkew = QtWidgets.QTextEdit(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textSkew.sizePolicy().hasHeightForWidth())
        self.textSkew.setSizePolicy(sizePolicy)
        self.textSkew.setMinimumSize(QtCore.QSize(0, 0))
        self.textSkew.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textSkew.setObjectName("textSkew")
        self.verticalLayout_5.addWidget(self.textSkew)
        self.horizontalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_6.addWidget(self.label_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_17 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_17.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_2.addWidget(self.label_17)
        self.labelFirstByte = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelFirstByte.setMinimumSize(QtCore.QSize(0, 0))
        self.labelFirstByte.setObjectName("labelFirstByte")
        self.horizontalLayout_2.addWidget(self.labelFirstByte)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_19 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_19.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_3.addWidget(self.label_19)
        self.labelSecondByte = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelSecondByte.setObjectName("labelSecondByte")
        self.horizontalLayout_3.addWidget(self.labelSecondByte)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_20 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_20.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_4.addWidget(self.label_20)
        self.labelTFByte = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelTFByte.setObjectName("labelTFByte")
        self.horizontalLayout_4.addWidget(self.labelTFByte)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout_6.addLayout(self.verticalLayout_2)
        self.horizontalLayout_7.addLayout(self.verticalLayout_6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.verticalLayout_3.setStretch(0, 2)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 997, 24))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(parent=self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Help = QtWidgets.QMenu(parent=self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_Open = QtGui.QAction(parent=MainWindow)
        self.action_Open.setObjectName("action_Open")
        self.action_About = QtGui.QAction(parent=MainWindow)
        self.action_About.setObjectName("action_About")
        self.action_Close = QtGui.QAction(parent=MainWindow)
        self.action_Close.setObjectName("action_Close")
        self.menu_File.addAction(self.action_Open)
        self.menu_File.addAction(self.action_Close)
        self.menu_Help.addAction(self.action_About)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.action_Close.triggered.connect(MainWindow.close)  # type: ignore

        # TODO: Add additional code into generated file
        self.action_Open.triggered.connect(self.open_logfile)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.listNTPLog.itemSelectionChanged.connect(self.load_selecteditem)

        # self.listNTPLog.itemClicked.connect(self.load_record)
        if self._start_file:
            self.load_file()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NTP Veiwer & Translator"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabPeerStats), _translate("MainWindow", "Peer Stats"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabLoopStats), _translate("MainWindow", "Loop Stats"))
        self.comboSearchItem.setItemText(0, _translate("MainWindow", "Time"))
        self.comboSearchItem.setItemText(1, _translate("MainWindow", "Peer IP"))
        self.comboSearchItem.setItemText(2, _translate("MainWindow", "Offset"))
        self.comboSearchItem.setItemText(3, _translate("MainWindow", "Delay"))
        self.comboSearchItem.setItemText(4, _translate("MainWindow", "Dispersion"))
        self.comboSearchItem.setItemText(5, _translate("MainWindow", "Skew"))
        self.comboComparator.setItemText(0, _translate("MainWindow", "eq"))
        self.comboComparator.setItemText(1, _translate("MainWindow", "gt"))
        self.comboComparator.setItemText(2, _translate("MainWindow", "ge"))
        self.comboComparator.setItemText(3, _translate("MainWindow", "lt"))
        self.comboComparator.setItemText(4, _translate("MainWindow", "le"))
        self.comboComparator.setItemText(5, _translate("MainWindow", "between"))
        self.comboConjunction.setItemText(0, _translate("MainWindow", "and"))
        self.pushSearch.setText(_translate("MainWindow", "&Search"))
        self.label.setText(_translate("MainWindow", "Time"))
        self.label_5.setText(_translate("MainWindow", "Offset"))
        self.label_7.setText(_translate("MainWindow", "Dispersion"))
        self.label_2.setText(_translate("MainWindow", "Peer IP"))
        self.label_6.setText(_translate("MainWindow", "Delay"))
        self.label_8.setText(_translate("MainWindow", "Skew"))
        self.label_3.setText(_translate("MainWindow", "Peer Status:"))
        self.label_17.setText(_translate("MainWindow", "First Byte:"))
        self.labelFirstByte.setText(_translate("MainWindow", "08\tbcst\tbroadcast association"))
        self.label_19.setText(_translate("MainWindow", "Second Byte:"))
        self.labelSecondByte.setText(
            _translate("MainWindow", "01\tsel_falsetick\tx\tdiscarded by intersection algorithm"))
        self.label_20.setText(_translate("MainWindow", "Third & Fourth Byte:"))
        self.labelTFByte.setText(_translate("MainWindow", "01\tmobilize association mobilized"))
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.menu_Help.setTitle(_translate("MainWindow", "&Help"))
        self.action_Open.setText(_translate("MainWindow", "&Open"))
        self.action_About.setText(_translate("MainWindow", "&About!"))
        self.action_Close.setText(_translate("MainWindow", "&Close"))

    # TODO: Add all extra methods below
    def getfile(self, title: str, start_dir: str) -> str:
        return QFileDialog.getOpenFileName(self, caption=title, directory=start_dir)

    def load_selecteditem(self):
        self.load_record(self.listNTPLog.selectedItems())

    def clear_form(self):
        self.listNTPLog.clear()
        self.statusbar.showMessage("")
        self.textTime.setText("")
        self.textSkew.setText("")
        self.textDelay.setText("")
        self.textOffset.setText("")
        self.textDispersion.setText("")
        self.textPeerIP.setText("")

    def display_form(self, record: tuple):
        date = juliandate.to_gregorian(float(record[0]) + 2400001)
        self.statusbar.showMessage(f"\tLog loaded for date: {date[1]}/{date[2]}/{date[0]}")

        self.textTime.setText(str(datetime.timedelta(seconds=float(record[1]))))

        self.textPeerIP.setText(str(record[2]))
        self.label_3.setText(f"Peer Status: {str(record[3])}")
        self.textOffset.setText(str(record[4]))
        self.textDelay.setText(str(record[5]))
        self.textDispersion.setText(str(record[6]))
        self.textSkew.setText(str(record[7]))

    def load_record(self, selected_item):
        if len(selected_item) <= 0:
            self.clear_form()
            return

        items = selected_item[0].text().split(" ")
        # ['60042', '892.170', '132.163.96.2', '169a', '-0.000374539', '0.044791018', '0.016764463', '0.000544924\n']

        self.display_form(items)


    def load_file(self):
        self.clear_form()
        if self._start_file:
            ft = self.get_filetype(self._start_file)
            if FileType.PEERSTAT == ft:
                # open file loop through it and add each line to the listbox.
                with open(str(self._start_file)) as peerstats:
                    for line in peerstats:
                        self.listNTPLog.addItem(line)

                self.listNTPLog.item(0).setSelected(True)

            elif FileType.LOOPSTAT == ft:
                pass
            else:
                pass #ignore

        else:
            self.listNTPLog.clear()

    def get_filetype(self, filename: str) -> FileType:
        p = Path(filename)
        if "peer" in p.parts[-1]:
            return FileType.PEERSTAT
        if "loop" in p.parts[-1]:
            raise Exception("Loop Stat not Implemented")
            return FileType.LOOPSTAT

    def open_logfile(self):
        filename = self.getfile("Select Pool or Loop Stats File", os.getcwd())[0]
        self._start_file = None if filename == '' else filename
        self.load_file()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
