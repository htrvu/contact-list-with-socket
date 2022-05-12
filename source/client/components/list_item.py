from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFrame, QLabel, QLayout, QHBoxLayout, QSpacerItem

from client.components.round_img import RoundImage

class ListItem(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setGeometry(QtCore.QRect(10, 10, 531, 81))        
        self.setStyleSheet("QFrame {border-bottom: 1px solid #ccc;} QLabel {border: none;}")

        # Main layout of list item (horizontal)
        self.main_layout = QHBoxLayout(self)
        self.main_layout.setSizeConstraint(QLayout.SetFixedSize)
        self.main_layout.setContentsMargins(11, 0, 0, 8)

        # 1. ID
        self.id = QLabel(self)
        self.id.setMinimumSize(QtCore.QSize(64, 64))
        self.id.setMaximumSize(QtCore.QSize(64, 64))
        self.id.setAlignment(QtCore.Qt.AlignCenter)
        self.main_layout.addWidget(self.id)

        # Spacer between ID and Image
        spacerItem1 = QSpacerItem(46, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.main_layout.addItem(spacerItem1)

        # 2. Image
        self.img = RoundImage(64)
        self.main_layout.addWidget(self.img)

        # Spacer between Image and Name
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.main_layout.addItem(spacerItem2)

        # 3. Name
        self.name = QtWidgets.QLabel(self)
        self.name.setMinimumSize(QtCore.QSize(284, 0))
        self.name.setWordWrap(False)
        self.name.setAlignment(QtCore.Qt.AlignCenter)
        self.main_layout.addWidget(self.name)

        # 3. Stretch the main layout
        self.main_layout.setStretch(2, 8)
    

    def set_data(self, data):
        self.id.setText(data['id'])
        self.name.setText(data['name'])
        self.img.set_img(data['img'])
        # self.setWhatThis(data['id'])

    # def __init__(self, parent=None):
    #     super().__init__(parent)

    #     self.setGeometry(QtCore.QRect(10, 10, 531, 81))        
    #     self.setStyleSheet("QFrame {border-bottom: 1px solid #ccc;} QLabel {border: none;}")

    #     # Main layout of list item (horizontal)
    #     self.main_layout = QHBoxLayout(self)
    #     self.main_layout.setSizeConstraint(QLayout.SetFixedSize)
    #     self.main_layout.setContentsMargins(11, 0, 0, 8)


    #     # 1. ID
    #     self.id = QLabel(self)
    #     self.id.setMinimumSize(QtCore.QSize(64, 64))
    #     self.id.setMaximumSize(QtCore.QSize(64, 64))
    #     self.id.setAlignment(QtCore.Qt.AlignCenter)
    #     self.main_layout.addWidget(self.id)


    #     # Spacer between ID and Infor
    #     spacerItem = QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
    #     self.main_layout.addItem(spacerItem)


    #     # 2. Information wrapper
    #     self.infor_wrapper = QtWidgets.QWidget(self)
    #     self.infor_wrapper.setMinimumSize(QtCore.QSize(383, 71))

    #     ## 2.1. Horizontal layout of information wrapper
    #     self.infor_layout = QtWidgets.QHBoxLayout(self.infor_wrapper)
    #     self.infor_layout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
    #     self.infor_layout.setContentsMargins(0, 0, 0, 0)
    #     self.infor_layout.setSpacing(10)

    #     ## 2.2. Small image
    #     # self.infor_img = QtWidgets.QLabel(self.infor_wrapper)
    #     # self.infor_img.setMaximumSize(QtCore.QSize(64, 64))
    #     # self.infor_img.setText("")
    #     self.infor_img = RoundImage(64)
    #     # self.infor_img.setPixmap(QtGui.QPixmap("alexis_barnett_sm.png"))
    #     self.infor_layout.addWidget(self.infor_img)

    #     ## 2.3. Name
    #     self.name = QtWidgets.QLabel(self.infor_wrapper)
    #     self.name.setMinimumSize(QtCore.QSize(318, 0))
    #     self.name.setWordWrap(False)
    #     self.infor_layout.addWidget(self.name)

    #     ## 2.4. Stretch the layout of information
    #     self.infor_layout.setStretch(0, 1)
    #     self.main_layout.addWidget(self.infor_wrapper)


    #     # 3. Stretch the main layout
    #     self.main_layout.setStretch(2, 8)
