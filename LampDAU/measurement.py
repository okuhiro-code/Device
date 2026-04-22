# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 17:49:34 2024

@author: gxii
"""

import numpy as np
from unit import Unit


class Measurement:
    def __init__(self):
        self.unit1 = Unit(True, "COM3", 0)
        self.unit2 = Unit(True, "COM3", 1)
        self.unit3 = Unit(True, "COM3", 2)
        self.unit4 = Unit(True, "COM4", 0)
        self.unit5 = Unit(True, "COM4", 1)
        self.unit6 = Unit(True, "COM4", 2)
        self.unit7 = Unit(True, "COM5", 0)
        self.unit8 = Unit(False, "COM5", 1)

    def unit_board(self, x):
        self.unit1.unit_board(x)
        self.unit2.unit_board(x)
        self.unit3.unit_board(x)
        self.unit4.unit_board(x)
        self.unit5.unit_board(x)
        self.unit6.unit_board(x)
        self.unit7.unit_board(x)
        self.unit8.unit_board(x)

    def measurement_board(self, x):
        self.unit1.measurement_board(x)
        self.unit2.measurement_board(x)
        self.unit3.measurement_board(x)
        self.unit4.measurement_board(x)
        self.unit5.measurement_board(x)
        self.unit6.measurement_board(x)
        self.unit7.measurement_board(x)
        self.unit8.measurement_board(x)

    def connection(self):
        self.unit1.connection()
        self.unit2.connection()
        self.unit3.connection()
        self.unit4.connection()
        self.unit5.connection()
        self.unit6.connection()
        self.unit7.connection()
        self.unit8.connection()

    def attenuator(self):
        self.unit1.attenuator()
        self.unit2.attenuator()
        self.unit3.attenuator()
        self.unit4.attenuator()
        self.unit5.attenuator()
        self.unit6.attenuator()
        self.unit7.attenuator()
        self.unit8.attenuator()

    def get_status(self):
        status1 = np.ones((7, 27, 16))

        status1[0] = self.unit1.get_status()
        status1[1] = self.unit2.get_status()
        status1[2] = self.unit3.get_status()
        status1[3] = self.unit4.get_status()
        status1[4] = self.unit5.get_status()
        status1[5] = self.unit6.get_status()
        status1[6] = self.unit7.get_status()

        status2 = np.ones((14, 16))
        status2 = self.unit8.get_status()

        return status1, status2

    def get_peak(self, select1, select2, select3):
        select1 = select1.reshape(5, 27, -1)
        select2 = select2.reshape(2, 27, -1)
        select3 = select3.reshape(14, -1)

        peak1 = np.zeros((5, 27, 4))
        peak2 = np.zeros((2, 27, 4))
        peak3 = np.zeros((14, 4))

        peak1[0] = self.unit1.get_peak(select1[0])
        peak1[1] = self.unit2.get_peak(select1[1])
        peak1[2] = self.unit3.get_peak(select1[2])
        peak1[3] = self.unit4.get_peak(select1[3])
        peak1[4] = self.unit5.get_peak(select1[4])
        peak2[0] = self.unit6.get_peak(select2[0])
        peak2[1] = self.unit7.get_peak(select2[1])
        peak1 = peak1.reshape(-1)
        peak2 = peak2.reshape(-1)

        peak3 = self.unit8.get_peak(select3)
        peak3 = peak3.reshape(-1)

        ra5 = np.zeros((2, 12))
        da1 = np.zeros((2, 12, 8))
        da2 = np.zeros((3, 12, 16))

        # Etruss:256ch+RA50XY:8ch=264ch
        step = 0
        for k in range(2):
            for j in range(4):
                for i in range(8):
                    da1[k, j, i] = peak1[step]
                    step += 1

        for k in range(3):
            for j in range(4):
                for i in range(16):
                    da2[k, j, i] = peak1[step]
                    step += 1

        for j in range(2):
            for i in range(4):
                ra5[j, i] = peak1[step]
                step += 1

        # Gtruss:256ch+RA50XY:8ch=264ch
        for k in range(2):
            for j in range(4):
                for i in range(8):
                    da1[k, j+8, i] = peak1[step]
                    step += 1

        for k in range(3):
            for j in range(4):
                for i in range(16):
                    da2[k, j+8, i] = peak1[step]
                    step += 1

        for j in range(2):
            for i in range(4):
                ra5[j, i+8] = peak1[step]
                step += 1

        # F Truss 256ch+RA50XY:8ch=264ch
        step = 0
        for k in range(2):  # 32ch*2=64ch
            for j in range(4):
                for i in range(8):
                    da1[k, j+4, i] = peak2[step]
                    step += 1

        # 64ch
        for k in range(2):
            for j in range(4):
                for i in range(16):
                    da2[k, j+4, i] = peak2[step]
                    step += 1

        # 64ch
        for i in range(16):
            da2[2, 4, i] = peak2[step]
            step += 1

        for i in range(8):
            da2[2, 5, i] = peak2[step]
            step += 1

        step = 0
        for i in range(8, 16):
            da2[2, 5, i] = peak3[step]
            step += 1

        for j in range(2):
            for i in range(16):
                da2[2, j+6, i] = peak3[step]
                step += 1

        for j in range(2):
            for i in range(4):
                ra5[j, i+4] = peak3[step]
                step += 1

        ra5 = ra5.astype(int)
        da1 = da1.astype(int)
        da2 = da2.astype(int)
        return ra5, da1, da2

    def get_waveform(self):
        waveform1 = np.zeros((5, 27, 4, 4000))
        waveform2 = np.zeros((2, 27, 4, 4000))
        waveform3 = np.zeros((14, 4, 4000))

        waveform1[0] = self.unit1.get_waveform()
        waveform1[1] = self.unit2.get_waveform()
        waveform1[2] = self.unit3.get_waveform()
        waveform1[3] = self.unit4.get_waveform()
        waveform1[4] = self.unit5.get_waveform()
        waveform2[0] = self.unit6.get_waveform()
        waveform2[1] = self.unit7.get_waveform()
        waveform3 = self.unit8.get_waveform()

        waveform1 = waveform1.reshape(-1, 4000)
        waveform2 = waveform2.reshape(-1, 4000)
        waveform3 = waveform2.reshape(-1, 4000)

        ra5 = np.zeros((2, 12, 4000))
        da1 = np.zeros((2, 12, 8, 4000))
        da2 = np.zeros((3, 12, 16, 4000))

        # E Truss
        step = 0
        for k in range(2):
            for j in range(4):
                for i in range(8):
                    da1[k, j, i] = waveform1[step]
                    step += 1

        for k in range(3):
            for j in range(4):
                for i in range(16):
                    da2[k, j, i] = waveform1[step]
                    step += 1

        for j in range(2):  # RA50XY
            for i in range(4):
                ra5[j, i] = waveform1[step]
                step += 1

        # G Truss
        for k in range(2):
            for j in range(4):
                for i in range(8):
                    da1[k, j+8, i] = waveform1[step]
                    step += 1

        for k in range(3):
            for j in range(4):
                for i in range(16):
                    da2[k, j+8, i] = waveform1[step]
                    step += 1

        for j in range(2):  # RA50XY
            for i in range(4):
                ra5[j, i+8] = waveform1[step]
                step += 1

        # F Truss
        for k in range(2):
            for j in range(4):
                for i in range(8):
                    da1[k, j+4, i] = waveform2[step]
                    step += 1

        for k in range(2):
            for j in range(4):
                for i in range(16):
                    da2[k, j+4, i] = waveform2[step]
                    step += 1

        for i in range(16):
            da2[2, 4, i] = waveform2[step]
            step += 1

        for i in range(8):
            da2[2, 5, i] = waveform2[step]
            step += 1

        # unit:8
        step = 0
        for i in range(8, 16):
            da2[2, 5, i] = waveform3[step]
            step += 1

        for j in range(2):
            for i in range(16):
                da2[2, j+6, i] = waveform3[step]
                step += 1

        for j in range(2):
            for i in range(4):
                ra5[j, i+4] = waveform3[step]
                step += 1

        ra5 = ra5.transpose(0, 2, 1)
        da1 = da1.reshape(2, -1, 4000)
        da1 = da1.transpose(0, 2, 1)
        da2 = da2.reshape(3, -1, 4000)
        da2 = da2.transpose(0, 1, 2)

        return ra5, da1, da2
