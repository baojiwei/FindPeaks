# -*- coding: utf-8 -*-
################################################################################
##  Project        :    spectrometers' dll
##  File           :    sp.py
##  Description    :    dll for spectrometers
##  Created by     :    baojiwei@baojiwei.com
##  Created date   :    12/08/2014
################################################################################
##  Reversion history
##  V0.1   28/04/2014   Baojiwei / Initial version
##  V0.2   11/08/2014   Baojiwei / Write OceanSpectrometers' dll
##  V0.3   12/08/2014   Baojiwei / Add OceanSpectrometers' dll
################################################################################

import clr
clr.AddReference('IdeaOptics')
from IdeaOptics import Wrapper
from IdeaOptics import IFX2KTemperature

clr.AddReference('NETOmniDriver')
from OmniDriver import CCoWrapper
from OmniDriver import CCoBoardTemperature
from OmniDriver import CCoCoefficients
        
class morphodll():
    def __init__(self):
        self.obj=Wrapper()
        self.tbj=IFX2KTemperature
    def OpenAllSpectrometers(self):
        return  self.obj.OpenAllSpectrometers()
    def GetSpectrometerName(self,spectrometerIndex):
        return self.obj.GetSpectrometerName(spectrometerIndex)
    def GetNonLinearityCorrectionCoefficient(self,spectrometerIndex):
        self.cbj=self.obj.GetNonLinearityCorrectionCoefficient(spectrometerIndex)
        return self.cbj.getNlCoefficients()
    def GetDetectorSerialNumber(self,spectrometerIndex):
        return self.obj.GetSerialNumber(spectrometerIndex)
    def GetTemperature(self,spectrometerIndex):
        self.tbj=self.obj.GetFX2KTemperature(spectrometerIndex)
        return self.tbj.GetSensorTemperature()
    def SetWindowsOfBox(self,spectrometerIndex,windowsOfBox):
        self.obj.SetWindowsOfBox(spectrometerIndex,windowsOfBox)
    def SetIntegrationTime(self,spectrometerIndex,IntegrationTime):
        self.obj.SetIntegrationTime(spectrometerIndex,IntegrationTime)
    def SetAverage(self,spectrometerIndex,AverageTimes):
        self.obj.SetAverage(spectrometerIndex,AverageTimes)
    def GetWavelength(self,spectrometerIndex):
        return self.obj.GetWavelength(spectrometerIndex)
    def GetSpectrum(self,spectrometerIndex):
        return self.obj.GetSpectrum(spectrometerIndex)


class omnidll():
    def __init__(self):
        self.obj=CCoWrapper()
        self.tbj=CCoBoardTemperature()
        self.cbj=CCoCoefficients()
    def OpenAllSpectrometers(self):
        return  self.obj.openAllSpectrometers()
    def GetSpectrometerName(self,spectrometerIndex):
        return self.obj.getName(spectrometerIndex)
    def GetNonLinearityCorrectionCoefficient(self,spectrometerIndex):
        self.cbj=self.obj.getCalibrationCoefficientsFromEEProm(spectrometerIndex)
        return self.cbj.getNlCoefficients()
    def GetDetectorSerialNumber(self,spectrometerIndex):
        return self.obj.getSerialNumber(spectrometerIndex)
    def GetTemperature(self,spectrometerIndex):
        self.tbj=self.obj.getFeatureControllerBoardTemperature(spectrometerIndex)
        return self.tbj.getBoardTemperatureCelsius()        
    def SetWindowsOfBox(self,spectrometerIndex,windowsOfBox):
        self.obj.setBoxcarWidth(spectrometerIndex,windowsOfBox)
    def SetIntegrationTime(self,spectrometerIndex,IntegrationTime):
        self.obj.setIntegrationTime(spectrometerIndex,IntegrationTime)
    def SetAverage(self,spectrometerIndex,AverageTimes):
        self.obj.setScansToAverage(spectrometerIndex,AverageTimes)
    def GetWavelength(self,spectrometerIndex):
        return self.obj.getWavelengths(spectrometerIndex)
    def GetSpectrum(self,spectrometerIndex):
        return self.obj.getSpectrum(spectrometerIndex)    
