from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPainter, QPainterPath
from PyQt5.QtWidgets import QLabel
import base64

def round_QLabel(obj, img_data, size):
    obj.target = QPixmap(obj.size())  
    obj.target.fill(Qt.transparent)   

    p = QPixmap()
    p.loadFromData(base64.b64decode(img_data))
    p = p.scaled(size, size, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)

    painter = QPainter(obj.target)
    painter.setRenderHint(QPainter.Antialiasing, True)
    painter.setRenderHint(QPainter.HighQualityAntialiasing, True)
    painter.setRenderHint(QPainter.SmoothPixmapTransform, True)

    path = QPainterPath()
    path.addRoundedRect(0, 0, obj.width(), obj.height(), size / 2, size / 2)

    painter.setClipPath(path)
    painter.drawPixmap(0, 0, p)

    obj.setPixmap(obj.target)


class RoundLabel(QLabel):
    def __init__(self, size, parent=None):
        super(RoundLabel, self).__init__(parent)
        self.__img_size = size
        self.setMaximumSize(size, size)
        self.setMinimumSize(size, size)

    def set_img_from_b64str(self, img_data):
        round_QLabel(self, img_data, self.__img_size)