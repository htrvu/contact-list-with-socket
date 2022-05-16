# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_connectdialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ConnectDialog(object):
    def setupUi(self, ConnectDialog):
        ConnectDialog.setObjectName("ConnectDialog")
        ConnectDialog.resize(400, 190)
        ConnectDialog.setStyleSheet("QDialog#ConnectDialog {\n"
"background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #acb6e5,  stop:1 #86fde8);\n"
"}")
        self.widget_2 = QtWidgets.QWidget(ConnectDialog)
        self.widget_2.setGeometry(QtCore.QRect(20, 10, 360, 171))
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.widget_3)
        self.label.setMaximumSize(QtCore.QSize(100, 100))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("assets/icons/contact.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.widget_4 = QtWidgets.QWidget(self.widget_3)
        self.widget_4.setStyleSheet("QLineEdit {\n"
"    padding: 8px;\n"
"    color: #333;\n"
"    border-radius: 10px;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"}")
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setSpacing(16)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.hostIP = QtWidgets.QLineEdit(self.widget_4)
        self.hostIP.setObjectName("hostIP")
        self.verticalLayout_2.addWidget(self.hostIP)
        self.hostPort = QtWidgets.QLineEdit(self.widget_4)
        self.hostPort.setObjectName("hostPort")
        self.verticalLayout_2.addWidget(self.hostPort)
        self.horizontalLayout_2.addWidget(self.widget_4)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget = QtWidgets.QWidget(self.widget_2)
        self.widget.setStyleSheet("QPushButton {\n"
"    background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #2d1299,  stop:1 #2980b9);\n"
"    padding: 4px 12px;\n"
"    font-size: 18px;\n"
"    color: #fff;\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #8e2de2,  stop:1 #4a00e0);\n"
"}")
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.connectBtn = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("SVN-Cookies")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.connectBtn.setFont(font)
        self.connectBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.connectBtn.setStyleSheet("")
        self.connectBtn.setObjectName("connectBtn")
        self.horizontalLayout.addWidget(self.connectBtn)
        self.exitBtn = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("SVN-Cookies")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.exitBtn.setFont(font)
        self.exitBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exitBtn.setStyleSheet("")
        self.exitBtn.setObjectName("exitBtn")
        self.horizontalLayout.addWidget(self.exitBtn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(ConnectDialog)
        QtCore.QMetaObject.connectSlotsByName(ConnectDialog)

    def retranslateUi(self, ConnectDialog):
        _translate = QtCore.QCoreApplication.translate
        ConnectDialog.setWindowTitle(_translate("ConnectDialog", "Dialog"))
        self.hostIP.setPlaceholderText(_translate("ConnectDialog", "Host IP"))
        self.hostPort.setPlaceholderText(_translate("ConnectDialog", "Host port"))
        self.connectBtn.setText(_translate("ConnectDialog", "Connect"))
        self.exitBtn.setText(_translate("ConnectDialog", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ConnectDialog = QtWidgets.QDialog()
    ui = Ui_ConnectDialog()
    ui.setupUi(ConnectDialog)
    ConnectDialog.show()
    sys.exit(app.exec_())

