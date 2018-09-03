import functools
def f1(a):
	return map(lambda x: x + 3, a)
def f2(a):
	return map(lambda x: x * 6, a)
def f3(a):
	return map(lambda x: x - 9, a)
a = [1, 2, 3]
# (a + 3) x 6 - 9
b = list(f3(f2(f1(a))))
print(b)
foo = functools.reduce(
	lambda fa, fb: lambda x: fa(fb(x)), [f3, f2, f1])
c = list(foo(a))
print(c)
def function_composer(*fs):
	return functools.reduce(
		lambda fa, fb: lambda x: fa(fb(x)), fs)
bar = function_composer(f3, f2, f1)
d = list(bar(a))
print(d)