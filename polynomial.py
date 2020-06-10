import ft_math as math

def zero(a):
	print("Reduced form : {} = 0\n".format(a))
	print("Polynomial degree : 0\n")
	if (a == 0):
		print("The solution is \033[32many real number\033[0m")
	else:
		print("There is \033[32mno solution\033[0m")

def first(a, b):
	# if degree 1 is null, check for zero degree
	if (a == 0):
		zero(b)
		return

	print("Reduced form : {} + {} * X = 0\n".format(b, a))
	print("Polynomial degree : 1\n")
	r = -(b / a)
	print("The solution is \033[32m{}\033[0m".format(r))

def second(a, b, c):
	# if degree 2 is null, check for first degree
	if (a == 0):
		first(b, c)
		return

	print("Reduced form : {} + {} * X + {} * X^2 = 0\n".format(c, b, a))
	print("Polynomial degree : 2\n")
	d = math.power(b, 2) - 4 * a * c

	if (d < 0 or a == 0):
		print("Discriminant is negative, there is \033[32mno solution\033[0m")
	elif (d == 0):
		r = -b / (2 * a)
		print("Discriminant is equal to 0, there is one solution : \033[32m{}\033[0m".format(round(r, 6)))
	else:
		r1 = (-b - math.sqrt(d)) / (2 * a)
		r2 = (-b + math.sqrt(d)) / (2 * a)
		print("Discriminant is strictly positive, there are two solutions : \033[32m{}\033[0m and \033[32m{}\033[0m".format(round(r1, 6), round(r2, 6)))