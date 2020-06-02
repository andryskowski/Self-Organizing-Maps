from matplotlib import pyplot as plt
import numpy as np
import math
pozycjaZwyc=[]
d=[]
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
	def __init__(self,weightX,weightY,pot):
		weightX= np.random.uniform(-10,10)
		self.weightX=weightX
		weightY=np.random.uniform(-10,10)
		self.weightY=weightY
		pot=1
		self.pot=pot

class Point:
   def __init__(self,x,y):
       self.x=x
       self.y=y
       wynik=0
       self.wynik=wynik
       podPierw=0
       self.podPierw=podPierw
	#Funkcja transmisji neuronów jest przeważnie (i takiej należy użyć rozwiązując niniejsze zadanie) 
	#funkcją odległości między wektorem wejściowym a wektorem wag
   def calculateDistance(self,Layer):
	   i=0
	   j=0
	   Wyniki = []
	   #print(self.x, self.y)
	   pozycjaZwyc.clear()
	   for i in range(len(Layer)): 
	    if Layer[i].pot>pmin:	   		
	   		podPierw=pow((self.x-float(Layer[i].weightX)),2)+pow((self.y-float(Layer[i].weightY)),2)
	   		wynik=math.sqrt(podPierw)
	   			#print(wynik)
	   		Wyniki.append(wynik)
	    else:
	   		Layer[i].pot=1 	   	

	   pozycjaZwyciezcy=np.argmin(Wyniki,axis=0)
	   #print(min(Wyniki), ": najmniejsza odleglosc miedzy Punktem, a Neuronem (zwycieskim)")
	   Wyniki.clear()
	   pozycjaZwyc.append(pozycjaZwyciezcy)
	   #print(pozycjaZwyc[0], ": to jest pozycja, na ktorej jest zwycieski neuron")

   def Potentials(self, Layer, n):
   	for i in range(len(Layer)):
   		#print(Layer[i].pot)
   		if pozycjaZwyc[0]==i:
	   		Layer[i].pot-=pmin
	   	else:
	   		Layer[i].pot+=(1/n)

   def calculateNeuronDistance(self,Layer):
   	d.clear()
   	for i in range(len(Layer)):
   		#if Layer[i].pot>pmin:   
   			podPierw=pow((float(Layer[pozycjaZwyc[0]].weightX)-float(Layer[i].weightX)),2)+pow((float(Layer[pozycjaZwyc[0]].weightY)-float(Layer[i].weightY)),2)
   			d.append(math.sqrt(podPierw))

   def updateWeights(self, Layer, eta, r):
    for i in range(len(Layer)):
    	#if Layer[i].pot>pmin: 
    		Layer[i].weightX+=eta*math.exp(-d[i]*d[i]/(2*r*r))*(self.x - Layer[i].weightX)
    		Layer[i].weightY+=eta*math.exp(-d[i]*d[i]/(2*r*r))*(self.y - Layer[i].weightY)

   def error(self, Layer,P):
    E=1/P*(pow(self.x-float(Layer[pozycjaZwyc[0]].weightX),2)+pow(self.y-float(Layer[pozycjaZwyc[0]].weightY),2))
    #print("to jest blad kwantyzacji-->")
    #print(E)

def main():

	n = int(input("Wprowadz liczbe neuronow n: "))
	xList, yList = np.loadtxt('file.txt', delimiter=',', unpack=True)
	numOfPoints=file_len('file.txt')

	Points=[]
	i=0
	while i<numOfPoints:
		Points.append(Point(xList[i],yList[i]))
		i+=1

	Layer=[]
	i=0
	pot=0.76
	while i<n:
		weightX=0
		weightY=0
		Layer.append(Neuron(weightX,weightY,pot))
		i+=1

	krokMinimum = 0.001 
	krokMax = 0.5
	promienMinimum = 0.00000001 
	promienMax =0.00006
	epoki=4
	#training
	#wykres(Points, Layer)
	for j in range(epoki):
		for i in range(1,len(Points)):
			Points[i].calculateDistance(Layer)
			if i<np.floor(numOfPoints/2):
				Points[i].Potentials(Layer, n)
			r=promienMax*pow(promienMinimum/promienMax,(j/(epoki)))	
			eta=krokMax*pow(krokMinimum/krokMax,((j)/(epoki)))
			Points[i].calculateNeuronDistance(Layer)
			Points[i].updateWeights(Layer,eta,r)
			if i>2:
				P=i
				Points[i].error(Layer,P)
		#print(" ")
	wykres(Points, Layer)

if __name__ == '__main__':
	main()