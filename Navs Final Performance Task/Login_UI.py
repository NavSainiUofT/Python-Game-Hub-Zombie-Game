# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Nav_Login_UI.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(401, 285)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.Signup_btn = QtGui.QPushButton(self.centralwidget)
        self.Signup_btn.setObjectName(_fromUtf8("Signup_btn"))
        self.gridLayout_2.addWidget(self.Signup_btn, 4, 0, 1, 1)
        self.Cancel_btn = QtGui.QPushButton(self.centralwidget)
        self.Cancel_btn.setObjectName(_fromUtf8("Cancel_btn"))
        self.gridLayout_2.addWidget(self.Cancel_btn, 5, 0, 1, 1)
        self.Login_btn = QtGui.QPushButton(self.centralwidget)
        self.Login_btn.setObjectName(_fromUtf8("Login_btn"))
        self.gridLayout_2.addWidget(self.Login_btn, 3, 0, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.Password_lbl = QtGui.QLabel(self.centralwidget)
        self.Password_lbl.setObjectName(_fromUtf8("Password_lbl"))
        self.gridLayout.addWidget(self.Password_lbl, 1, 0, 1, 1)
        self.Username_txtfield = QtGui.QLineEdit(self.centralwidget)
        self.Username_txtfield.setObjectName(_fromUtf8("Username_txtfield"))
        self.gridLayout.addWidget(self.Username_txtfield, 0, 1, 1, 1)
        self.Username_lbl = QtGui.QLabel(self.centralwidget)
        self.Username_lbl.setObjectName(_fromUtf8("Username_lbl"))
        self.gridLayout.addWidget(self.Username_lbl, 0, 0, 1, 1)
        self.Password_txtfield = QtGui.QLineEdit(self.centralwidget)
        self.Password_txtfield.setEchoMode(QtGui.QLineEdit.Password)
        self.Password_txtfield.setObjectName(_fromUtf8("Password_txtfield"))
        self.gridLayout.addWidget(self.Password_txtfield, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.Score_btn = QtGui.QPushButton(self.centralwidget)
        self.Score_btn.setObjectName(_fromUtf8("Score_btn"))
        self.gridLayout_2.addWidget(self.Score_btn, 2, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 3, 0, 1, 1)
        self.Title_lbl = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(28)
        self.Title_lbl.setFont(font)
        self.Title_lbl.setMouseTracking(True)
        self.Title_lbl.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Title_lbl.setAutoFillBackground(False)
        self.Title_lbl.setFrameShape(QtGui.QFrame.Box)
        self.Title_lbl.setTextFormat(QtCore.Qt.AutoText)
        self.Title_lbl.setScaledContents(False)
        self.Title_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.Title_lbl.setObjectName(_fromUtf8("Title_lbl"))
        self.gridLayout_3.addWidget(self.Title_lbl, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 401, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Login", None))
        self.Signup_btn.setText(_translate("MainWindow", "Signup", None))
        self.Cancel_btn.setText(_translate("MainWindow", "Cancel", None))
        self.Login_btn.setText(_translate("MainWindow", "Login", None))
        self.Password_lbl.setText(_translate("MainWindow", "Password", None))
        self.Username_lbl.setText(_translate("MainWindow", "Username", None))
        self.Score_btn.setText(_translate("MainWindow", "Top 10 Players", None))
        self.Title_lbl.setText(_translate("MainWindow", "Game Center", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

