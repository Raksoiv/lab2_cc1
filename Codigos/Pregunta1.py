#Constantes
e_mach = 2**(-52)
def lineal(ei, eii):
	print("Lineal: " + str(eii / ei))

def superLineal(ei, eii):
	err = eii / (ei**((1 + sqrt(5)) / (2)))
	print("Super Lineal: " + str(err))

def cuadratic(ei, eii):
	print("Cuadratico: " + str(eii/ei**2))

def bisection(a, b, f, tol):
	"""Metodo de la biseccion para la función f(x)
	entre los intervalos a y b y con una tolerancia TOL"""
	print("Biseccion")
	while(((b - a) / 2.0) > tol):
		c = (a + b) / 2
		if(f(c) == 0):
			print("Raiz encontrada: " + str(c))
			return c
		elif((f(a) * f(c)) <= 0):
			b = c
		else:
			a = c
	print("Se alcanso la tolerancia")
	print("La raiz aproximada es: " + str(c))
	return c

def secantMethod(f, x0, x1):
	"""Metodo de la secante para la funcion f(x) con los valores iniciales x0 y x1"""
	print("Secante")
	xi = x0
	xii = x1
	while(f(xi) > e_mach):
		temp = xii - ((f(xii) * (xii - xi)) / (f(xii) - f(xi)))
		xii = xi
		xi = temp
	print("Raiz encontrada: " + str(xi))
	return xi

def fixedPoint(g, x0, tol):
	"""Metodo de punto fijo utlizando g(x) y punto inicial x0
	Con una toleracia tol"""
	print("Punto Fijo")
	xi = x0
	while(abs(g(xi) - xi) > tol):
		xi = g(xi)
	print("Raiz encontrada: " + str(xi))
	return xi

def newtonMethod(f, f_prima, x0, tol):
	"""Metodo de punto fijo, con la funcion de Newton
	donde f es la funcion a la que se le busca la raiz
	f_prima es la derivada de la funcion f y x0 el valor inicial
	Se considera una tolerancia tol"""
	print("Newton")
	xi = x0
	while(abs(f(xi) - xi) > tol):
		xi = xi - ((f(xi)) / (f_prima(xi)))
	print("Raiz encontrada: " + str(xi))
	return xi

def newthonModifiedMethod(f, f_prima, x0, m, tol):
	"""Metodo de punto fijo, con la funcion de Newton Modificado
	donde f es la funcion a la que se le busca la raiz
	f_prima es la derivada de la funcion f y x0 el valor inicial
	y m la cantidad de raices repetidas en torno a x0
	Se considera una tolerancia tol"""
	print("Newton Modificado")
	xi = x0
	while(abs(f(xi) - xi) > tol):
		xi = xi - ((m * f(xi)) / (f_prima(xi)))
	print("Raiz encontrada: " + str(xi))
	return xi

# Pruebas
# f = lambda x: x**3
# g = lambda x: -(x**3 - x)
# f_prima = lambda x: 3 * x**2
# bisection(-.4, .6, f, .00001)
# secantMethod(f, .5, .1)
# fixedPoint(g, .5, .001)
# newtonMethod(f, f_prima, .5, .01)
# newthonModifiedMethod(f, f_prima, .5, 3, .001)