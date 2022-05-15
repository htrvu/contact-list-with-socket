from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPainter, QPainterPath
from PyQt5.QtWidgets import QLabel

def round_QLabel(obj, byte_img, size):
    obj.target = QPixmap(obj.size())  
    obj.target.fill(Qt.transparent)   

    # change here when use socket
    # p = QPixmap(f'../../data/large_image/{name}').scaled(  
    #     self.__img_size, self.__img_size, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
    p = QPixmap()
    p.loadFromData(byte_img)
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

    def set_img_from_bytes(self, byte_img):
        round_QLabel(self, byte_img, self.__img_size)

        # self.target = QPixmap(self.size())  
        # self.target.fill(Qt.transparent)   

        # # change here when use socket
        # # p = QPixmap(f'../../data/large_image/{name}').scaled(  
        # #     self.__img_size, self.__img_size, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        # p = QPixmap()
        # p.loadFromData(byte_img)
        # p = p.scaled(self.__img_size, self.__img_size, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)

        # painter = QPainter(self.target)
        # painter.setRenderHint(QPainter.Antialiasing, True)
        # painter.setRenderHint(QPainter.HighQualityAntialiasing, True)
        # painter.setRenderHint(QPainter.SmoothPixmapTransform, True)

        # path = QPainterPath()
        # path.addRoundedRect(0, 0, self.width(), self.height(), self.__radius, self.__radius)

        # painter.setClipPath(path)
        # painter.drawPixmap(0, 0, p)
        # self.setPixmap(self.target)

    

# class Window(QWidget):
#     def __init__(self, *args, **kwargs):
#         super(Window, self).__init__(*args, **kwargs)
#         layout = QHBoxLayout(self)
#         layout.addWidget(RoundImage(600))
#         self.setStyleSheet("background: blue;")           

# if __name__ == "__main__":
#     import sys
#     app = QApplication(sys.argv)
#     w = Window()
#     w.show()
#     sys.exit(app.exec_())
