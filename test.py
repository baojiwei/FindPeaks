import spdll
from FindPeaks import GetBaseline
wrapper=spdll.morphodll()
wrapper.OpenAllSpectrometers()
Spectrum=wrapper.GetSpectrum(0)
Ag=GetBaseline()
Ag.FindBaseline(Spectrum)
Ag.DeductionBaseline()
Peaks=Ag.FindPeaks()
Wavelength=wrapper.GetWavelength(0)
for i in range(1,len(Peaks)+1):
    print Ag.GetFWHM(Wavelength,i)
