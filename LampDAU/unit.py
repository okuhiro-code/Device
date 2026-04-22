# -*- coding: utf-8 -*-
"""
Created on Mon May 13 10:52:43 2024

@author: gxii
"""

import csv
import serial
import math
import numpy as np


class Unit:
    def __init__(self, board, port, number):
        self.sp = serial.Serial(port)
        self.sp.baudrate = 921600
        self.sp.bytesize = 8
        self.sp.stopbits = 1
        self.sp.parity = "N"
        self.sp.xonxoff = False
        self.sp.dsrdtr = False
        self.sp.dsrdtr = False
        self.sp.timeout = 1
        self.sp.close()

        self.unit = number

        if board:
            self.board = 27
        else:
            self.board = 14
        self.channel = 4

        self.bit1 = [0 for i in range(8)]
        self.bit2 = [0 for i in range(8)]

    def check_sum(self, x):
        bit = [0 for i in range(8)]
        for i in range(8):
            bit[i] = x % 2
            x = int(x / 2)

        check = 0
        for i in range(8):
            check += bit[i]*math.pow(2.0, i)
        return int(check)

    def bit2int(self, x1, x2):
        for i in range(8):
            self.bit1[i] = x1 % 2
            x1 = int(x1 / 2)

        for i in range(8):
            self.bit2[i] = x2 % 2
            x2 = int(x2 / 2)

        sum1 = 0
        for i in range(8):
            sum1 += self.bit1[i]*math.pow(2.0, i)
            sum1 += self.bit2[i]*math.pow(2.0, i+8)
        return int(sum1)

    def unit_board(self, x):
        command = [0 for i in range(10)]
        command[0] = 0x55
        command[1] = 0xFF
        command[2] = 0xFF
        command[3] = self.unit
        command[4] = 0xFF
        command[5] = 0x00
        command[6] = 0x00
        command[7] = x
        command[9] = 0xaa

        self.sp.open()
        sum1 = 0
        for i in range(1, 8):
            sum1 += command[i]
        command[8] = self.check_sum(sum1)
        self.sp.write(command)
        rec = b""
        while True:
            rec += self.sp.read_all()
            if rec.find(0xaa) > -1:
                break
        self.sp.close()

    def measurement_board(self, x):
        command = [0 for i in range(10)]
        command[0] = 0x55
        command[1] = 0xFF
        command[2] = 0xFF
        command[3] = self.unit
        command[5] = 0x00
        command[6] = 0x00
        command[7] = x
        command[9] = 0xaa

        self.sp.open()
        for i in range(self.board):
            command[4] = i
            sum1 = 0
            for i in range(1, 8):
                sum1 += command[i]
            command[8] = self.check_sum(sum1)
            self.sp.write(command)
            rec = b""
            while True:
                rec += self.sp.read_all()
                if rec.find(0xaa) > -1:
                    break
        self.sp.close()

    def connection(self):
        command = [0 for i in range(10)]
        command[0] = 0x55
        command[1] = 0xFF
        command[2] = 0xFF
        command[3] = self.unit
        command[5] = 0x00
        command[6] = 0x00
        command[7] = 0x00
        command[9] = 0xaa

        self.sp.open()
        for j in range(self.board):
            command[4] = j

            sum1 = 0
            for i in range(1, 8):
                sum1 += command[i]
            command[8] = self.check_sum(sum1)
            self.sp.write(command)

            rec = b""
            while True:
                rec += self.sp.read_all()
                if rec.find(0xaa) > -1:
                    break
            print("connection unit:"+str(self.unit+1)+" board:" + str(j+1))
        self.sp.close()

    def attenuator(self):
        command = [0 for i in range(13)]
        command[0] = 0x55
        command[1] = 0xFF  # 送信元
        command[2] = 0xFF  # 送信元
        command[3] = self.unit
        command[5] = 0x03  # ペイロード長
        command[6] = 0x00  # ペイロード長
        command[7] = 0x04  # command
        command[10] = 0x00
        command[12] = 0xaa

        self.sp.open()
        for j in range(self.board):
            command[4] = j
            for i in range(self.channel):
                command[8] = i
                command[9] = 2
                sum1 = 0
                for x in range(1, 11):
                    sum1 += command[x]

                command[11] = self.check_sum(sum1)
                self.sp.write(command)
                rec = b""
                while True:
                    rec += self.sp.read_all()
                    if rec.find(0xaa) > -1:
                        break
                print("attenuator unit:"+str(self.unit+1)+" board:" +
                      str(j+1)+" channel:"+str(i+1))
        self.sp.close()

    def get_status(self):
        command = [0 for i in range(10)]
        command[0] = 0x55
        command[1] = 0xFF
        command[2] = 0xFF
        command[3] = self.unit
        command[5] = 0x00
        command[6] = 0x00
        command[7] = 0x01
        command[9] = 0xaa

        buffer = []
        self.sp.open()
        for j in range(self.board):
            command[4] = j
            sum1 = 0
            for i in range(1, 8):
                sum1 += command[i]
            command[8] = self.check_sum(sum1)

            self.sp.write(command)
            rec = b""
            while True:
                rec += self.sp.read_all()
                if rec.find(0xaa) > -1:
                    buffer.append(rec)
                    print(rec)
                    break
        self.sp.close()

        status = np.ones((self.board, 16))

        for j in range(self.board):
            data = buffer[j]
            payload_length = 16*data[6]+data[5]
            # print(payload_length)

            if payload_length == 4:
                x = data[8]
                for i in range(8):
                    status[j, i] = x % 2
                    x = int(x / 2)
                x = data[9]
                for i in range(8):
                    status[j, i+8] = x % 2
                    x = int(x / 2)

        status = status.reshape(-1, 16)
        return status

    def get_peak(self, select):
        command = [0 for i in range(11)]
        command[0] = 0x55
        command[1] = 0xFF  # 送信元
        command[2] = 0xFF  # 送信元
        command[3] = self.unit  # 送信先
        command[5] = 0x01  # ペイロード長
        command[6] = 0x00  # ペイロード長
        command[7] = 0x81  # command
        command[10] = 0xaa

        peak = np.zeros((self.board, self.channel))
        data = []

        self.sp.open()
        for k in range(self.board):
            command[4] = k  # 送信先
            for j in range(self.channel):
                if select[k, j]:
                    command[8] = j  # channel

                    sum1 = 0
                    for i in range(1, 9):
                        sum1 += command[i]
                    command[9] = self.check_sum(sum1)

                    self.sp.write(command)
                    rec = b""
                    while True:
                        rec += self.sp.read_all()
                        if len(rec) >= 13:
                            if rec[7] == 0x01:
                                peak[k, j] = -2
                                break
                            elif rec[7] == 0x81:
                                if len(rec) == 13:
                                    data.append(rec)
                                    peak[k, j] = self.bit2int(rec[8], rec[9])
                                    break
                            else:
                                peak[k, j] = -3
                                break
                else:
                    peak[k, j] = -1
                print("peak data unit:"+str(self.unit+1)+" board:" +
                      str(k+1)+" channel:"+str(j+1))

        self.sp.close()
        with open("rec"+str(self.unit+1)+".csv", 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(data)
        return peak

    def get_waveform(self):
        command = [0 for i in range(11)]
        command[0] = 0x55
        command[1] = 0xFF  # 送信元
        command[2] = 0xFF  # 送信元
        command[3] = self.unit
        command[5] = 0x01  # ペイロード長
        command[6] = 0x00  # ペイロード長
        command[7] = 0x80  # command
        command[10] = 0xaa
        waveform = np.zeros((self.board, self.channel, 4000))

        self.sp.open()
        for k in range(self.board):
            command[4] = k  # 送信先
            for j in range(self.channel):
                command[8] = j  # channel

                sum1 = 0
                for i in range(1, 9):
                    sum1 += command[i]
                command[9] = self.check_sum(sum1)

                self.sp.write(command)
                rec = b""
                while True:
                    rec += self.sp.read_all()

                    if len(rec) >= 14:
                        if rec[7] == 0x01:
                            for i in range(4000):
                                waveform[k, j, i] = 0.0
                            break
                        elif rec[7] == 0x80:
                            if len(rec) == 8013:
                                for i in range(4000):
                                    waveform[k, j, i] = self.bit2int(
                                        rec[8+2*i], rec[9+2*i])
                                break
                        else:
                            for i in range(4000):
                                waveform[k, j, i] = 0.0
                            break
                print("unit:"+str(self.unit+1)+" board:" +
                      str(k+1)+" channel:"+str(j+1))
        self.sp.close()
        return waveform
