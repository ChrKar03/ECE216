# Authors: Xristos Karagiannis, Emmanouil Angelos Tsigkas

import numpy as np
import math as m
import random as ran
import time as t
import sys

# First-Fit algorithm
def FF(bins, element):
	global max_bins
	for i in range(max_bins):
		if bins[i] + element < 1:
			bins[i] += element
			break
		else:
			bins.append(element)
			max_bins += 1
			break
	return bins

# Best-Fit algorithm
def BF(bins, element):
	global max_bins
	pos = None
	dif = 1
	for i in range(max_bins):
		if (bins[i] + element) < 1 and (1 - (bins[i] + element)) < dif:
			pos = i
			dif = 1 - bins[i] + element
	if pos == None:
		bins.append(element)
		max_bins += 1
	else:
		bins[pos] += element
	return bins

# Functions for natural logarithmic and uniform distribution
def log_dist(elem):
	arr = []
	for i in range(elem):
		arr.append(-0.3*m.log(ran.random())) 
	return arr

def uni_dist(elem):
	arr = []
	for _ in range(elem):
		arr.append((float)(ran.random()))
	return arr

#----------------------------------Test----------------------------------#

if __name__ == '__main__':
	loop = 100
	elem = [50, 250, 500, 1000]
	ff_time = [0, 0, 0, 0]
	bf_time = [0, 0, 0, 0]
	av = np.empty((2, len(elem)), None)
	bins_ff = [0]*len(elem)
	bins_bf = [0]*len(elem)

	print("Uniform Distribution Test")
	#print("Natural Logarithm Distribution Test")

	for w in range(4):
		for _ in range(elem[w]*loop):
			uni_elem = uni_dist(elem[w])
			#log_elem = log_dist(elem[w])


			max_bins = 1
			bins = [0]

			ts1 = t.time()
			for i in range(elem[w]):
				bins = FF(bins, uni_elem[i])
				#bins = FF(bins, log_elem[i])
			te1 = t.time()

			ff_time[w] += te1 - ts1
			bins_ff[w] += max_bins

			max_bins = 1
			bins = [0]

			ts2 = t.time()
			for i in range(elem[w]):
				bins = BF(bins, uni_elem[i])
				#bins = BF(bins, log_elem[i])
			te2 = t.time()

			bf_time[w] += te2 - ts2
			bins_bf[w] += max_bins

		bins_ff[w] /= elem[w]*loop
		bins_bf[w] /= elem[w]*loop
		av[0][w] = ff_time[w]/loop
		av[1][w] = bf_time[w]/loop
		print ("elem: " + str(elem[w]) + ", bins_ff: " + str(bins_ff) + ", bins_bf: " + str(bins_bf) + " time_ff: " + str(av[0][w]) + " time_bf: " + str(av[0][w]) + "\n")
