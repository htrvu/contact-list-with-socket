from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFrame, QVBoxLayout
import sys

sys.path.append('..')

from client.ui_mainwindow import Ui_MainWindow
from client.components.list_item import ListItem

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Reset index of stacked widget
        self.ui.stackedWidget.setCurrentIndex(0)

        # Button Clicked Events
        self.__set_btn_slots()

    def __stacked_index_slots(self, index):
        return lambda : self.ui.stackedWidget.setCurrentIndex(index)

    def __contact_list_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.__show_contact_list()

    def __set_btn_slots(self):
        # Home page
        self.ui.contactListBtn.clicked.connect(self.__contact_list_btn_clicked)
        self.ui.aboutUsBtn.clicked.connect(self.__stacked_index_slots(3))
        self.ui.exitBtn.clicked.connect(self.close)

        # List page
        self.ui.listBackBtn.clicked.connect(self.__stacked_index_slots(0))

        # Detail page
        self.ui.detailBackBtn.clicked.connect(self.__stacked_index_slots(0))

        # About page
        self.ui.aboutBackBtn.clicked.connect(self.__stacked_index_slots(0))

    def __show_contact_list(self):
        self.ui.listScrollWrapper.setWidget(None)

        data = [{
            'id': 'C000001',
            'name': 'Alexis Barnett',
            'img': 'alexis_barnett_sm.png'
        },
        {
            'id': 'C000001',
            'name': 'Alexis Barnett',
            'img': 'alexis_barnett_sm.png'
        },
        {
            'id': 'C000001',
            'name': 'Hello Welcome to my channel',
            'img': 'alexis_barnett_sm.png'
        },
        {
            'id': 'C000001',
            'name': 'Alexis Barnett',
            'img': 'alexis_barnett_sm.png'
        },
        {
            'id': 'C000001',
            'name': 'Alexis Barnett',
            'img': 'alexis_barnett_sm.png'
        }]


        container = QFrame()
        layout = QVBoxLayout(container)

        for item in data:
            list_item = ListItem()
            list_item.set_data(item)
            layout.addWidget(list_item)

        self.ui.listScrollWrapper.setWidgetResizable(True)
        self.ui.listScrollWrapper.setWidget(container)