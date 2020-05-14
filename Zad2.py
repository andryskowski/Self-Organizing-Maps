from matplotlib import pyplot as plt
import numpy as np
import math
lambdaa = 0.8
r=1
epoch = 10
# wspolczynnik uczenia
eta0 = 0.8
#promien sasiedztwa
r0 = 0.5
pozycjaZwyciezcy=0
d=[]
#nowe stale
krokMinimum = 0.01 
krokMax = 0.5
promienMinimum = 0.01 
promienMax = 0.5

#wynik=0
def wykres(Points, Layer):
	x, y = np.loadtxt('file2.txt', delimiter=',', unpack=True)
	a=np.loadtxt('file2.txt', delimiter=',', unpack=True)
	x_list = [-1.9,-1.8,-1.6, -1.2, -1.0, -0.8]
	y_list = [1.8, 1.6, 1.75, 1.4, 1.2, 1.5]
	for j in range(len(Layer)):
		plt.plot(float(Layer[j].weightX), float(Layer[j].weightY), color='r', linestyle='',marker='*')
	for i in range(len(x_list)):
		plt.plot(float(x_list[i]), float(y_list[i]), color='g', linestyle='',marker='.')
	plt.show()

class Neuron:
	def __init__(self,weightX,weightY):
		weightX= np.random.uniform(-2,0)
		self.weightX=weightX
		weightY=np.random.uniform(1,2)
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
	   #Neuron jest randomowym punktem z przedzialu [-3,3]
   def calculateDistance(self,Layer):
	   i=0
	   j=0
	   Wyniki = []
	   print(self.x, self.y)
	   #print("OTOTOTO")
	   #print(Layer[0].weightX, Layer[0].weightY)
	   #print(Layer[1].weightX, Layer[1].weightY)
	   #print("ABUDABU")
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
	   print("Neuron #0")
	   print(Layer[0].weightX)
	   print(Layer[0].weightY)
	   print("Neuron #1")
	   print(Layer[1].weightX)
	   print(Layer[1].weightY)

   def calculateNeuronDistance(self,Layer):
   	d.clear()
   	for i in range(len(Layer)):
   	 	podPierw=pow((float(Layer[pozycjaZwyciezcy].weightX)-float(Layer[i].weightX)),2)+pow((float(Layer[pozycjaZwyciezcy].weightY)-float(Layer[i].weightY)),2)
   	 	d.append(math.sqrt(podPierw))		

   def updateWeights(self, Layer, eta, r):
    for i in range(len(Layer)):
        Layer[i].weightX+=eta*math.exp(-d[i]*d[i]/2*r)*(self.x - Layer[i].weightX)
        Layer[i].weightY+=eta*math.exp(-d[i]*d[i]/2*r)*(self.y - Layer[i].weightY)
   def showPoints(self):
   	print (self.x, self.y)

def main():

	n = int(input("Wprowadz liczbe neuronow n: "))

	x_list = [-1.9,-1.8,-1.6, -1.2, -1.0, -0.8]
	y_list = [1.8, 1.6, 1.4, 1.4, 1.2, 1.5]

	Points=[]
	i=0
	while i<6:
		x = x_list[i]
		y = y_list[i]
		Points.append(Point(x,y))
		i+=1
	np.random.shuffle(Points)

	Layer=[]
	i=0
	while i<n:
		weightX=0
		weightY=0
		Layer.append(Neuron(weightX,weightY))
		i+=1

	krokMinimum = 0.01 
	krokMax = 0.5
	promienMinimum = 0.01 
	promienMax = 0.5
	j=0

	while j<6:
		r=promienMax*pow(promienMinimum/promienMax,(j/6))	
		eta=krokMax*pow(krokMinimum/krokMax,(j/6))	
		for i in range(len(Points)):
			Points[i].calculateDistance(Layer)
			Points[i].calculateNeuronDistance(Layer)
			Points[i].updateWeights(Layer,eta,r)
			print(" ")
		j+=1

	wykres(Points, Layer)

if __name__ == '__main__':
	main()