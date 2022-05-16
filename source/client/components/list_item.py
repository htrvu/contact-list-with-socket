from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QLabel, QLayout, QHBoxLayout, QSpacerItem

from client.components.my_frame import MyFrame
from client.components.round_label import RoundLabel
from common.utils import image_to_bytes

class ListItem(MyFrame):
    def __init__(self, data, parent=None):
        super().__init__(parent)

        self.setStyleSheet("QFrame {border-bottom: 1px solid #ccc;} QFrame:hover {background-color: #cff4ff;} QLabel {background-color: transparent; border: none;}")
        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.__set_layout()
        self.__set_data(data)


    def __set_layout(self):
        # Main layout of list item (horizontal)
        self.__main_layout = QHBoxLayout(self)
        self.__main_layout.setSizeConstraint(QLayout.SetFixedSize)
        self.__main_layout.setContentsMargins(11, 8, 0, 8)

        # 1. ID
        self.__id = QLabel(self)
        self.__id.setMinimumSize(QtCore.QSize(64, 64))
        self.__id.setMaximumSize(QtCore.QSize(64, 64))
        self.__id.setAlignment(QtCore.Qt.AlignCenter)
        self.__main_layout.addWidget(self.__id)

        # Spacer between ID and Image
        spacerItem1 = QSpacerItem(46, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.__main_layout.addItem(spacerItem1)

        # 2. Image
        self.__img = RoundLabel(64)
        self.__main_layout.addWidget(self.__img)

        # Spacer between Image and Name
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.__main_layout.addItem(spacerItem2)

        # 3. Name
        self.__name = QtWidgets.QLabel(self)
        self.__name.setMinimumSize(QtCore.QSize(284, 0))
        self.__name.setWordWrap(False)
        self.__name.setAlignment(QtCore.Qt.AlignCenter)
        self.__main_layout.addWidget(self.__name)

        # 3. Stretch the main layout
        self.__main_layout.setStretch(2, 8)
    

    def __set_data(self, data):
        self.setWhatsThis(data['id'])
        self.__id.setText(data['id'])
        self.__name.setText(data['name'])
        
        # (change here when use socket)
        byte_img = image_to_bytes(f'../data/small_image/{data["image"]}')

        self.__img.set_img_from_bytes(byte_img)
