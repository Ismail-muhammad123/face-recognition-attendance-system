# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/checkin.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_checkinWindow(object):
    def setupUi(self, checkinWindow):
        checkinWindow.setObjectName("checkinWindow")
        checkinWindow.resize(800, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(checkinWindow.sizePolicy().hasHeightForWidth())
        checkinWindow.setSizePolicy(sizePolicy)
        checkinWindow.setMinimumSize(QtCore.QSize(800, 300))
        self.centralwidget = QtWidgets.QWidget(checkinWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.feedLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.feedLabel.sizePolicy().hasHeightForWidth())
        self.feedLabel.setSizePolicy(sizePolicy)
        self.feedLabel.setMinimumSize(QtCore.QSize(500, 300))
        self.feedLabel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.feedLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.feedLabel.setObjectName("feedLabel")
        self.verticalLayout.addWidget(self.feedLabel)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.scanningLabel = QtWidgets.QLabel(self.centralwidget)
        self.scanningLabel.setStyleSheet("font: italic 14pt \"Arial\";\n"
"color: blue;")
        self.scanningLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.scanningLabel.setObjectName("scanningLabel")
        self.verticalLayout.addWidget(self.scanningLabel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
"color: rgb(0, 85, 255);")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.nameLabel = QtWidgets.QLabel(self.centralwidget)
        self.nameLabel.setObjectName("nameLabel")
        self.horizontalLayout.addWidget(self.nameLabel)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.statusLabel = QtWidgets.QLabel(self.centralwidget)
        self.statusLabel.setText("")
        self.statusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statusLabel.setObjectName("statusLabel")
        self.verticalLayout.addWidget(self.statusLabel)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        checkinWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(checkinWindow)
        self.statusbar.setObjectName("statusbar")
        checkinWindow.setStatusBar(self.statusbar)

        self.retranslateUi(checkinWindow)
        QtCore.QMetaObject.connectSlotsByName(checkinWindow)

    def retranslateUi(self, checkinWindow):
        _translate = QtCore.QCoreApplication.translate
        checkinWindow.setWindowTitle(_translate("checkinWindow", "MainWindow"))
        self.feedLabel.setText(_translate("checkinWindow", "TextLabel"))
        self.scanningLabel.setText(_translate("checkinWindow", "scanning..."))
        self.label_4.setText(_translate("checkinWindow", "NAME: "))
        self.nameLabel.setText(_translate("checkinWindow", "scanning..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    checkinWindow = QtWidgets.QMainWindow()
    ui = Ui_checkinWindow()
    ui.setupUi(checkinWindow)
    checkinWindow.show()
    sys.exit(app.exec_())
