n = int(input(""))
x = int("0")
a = "Fizz"
b = "Buzz"
while x < n:
	x = (x+1)
	if (x % 3 != 0):
		if (x % 5 != 0): print (x)
		else: print(b)
	else:
		if (x % 5 != 0): print (a)
		else: print(a + b)