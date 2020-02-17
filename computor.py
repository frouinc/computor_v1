#!/usr/bin/env python3

import sys
import polynomial

def get_tri(s):
	s = s.split("+")
	arr = [0.0, 0.0, 0.0]
	for p in s:
		if (len(p) == 0):
			continue
		tmp = p.split("*X^")
		if (len(tmp) == 1):
			arr[0] = float(tmp[0])
		else:
			if (int(tmp[1]) > 2):
				print("The polynomial degree is stricly greater than 2, I can't solve.")
				exit()
			arr[int(tmp[1])] = (float(tmp[0]))
	return arr

def parse(s):
	s = s.replace(" ", "").replace("-", "+-")
	sides = s.split("=")
	left = get_tri(sides[0])
	right = get_tri(sides[1])
	return [a_i - b_i for a_i, b_i in zip(left, right)]

if (len(sys.argv) == 1):
	print("You need to supply at least one equation.")
	exit()

i = 1
while (i < len(sys.argv)):
	s = sys.argv[i]
	print("--Trying to calculate the equation : {}".format(s))
	a, b, c = parse(s)
	polynomial.second(c, b, a)
	i += 1