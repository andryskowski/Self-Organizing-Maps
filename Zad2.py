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
d=0

#nowe stale
krokMinimum = 0.01 
krokMax = 0.5
promienMinimum = 0.01 
promienMax = 0.5

#wynik=0
def wykres(Points, Layer):
	x, y = np.loadtxt('file2.txt', delimiter=',', unpack=True)
	a=np.loadtxt('file2.txt', delimiter=',', unpack=True)
	#plt.plot(x, y, color='b', linestyle='', marker='.')
	#-1.9,-1.8,-1.6, -1.2, -1.0, -0.8
	#1.8, 1.6, 1.75, 1.4, 1.2, 1.5

	x_list = [-1.9,-1.8,-1.6, -1.2, -1.0, -0.8]
	y_list = [1.8, 1.6, 1.75, 1.4, 1.2, 1.5]
	for j in range(len(Layer)):
		plt.plot(float(Layer[j].weightX), float(Layer[j].weightY), color='r', linestyle='',marker='*')
	for i in range(len(x_list)):
		plt.plot(float(x_list[i]), float(y_list[i]), color='g', linestyle='',marker='.')
	plt.show()

class Neuron:
	def __init__(self,weightX,weightY):
		weightX= np.random.random_sample((1)) - 2
		self.weightX=weightX
		weightY=2* np.random.random_sample((1)) +1
		self.weightY=weightY
	#def punkty(self):
		#x,y = [1.5, 2.3, 2.5, 8.2, 8.3, 9.2]

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
	   	#to co pod pierwiastkiem we wzorze ... (dopisac wzor)
	   	#for i=0, i<allInputsSize, i++; J i
	   i=0
	   j=0
	   Wyniki = []
	   print(self.x, self.y)
	   print("OTOTOTO")
	   print(Layer[0].weightX, Layer[0].weightY)
	   print(Layer[1].weightX, Layer[1].weightY)
	   print("ABUDABU")
	   for i in range(len(Layer)):
	   	podPierw=pow((self.x-float(Layer[i].weightX)),2)+pow((self.y-float(Layer[i].weightY)),2)
	   	pozMin=0
	   	wynik=math.sqrt(podPierw)
	   	print(wynik)
	   	Wyniki.append(wynik)
	   	global pozycjaZwyciezcy
	   minimalna=min(Wyniki)
	   pozycjaZwyciezcy=Wyniki.index(minimalna)
	   print(min(Wyniki), ": najmniejsza odleglosc miedzy Punktem, a Neuronem (zwycieskim)")
	   print(pozycjaZwyciezcy, ": to jest pozycja, na ktorej jest zwycieski neuron")

   def calculateNeuronDistance(self,Layer):
   	global d
   	for i in range(len(Layer)):
   		podPierw=pow((float(Layer[pozycjaZwyciezcy].weightX)-float(Layer[i].weightX)),2)+pow((float(Layer[pozycjaZwyciezcy].weightY)-float(Layer[i].weightY)),2)
	   	d=math.sqrt(podPierw)
	   	print(d) 		
#    void updateWeightsKohonen(vector<double> V, double d)
#          weights[i] +=  eta*exp(-d*d/(2*r))*(V[i]-weights[i]);
 #  def updateWeightsKohonen(self, inputVector, d)
  # 	    self.weights[i]+= eta*exp(-d*d/(2*r))*(V[i]-weights[i]);

   def updateWeights(self, Layer, eta, r):
    print(d)
    for i in range(len(Layer)):
        Layer[i].weightX+=eta*math.exp(-d*d/2*r)*(self.x - Layer[i].weightX)
        Layer[i].weightY+=eta*math.exp(-d*d/2*r)*(self.y - Layer[i].weightY)
   def showPoints(self):
   	print (self.x, self.y)

def main():
	#wykres()
#inputWektor
	with open('file2.txt') as plik:
		inputVector = [list(map(float, wiersz.split(','))) for wiersz in plik]

	n = int(input("Wprowadz liczbe neuronow n: "))
	#for 0 -> n odbywa sie dodawanie neuronow do wektora layer

	x_list = [-1.9,-1.8,-1.6, -1.2, -1.0, -0.8]
	y_list = [1.8, 1.6, 1.4, 1.4, 1.2, 1.5]

	Points=[]
	i=0
	while i<6:
		x = x_list[i]
		y = y_list[i]
		Points.append(Point(x,y))
		i+=1

	Layer=[]
	i=0
	while i<n:
		weightX=0
		weightY=0
		Layer.append(Neuron(weightX,weightY))
		i+=1
	#layer[2].getWeight()
	#przekazac do wykres n i liste neuronow 
	e=0
	i=0
	p=0
	j=0
	k=0
	d=0
	#points = 10* np.random.random_sample((12)) - 10
	#print(points)
	print("przerwa")
	#print(points[0])
	#for e in range(epoch):
	 	#n1.calculateDistance(inputVector)
	#KOHONEN

	#nowe stale od fajnej dziewczyny Karoliny
	krokMinimum = 0.01 
	krokMax = 0.5
	promienMinimum = 0.01 
	promienMax = 0.5


	#epoki=[0,1]
	while j<6:
		print("krok ", j+1)
		r=promienMax*pow(promienMinimum/promienMax,(j/6))	
		eta=krokMax*pow(krokMinimum/krokMax,(j/6))	
		for i in range(len(Points)):
			Points[i].calculateDistance(Layer)
			Points[i].calculateNeuronDistance(Layer)
			Points[i].updateWeights(Layer,eta,r)
			print(" ")
		j+=1

	wykres(Points, Layer)

	





#	for i in range(len(inputVector)):
#	 		#for p in range(len(layer)):
#	 		for p in range(len(layer)):
#	 			#layer[p].calculateDistance()
#	 			#print("WYNIK")
#	 			eta=eta0*(epoch-e)/epoch
#	 			r = r0*math.exp(-e/lambdaa)
#	 			minPos=0
##	 			if(layer[j].wynik<layer[minPos].wynik):
	 #				minPos=j
	 				#d=layer[minPos].calculateDistance(inputVector)
	 #				print("cos tam")
	 		#for k in range(len(layer)):
	 			
	 			#layer[k].updateWeightsKohonen

	#wykres()
	#print(len(inputVector))

if __name__ == '__main__':
	main()