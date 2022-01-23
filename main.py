from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QGridLayout
from PyQt5.QtGui import QPainter, QPixmap, QPen, QColor
from PyQt5 import uic
import sys
from lol import Ui_MainWindow
from random import randint 


class Yellow_circle(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.label = QLabel()
        canvas = QPixmap(600, 600)
        self.label.setPixmap(canvas)

        layout = QGridLayout(self.centralwidget)
        layout.addWidget(self.pushButton)
        layout.addWidget(self.label)

        self.pushButton.clicked.connect(self.circle)

    def circle(self):
        x, y = [randint(10, 500) for _ in range(2)]
        w, h = [randint(10, 100) for _ in range(2)]
        painter = QPainter(self.label.pixmap())
        pen = QPen()
        pen.setWidth(10)
        pen.setColor(QColor(255, 255, 0))
        painter.setPen(pen)
        painter.drawEllipse(x, y, w, h)
        painter.end()
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    a = Yellow_circle()
    a.show()
    sys.exit(app.exec())