def f1(x):
	return x + 3
a = 1
b = f1(a)
print(b)
c = [1, 2, 3]
#d = f1(c)
d = list(map(f1, c))
print(d)
e = list(map(lambda x: x + 3, c))
print(e)