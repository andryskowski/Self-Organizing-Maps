from matplotlib import pyplot as plt
import numpy as np
import math
podPierw=0
lambdaa = 0.8
r=1
epoch = 20
# wspolczynnik uczenia
eta0 = 0.8
#promien sasiedztwa
r0 = 0.5
def wykres():
	x, y = np.loadtxt('file2.txt', delimiter=',', unpack=True)
	a=np.loadtxt('file2.txt', delimiter=',', unpack=True)
	plt.plot(x, y, color='b', linestyle='', marker='.')
	x_list = [1.4, 1.3, 1.9, 5.4]
	y_list = [8, 4, -3, -5]
	plt.plot(x_list, y_list, color='g', linestyle='',marker='.')
	plt.show()

class Neuron:
   def __init__(self, name):
	   self.name = name
	   weights = 10* np.random.random_sample((2)) - 10
	   self.weights=weights
	   print(name)
	   #Neuron jest randomowym punktem z przedzialu [-10,10]
   def getWeight(self):
	   print(self.weights) 
   def calculateDistance(self,inputVector):
	   global podPierw
	   i=0
	   while i<2:
	   	#to co pod pierwiastkiem we wzorze ... (dopisac wzor)
	   	#for i=0, i<allInputsSize, i++; J i
	   	i=0
	   	while i<2:
	   		podPierw=(self.weights[i]-inputVector[0][i])*(self.weights[0]-inputVector[1][i])
	   		i+=1
	   print(math.sqrt(podPierw))

#    void updateWeightsKohonen(vector<double> V, double d)
#          weights[i] +=  eta*exp(-d*d/(2*r))*(V[i]-weights[i]);
 #  def updateWeightsKohonen(self, inputVector, d)
  # 	    self.weights[i]+= eta*exp(-d*d/(2*r))*(V[i]-weights[i]);
def main():
	#wykres()
#inputWektor
	with open('file2.txt') as plik:
		inputVector = [list(map(float, wiersz.split(','))) for wiersz in plik]
	n1 = Neuron("Pierwszak")
	n1.calculateDistance(inputVector)
	n = int(input("Wprowadz liczbe neuronow n: "))
	n1.getWeight()
	#for 0 -> n odbywa sie dodawanie neuronow do wektora layer
	layer=[]
	i=0
	while i<n:
		layer.append(Neuron(""))
		i+=1
	layer[2].getWeight()
	print(len(layer))
	#przekazac do wykres n i liste neuronow 

	e=0
	i=0
	p=0
	while e<epoch:
	 	#n1.calculateDistance(inputVector)
		for i in range(len(inputVector)):
	 		#for p in range(len(layer)):
	 		layer[i].calculateDistance(inputVector)
	 		print("WYNIK")
	 		eta=eta0*(epoch-e)/epoch
		e+=1

	wykres()
if __name__ == '__main__':
	main()