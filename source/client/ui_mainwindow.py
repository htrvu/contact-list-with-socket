# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QPushButton {\n"
"    outline: none !important; \n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 16px;\n"
"    color: #333;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.stackedWidget.setStyleSheet("QStackedWidget QWidget#homePage, QStackedWidget QWidget#listPage, QStackedWidget QWidget#detailPage, QStackedWidget QWidget#aboutPage {\n"
"background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #acb6e5,  stop:1 #86fde8);\n"
"}")
        self.stackedWidget.setObjectName("stackedWidget")
        self.homePage = QtWidgets.QWidget()
        self.homePage.setStyleSheet("")
        self.homePage.setObjectName("homePage")
        self.label = QtWidgets.QLabel(self.homePage)
        self.label.setGeometry(QtCore.QRect(0, 80, 800, 80))
        font = QtGui.QFont()
        font.setFamily("SVN-Cookies")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("font-size: 48px;\n"
"color: #2d1299;\n"
"font-weight: bold;")
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(self.homePage)
        self.widget.setGeometry(QtCore.QRect(290, 250, 220, 240))
        self.widget.setStyleSheet("QPushButton {\n"
"    background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #2d1299,  stop:1 #2980b9);\n"
"    padding: 10px 8px 12px 8px;\n"
"    font-size: 24px;\n"
"    color: #fff;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #8e2de2,  stop:1 #4a00e0);\n"
"}")
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(16)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.contactListBtn = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("SVN-Cookies")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.contactListBtn.setFont(font)
        self.contactListBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.contactListBtn.setStyleSheet("")
        self.contactListBtn.setObjectName("contactListBtn")
        self.verticalLayout_2.addWidget(self.contactListBtn)
        self.aboutUsBtn = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("SVN-Cookies")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.aboutUsBtn.setFont(font)
        self.aboutUsBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.aboutUsBtn.setObjectName("aboutUsBtn")
        self.verticalLayout_2.addWidget(self.aboutUsBtn)
        self.exitBtn = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("SVN-Cookies")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.exitBtn.setFont(font)
        self.exitBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exitBtn.setObjectName("exitBtn")
        self.verticalLayout_2.addWidget(self.exitBtn)
        self.label_11 = QtWidgets.QLabel(self.homePage)
        self.label_11.setGeometry(QtCore.QRect(370, 160, 64, 64))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("assets/icons/contact.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.stackedWidget.addWidget(self.homePage)
        self.listPage = QtWidgets.QWidget()
        self.listPage.setObjectName("listPage")
        self.label_2 = QtWidgets.QLabel(self.listPage)
        self.label_2.setGeometry(QtCore.QRect(0, 30, 800, 51))
        font = QtGui.QFont()
        font.setFamily("SVN-Cookies")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font-size: 30px;\n"
"color: #2d1299;\n"
"font-weight: bold;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.listWidget = QtWidgets.QWidget(self.listPage)
        self.listWidget.setGeometry(QtCore.QRect(100, 99, 600, 420))
        self.listWidget.setStyleSheet("QWidget#listWidget {\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QWidget {\n"
"    background-color: #fff;\n"
"}")
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.listWidget)
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.listWidget)
        self.frame.setStyleSheet("font-size: 16px;\n"
"color: #333;\n"
"font-weight: bold;")
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 12, 7)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout.addWidget(self.label_9)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 3)
        self.verticalLayout.addWidget(self.frame)
        self.listScrollWrapper = QtWidgets.QScrollArea(self.listWidget)
        self.listScrollWrapper.setStyleSheet("QScrollArea {\n"
"    border: none;\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"QScrollBar:vertical {              \n"
"    /*border: 1px solid #999999;*/\n"
"    border-radius: 5px;\n"
"    background: transparent;\n"
"    width: 18px;    \n"
"    margin: 8px 0px 0px 8px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    /*cff4ff*/\n"
"    background: #86fde8;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    height: 0 px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}")
        self.listScrollWrapper.setWidgetResizable(True)
        self.listScrollWrapper.setObjectName("listScrollWrapper")
        self.listScrollArea = QtWidgets.QWidget()
        self.listScrollArea.setGeometry(QtCore.QRect(0, 0, 570, 364))
        self.listScrollArea.setObjectName("listScrollArea")
        self.listScrollWrapper.setWidget(self.listScrollArea)
        self.verticalLayout.addWidget(self.listScrollWrapper)
        self.label_10 = QtWidgets.QLabel(self.listPage)
        self.label_10.setGeometry(QtCore.QRect(115, 140, 570, 1))
        self.label_10.setStyleSheet("border-top: 2px solid #333;")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.listBackBtn = QtWidgets.QPushButton(self.listPage)
        self.listBackBtn.setGeometry(QtCore.QRect(300, 535, 200, 28))
        font = QtGui.QFont()
        font.setFamily("SVN-Cookies")
        font.setPointSize(-1)
        self.listBackBtn.setFont(font)
        self.listBackBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.listBackBtn.setStyleSheet("QPushButton {\n"
"font-size: 20px;\n"
"color: #2d1299;\n"
"background-color: none;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: #8e2de2;\n"
"}")
        self.listBackBtn.setObjectName("listBackBtn")
        self.stackedWidget.addWidget(self.listPage)
        self.detailPage = QtWidgets.QWidget()
        self.detailPage.setStyleSheet("")
        self.detailPage.setObjectName("detailPage")
        self.detailBackBtn = QtWidgets.QPushButton(self.detailPage)
        self.detailBackBtn.setGeometry(QtCore.QRect(289, 532, 221, 28))
        font = QtGui.QFont()
        font.setFamily("SVN-Cookies")
        font.setPointSize(-1)
        self.detailBackBtn.setFont(font)
        self.detailBackBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.detailBackBtn.setStyleSheet("QPushButton {\n"
"font-size: 20px;\n"
"color: #2d1299;\n"
"background-color: none;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: #8e2de2;\n"
"}")
        self.detailBackBtn.setObjectName("detailBackBtn")
        self.detailWrapper = QtWidgets.QWidget(self.detailPage)
        self.detailWrapper.setGeometry(QtCore.QRect(120, 60, 560, 461))
        self.detailWrapper.setStyleSheet("QWidget#detailWrapper {\n"
"    background-color: #fff;\n"
"    border-radius: 15px;\n"
"}")
        self.detailWrapper.setObjectName("detailWrapper")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.detailWrapper)
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_4.setContentsMargins(11, 16, 11, 12)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_4 = QtWidgets.QWidget(self.detailWrapper)
        self.widget_4.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.detailImg = QtWidgets.QLabel(self.widget_4)
        self.detailImg.setMinimumSize(QtCore.QSize(250, 250))
        self.detailImg.setMaximumSize(QtCore.QSize(250, 250))
        self.detailImg.setText("")
        self.detailImg.setObjectName("detailImg")
        self.horizontalLayout_2.addWidget(self.detailImg)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_4.addWidget(self.widget_4)
        self.widget_8 = QtWidgets.QWidget(self.detailWrapper)
        self.widget_8.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_8.setMaximumSize(QtCore.QSize(16777215, 30))
        self.widget_8.setStyleSheet("font-size: 16px;")
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.label_13 = QtWidgets.QLabel(self.widget_8)
        self.label_13.setStyleSheet("font-weight: bold;")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_6.addWidget(self.label_13)
        self.detailID = QtWidgets.QLabel(self.widget_8)
        self.detailID.setAlignment(QtCore.Qt.AlignCenter)
        self.detailID.setObjectName("detailID")
        self.horizontalLayout_6.addWidget(self.detailID)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.verticalLayout_4.addWidget(self.widget_8)
        self.detailName = QtWidgets.QLabel(self.detailWrapper)
        self.detailName.setMinimumSize(QtCore.QSize(0, 0))
        self.detailName.setMaximumSize(QtCore.QSize(16777215, 35))
        self.detailName.setStyleSheet("font-size: 28px;\n"
"color: #2d1299;\n"
"font-weight: bold;")
        self.detailName.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.detailName.setObjectName("detailName")
        self.verticalLayout_4.addWidget(self.detailName)
        self.widget_9 = QtWidgets.QWidget(self.detailWrapper)
        self.widget_9.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_9.setMaximumSize(QtCore.QSize(16777215, 70))
        self.widget_9.setObjectName("widget_9")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_9)
        self.verticalLayout_5.setContentsMargins(-1, 8, -1, 8)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget_10 = QtWidgets.QWidget(self.widget_9)
        self.widget_10.setObjectName("widget_10")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_10)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.label_14 = QtWidgets.QLabel(self.widget_10)
        self.label_14.setMaximumSize(QtCore.QSize(24, 24))
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap("assets/icons/phone.png"))
        self.label_14.setScaledContents(True)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_7.addWidget(self.label_14)
        self.detailPhone = QtWidgets.QLabel(self.widget_10)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.detailPhone.setFont(font)
        self.detailPhone.setAlignment(QtCore.Qt.AlignCenter)
        self.detailPhone.setObjectName("detailPhone")
        self.horizontalLayout_7.addWidget(self.detailPhone)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.verticalLayout_5.addWidget(self.widget_10)
        self.widget_11 = QtWidgets.QWidget(self.widget_9)
        self.widget_11.setObjectName("widget_11")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_11)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem6)
        self.label_18 = QtWidgets.QLabel(self.widget_11)
        self.label_18.setMaximumSize(QtCore.QSize(24, 24))
        self.label_18.setText("")
        self.label_18.setPixmap(QtGui.QPixmap("assets/icons/email.png"))
        self.label_18.setScaledContents(True)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_8.addWidget(self.label_18)
        self.detailEmail = QtWidgets.QLabel(self.widget_11)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.detailEmail.setFont(font)
        self.detailEmail.setAlignment(QtCore.Qt.AlignCenter)
        self.detailEmail.setObjectName("detailEmail")
        self.horizontalLayout_8.addWidget(self.detailEmail)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem7)
        self.verticalLayout_5.addWidget(self.widget_11)
        self.verticalLayout_4.addWidget(self.widget_9)
        self.widget_3 = QtWidgets.QWidget(self.detailWrapper)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.detailBio = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(-1)
        self.detailBio.setFont(font)
        self.detailBio.setStyleSheet("color: #707070;")
        self.detailBio.setAlignment(QtCore.Qt.AlignCenter)
        self.detailBio.setWordWrap(True)
        self.detailBio.setObjectName("detailBio")
        self.horizontalLayout_3.addWidget(self.detailBio)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.verticalLayout_4.addWidget(self.widget_3)
        self.stackedWidget.addWidget(self.detailPage)
        self.aboutPage = QtWidgets.QWidget()
        self.aboutPage.setObjectName("aboutPage")
        self.label_4 = QtWidgets.QLabel(self.aboutPage)
        self.label_4.setGeometry(QtCore.QRect(0, 30, 800, 51))
        font = QtGui.QFont()
        font.setFamily("SVN-Cookies")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font-size: 30px;\n"
"color: #2d1299;\n"
"font-weight: bold;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.widget_2 = QtWidgets.QWidget(self.aboutPage)
        self.widget_2.setGeometry(QtCore.QRect(170, 130, 120, 80))
        self.widget_2.setStyleSheet("QWidget#listWidget {\n"
"    background-color: #fff;\n"
"    border-radius: 15px;\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.aboutBackBtn = QtWidgets.QPushButton(self.aboutPage)
        self.aboutBackBtn.setGeometry(QtCore.QRect(300, 535, 200, 28))
        font = QtGui.QFont()
        font.setFamily("SVN-Cookies")
        font.setPointSize(-1)
        self.aboutBackBtn.setFont(font)
        self.aboutBackBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.aboutBackBtn.setStyleSheet("QPushButton {\n"
"font-size: 20px;\n"
"color: #2d1299;\n"
"background-color: none;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: #8e2de2;\n"
"}")
        self.aboutBackBtn.setObjectName("aboutBackBtn")
        self.stackedWidget.addWidget(self.aboutPage)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Contact List"))
        self.label.setText(_translate("MainWindow", "Digital Contact List"))
        self.contactListBtn.setText(_translate("MainWindow", "Contact List"))
        self.aboutUsBtn.setText(_translate("MainWindow", "About Us"))
        self.exitBtn.setText(_translate("MainWindow", "Exit"))
        self.label_2.setText(_translate("MainWindow", "Contact List"))
        self.label_8.setText(_translate("MainWindow", "ID"))
        self.label_3.setText(_translate("MainWindow", "Image"))
        self.label_9.setText(_translate("MainWindow", "Name"))
        self.listBackBtn.setText(_translate("MainWindow", "Back to Home"))
        self.detailBackBtn.setText(_translate("MainWindow", "Back to Contact List"))
        self.label_13.setText(_translate("MainWindow", "ID:"))
        self.detailID.setText(_translate("MainWindow", "C1"))
        self.detailName.setText(_translate("MainWindow", "Alexandir gaga ehehehehe"))
        self.detailPhone.setText(_translate("MainWindow", "01234567890"))
        self.detailEmail.setText(_translate("MainWindow", "aaaaaaacdef@gmail.com"))
        self.detailBio.setText(_translate("MainWindow", "TextLabel"))
        self.label_4.setText(_translate("MainWindow", "About Us"))
        self.aboutBackBtn.setText(_translate("MainWindow", "Back to Home"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
