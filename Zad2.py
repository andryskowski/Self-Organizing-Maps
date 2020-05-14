from matplotlib import pyplot as plt
import numpy as np
import math
pozycjaZwyciezcy=0
d=[]
#nowe stale

#wynik=0
def wykres(Points, Layer):

	for j in range(len(Layer)):
		plt.plot(float(Layer[j].weightX), float(Layer[j].weightY), color='r', linestyle='',marker='*')
	for i in range(len(Points)):
		plt.plot(float(Points[i].x), float(Points[i].y), color='g', linestyle='',marker='.')
	plt.show()

class Neuron:
	def __init__(self,weightX,weightY):
		weightX= np.random.uniform(-12,12)
		self.weightX=weightX
		weightY=np.random.uniform(-12,12)
		self.weightY=weightY

class Point:
   def __init__(self,x,y):
       self.x=x
       self.y=y
       wynik=0
       self.wynik=wynik
       podPierw=0
       self.podPierw=podPierw
       pozycjaZwyciezcy=0
       self.pozycjaZwyciezcy=pozycjaZwyciezcy

   def calculateDistance(self,Layer):
	   i=0
	   j=0
	   Wyniki = []
	   print(self.x, self.y)
	   for i in range(len(Layer)):
	   	podPierw=pow((self.x-float(Layer[i].weightX)),2)+pow((self.y-float(Layer[i].weightY)),2)
	   	wynik=math.sqrt(podPierw)
	   	print(wynik)
	   	Wyniki.append(wynik)
	   	#global pozycjaZwyciezcy
	   #pozycjaZwyciezcy=Wyniki.index(minimalna)
	   pozycjaZwyciezcy=np.argmin(Wyniki,axis=0)
	   print(min(Wyniki), ": najmniejsza odleglosc miedzy Punktem, a Neuronem (zwycieskim)")
	   Wyniki.clear()
	   print(pozycjaZwyciezcy, ": to jest pozycja, na ktorej jest zwycieski neuron")

   def calculateNeuronDistance(self,Layer):
   	d.clear()
   	for i in range(len(Layer)):
   	 	podPierw=pow((float(Layer[pozycjaZwyciezcy].weightX)-float(Layer[i].weightX)),2)+pow((float(Layer[pozycjaZwyciezcy].weightY)-float(Layer[i].weightY)),2)
   	 	d.append(math.sqrt(podPierw))		

   def updateWeights(self, Layer, eta, r):
    for i in range(len(Layer)):
        Layer[i].weightX+=eta*math.exp(-d[i]*d[i]/(2*r*r))*(self.x - Layer[i].weightX)
        Layer[i].weightY+=eta*math.exp(-d[i]*d[i]/(2*r*r))*(self.y - Layer[i].weightY)
   def showPoints(self):
   	print (self.x, self.y)

def main():

	n = int(input("Wprowadz liczbe neuronow n: "))

	xList, yList = np.loadtxt('file.txt', delimiter=',', unpack=True)
	Points=[]
	i=0
	while i<10000:
		Points.append(Point(xList[i],yList[i]))
		i+=1

	Layer=[]
	i=0
	while i<n:
		weightX=0
		weightY=0
		Layer.append(Neuron(weightX,weightY))
		i+=1

	j=0

	krokMinimum = 0.01 
	krokMax = 0.5
	promienMinimum = 0.01 
	promienMax = 0.5

	wykres(Points, Layer)
	for i in range(len(Points)):
		r=promienMax*pow(promienMinimum/promienMax,(i/10000))	
		eta=krokMax*pow(krokMinimum/krokMax,(i/10000))
		Points[i].calculateDistance(Layer)
		Points[i].calculateNeuronDistance(Layer)
		Points[i].updateWeights(Layer,eta,r)
		print(" ")
	
	wykres(Points, Layer)

if __name__ == '__main__':
	main()