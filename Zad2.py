from matplotlib import pyplot as plt
import numpy as np
import math
lambdaa = 0.8
r=1
epoch = 20
# wspolczynnik uczenia
eta0 = 0.8
#promien sasiedztwa
r0 = 0.5
#wynik=0
def wykres():
	x, y = np.loadtxt('file2.txt', delimiter=',', unpack=True)
	a=np.loadtxt('file2.txt', delimiter=',', unpack=True)
	plt.plot(x, y, color='b', linestyle='', marker='.')
	x_list = [1.4, 1.3, 1.9, 5.4]
	y_list = [8, 4, -3, -5]
	plt.plot(x_list, y_list, color='g', linestyle='',marker='.')
	plt.show()

class Point:
	def __init__(self,x,y):
		x=10* np.random.random_sample((1)) - 10
		self.x=x
		y=10* np.random.random_sample((1)) - 10
		self.y=y
	def punkty(self):
		x,y = [1.5, 2.3, 2.5, 8.2, 8.3, 9.2]

class Neuron:
   def __init__(self, name, weightX, weightY):
	   self.name = name
	   self.weightX=weightX
	   self.weightY=weightY
	   wynik=0
	   self.wynik=wynik
	   podPierw=0
	   self.podPierw=podPierw
	   weightX = 1 #10* np.random.random_sample((1)) - 10
	   weightY = 2 #10* np.random.random_sample((1)) - 10
	   #Neuron jest randomowym punktem z przedzialu [-10,10]
   def calculateDistance(self,Points):
	   	#to co pod pierwiastkiem we wzorze ... (dopisac wzor)
	   	#for i=0, i<allInputsSize, i++; J i
	   i=0
	   j=0
	   Wyniki = []
	   for i in range(len(Points)):
	   	podPierw=pow((self.weightX-float(Points[i].x)),2)+pow((self.weightY-float(Points[i].y)),2)
	   	pozMin=0
	   	wynik=math.sqrt(podPierw)
	   	print(wynik)
	   	Wyniki.append(wynik)
	   print(min(Wyniki))

#    void updateWeightsKohonen(vector<double> V, double d)
#          weights[i] +=  eta*exp(-d*d/(2*r))*(V[i]-weights[i]);
 #  def updateWeightsKohonen(self, inputVector, d)
  # 	    self.weights[i]+= eta*exp(-d*d/(2*r))*(V[i]-weights[i]);
def main():
	#wykres()
#inputWektor
	with open('file2.txt') as plik:
		inputVector = [list(map(float, wiersz.split(','))) for wiersz in plik]

	n = int(input("Wprowadz liczbe neuronow n: "))
	#for 0 -> n odbywa sie dodawanie neuronow do wektora layer
	layer=[]
	i=0
	while i<n:
		weightX = 10* np.random.random_sample((1)) - 10
		weightY = 10* np.random.random_sample((1)) - 10
		layer.append(Neuron("", weightX, weightY))
		i+=1

	Points=[]
	i=0
	while i<n:
		x=0
		y=0
		Points.append(Point(x,y))
		i+=1
	#layer[2].getWeight()
	print(len(layer))
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
	for i in range(len(layer)):
		layer[i].calculateDistance(Points)
		pozMinim=0
		if(layer[i].wynik<layer[pozMinim].wynik):
			pozMinim=i
		print(pozMinim)
		print(" ")





	for i in range(len(inputVector)):
	 		#for p in range(len(layer)):
	 		for p in range(len(layer)):
	 			#layer[p].calculateDistance()
	 			#print("WYNIK")
	 			eta=eta0*(epoch-e)/epoch
	 			r = r0*math.exp(-e/lambdaa)
	 			minPos=0
	 		for j in range(len(layer)):
	 			if(layer[j].wynik<layer[minPos].wynik):
	 				minPos=j
	 				#d=layer[minPos].calculateDistance(inputVector)
	 				print("cos tam")
	 		#for k in range(len(layer)):
	 			
	 			#layer[k].updateWeightsKohonen

	#wykres()
	#print(len(inputVector))
if __name__ == '__main__':
	main()