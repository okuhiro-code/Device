# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 16:22:05 2024

@author: gxii
"""

import os
import sys
import csv
import time
import datetime

import threading
import pandas as pd
import numpy as np
from PySide6 import QtCore
from PySide6 import QtGui
from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QHBoxLayout
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QGridLayout
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QListWidget
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt

from control import Control
from measurement import Measurement


class TableModel1(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]
            return str(value)

        if role == Qt.BackgroundRole:
            value = self._data.iloc[index.row()][index.column()]
            if 0 <= value and value < 50:
                return QtGui.QColor("red")
            elif 50 <= value and value < 100:
                return QtGui.QColor("yellow")
            elif 100 <= value:
                return QtGui.QColor("lightgreen")
            elif value == -2:
                return QtGui.QColor("darkviolet")
            elif value == -3:
                return QtGui.QColor("mediumvioletred")
            else:
                return QtGui.QColor("darkgray")

        if role == Qt.TextAlignmentRole:
            return Qt.AlignCenter

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, index):
        return self._data.shape[1]

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])

            if orientation == Qt.Vertical:
                return str(self._data.index[section])


class TableModel2(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]
            return str(value)

        if role == Qt.BackgroundRole:
            value = self._data.iloc[index.row()][index.column()]
            if 0 <= value and value < 2000:
                return QtGui.QColor("red")
            elif 2000 <= value and value < 4000:
                return QtGui.QColor("yellow")
            elif 4000 <= value:
                return QtGui.QColor("lightgreen")
            elif value == -2:
                return QtGui.QColor("darkviolet")
            elif value == -3:
                return QtGui.QColor("mediumvioletred")
            else:
                return QtGui.QColor("darkgray")

        if role == Qt.TextAlignmentRole:
            return Qt.AlignCenter

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, index):
        return self._data.shape[1]

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])

            if orientation == Qt.Vertical:
                return str(self._data.index[section])


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BusInterface")
        self.cnt1 = Control("COM1")
        self.cnt2 = Control("COM2")
        self.cnt3 = Control("COM3")

        self.mes = Measurement()
        self.shot_mode = True
        self.shot_number = 0
        self.select1 = np.empty(540)
        self.select2 = np.empty(216)
        self.select3 = np.empty(56)

        for i in range(540):
            self.select1[i] = True

        for i in range(216):
            self.select2[i] = True

        for i in range(56):
            self.select3[i] = True

        self.beam = []
        self.beam.append("E01")
        self.beam.append("E02")
        self.beam.append("E07")
        self.beam.append("E08")
        self.beam.append("F03")
        self.beam.append("F04")
        self.beam.append("F09")
        self.beam.append("F10")
        self.beam.append("G05")
        self.beam.append("G06")
        self.beam.append("G11")
        self.beam.append("G12")

        self.channel1 = []
        self.channel1.append("ch1")
        self.channel1.append("ch2")
        self.channel1.append("ch3")
        self.channel1.append("ch4")
        self.channel1.append("ch5")
        self.channel1.append("ch6")
        self.channel1.append("ch7")
        self.channel1.append("ch8")

        self.channel2 = []
        self.channel2.append("ch1")
        self.channel2.append("ch2")
        self.channel2.append("ch3")
        self.channel2.append("ch4")
        self.channel2.append("ch5")
        self.channel2.append("ch6")
        self.channel2.append("ch7")
        self.channel2.append("ch8")
        self.channel2.append("ch9")
        self.channel2.append("ch10")
        self.channel2.append("ch11")
        self.channel2.append("ch12")
        self.channel2.append("ch13")
        self.channel2.append("ch14")
        self.channel2.append("ch15")
        self.channel2.append("ch16")

        self.ra5xy = np.zeros((2, 12))
        self.da1x = np.zeros((12, 8))
        self.da1y = np.zeros((12, 8))
        self.da2x = np.zeros((12, 16))
        self.da2y = np.zeros((12, 16))
        self.da2z = np.zeros((12, 16))

        for j in range(2):
            for i in range(12):
                self.ra5xy[j, i] = -1
        self.ra5xy = self.ra5xy.astype(int)

        for j in range(12):
            for i in range(8):
                self.da1x[j, i] = -1
        self.da1x = self.da1x.astype(int)

        for j in range(12):
            for i in range(8):
                self.da1y[j, i] = -1
        self.da1y = self.da1y.astype(int)

        for j in range(12):
            for i in range(16):
                self.da2x[j, i] = -1
        self.da2x = self.da2x.astype(int)

        for j in range(12):
            for i in range(16):
                self.da2y[j, i] = -1
        self.da2y = self.da2y.astype(int)

        for j in range(12):
            for i in range(16):
                self.da2z[j, i] = -1
        self.da2z = self.da2z.astype(int)

        self.listbox = QListWidget()
        self.btn1 = QPushButton("Start")
        self.btn1.setFixedSize(100, 30)
        self.btn1.clicked.connect(self.thread_start)

        self.btn2 = QPushButton("Stop")
        self.btn2.setFixedSize(100, 30)
        self.btn2.clicked.connect(self.thread_stop)

        self.btn3 = QPushButton("Trigger")
        self.btn3.setFixedSize(100, 30)
        self.btn3.clicked.connect(self.thread_trigger)

        self.btn4 = QPushButton("Peak")
        self.btn4.setFixedSize(100, 30)
        self.btn4.clicked.connect(self.thread_peak)

        self.btn5 = QPushButton("Waveform")
        self.btn5.setFixedSize(100, 30)
        self.btn5.clicked.connect(self.thread_waveform)

        self.btn6 = QPushButton("Status1")
        self.btn6.setFixedSize(100, 30)
        self.btn6.clicked.connect(self.thread_status1)

        self.btn7 = QPushButton("Status2")
        self.btn7.setFixedSize(100, 30)
        self.btn7.clicked.connect(self.thread_status2)

        self.btn8 = QPushButton("Reset")
        self.btn8.setFixedSize(100, 30)
        self.btn8.clicked.connect(self.thread_reset)

        layoutA = QHBoxLayout()
        layoutA.addWidget(self.btn1)
        layoutA.addWidget(self.btn2)
        layoutA.addWidget(self.btn3)
        layoutA.addWidget(self.btn4)
        layoutA.addWidget(self.btn5)
        layoutA.addWidget(self.btn6)
        layoutA.addWidget(self.btn7)
        layoutA.addWidget(self.btn8)

        self.table1 = QtWidgets.QTableView()
        self.table2 = QtWidgets.QTableView()
        self.table3 = QtWidgets.QTableView()
        self.table4 = QtWidgets.QTableView()
        self.table5 = QtWidgets.QTableView()
        self.table6 = QtWidgets.QTableView()

        ra5df = pd.DataFrame(self.ra5xy, columns=self.beam,
                             index=["X", "Y"])
        self.table1.setModel(TableModel1(ra5df))
        self.table1.setFixedSize(885, 85)

        da1xdf = pd.DataFrame(
            self.da1x, columns=self.channel1, index=self.beam)
        self.table2.setModel(TableModel1(da1xdf))

        da1ydf = pd.DataFrame(
            self.da1y, columns=self.channel1, index=self.beam)
        self.table3.setModel(TableModel1(da1ydf))

        self.table4 = QtWidgets.QTableView()
        da2xdf = pd.DataFrame(
            self.da2x, columns=self.channel2, index=self.beam)
        self.table4.setModel(TableModel1(da2xdf))

        da2ydf = pd.DataFrame(
            self.da2y, columns=self.channel2, index=self.beam)
        self.table5.setModel(TableModel1(da2ydf))

        da2zdf = pd.DataFrame(
            self.da2z, columns=self.channel2, index=self.beam)
        self.table6.setModel(TableModel1(da2zdf))

        for i in range(0, 13):
            self.table1.setColumnWidth(i, 72)
            self.table1.setRowHeight(i, 25)
            self.table2.setRowHeight(i, 25)
            self.table3.setRowHeight(i, 25)

        for i in range(0, 9):
            self.table2.setColumnWidth(i, 105)
            self.table3.setColumnWidth(i, 105)

        for i in range(0, 17):
            self.table4.setColumnWidth(i, 55)
            self.table5.setColumnWidth(i, 55)
            self.table6.setColumnWidth(i, 55)

        for i in range(0, 13):
            self.table4.setRowHeight(i, 25)
            self.table5.setRowHeight(i, 25)
            self.table6.setRowHeight(i, 25)

        layoutB = QHBoxLayout()
        layoutB.addWidget(QLabel("History"))

        layoutB.addWidget(self.listbox)

        layoutC = QHBoxLayout()
        layoutC.addWidget(QLabel("RA50XY"))
        layoutC.addWidget(self.table1)

        layout11 = QVBoxLayout()
        layout11.addLayout(layoutA)
        layout11.addLayout(layoutB)
        layout11.addLayout(layoutC)

        layout2 = QHBoxLayout()
        layout2.addWidget(QLabel("DA100X"))
        layout2.addWidget(self.table2)

        layout3 = QHBoxLayout()
        layout3.addWidget(QLabel("DA100Y"))
        layout3.addWidget(self.table3)

        layout = QGridLayout()
        layout.addLayout(layout11, 0, 0)
        layout.addLayout(layout2, 1, 0)
        layout.addLayout(layout3, 2, 0)

        layout.addWidget(self.table4, 0, 2)
        layout.addWidget(self.table5, 1, 2)
        layout.addWidget(self.table6, 2, 2)
        layout.addWidget(QLabel("DA200X"), 0, 1)
        layout.addWidget(QLabel("DA200Y"), 1, 1)
        layout.addWidget(QLabel("DA200Z"), 2, 1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def update(self):
        if self.shot_mode:
            ra5df = pd.DataFrame(self.ra5xy, columns=self.beam,
                                 index=["X", "Y"])
            self.table1.setModel(TableModel1(ra5df))

            da1xdf = pd.DataFrame(
                self.da1x, columns=self.channel1, index=self.beam)
            self.table2.setModel(TableModel1(da1xdf))

            da1ydf = pd.DataFrame(
                self.da1y, columns=self.channel1, index=self.beam)
            self.table3.setModel(TableModel1(da1ydf))

            da2xdf = pd.DataFrame(
                self.da2x, columns=self.channel2, index=self.beam)
            self.table4.setModel(TableModel1(da2xdf))

            da2ydf = pd.DataFrame(
                self.da2y, columns=self.channel2, index=self.beam)
            self.table5.setModel(TableModel1(da2ydf))

            da2zdf = pd.DataFrame(
                self.da2z, columns=self.channel2, index=self.beam)
            self.table6.setModel(TableModel1(da2zdf))
        else:
            ra5df = pd.DataFrame(self.ra5xy, columns=self.beam,
                                 index=["X", "Y"])
            self.table1.setModel(TableModel2(ra5df))

            da1xdf = pd.DataFrame(
                self.da1x, columns=self.channel1, index=self.beam)
            self.table2.setModel(TableModel2(da1xdf))

            da1ydf = pd.DataFrame(
                self.da1y, columns=self.channel1, index=self.beam)
            self.table3.setModel(TableModel2(da1ydf))

            da2xdf = pd.DataFrame(
                self.da2x, columns=self.channel2, index=self.beam)
            self.table4.setModel(TableModel2(da2xdf))

            da2ydf = pd.DataFrame(
                self.da2y, columns=self.channel2, index=self.beam)
            self.table5.setModel(TableModel2(da2ydf))

            da2zdf = pd.DataFrame(
                self.da2z, columns=self.channel2, index=self.beam)
            self.table6.setModel(TableModel2(da2zdf))

    def thread_start(self):
        thread = threading.Thread(target=self.cnt_start, daemon=True)
        thread.start()

    def cnt_start(self):
        now = datetime.datetime.now()
        mes = str(now.strftime('%Y-%m-%d %H:%M:%S'))
        mes += " mesurement start"
        self.listbox.insertItem(0, mes)

        self.btn1.setEnabled(False)

        self.cnt1.delay()
        self.cnt2.delay()
        self.cnt3.delay()

        self.mes.connection()
        self.mes.attenuator()
        self.mes.measurement_board(0x05)
        self.mes.unit_board(0x05)

        self.cnt1.control_board(0x05)
        self.cnt2.control_board(0x05)
        self.cnt3.control_board(0x05)

        self.btn1.setEnabled(True)
        now = datetime.datetime.now()
        mes = str(now.strftime('%Y-%m-%d %H:%M:%S'))
        mes += " mesurement start: completed."
        self.listbox.insertItem(0, mes)

    def thread_stop(self):
        thread = threading.Thread(target=self.cnt_stop, daemon=True)
        thread.start()

    def cnt_stop(self):
        self.btn2.setEnabled(False)
        now = datetime.datetime.now()
        mes = str(now.strftime('%Y-%m-%d %H:%M:%S'))
        mes += " mesurement stop"
        self.listbox.insertItem(0, mes)

        self.cnt1.control_board(0x06)
        self.cnt2.control_board(0x06)
        self.cnt3.control_board(0x06)

        self.mes.unit_board(0x06)
        self.mes.measurement_board(0x06)
        self.btn2.setEnabled(True)
        now = datetime.datetime.now()
        mes = str(now.strftime('%Y-%m-%d %H:%M:%S'))
        mes += " mesurement stop: completed."
        self.listbox.insertItem(0, mes)

    def thread_trigger(self):
        thread = threading.Thread(target=self.trigger, daemon=True)
        thread.start()

    def trigger(self):
        now = datetime.datetime.now()
        mes = str(now.strftime('%Y-%m-%d %H:%M:%S'))
        mes += " trigger output"
        self.listbox.insertItem(0, mes)
        self.btn3.setEnabled(False)
        self.cnt1.software_trigger()
        self.cnt2.software_trigger()
        self.cnt3.software_trigger()
        self.btn3.setEnabled(True)

    def thread_peak(self):
        thread = threading.Thread(target=self.get_peak, daemon=True)
        thread.start()

    def get_peak(self):
        now = datetime.datetime.now()
        mes = str(now.strftime('%Y-%m-%d %H:%M:%S'))
        mes += " peak data"
        self.listbox.insertItem(0, mes)
        self.btn4.setEnabled(False)
        path = "peak/"+str(self.shot_number)
        if os.path.exists(path) == False:
            os.mkdir(path)

        self.ra5xy, da1, da2 = self.mes.get_peak(
            self.select1, self.select2, self.select3)
        self.da1x = da1[0]
        self.da1y = da1[1]
        self.da2x = da2[0]
        self.da2y = da2[1]
        self.da2z = da2[2]
        self.update()

        with open(path+"/ra5.csv", 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(self.ra5xy)

        with open(path+"/da1x.csv", 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(da1[0])

        with open(path+"/da1y.csv", 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(da1[1])

        with open(path+"/da2x.csv", 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(da2[0])

        with open(path+"/da2y.csv", 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(da2[1])

        with open(path+"/da2z.csv", 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(da2[2])
        self.btn4.setEnabled(True)
        now = datetime.datetime.now()
        mes = str(now.strftime('%Y-%m-%d %H:%M:%S'))
        mes += " peak data: completed."
        self.listbox.insertItem(0, mes)

    def thread_waveform(self):
        thread = threading.Thread(target=self.get_waveform, daemon=True)
        thread.start()

    def get_waveform(self):
        now = datetime.datetime.now()
        self.listbox.insertItem(
            0, str(now.strftime('%Y-%m-%d %H:%M:%S'))+" waveform data")
        self.btn5.setEnabled(False)
        ra5, da1, da2 = self.mes.get_waveform()

        path = "waveform/"+str(self.shot_number)
        if os.path.exists(path) == False:
            os.mkdir(path)

        with open(path+"/ra5x.csv", 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(ra5[0])

        with open(path+"/ra5y.csv", 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(ra5[1])

        with open(path+"/da1x.csv", 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(da1[0])

        with open(path+"/da1y.csv", 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(da1[1])

        with open(path+"/da2x.csv", 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(da2[0])

        with open(path+"/da2y.csv", 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(da2[1])

        with open(path+"/da2z.csv", 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(da2[2])
        self.btn5.setEnabled(True)
        now = datetime.datetime.now()
        mes = str(now.strftime('%Y-%m-%d %H:%M:%S'))
        mes += " waveform data: completed"
        self.listbox.insertItem(0, mes)

    def thread_status1(self):
        thread = threading.Thread(target=self.get_status1, daemon=True)
        thread.start()

    def get_status1(self):
        self.btn6.setEnabled(False)
        status = self.cnt.get_status()

        if status[8] == 1:
            now = datetime.datetime.now()
            mes = str(now.strftime('%Y-%m-%d %H:%M:%S'))
            mes += " trigger: in"
            self.listbox.insertItem(0, mes)
            self.trigger_check = True
        else:
            self.trigger_check = False
        self.btn6.setEnabled(True)

    def thread_status2(self):
        thread = threading.Thread(target=self.get_status2, daemon=True)
        thread.start()

    def get_status2(self):
        self.btn7.setEnabled(False)
        status1, status2 = self.mes.get_status()

        for j in range(7):
            for i in range(27):
                self.listbox.insertItem(0, str(status1[j, i]))
                self.listbox.insertItem(
                    0, "unit:"+str(j+1)+" board:" + str(i+1))

        for i in range(14):
            self.listbox.insertItem(0, str(status2[i]))
            self.listbox.insertItem(0, "unit:8 board:" + str(i+1))
        self.btn6.setEnabled(True)

    def thread_reset(self):
        thread = threading.Thread(target=self.reset, daemon=True)
        thread.start()

    def reset(self):
        now = datetime.datetime.now()
        mes = str(now.strftime('%Y-%m-%d %H:%M:%S'))
        mes += " reset"
        self.listbox.insertItem(0, mes)
        self.btn8.setEnabled(False)
        self.cnt1.reset()
        self.cnt2.reset()
        self.cnt3.reset()
        self.btn8.setEnabled(True)

    def sequence1(self):
        self.trigger_check = False
        self.shot_completed = False
        self.clear()
        self.cnt_start()

        while True:
            if self.trigger_check:
                self.cnt_peak()
                break
            elif self.shot_completed:
                break
            else:
                self.cnt_status1()
                time.sleep(2)

    def sequence2(self):
        self.trigger_check = False
        self.shot_completed = False
        self.clear()
        self.cnt_start()
        while True:
            if self.trigger_check:
                self.cnt_peak()
                self.cnt_waveform()
                break
            elif self.shot_completed:
                break
            else:
                self.cnt_status1()
                time.sleep(2)

    def clear(self):
        for j in range(2):
            for i in range(12):
                self.ra5xy[j, i] = -1
        self.ra5xy = self.ra5xy.astype(int)

        for j in range(12):
            for i in range(8):
                self.da1x[j, i] = -1
        self.da1x = self.da1x.astype(int)

        for j in range(12):
            for i in range(8):
                self.da1y[j, i] = -1
        self.da1y = self.da1y.astype(int)

        for j in range(12):
            for i in range(16):
                self.da2x[j, i] = -1
        self.da2x = self.da2x.astype(int)

        for j in range(12):
            for i in range(16):
                self.da2y[j, i] = -1
        self.da2y = self.da2y.astype(int)

        for j in range(12):
            for i in range(16):
                self.da2z[j, i] = -1
        self.da2z = self.da2z.astype(int)
        self.update()


if __name__ == "__main__":
    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()

    window = MainWindow()
    window.show()
    app.exec()
