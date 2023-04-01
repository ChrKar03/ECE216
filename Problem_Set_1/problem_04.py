# Authors: Xristos Karagiannis, Emmanouil Angelos Tsigkas

import numpy as np
import math as m
import sys

comps = 0

###########################---- Algorithms ----###########################

# Mergesort function
def mergesort(array, i1, j):
	global comps
	final = []
	j1 = j2 = i = 0

	while j1 < j and j2 < j:
		comps += 1
		if array[i1][j1] > array[i1 + 1][j2]:
			final.insert(i, array[i1 + 1][j2])
			j2 += 1
		else:
			final.insert(i, array[i1][j1])
			j1 += 1
		i += 1

	if j1 == j:
		final.extend(array[i1 + 1][j2:])
	else:
		final.extend(array[i1][j1:])

	return final

# Recursive function that merges n sequences 
def algo(array, rows, cols):
	global fin
	fin = []
	stop = int(rows/2)
	for i in range(stop):
		fin.insert(i, mergesort(array, i*2, cols))
	if stop == 1:
		return fin
	else:
		return algo(fin, rows/2, cols*2)


#########################---- User Interface ----#########################

if __name__ == '__main__':

	opt = sys.argv

	if len(opt) < 1:
		print("problem_04.py -n<number of elements> -s#boolvalue (single sequence) \
		-r#boolvalue<random> -i <inputfile> -o <outputfile>\n")
		exit()

	if opt[1] == '-h':
		print("problem_04.py -n<number of elements> -s#boolvalue (single sequence) \
-r#boolvalue<random> -i <inputfile> -o <outputfile>\n")
		print(" -n#number	--number of elements(even power of 2)\n -s#boolvalue	\
--single sequence\n -r#boolvalue	--random number generator\n -i		--inputfile>\n -o		--outputfile>\n")
		exit()

	# Size of the matrix to be merged
	arr = 0
	m = n = int(m.sqrt(int(opt[1][2:])))

	# Vector sort option
	if opt[2][:2] == '-s' and int(opt[2][2]):
		n = 1
		m = m*m

	# Random, file or manual input option 
	if opt[3][:2] == '-r' and int(opt[3][2]):
		arr = np.random.randint(0,1000,size=(m,n))
		arr.sort()
	elif len(opt) > 6 and opt[4][:2] == '-i':
		f = open(opt[5], "r")
		for i in range(m):
			for j in range(m):
				arr[i][j] = int(f.readline())
		f.close()
	else:
		print("Enter elements by row sorted\n")
		for i in range(m):
			for j in range(m):
				arr[i][j] = int(input())

	# Check that we have the desired input
	print(arr)

	#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-^^^^^^-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

	arr = algo(arr, m, n)

	# Check that we have the desired output
	print(arr)

	# Write comparisons results to file option 
	if len(opt) > 6 and opt[6] == '-o':
		f = open (opt[7], "w")
		f.write(comps)
		f.close()
	else:
		print (comps)