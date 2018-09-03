import functools
def f1(x, y):
	return x + y
a, b = 1, 2
print(f1(a, b))
c = [3, 4, 5]
d = functools.reduce(f1, c)
print(d)
e = functools.reduce(lambda x, y: x * y, c)
print(e)