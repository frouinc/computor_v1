def power(n, p):
	if (p == 0):
		return (1)
	r = n
	while (p > 1):
		r *= n
		p -= 1
	return (r) 

def sqrt(x, TOL = 0.000000001):
    y = 1.0
    while (abs(x / y - y) > TOL):
        y = (y + x / y) / 2.0
    return y

# def sqrt(n):
# 	if (n < 0):
# 		return (0)
# 	r = 1
# 	while (r * r < n):
# 		r += 1
# 	if (r * r == n):
# 		return (r)
# 	return (0)