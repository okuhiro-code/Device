# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 14:45:02 2021

@author: gxii-osc
"""

from PIL import Image
import tisgrabber as IC


class Camera():
    def __init__(self):
        self.image_w = 640
        self.image_h = 480
        self.img = Image.new('RGB', (self.image_w, self.image_h))

        self.cam = IC.TIS_CAM()

        Devices = self.cam.GetDevices()

        for i in range(len(Devices)):
            print(str(i)+" : "+str(Devices[i]))

        self.cam.ShowDeviceSelectionDialog()

        if self.cam.IsDevValid() == 1:
            ExposureAuto = [1]
            print(ExposureAuto)

            self.cam.GetPropertySwitch("Exposure", "Auto", ExposureAuto)
            print("Exposure auto : ", ExposureAuto[0])

            self.cam.SetPropertySwitch("Exposure", "Auto", 0)
            # "0" is off, "1" is on.

            ExposureTime = [0]
            self.cam.GetPropertyAbsoluteValue(
                "Exposure", "Value", ExposureTime)
            print("Exposure time abs: ", ExposureTime[0])

            # Set an absolute exposure time, given in fractions of seconds. 0.0303 is 1/30 second:
            self.cam.SetPropertyAbsoluteValue("Exposure", "Value", 0.0303)

            # Proceed with Gain, since we have gain automatic, disable first. Then set values.
            Gainauto = [0]
            self.cam.GetPropertySwitch("Gain", "Auto", Gainauto)
            print("Gain auto : ", Gainauto[0])

            self.cam.SetPropertySwitch("Gain", "Auto", 0)

            WhiteBalanceAuto = [0]
            # Same goes with white balance. We make a complete red image:
            self.cam.SetPropertySwitch("WhiteBalance", "Auto", 1)
            self.cam.GetPropertySwitch(
                "WhiteBalance", "Auto", WhiteBalanceAuto)
            print("WB auto : ", WhiteBalanceAuto[0])

            self.cam.SetPropertySwitch("WhiteBalance", "Auto", 0)
            self.cam.GetPropertySwitch(
                "WhiteBalance", "Auto", WhiteBalanceAuto)
            print("WB auto : ", WhiteBalanceAuto[0])

            self.cam.SetPropertyValue(
                "WhiteBalance", "White Balance Red", 64)
            self.cam.SetPropertyValue(
                "WhiteBalance", "White Balance Green", 64)
            self.cam.SetPropertyValue(
                "WhiteBalance", "White Balance Blue", 64)
        else:
            print("No device selected")

    def start_live(self):
        self.cam.StartLive(0)

    def stop_live(self):
        self.cam.StopLive()

    def snap_image(self):
        self.cam.SnapImage()
        return self.cam.GetImage()
