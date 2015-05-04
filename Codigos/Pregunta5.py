from math import *
import math

e_mach = 2**(-52)

def taylor_a(x, x0):
	def g(x, x0, c):
		return cos(x0) - sin(x0) * (x - x0) - cos(c) * ((x - x0) / 2.0)
	c = math.pi
	while(g(x, x0, c) - cos(x) > e_mach):
		c = g(x, x0, c)
	print("c = " + str(c))

def taylor_b():
	i = -.75
	while(i < .85):
		taylor(i, math.pi/2.0)
		i += .5

taylor(math.pi, math.pi/2.0)