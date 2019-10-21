""" Python file which converts base 10 decimal numbers to a provided base (e.g., 2,4,8,60)) """ 

import sys

MAX_PRECISION = 8
TAB = '\t'

def main(argv):
	base = argv.pop(0)
	inputNumbers = []

	for num in argv:
			inputNumbers.append(num)

	convertedNumbers = convertToBase(base, inputNumbers)
	
	display(base, inputNumbers, convertedNumbers)
   
def convertToBase(base, inputNumbers):

	convertedNumbers = []
	
	# testString = ';' . join(numInNewBase)

	for num in inputNumbers:
		numInNewBase = []
		remainder = 1
		i = 0
		baseInt = int(base)
		currentNum = float(num)

		while(i < MAX_PRECISION and remainder != 0):

			currentNum = currentNum * baseInt
			remainder = round(currentNum % 1, 8)

			if currentNum < 1 :
				numInNewBase.append(str(0))
			
			else:
				newBaseNum = currentNum - remainder
				currentNum = remainder
				numInNewBase.append(str(newBaseNum))
		
			i += 1

		convertedNumbers.append(numInNewBase[:])

	return convertedNumbers





          
def display(base, inputNumbers, convertedNumbers):
	print(f'|  BASE 10   |        BASE {base}          |')
	print(f'|------------|-------------------------|')

	formattedNumbers = []

	for convertedNum in convertedNumbers:
		formattedNumbers.append(preformatNumbers(convertedNum))

	for i in range(0, len(inputNumbers)):
		print('| {:8s}   |    {:20s} |'.format(inputNumbers[i], formattedNumbers[i]))
	

def preformatNumbers(list):
	decimal = '.'
	formattedNum = decimal + ';'.join(map(trimZeroes, list))
	return formattedNum

def trimZeroes(number):
	#A bit crude.... quick messy solution to formatting
	return str(int(float(number)))



    
if(__name__ == "__main__"):

	if (len(sys.argv) == 1):
		print("Usage: python convert_base.py [any base] [values to be converted] ")
		sys.exit()
	elif (len(sys.argv) == 2):
		print("Usage: python convert_base.py [any base] [values to be converted] ")
		sys.exit()
		
	main(sys.argv[1:])





