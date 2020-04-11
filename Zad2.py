from matplotlib import pyplot as plt
import numpy as np
import math
podPierw=0

def wykres():
	x, y = np.loadtxt('file2.txt', delimiter=',', unpack=True)
	a=np.loadtxt('file2.txt', delimiter=',', unpack=True)
	plt.plot(x, y, color='b', linestyle='', marker='.')
	plt.show()

class Neuron:
   def __init__(self, name):
	   self.name = name
	   weights = 10* np.random.random_sample((2)) - 10
	   self.weights=weights
	   print(name)

	   #Neuron jest randomowym punktem z przedzialu [-10,10]
   def calculateDistance(self,inputVector):
	   global podPierw
	   i=0
	   while i<2:
	   	#to co pod pierwiastkiem we wzorze ... (dopisac wzor)
	   	#for i=0, i<allInputsSize, i++; J i
	   	i=0
	   	while i<2:
	   		podPierw=(self.weights[i]-inputVector[0][i])*(self.weights[0]-inputVector[0][i])
	   		i+=1
	   print(podPierw)
	   print(math.sqrt(podPierw))

def main():
	#wykres()
#inputWektor
	with open('file2.txt') as plik:
		inputVector = [list(map(float, wiersz.split(','))) for wiersz in plik]
	n1 = Neuron("Pierwszak")
	n1.calculateDistance(inputVector)

if __name__ == '__main__':
	main()