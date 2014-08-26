import spdll
from FindPeaks import FindPeaks
wrapper=spdll.morphodll()
wrapper.OpenAllSpectrometers()
Spectrum=wrapper.GetSpectrum(0)
Ag=FindPeaks()
a=Ag.FindBaseline(Spectrum)
print a
Ag.DeductionBaseline()
Peaks=Ag.FindPeaks()
Wavelength=wrapper.GetWavelength(0)
Wavelength=list(Wavelength)
for i in range(0,len(Peaks)):
    print Wavelength[Peaks[i]]
for i in range(1,len(Peaks)+1):
    print Ag.GetFWHM(Wavelength,i)
import matplotlib.pyplot as plt
plt.plot(list(Wavelength),list(Spectrum))
plt.show()
