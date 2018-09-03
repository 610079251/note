import functools
def f1(x):
	return x + 3
def f2(x):
	return x * 6
def f3(x):
	return x - 9
a = 1
# (a + 3) x 6 - 9
b = f3(f2(f1(a)))
print(b)
foo = functools.reduce(
	lambda fa, fb: lambda x: fa(fb(x)), [f3, f2, f1])
c = foo(a)
print(c)
def function_composer(*fs):
	return functools.reduce(
		lambda fa, fb: lambda x: fa(fb(x)), fs)
bar = function_composer(f3, f2, f1)
d = bar(a)
print(d)