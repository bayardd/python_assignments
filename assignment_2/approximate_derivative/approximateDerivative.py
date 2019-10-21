""" Program which will approximate the approximate value for the derivative of f(x) of the finite distance formula. This program uses takes no inputs, and uses sin(x) as f(x), where 
x is a constant 1 and the known f'(x) is cos(x) (up to machine precision)"""


import sys
from math import cos, sin
import matplotlib.pyplot as plt
# import matplotlib.ticker as plticker


def main():
   
	x = 1
	knownDerivative = cos(1)
	hValues = []
	approxDerivatives = []
	absoluteErrors = []
	
	genInputs(hValues)
	genApproxDerivatives(x, hValues, approxDerivatives)
	genAbsoluteErrors(approxDerivatives, knownDerivative, absoluteErrors)
	
	#### Comment below function to prevent graph from rendering ####
	generateGraph(hValues, absoluteErrors)
	
	display(x, approxDerivatives, knownDerivative, absoluteErrors)


def genInputs(hValues):

	for num in range(1, 31):

		h = 2 ** (-num)
		hValues.append(h)


def genApproxDerivatives(x, hValues, approxDerivatives):

	for h in hValues:
		calcFiniteDiff = (sin(x + h) - sin(x)) / h
		approxDerivatives.append(calcFiniteDiff)

        
def genAbsoluteErrors(approxDerivatives, knownDerivative, absoluteErrors):

	for approxDiv in approxDerivatives:
		absoluteError = abs(approxDiv - knownDerivative)
		absoluteErrors.append(absoluteError)

             
def generateGraph(hValues, absoluteErrors):
    
	fig, ax = plt.subplots()
	ax.set_xscale('log', basex=2)
	ax.set_yscale('log', basey=2)
	ax.set_xlabel('H - Values')
	ax.set_ylabel('Absolute Error')
	ax.set_title('Approximating The Derivative')
	ax.plot(hValues,absoluteErrors )
	plt.show()


def display(x, approxDerivatives, knownDerivative, absoluteErrors):
	formatNumbers(approxDerivatives)
	formatNumbers(absoluteErrors)
	knownDerivative = round(knownDerivative, 8)

	print(f"|  h  |      x      |  Approx. f'(x)  |  Known f'(x)  |  Abs. Error  |")
	print(f"----------------------------------------------------------------------")

	for i in range(0, len(approxDerivatives)):
		print(f"| 2^-{i} | {x:.8f} |   {approxDerivatives[i]:.8f}   |   {knownDerivative:8f}   |   {absoluteErrors[i]:.8f}    |")


def formatNumbers(listNumbers):
	formattedNumbers = []
	for i in range(0, len(listNumbers)):
		
		roundedNum = round(listNumbers[i], 8)
		# print(listNumbers[i])
		listNumbers[i] = (roundedNum)
		# print(num)



if(__name__ == "__main__"):
	main()
  
