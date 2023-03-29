import numpy as np
import math as m

global n
comps = 0

# Mergesort function
def mergesort(array, i1):
	global comps, final
	final = []
	j1 = j2 = i = 0

	while j1 < n and j2 < n:
		comps += 1
		if array[i1][j1] > array[i1 + 1][j2]:
			final.insert(i, array[i1 + 1][j2])
			j2 += 1
		else:
			final.insert(i, array[i1][j1])
			j1 += 1
		i += 1

	if j1 == n:
		final.extend(array[i1 + 1][j2:])
	else:
		final.extend(array[i1][j1:])

	return final

# Recursive function that merges n sequences 
def algo(array, rows):
	global fin
	fin = []
	stop = int(rows/2)
	for i in range(stop):
		fin.insert(i, mergesort(array, i*2))
	if stop == 1:
		return fin
	else:
		return algo(fin, rows/2)

if __name__ == '__main__':

	n = int(input("Input even power of 2:"))

	arr = np.random.randint(0,1000,size=(n,n))
	arr.sort()

	print(arr)

	arr = algo(arr, n)

	print(arr)
	print(comps)
