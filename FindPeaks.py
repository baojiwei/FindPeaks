# -*- uft-8 -*-
#########################################################################
##	Project		:	FindPeaks
##	File		:	FindPeaks.py
##	Description	:	Find Out Spectrum Peaks
##	Created by	:	baojiwei@baojiwei.com
##	Created date:	14/08/2014
#########################################################################
##	Reversion history
##	V0.1	25/08/2014	BaoJiwei / Initial version
##      TODO:   ChangeName/Develop Baseline Argion
#########################################################################
class GetBaseline():
	"""find out baseline"""
	def __init__(self):
		self.baseline=0
		self.Spectrum=[]
		self.PeakPixel=[]
		self.PeakLeft=[]
		self.PeakRight=[]
		self.Wavelength=[]


	def FindBaseline(self,Spectrum):
	# find out baseline
	# only used in Hg light
		self.Spectrum=list(Spectrum)
		a=min(self.Spectrum)
		temp=[]
		for i in range(int(a),30000,2000):	# every 2000 finds		
			c_temp=0
			for n in range(0,2048):
				if self.Spectrum[n]>i and self.Spectrum[n]<i+2000:
					c_temp+=1
			temp.append(c_temp)
		self.baseline=int(a)+(1+temp.index(max(temp)))*2000
		return self.baseline

	def DeductionBaseline(self):
	#deduction Baseline
		for i in range(0,2048):
			# if Spectrum is bigger than baseline cut baseline
			if self.Spectrum[i]>self.baseline:
				self.Spectrum[i]-=self.baseline
			else:
			# else let Spectrum = 0
				self.Spectrum[i]=0
		return self.Spectrum

	def FindPeaks(self):
	#find out All Peaks
		temp=[]
		for i in range(0,2048):
			if self.Spectrum[i]!=0:
				temp.append(i)
		atemp=[temp[0]]
		btemp=[]
		for i in range(1,len(temp)):
			#find out not continues points
			#a_temp is left point
			#b_temp is right point
			if temp[i]-temp[i-1]>1:
				atemp.append(temp[i])
				btemp.append(temp[i-1])
		btemp.append(temp[-1])
		PeakPixel=[]
		sp_temp=[]
		for i in range(0,len(atemp)):
			#get Peaks pixels
			if atemp[i]!=btemp[i]:
				sp_temp=self.Spectrum[atemp[i]:btemp[i]]
				PeakPixel.append(sp_temp.index(max(sp_temp))+atemp[i]+1)
				self.PeakLeft.append(atemp[i])
				#PeakLeft is index of list
				self.PeakRight.append(btemp[i])
		self.PeakPixel=PeakPixel
		#Caution:PeakPixel is pixel of Peaks not list's index of Spectrum
		return self.PeakPixel
	
	def GetFWHM(self,Wavelength,PeakIndex):
		#input Peak's Index can get FWHM
		self.Wavelength=list(Wavelength)
		peakid=PeakIndex-1
		Area=0.0
		for i in range(self.PeakLeft[peakid],self.PeakRight[peakid]-1):
			Area=Area+0.5*(Wavelength[i+1]-Wavelength[i])*(self.Spectrum[i+1]+self.Spectrum[i])
			#PeakLeft & PeakRight are indexs of lists do not -1
		Height=self.Spectrum[self.PeakPixel[peakid]]
		FWHM=Area/Height
		self.FWHM=FWHM
		return self.FWHM


