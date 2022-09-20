# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Nav_Top10_UI.ui'
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

class Ui_Top_10_Scorers(object):
    def setupUi(self, Top_10_Scorers):
        Top_10_Scorers.setObjectName(_fromUtf8("Top_10_Scorers"))
        Top_10_Scorers.resize(656, 332)
        Top_10_Scorers.setMinimumSize(QtCore.QSize(656, 332))
        Top_10_Scorers.setMaximumSize(QtCore.QSize(656, 332))
        self.centralwidget = QtGui.QWidget(Top_10_Scorers)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.Snake_Table = QtGui.QTableWidget(self.centralwidget)
        self.Snake_Table.setObjectName(_fromUtf8("Snake_Table"))
        self.Snake_Table.setColumnCount(0)
        self.Snake_Table.setRowCount(0)
        self.gridLayout.addWidget(self.Snake_Table, 1, 0, 1, 1)
        self.Snake_lbl = QtGui.QLabel(self.centralwidget)
        self.Snake_lbl.setObjectName(_fromUtf8("Snake_lbl"))
        self.gridLayout.addWidget(self.Snake_lbl, 0, 0, 1, 1)
        self.Zombie_lbl = QtGui.QLabel(self.centralwidget)
        self.Zombie_lbl.setObjectName(_fromUtf8("Zombie_lbl"))
        self.gridLayout.addWidget(self.Zombie_lbl, 0, 1, 1, 1)
        self.Zombie_Table = QtGui.QTableWidget(self.centralwidget)
        self.Zombie_Table.setObjectName(_fromUtf8("Zombie_Table"))
        self.Zombie_Table.setColumnCount(0)
        self.Zombie_Table.setRowCount(0)
        self.gridLayout.addWidget(self.Zombie_Table, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.Close_btn_topscorers = QtGui.QPushButton(self.centralwidget)
        self.Close_btn_topscorers.setObjectName(_fromUtf8("Close_btn_topscorers"))
        self.gridLayout_2.addWidget(self.Close_btn_topscorers, 1, 0, 1, 1)
        Top_10_Scorers.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Top_10_Scorers)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 656, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Top_10_Scorers.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Top_10_Scorers)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Top_10_Scorers.setStatusBar(self.statusbar)

        self.retranslateUi(Top_10_Scorers)
        QtCore.QMetaObject.connectSlotsByName(Top_10_Scorers)

    def retranslateUi(self, Top_10_Scorers):
        Top_10_Scorers.setWindowTitle(_translate("Top_10_Scorers", "Top 10", None))
        self.Snake_lbl.setText(_translate("Top_10_Scorers", "Snake Game", None))
        self.Zombie_lbl.setText(_translate("Top_10_Scorers", "Zombie Game", None))
        self.Close_btn_topscorers.setText(_translate("Top_10_Scorers", "Close", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Top_10_Scorers = QtGui.QMainWindow()
    ui = Ui_Top_10_Scorers()
    ui.setupUi(Top_10_Scorers)
    Top_10_Scorers.show()
    sys.exit(app.exec_())

