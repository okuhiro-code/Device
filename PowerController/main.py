# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 15:47:44 2026

@author: oku-hiro
"""
import csv
import sys
from PySide6 import QtCore
from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QPushButton
import numpy as np
import sequence1 as sq1


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data, status):
        super().__init__()
        self._data = data
        self._status = status

    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self._data[index.column()][index.row()]
            if isinstance(value, str):
                return '%s' % value

        if role == Qt.BackgroundRole:
            value = self._status[index.column()][index.row()]
            if value > 0:
                return QColor("#FFCCCC")

    def rowCount(self, index):
        return len(self._data[0])

    def columnCount(self, index):
        return len(self._data)


class SequenceWindow1(QWidget):
    def __init__(self):
        super().__init__()
        self.label1 = QLabel("Sequence Controller: 1")
        self.label2 = QLabel("Sequence Controller: 2")

        labels1 = []
        with open("label1.csv", "r", newline="") as f:
            reader = csv.reader(f)
            for j, row in enumerate(reader):
                label = []
                for i in range(len(row)):
                    label.append(row[i])
                labels1.append(label)

        self.address1A = {}
        self.address2A = {}
        for i in range(len(labels1)):
            self.address1A[i] = int(100*float(labels1[i][0]))
            self.address2A[int(100*float(labels1[i][0]))] = i

        font = QFont()
        font.setPointSize(6)
        self.table11 = QtWidgets.QTableView()
        self.table12 = QtWidgets.QTableView()
        
        self.table21 = QtWidgets.QTableView()
        self.table11.setFont(font)
        self.table12.setFont(font)
        self.table21.setFont(font)

        n = 0
        data1 = []
        for j in range(51):
            x = []
            for i in range(16):
                x.append(labels1[n][1])
                n += 1
            data1.append(x)

        self.status1 = np.zeros((len(data1), 16))

        self.data11 = data1[0:30]
        self.data12 = data1[30:51]

        model = TableModel(self.data11, self.status1[0:30])
        self.table11.setModel(model)
        self.table11.resizeColumnsToContents()
        self.table11.resizeRowsToContents()

        model = TableModel(self.data12, self.status1[30:51])
        self.table12.setModel(model)
        self.table12.resizeColumnsToContents()
        self.table12.resizeRowsToContents()

        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.table11)
        layout.addWidget(self.table12)

        self.setLayout(layout)

    def update(self):
        sq1.relay[self.address1A[0]] = True
        sq1.main()

        for i in range(len(self.address1A)):
            if sq1.relay[self.address1A[i]]:
                x = int(i/16)
                y = i % 16
                #print(self.address1A[i])
                self.status1[x, y] = 1

        model = TableModel(self.data11, self.status1[0:30])
        self.table11.setModel(model)
        model = TableModel(self.data12, self.status1[30:51])
        self.table12.setModel(model)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.w1 = SequenceWindow1()
        self.w1.show()

        btn1 = QPushButton("test")
        btn1.clicked.connect(self.on_button_clicked)

        widget = QWidget()

        layout = QVBoxLayout()
        layout.addWidget(btn1)
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def on_button_clicked(self):
        self.w1.status1[0, 0] = 1

        self.w1.update()


if __name__ == "__main__":
    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()
    w = MainWindow()
    w.setAutoFillBackground(True)
    # w.setFixedSize(2200, 1160)
    w.show()
    app.exec()
