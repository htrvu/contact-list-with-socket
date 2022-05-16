from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QFrame

class FrameSignals(QObject):
    clicked = pyqtSignal(str)

class MyFrame(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

        # signal for mouse click, `str` will be the ID of contacter
        self.signals = FrameSignals()

    # override mouse press event
    def mousePressEvent(self, event):
        self.signals.clicked.emit(self.whatsThis())