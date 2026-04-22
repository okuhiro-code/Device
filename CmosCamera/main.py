# -*- coding: utf-8 -*-
"""
Created on Fri May 17 09:34:19 2024

@author: oku-hiro
"""

import sys
import threading
import cv2
import imagingsource
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QHBoxLayout

from PySide6.QtGui import QPainter
from PySide6.QtGui import QImage
from PySide6.QtGui import QPixmap


class Canvas(QLabel):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.image_w = 640
        self.image_h = 480
        channel = 3
        self.bytesPerLine = channel * self.image_w
        self.painter = QPainter()
        self.canvas = QPixmap(self.image_w, self.image_h)
        self.canvas.fill(Qt.white)
        self.setPixmap(self.canvas)
        self.pixmap = QPixmap()
        self.camera = imagingsource.Camera()

    def start(self):
        self.thread = True
        t = threading.Thread(target=self.snap)
        t.start()

    def stop(self):
        self.thread = False
        self.camera.stop_live()

    def snap(self):
        self.camera.start_live()
        while True:
            if self.thread:
                img = self.camera.snap_image()
                img = cv2.applyColorMap(img, cv2.COLORMAP_RAINBOW)
                qimg = QImage(img, self.image_w, self.image_h,
                              self.bytesPerLine, QImage.Format_RGB888)
                #qimg.save(self.name+".png")
                self.pixmap = QPixmap.fromImage(qimg)
                self.update()
            else:
                break

    def paintEvent(self, event):
        self.painter.begin(self)
        self.painter.drawPixmap(0, 0, self.pixmap)
        self.painter.end()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.image_w = 640
        self.image_h = 480

        self.setGeometry(0, 0, 660, 500)
        self.canvas1 = Canvas("nfp")
        self.canvas2 = Canvas("ffp")

        vb = QVBoxLayout()
        hb1 = QHBoxLayout()
        hb1.addWidget(self.canvas1)
        hb1.addWidget(self.canvas2)

        btn1 = QPushButton("start")
        btn1.pressed.connect(self.start)
        btn2 = QPushButton("stop")
        btn2.pressed.connect(self.stop)

        hb2 = QHBoxLayout()
        hb2.addWidget(btn1)
        hb2.addWidget(btn2)

        vb.addLayout(hb1)
        vb.addLayout(hb2)

        widget = QWidget()
        widget.setLayout(vb)

        self.setCentralWidget(widget)

    def start(self):
        self.canvas1.start()
        self.canvas2.start()

    def stop(self):
        self.canvas1.stop()
        self.canvas2.stop()

if __name__ == "__main__":
    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()
    window = MainWindow()
    window.show()
    app.exec()

