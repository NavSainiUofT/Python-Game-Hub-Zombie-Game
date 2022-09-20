# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup_UI.ui'
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

class Ui_signup(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(442, 252)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.username_lbl_signup = QtGui.QLabel(self.centralwidget)
        self.username_lbl_signup.setObjectName(_fromUtf8("username_lbl_signup"))
        self.gridLayout.addWidget(self.username_lbl_signup, 0, 0, 1, 1)
        self.password_lbl_signup = QtGui.QLabel(self.centralwidget)
        self.password_lbl_signup.setObjectName(_fromUtf8("password_lbl_signup"))
        self.gridLayout.addWidget(self.password_lbl_signup, 2, 0, 1, 1)
        self.confirmpassword_lbl_signup = QtGui.QLabel(self.centralwidget)
        self.confirmpassword_lbl_signup.setObjectName(_fromUtf8("confirmpassword_lbl_signup"))
        self.gridLayout.addWidget(self.confirmpassword_lbl_signup, 3, 0, 1, 1)
        self.username_txtfield_signup = QtGui.QLineEdit(self.centralwidget)
        self.username_txtfield_signup.setObjectName(_fromUtf8("username_txtfield_signup"))
        self.gridLayout.addWidget(self.username_txtfield_signup, 0, 1, 1, 1)
        self.password_txtfield_signup = QtGui.QLineEdit(self.centralwidget)
        self.password_txtfield_signup.setObjectName(_fromUtf8("password_txtfield_signup"))
        self.gridLayout.addWidget(self.password_txtfield_signup, 2, 1, 1, 1)
        self.confirmpassword_txtfield_signup = QtGui.QLineEdit(self.centralwidget)
        self.confirmpassword_txtfield_signup.setObjectName(_fromUtf8("confirmpassword_txtfield_signup"))
        self.gridLayout.addWidget(self.confirmpassword_txtfield_signup, 3, 1, 1, 1)
        self.signup_btn_signup = QtGui.QPushButton(self.centralwidget)
        self.signup_btn_signup.setObjectName(_fromUtf8("signup_btn_signup"))
        self.gridLayout.addWidget(self.signup_btn_signup, 4, 0, 1, 2)
        self.cancel_btn_signup = QtGui.QPushButton(self.centralwidget)
        self.cancel_btn_signup.setObjectName(_fromUtf8("cancel_btn_signup"))
        self.gridLayout.addWidget(self.cancel_btn_signup, 5, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 442, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Sign Up", None))
        self.username_lbl_signup.setText(_translate("MainWindow", "Username", None))
        self.password_lbl_signup.setText(_translate("MainWindow", "Password", None))
        self.confirmpassword_lbl_signup.setText(_translate("MainWindow", "Confirm Password", None))
        self.signup_btn_signup.setText(_translate("MainWindow", "Signup", None))
        self.cancel_btn_signup.setText(_translate("MainWindow", "Cancel", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_signup()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

