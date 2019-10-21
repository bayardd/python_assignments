""" Python file which converts binary numbers to their decimal equivelance. """ 

import sys

MAX_PRECISION = 8
TAB = '\t'

def main(argv):

	listBinaries = []

	for number in argv:
		listBinaries.append(convertToBinary(number))

	printNumbers(argv, listBinaries)
		
   
def convertToBinary(number):
	i = 0
	current_dec = float(number)
	buffer = 0
	binary_num = float(0)
	offset = 0
	#needAddZeroes = False

	while(i < MAX_PRECISION and current_dec % 1 != 0.0):
		i = i + 1
		buffer = current_dec * 2

		if(buffer >= 1):
			offset = 10 ** i
			binary_num = binary_num + (1 / offset)
			current_dec = round(buffer % 1, 8)
			#needAddZeroes = False

		else:
			current_dec = buffer % 1
			#needAddZeroes = True

	## Because 0 x 10^-x cannot be added to the back of a decimal
	## Add the "padding" zeroes to the end of strings when necessary
	# if(needAddZeroes == True):
	# 		binary_num = format(binary_num, '.8f')
	
	return binary_num


def printNumbers(listDecimals, listBinaries):
	print(f'| BASE 10 |   BASE 2     |')
	print(f'----------|---------------')
	
	for x in range(len(listDecimals)):
		print(f'| {listDecimals[x]}{TAB}  | {listBinaries[x]} {TAB} |')


		
if(__name__ == "__main__"):

	if (len(sys.argv) == 1):
		print("Usage: python convert_base.py base 10 decimal(s)")
		sys.exit()

	main(sys.argv[1:])





