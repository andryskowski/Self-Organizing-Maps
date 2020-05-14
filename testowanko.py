from matplotlib import pyplot as plt
import numpy as np
import math

def main():
	xList, yList = np.loadtxt('file.txt', delimiter=',', unpack=True)
	print(xList[9999])
	print(yList[9999])
if __name__ == '__main__':
	main()