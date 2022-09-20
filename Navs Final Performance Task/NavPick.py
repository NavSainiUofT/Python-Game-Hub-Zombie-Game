# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NavPick.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Game_Pick(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(639, 316)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Candara"))
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_3.addWidget(self.label, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 0, 1, 1, 1)
        self.back_btn = QtGui.QPushButton(self.centralwidget)
        self.back_btn.setObjectName(_fromUtf8("back_btn"))
        self.gridLayout.addWidget(self.back_btn, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.gridLayout_8 = QtGui.QGridLayout()
        self.gridLayout_8.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.gridLayout_8.setVerticalSpacing(2)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_8.addWidget(self.label_2, 0, 0, 1, 1)
        self.snake_scorelcd = QtGui.QLCDNumber(self.centralwidget)
        self.snake_scorelcd.setObjectName(_fromUtf8("snake_scorelcd"))
        self.gridLayout_8.addWidget(self.snake_scorelcd, 0, 1, 1, 1)
        self.zombie_scorelcd = QtGui.QLCDNumber(self.centralwidget)
        self.zombie_scorelcd.setObjectName(_fromUtf8("zombie_scorelcd"))
        self.gridLayout_8.addWidget(self.zombie_scorelcd, 0, 3, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_8.addWidget(self.label_3, 0, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_8, 3, 0, 1, 1)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.snake_btn = QtGui.QPushButton(self.centralwidget)
        self.snake_btn.setMinimumSize(QtCore.QSize(0, 150))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roman"))
        font.setPointSize(28)
        self.snake_btn.setFont(font)
        self.snake_btn.setObjectName(_fromUtf8("snake_btn"))
        self.gridLayout_4.addWidget(self.snake_btn, 0, 0, 1, 1)
        self.zombie_btn = QtGui.QPushButton(self.centralwidget)
        self.zombie_btn.setMinimumSize(QtCore.QSize(0, 150))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roman"))
        font.setPointSize(28)
        self.zombie_btn.setFont(font)
        self.zombie_btn.setObjectName(_fromUtf8("zombie_btn"))
        self.gridLayout_4.addWidget(self.zombie_btn, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_4, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 639, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Game Picker", None))
        self.label.setText(_translate("MainWindow", "CHOOSE YOUR GAME!", None))
        self.back_btn.setText(_translate("MainWindow", "Log Out", None))
        self.label_2.setText(_translate("MainWindow", "High Score:", None))
        self.label_3.setText(_translate("MainWindow", "High Score:", None))
        self.snake_btn.setText(_translate("MainWindow", "Snake Game", None))
        self.zombie_btn.setText(_translate("MainWindow", "The Running Dead", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

