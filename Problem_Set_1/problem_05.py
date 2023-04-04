# Authors: Xristos Karagiannis, Emmanouil Angelos Tsigkas

import numpy as np
import math as m
import random as ran
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
	pos = -1
	dif = 1
	for i in range(max_bins):
		if (bins[i] + element) < 1 and (1 - (bins[i] + element)) < dif:
			pos = i
			dif = 1 - bins[i] + element
	if pos == -1:
		bins.append(element)
		max_bins += 1
	else:
		bins[pos] += element
	return bins

# Functions for natural logarithmic and uniform distribution
def log_dist(elem):
	arr = []
	for i in range(elem):
		arr.insert(i, -0.3*m.log(ran.random())) 
	return arr

def uni_dist(elem):
	arr = []
	for i in range(elem):
		arr.insert(i, (float)(ran.random()))
	return arr

if __name__ == '__main__':
	elem = 5000

	uni_elem = uni_dist(elem)
	log_elem = log_dist(elem)

	max_bins = 1
	bins = [0]

	for i in range(elem):
		bins = FF(bins, uni_elem[i])

	print(max_bins)

	max_bins = 1
	bins = [0]

	for i in range(elem):
		bins = BF(bins, uni_elem[i])

	print(max_bins)