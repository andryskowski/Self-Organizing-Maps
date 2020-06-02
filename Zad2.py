from matplotlib import pyplot as plt
import numpy as np
import math
pozycjaZwyc=[]
d=[]
#wynik=0
def wykres(Points, Layer):
	x, y = np.loadtxt('file2.txt', delimiter=',', unpack=True)
	a=np.loadtxt('file2.txt', delimiter=',', unpack=True)
	x, y = np.loadtxt('file.txt', delimiter=',', unpack=True)
	x_list = [-1.9,-1.9,-1.8,-0.6,-0.6,-0.5]
	y_list = [1.9,1.8,1.9,1.3,1.2,1.2]
	for j in range(len(Layer)):
		plt.plot(float(Layer[j].weightX), float(Layer[j].weightY), color='r', linestyle='',marker='*')
	for i in range(len(x_list)):
		plt.plot(float(x_list[i]), float(y_list[i]), color='g', linestyle='',marker='.')
	plt.show()

class Neuron:
	def __init__(self,weightX,weightY,pot, wynik, kolejnosc):
		weightX= np.random.uniform(-2,0)
		self.weightX=weightX
		weightY=np.random.uniform(1,2)
		self.weightY=weightY
		pot=0.76
		self.pot=pot
		wynik=0
		self.wynik=wynik
		kolejnosc=0
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
	   i=0
	   j=0
	   Wyniki = []
	   print(self.x, self.y)
	   pozycjaZwyc.clear()
	   for i in range(len(Layer)):
	   	podPierw=pow((self.x-float(Layer[i].weightX)),2)+pow((self.y-float(Layer[i].weightY)),2)
	   	Layer[i].wynik=math.sqrt(podPierw)
	   	print(Layer[i].wynik)
	   	Wyniki.append(Layer[i].wynik)

	   sortWyniki=np.sort(Wyniki)
	   p=0
	   pozycjaZwyciezcy=np.argmin(Wyniki,axis=0)
	   print(min(Wyniki), ": najmniejsza odleglosc miedzy Punktem, a Neuronem (zwycieskim)")
	   Wyniki.clear()
	   pozycjaZwyc.append(pozycjaZwyciezcy)
	   #pot += (1/numberOfNeurons)
	   pmin=0.75
	   for i in range(len(Layer)):
	   	if i==pozycjaZwyciezcy:   
	   		Layer[i].pot-=0.75
	   	else:
	   		Layer[i].pot+=(1/100)

	   print(pozycjaZwyc[0], ": to jest pozycja, na ktorej jest zwycieski neuron")
	   print("Neuron #0")
	   print(Layer[0].weightX)
	   print(Layer[0].weightY)
	   print(Layer[0].pot)
	   print("Neuron #1")
	   print(Layer[1].weightX)
	   print(Layer[1].weightY)
	   print(Layer[1].pot)

   def calculateNeuronDistance(self,Layer):
   	d.clear()
   	for i in range(len(Layer)):
   	 	podPierw=pow((float(Layer[pozycjaZwyc[0]].weightX)-float(Layer[i].weightX)),2)+pow((float(Layer[pozycjaZwyc[0]].weightY)-float(Layer[i].weightY)),2)
   	 	d.append(math.sqrt(podPierw))		

   def updateWeights(self, Layer, eta, r):
    for i in range(len(Layer)):
        Layer[i].weightX+=eta*math.exp(-d[i]*d[i]/(2*r*r))*(self.x - Layer[i].weightX)
        Layer[i].weightY+=eta*math.exp(-d[i]*d[i]/(2*r*r))*(self.y - Layer[i].weightY)
        print(Layer[i].kolejnosc)
   def showPoints(self):
   	print (self.x, self.y)

def main():

	n = int(input("Wprowadz liczbe neuronow n: "))

	x_list = [-1.9,-1.9,-1.8,-0.6,-0.6,-0.5]
	y_list = [1.9,1.8,1.9,1.3,1.2,1.2]

	Points=[]
	i=0
	while i<6:
		x = x_list[i]
		y = y_list[i]
		Points.append(Point(x,y))
		i+=1

	Layer=[]
	i=0
	pot=0.76
	wynik=0
	kolejnosc=0
	while i<n:
		weightX=0
		weightY=0
		Layer.append(Neuron(weightX,weightY,pot,wynik, kolejnosc))
		i+=1

	Layer[0].weightX=-1.3
	Layer[0].weightY=1.8
	Layer[1].weightX=-1
	Layer[1].weightY=1.7
	krokMinimum = 0.01
	krokMax = 0.5
	promienMinimum = 0.01
	promienMax = 0.1
	j=0

	wykres(Points, Layer)


	for i in range(len(Points)):
		Points[i].calculateDistance(Layer)
		r=promienMax*pow(promienMinimum/promienMax,(i/6))	
		eta=krokMax*pow(krokMinimum/krokMax,(i/6))
		Points[i].calculateNeuronDistance(Layer)
		#Points[i].updateWeights(Layer,eta,r)
		wykres(Points, Layer)
		print(" ")
	



if __name__ == '__main__':
	main()