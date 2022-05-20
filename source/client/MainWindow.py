from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QFrame, QVBoxLayout

import socket

from ui_mainwindow import Ui_MainWindow
from components.list_item import ListItem
from components.round_label import round_QLabel
from request_handle import request_to_server, create_single_id_request, create_block_request
from components.my_messagebox import MyMessageBox
from components.my_dialog import MyDialog

from connection import ReconnectRunner

from utils import print_color, text_format

import app_logging as logging


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, my_socket: socket.socket = None, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Socket for current client
        self.__my_socket = my_socket
        self.__server_ip, self.__server_port = my_socket.getpeername()

        # Reset index of stacked widget
        self.ui.stackedWidget.setCurrentIndex(0)

        # Button Clicked Events
        self.__set_btn_slots()

        # Infinite scroll
        self.__block_count = 0
        self.ui.listScrollWrapper.verticalScrollBar().valueChanged.connect(self.__infinite_scroll)


    def __infinite_scroll(self, value):
        if value == self.ui.listScrollWrapper.verticalScrollBar().maximum():
            status = self.__show_contact_list(show_more=True)
            if not status:
                self.__show_connect_error('Failed to get more contact list from Server!')
                logging.log('[ERROR] Failed to get more contact list from Server!')


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
        self.ui.listScrollWrapper.setWidget(None)
        status = self.__show_contact_list()

        if not status:
            self.__show_connect_error('Failed to get contact list from Server!')
            logging.log('[ERROR] Failed to get contact list from Server!')
            return

        self.ui.stackedWidget.setCurrentIndex(1)


    def __show_contact_list(self, show_more=False):
        if not show_more:
            self.ui.listScrollWrapper.setWidget(None)

            container = QFrame()
            layout = QVBoxLayout(container)
            layout.setSpacing(0)

            self.__block_count = 0

            # send request to server and get response
            request = create_block_request(0)
            response = request_to_server(self.__my_socket, request)

            if not response:
                return False

            for item in response['data']:
                list_item = ListItem(data=item)
                list_item.signals.clicked.connect(self.__show_detail)
                layout.addWidget(list_item)
                
            self.ui.listScrollWrapper.setWidgetResizable(True)
            self.ui.listScrollWrapper.setWidget(container)
            
        else:
            self.__block_count += 1

            # send request to server and get response
            request = create_block_request(self.__block_count)
            response = request_to_server(self.__my_socket, request)

            if not response:
                return False

            if len(response['data']) > 0:
                for item in response['data']:
                    list_item = ListItem(data=item)
                    # connect the clicked signal of list item to show detail page
                    list_item.signals.clicked.connect(self.__show_detail)
                    self.ui.listScrollWrapper.widget().layout().addWidget(list_item)    
            else:
                self.__block_count -= 1

        return True

    def __show_detail(self, id):
        # send request to server and get response
        request = create_single_id_request(id)
        response = request_to_server(self.__my_socket, request)

        if not response:
            self.__show_connect_error('Failed to get contact detail from Server!')
            logging.log('[ERROR] Failed to get contact detail from Server!')
            return

        data = response['data']

        # image
        round_QLabel(self.ui.detailImg, data['image'], 250)
        # id
        self.ui.detailID.setText(id)
        # name
        self.ui.detailName.setText(data['name'])
        # phone number
        self.ui.detailPhone.setText(data['phone_number'])
        # mail
        self.ui.detailEmail.setText(data['email'])
        # bio
        self.ui.detailBio.setText(data['bio'] if data['bio'] else 'Hello friend\u2019!')

        # change page index
        self.ui.stackedWidget.setCurrentIndex(2)

    def __show_connect_error(self, msg):
        message_box = MyMessageBox(msg, ['Reconnect', 'Cancel'] ,self)
        reply = message_box.exec_()

        if reply == 0:
            print_color('Reconnecting...', text_format.OKGREEN)
            logging.log(f'[STATUS] Reconnecting to {self.__server_ip}:{self.__server_port}')
            self.__reconnect_threading()         
        else:
            print_color('Cancel', text_format.CLOSE)
            logging.log(f'[STATUS] Reconnect canceled')

    def __show_reconnect_msg(self, result):
        self.__dialog.close()
        
        if result:
            print_color('Reconnected successfully!!', text_format.OKGREEN)
            logging.log('[STATUS] Reconnected successfully!')
            MyMessageBox('Reconnected successfully!', [], self).exec_()
        else:
            print_color('Failed to reconnect!', text_format.FAIL)
            logging.log('[STATUS] Failed to reconnect!')
            MyMessageBox('Failed to reconnect!', [], self).exec_()

    def closeEvent(self, event):
        reply = MyMessageBox('Do you want to close the window?', ['Yes', 'No'] ,self).exec_()

        if reply == 0:
            logging.log('[STATUS] Close connection with server')
            self.__my_socket.send(b'close_connection')
            self.__my_socket.close()
            super(MainWindow, self).closeEvent(event)
            event.accept()
            logging.log('[STATUS] Application closed')
        else:
            event.ignore()
            logging.log('[STATUS] Application still opening')

    def __reconnect_threading(self):
        # close current socket
        self.__my_socket.close()
        self.__my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # show dialog
        self.__dialog = MyDialog('Message', 'Reconnecting...', self)
        self.__dialog.show()

        # create thread and start
        self.__thread = QThread()
        self.__target = ReconnectRunner(self.__my_socket, self.__server_ip, self.__server_port)
        self.__target.moveToThread(self.__thread)

        self.__thread.started.connect(self.__target.run)

        self.__target.finished.connect(self.__thread.quit)
        self.__target.ok.connect(lambda: self.__show_reconnect_msg(True))
        self.__target.fail.connect(lambda: self.__show_reconnect_msg(False))

        self.__thread.start()

