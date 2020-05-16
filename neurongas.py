from matplotlib import pyplot as plt
import numpy as np
import math
pozycjaZwyc=[]
d=[]
gasOrder=[]
pmin=0.75

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def wykres(Points, Layer):
	for j in range(len(Layer)):
		plt.plot(float(Layer[j].weightX), float(Layer[j].weightY), color='r', linestyle='',marker='*')
	for i in range(len(Points)):
		plt.plot(float(Points[i].x), float(Points[i].y), color='g', linestyle='',marker='.')
	plt.show()

class Neuron:
	def __init__(self,weightX,weightY,pot,wynik,kolejnosc):
		weightX= np.random.uniform(-10,12)
		self.weightX=weightX
		weightY=np.random.uniform(-10,10)
		self.weightY=weightY
		pot=0.76
		self.pot=pot
		self.wynik=wynik
		self.kolejnosc=kolejnosc
class Point:
   def __init__(self,x,y):
       self.x=x
       self.y=y
       wynik=0
       self.wynik=wynik
       podPierw=0
       self.podPierw=podPierw
	   #Neuron jest randomowym punktem z przedzialu [-3,3]
   def calculateDistance(self,Layer):
	   print("wywolano funkcje calculateDistance")
	   i=0
	   j=0
	   Wyniki = []
	   print(self.x, self.y)
	   self.pot = 0.76
	   pozycjaZwyc.clear()
	   gasOrder.clear()
	   for i in range(len(Layer)):
	   		if Layer[i].pot>pmin:
	   			podPierw=pow((self.x-float(Layer[i].weightX)),2)+pow((self.y-float(Layer[i].weightY)),2)
	   			Layer[i].wynik=math.sqrt(podPierw)
	   			print(Layer[i].wynik)
	   			Wyniki.append(Layer[i].wynik)
	   pozycjaZwyciezcy=np.argmin(Wyniki,axis=0)

	   sortWyniki=np.sort(Wyniki)
	   for p in range(len(Wyniki)):
	   	for k in range(len(Wyniki)):
	   		if Wyniki[p]==sortWyniki[k]:
	   			Layer[p].kolejnosc=k

	   print("koniec punktu")
	   Wyniki.clear()
	   pozycjaZwyc.append(pozycjaZwyciezcy)
	   #wywolanie funkcji do liczenia potencjalu

	   #dzialania dla algorytmu gazu neuronowego	   
	   print(pozycjaZwyc[0], ": to jest pozycja, na ktorej jest zwycieski neuron")

   def Potentials(self, Layer):
   	for i in range(len(Layer)):
	   	if i==pozycjaZwyc[0]:   
	   		Layer[pozycjaZwyc[0]].pot-=pmin
	   	else:
	   		Layer[pozycjaZwyc[0]].pot+=(1/100)

   def calculateNeuronDistance(self,Layer):
   	d.clear()
   	for i in range(len(Layer)):
   		if Layer[pozycjaZwyc[0]].pot>pmin:
   			podPierw=pow((float(Layer[pozycjaZwyc[0]].weightX)-float(Layer[i].weightX)),2)+pow((float(Layer[pozycjaZwyc[0]].weightY)-float(Layer[i].weightY)),2)
   			d.append(math.sqrt(podPierw))		

   def updateWeights(self, Layer, eta, r):
    for i in range(len(Layer)):
    	if Layer[pozycjaZwyc[0]].pot>pmin:
        	Layer[i].weightX+=eta*math.exp(-d[i]*d[i]/(2*r*r))*(self.x - Layer[i].weightX)
        	Layer[i].weightY+=eta*math.exp(-d[i]*d[i]/(2*r*r))*(self.y - Layer[i].weightY)
   def showPoints(self):
   	print (self.x, self.y)

   def updateWeightsGas(self, Layer, eta, r):
   	for i in range(len(Layer)):
   		Layer[i].weightX+=eta*np.exp(-(Layer[i].kolejnosc)/r)*(self.x - Layer[i].weightX)
   		Layer[i].weightY+=eta*np.exp(-(Layer[i].kolejnosc)/r)*(self.y - Layer[i].weightY)

def main():
	numOfPoints=file_len('file.txt')
	xList, yList = np.loadtxt('file.txt', delimiter=',', unpack=True)
	w=int(input("1. Kohonen 2. Algorytm gazu neuronowego: "))

	Points=[]
	i=0

	while i<10000:
		Points.append(Point(xList[i],yList[i]))
		i+=1

	krokMinimum = 0.01 
	krokMax = 0.5
	promienMinimum = 0.01 
	promienMax =1
	j=0
	wynik=0
	kolejnosc=0

	Layer=[]
	q=0
	pot=0.76
	n = int(input("Wprowadz liczbe neuronow n: "))
	while q<100:
		weightX=0
		weightY=0
		Layer.append(Neuron(weightX,weightY,pot,wynik,kolejnosc))
		q+=1

	if w==1:

		wykres(Points, Layer)
		for i in range(len(Points)):
			Points[i].calculateDistance(Layer)
			r=promienMax*pow(promienMinimum/promienMax,(i/numOfPoints))	
			eta=krokMax*pow(krokMinimum/krokMax,(i/numOfPoints))
			Points[i].calculateNeuronDistance(Layer)
			if(i<np.floor(numOfPoints/2)):
				Points[i].Potentials(Layer)
			Points[i].updateWeights(Layer,eta,r)
			print(" ")
		wykres(Points, Layer)
	
	else:
		print("gas")
		for i in range(len(Points)):
			r=promienMax*pow(promienMinimum/promienMax,(i/numOfPoints))	
			eta=krokMax*pow(krokMinimum/krokMax,(i/numOfPoints))
			Points[i].calculateDistance(Layer)
			Points[i].updateWeightsGas(Layer,eta,r)
		wykres(Points, Layer)
if __name__ == '__main__':
	main()