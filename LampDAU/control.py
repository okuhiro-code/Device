import serial
import math
import numpy as np


class Control:
    def __init__(self, port):
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

    def check_sum(self, x):
        bit = [0 for i in range(8)]
        for i in range(8):
            bit[i] = x % 2
            x = int(x / 2)

        check = 0
        for i in range(8):
            check += bit[i]*math.pow(2.0, i)
        return int(check)

    def version(self):
        ret = self.send(self.common(0xFF))
        print(ret)

    def control_board(self, x):
        command = [0 for i in range(10)]
        command[0] = 0x55
        command[1] = 0xFF
        command[2] = 0xFF
        command[3] = 0xFE
        command[4] = 0xFF
        command[5] = 0x00
        command[6] = 0x00
        command[7] = x

        sum1 = 0
        for i in range(1, 8):
            sum1 += command[i]
        command[8] = self.check_sum(sum1)
        command[9] = 0xaa
        self.sp.open()
        self.sp.write(command)
        rec = b""
        while True:
            rec += self.sp.read_all()
            if rec.find(0xaa) > -1:
                break
        self.sp.close()

    def reset(self):
        command = [0 for i in range(10)]
        command[0] = 0x55
        command[1] = 0xFF
        command[2] = 0xFF
        command[3] = 0xFE
        command[4] = 0xFF
        command[5] = 0x00
        command[6] = 0x00
        command[7] = 0x02

        sum1 = 0
        for i in range(1, 8):
            sum1 += command[i]
        command[8] = self.check_sum(sum1)
        command[9] = 0xaa

        self.sp.open()
        self.sp.write(command)
        rec = b""
        while True:
            rec += self.sp.read_all()
            if rec.find(0xaa) > -1:
                break
        self.sp.close()

    def software_trigger(self):
        command = [0 for i in range(10)]
        command[0] = 0x55
        command[1] = 0xFF
        command[2] = 0xFF
        command[3] = 0xFE
        command[4] = 0xFF
        command[5] = 0x00
        command[6] = 0x00
        command[7] = 0x07

        sum1 = 0
        for i in range(1, 8):
            sum1 += command[i]
        command[8] = self.check_sum(sum1)
        command[9] = 0xaa
        self.sp.open()
        self.sp.write(command)

        rec = b""
        while True:
            rec += self.sp.read_all()
            if rec.find(0xaa) > -1:
                break

        self.sp.close()

    def delay(self):
        command = [0 for i in range(14)]
        command[0] = 0x55
        command[1] = 0xFF  # 送信元
        command[2] = 0xFF  # 送信元
        command[3] = 0xFE  # 送信先
        command[4] = 0xFF  # 送信先
        command[5] = 0x04  # ペイロード長
        command[6] = 0x00  # ペイロード長
        command[7] = 0x03  # command
        command[8] = 0x00  # delay
        command[9] = 0x00  # delay
        command[10] = 0x00  # delay
        command[11] = 0x00  # delay

        sum1 = 0
        for i in range(1, 8):
            sum1 += command[i]

        command[12] = self.check_sum(sum1)
        command[13] = 0xaa

        self.sp.open()
        self.sp.write(command)
        rec = b""
        while True:
            rec += self.sp.read_all()
            if rec.find(0xaa) > -1:
                break
        self.sp.close()

    def get_status(self):
        command = [0 for i in range(10)]
        command[0] = 0x55
        command[1] = 0xFF
        command[2] = 0xFF
        command[3] = 0xFE
        command[4] = 0xFF
        command[5] = 0x00
        command[6] = 0x00
        command[7] = 0x01
        command[9] = 0xaa

        sum1 = 0
        for i in range(1, 8):
            sum1 += command[i]
        command[8] = self.check_sum(sum1)

        self.sp.open()
        self.sp.write(command)
        rec = b""
        while True:
            rec += self.sp.read_all()
            if rec.find(0xaa) > -1:
                break
        self.sp.close()

        status = np.ones(16)
        payload_length = 16*rec[6]+rec[5]

        if payload_length == 4:
            x = rec[8]
            for i in range(8):
                status[i] = x % 2
                x = int(x / 2)
            x = rec[9]
            for i in range(8):
                status[i+8] = x % 2
                x = int(x / 2)
        return status
