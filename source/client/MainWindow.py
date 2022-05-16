from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QFrame, QVBoxLayout
import sys

sys.path.append('..')

from client.ui_mainwindow import Ui_MainWindow
from client.components.list_item import ListItem
from client.components.round_label import round_QLabel

from common.utils import image_to_bytes

# for demo
# 1. contact data (dictionary)
import json
with open('../data/contact_data.json') as f:
    contact_data = json.load(f)
# print(contact_data)

# 2. list data (list of dictionary)
list_data = []
for id in contact_data.keys():
    list_data.append({
        'id': id,
        'name': contact_data[id]['name'],
        'image': contact_data[id]['image']
    })
    

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Reset index of stacked widget
        self.ui.stackedWidget.setCurrentIndex(0)

        # Button Clicked Events
        self.__set_btn_slots()

        # Infinite scroll
        self.__block_count = 0
        self.ui.listScrollWrapper.verticalScrollBar().valueChanged.connect(self.__infinite_scroll)


    def __infinite_scroll(self, value):
        if value == self.ui.listScrollWrapper.verticalScrollBar().maximum():
            self.__show_contact_list(show_more=True)


    def __stacked_index_slots(self, index):
        return lambda : self.ui.stackedWidget.setCurrentIndex(index)


    def __set_btn_slots(self):
            # Home page
            self.ui.contactListBtn.clicked.connect(self.__contact_list_btn_clicked)
            self.ui.aboutUsBtn.clicked.connect(self.__stacked_index_slots(3))
            self.ui.exitBtn.clicked.connect(self.close)

            # List page
            self.ui.listBackBtn.clicked.connect(self.__stacked_index_slots(0))

            # Detail page
            self.ui.detailBackBtn.clicked.connect(self.__stacked_index_slots(1))

            # About page
            self.ui.aboutBackBtn.clicked.connect(self.__stacked_index_slots(0))


    def __contact_list_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.__show_contact_list()


    def __show_contact_list(self, show_more=False):
        if not show_more:
            self.ui.listScrollWrapper.setWidget(None)

            container = QFrame()
            layout = QVBoxLayout(container)
            layout.setSpacing(0)

            self.__block_count = 0
            for item in list_data[:15]:
                list_item = ListItem(data=item)
                list_item.signals.clicked.connect(self.__show_detail)
                layout.addWidget(list_item)
                
            self.ui.listScrollWrapper.setWidgetResizable(True)
            self.ui.listScrollWrapper.setWidget(container)
            
        else:
            self.__block_count += 1
            start = self.__block_count * 15
            end = min(start + 15, len(list_data))

            for item in list_data[start:end]:
                list_item = ListItem(data=item)
                # connect the clicked signal of list item to show detail page
                list_item.signals.clicked.connect(self.__show_detail)
                self.ui.listScrollWrapper.widget().layout().addWidget(list_item)    


    def __show_detail(self, id):
        data = contact_data[id]

        # # (change here when use socket)
        byte_img = image_to_bytes(f'../data/large_image/{data["image"]}')
        # self.ui.detailImg.set_img_from_bytes(byte_img)
        round_QLabel(self.ui.detailImg, byte_img, 250)

        # id
        self.ui.detailID.setText(id)
        # name
        self.ui.detailName.setText(data['name'])
        # phone number
        self.ui.detailPhone.setText(data['phone_number'])
        # mail
        self.ui.detailEmail.setText(data['email'])
        # bio
        self.ui.detailBio.setText(data['bio'] if data['bio'] else 'Hello motherfucker, hehehe hahaha, one two three. ABC DEF XGHSAD ASDA DASD asd asdas qwe q asdas da')

        # change page index
        self.ui.stackedWidget.setCurrentIndex(2)
