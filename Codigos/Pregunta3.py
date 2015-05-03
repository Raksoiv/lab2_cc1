from Pregunta1 import *
from math import *

def f1(x):
	return x**2 - 6.0

def g1(x):
	return 6 + x - x**2

def g1_prima(x):
	return 1 - 2 * x

print("==========A==========")
bisection(-2, 3, f1, .001)
print("=====================")
newtonMethod(g1, g1_prima, 0, .001, 20)

def f2(x):
	return x**5 - 5 * x**2 + 4

def g2(x):
	return (5.0 * x**2 - 4)**(1/5-0)

def g2_prima(x):
	return (10 * x) / (5 * x**2 - 4.0)**(4.0/5.0)

print("==========B==========")
bisection(.5, 1.5, f2, .001)
print("=====================")
newtonMethod(g2, g2_prima, 2, .001, 20)

def f3(x):
	return x**4 - 6 * x**3 + 12 * x**2 - 10 * x + 3

def g3(x):
	return (x**4 - 6 * x**3 + 12 * x**2 + 3) / 10.0

def g3_prima(x):
	return (4 * x**3 - 18 * x**2 + 24 * x) / 10.0

print("==========C==========")
bisection(0, 4, f3, .001)
print("=====================")
newtonMethod(g3, g3_prima, 2.5, .001, 20)

def f4(x):
	return exp(x**2)*x

def g4(x):
	return x * (exp(x**2) + 1)

def g4_prima(x):
	return exp(x**2) * (2 * x**2 + 1) + 1

print("==========D==========")
bisection(1, 2, f4, .001)
print("=====================")
newtonMethod(g4, g4_prima, 1, .001, 20)