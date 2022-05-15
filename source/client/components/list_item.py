from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFrame, QLabel, QLayout, QHBoxLayout, QSpacerItem

from client.components.my_frame import MyFrame
from client.components.round_img import RoundImage
from common.utils import image_to_bytes
class ListItem(MyFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setGeometry(QtCore.QRect(10, 10, 531, 81))         # cff4ff
        self.setStyleSheet("QFrame {border-bottom: 1px solid #ccc;} QFrame:hover {background-color: #cff4ff;} QLabel {background-color: transparent; border: none;}")

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
        self.__img = RoundImage(64)
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
    

    def set_data(self, data):
        self.setWhatsThis(data['id'])
        self.__id.setText(data['id'])
        self.__name.setText(data['name'])
        
        # change here when use socket
        byte_img = image_to_bytes(f'../data/small_image/{data["image"]}')

        self.__img.set_img_from_bytes(byte_img)


    # def __init__(self, parent=None):
    #     super().__init__(parent)

    #     self.setGeometry(QtCore.QRect(10, 10, 531, 81))        
    #     self.setStyleSheet("QFrame {border-bottom: 1px solid #ccc;} QLabel {border: none;}")

    #     # Main layout of list item (horizontal)
    #     self.__main_layout = QHBoxLayout(self)
    #     self.__main_layout.setSizeConstraint(QLayout.SetFixedSize)
    #     self.__main_layout.setContentsMargins(11, 0, 0, 8)


    #     # 1. ID
    #     self.__id = QLabel(self)
    #     self.__id.setMinimumSize(QtCore.QSize(64, 64))
    #     self.__id.setMaximumSize(QtCore.QSize(64, 64))
    #     self.__id.setAlignment(QtCore.Qt.AlignCenter)
    #     self.__main_layout.addWidget(self.__id)


    #     # Spacer between ID and Infor
    #     spacerItem = QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
    #     self.__main_layout.addItem(spacerItem)


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
    #     self.__name = QtWidgets.QLabel(self.infor_wrapper)
    #     self.__name.setMinimumSize(QtCore.QSize(318, 0))
    #     self.__name.setWordWrap(False)
    #     self.infor_layout.addWidget(self.__name)

    #     ## 2.4. Stretch the layout of information
    #     self.infor_layout.setStretch(0, 1)
    #     self.__main_layout.addWidget(self.infor_wrapper)


    #     # 3. Stretch the main layout
    #     self.__main_layout.setStretch(2, 8)
