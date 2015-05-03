#imports
from math import sqrt

#Constantes
e_mach = 2**(-52)

#Pregunta II
def lineal(listOfResult):
	listOfErrors = []
	for i in range(0, len(listOfResult) - 1):
		listOfErrors.append(abs(listOfResult[i] - listOfResult[i+1]))
	for i in range(0, len(listOfErrors) - 1):
		if(listOfErrors[i] != 0):
			print("Lineal: " + str((float)(listOfErrors[i+1]) / listOfErrors[i]))

def superLineal(listOfResult):
	listOfErrors = []
	for i in range(0, len(listOfResult) - 1):
		listOfErrors.append(abs(listOfResult[i] - listOfResult[i+1]))
	for i in range(0, len(listOfErrors) - 1):
		if(listOfErrors[i] != 0):
			err = (float)(listOfErrors[i+1]) / ((float)(listOfErrors[i]**((1.0 + sqrt(5)) / 2.0)))
		print("Super Lineal: " + str(err))

def cuadratico(listOfResult):
	listOfErrors = []
	for i in range(0, len(listOfResult) - 1):
		listOfErrors.append(abs(listOfResult[i] - listOfResult[i+1]))
	for i in range(0, len(listOfErrors) - 1):
		if(listOfErrors[i] != 0):
			print("Cuadratico: " + str((float)(listOfErrors[i+1])/listOfErrors[i]**2))

#Pregunta I
def bisection(a, b, f, tol):
	"""Metodo de la biseccion para la función f(x)
	entre los intervalos a y b y con una tolerancia TOL
	listOfResult se utiliza para la deteccion del error"""
	listOfResult = []
	print("Biseccion")
	while(((b - a) / 2.0) > tol):
		c = (a + b) / 2
		listOfResult.append(c)
		if(f(c) == 0):
			break
		elif((f(a) * f(c)) <= 0):
			b = c
		else:
			a = c
	print("La raiz es: " + str(c))
	lineal(listOfResult)
	superLineal(listOfResult)
	cuadratico(listOfResult)
	return c

def secantMethod(f, x0, x1):
	"""Metodo de la secante para la funcion f(x) con los valores iniciales x0 y x1"""
	print("Secante")
	xi = x0
	xii = x1
	listOfResult = []
	listOfResult.append(xi)
	for i in range(0, limit):
		xiii = xii - ((f(xii) * (xii - xi)) / (f(xii) - f(xi)))
		if(((xii != 0) and (xi != 0) and (abs(xii - xi) / abs(xii) < tol)) or (abs(xii - xi) == 0)):
			break
		xi = xii
		xii = xiii
		listOfResult.append(xi)
	print("Raiz encontrada: " + str(xi))
	lineal(listOfResult)
	superLineal(listOfResult)
	cuadratico(listOfResult)
	return xi

def fixedPoint(g, x0, tol):
	"""Metodo de punto fijo utlizando g(x) y punto inicial x0
	Con una toleracia tol"""
	print("Punto Fijo")
	xi = x0
	listOfResult = []
	listOfResult.append(xi)
	for i in range(0, limit):
		xii = g(xi)
		if(((xii != 0) and (xi != 0) and (abs(xii - xi) / abs(xii) < tol)) or (abs(xii - xi) == 0)):
			break
		xi = xii
		listOfResult.append(xi)
	print("Raiz encontrada: " + str(xi))
	lineal(listOfResult)
	superLineal(listOfResult)
	cuadratico(listOfResult)
	return xi

def newtonMethod(f, f_prima, x0, tol, limit):
	"""Metodo de punto fijo, con la funcion de Newton
	donde f es la funcion a la que se le busca la raiz
	f_prima es la derivada de la funcion f y x0 el valor inicial
	Se considera una tolerancia tol y un limite de iteraciones lim"""
	print("Newton")
	xi = x0
	listOfResult = []
	listOfResult.append(xi)
	for i in range(0, limit):
		y = f(xi)
		yp = f_prima(xi)
		if(abs(yp) < e_mach):
			print("division por cero")
			break
		xii = xi - y/yp
		if(((xii != 0) and (xi != 0) and (abs(xii - xi) / abs(xii) < tol)) or (abs(xii - xi) == 0)):
			break
		xi = xii
		listOfResult.append(xi)
	print("raiz encontrada: " + str(xi))
	lineal(listOfResult)
	superLineal(listOfResult)
	cuadratico(listOfResult)

def newthonModifiedMethod(f, f_prima, x0, m, tol):
	"""Metodo de punto fijo, con la funcion de Newton Modificado
	donde f es la funcion a la que se le busca la raiz
	f_prima es la derivada de la funcion f y x0 el valor inicial
	y m la cantidad de raices repetidas en torno a x0
	Se considera una tolerancia tol"""
	print("Newton Modificado")
	xi = x0
	listOfResult = []
	listOfResult.append(xi)
	for i in range(0, limit):
		y = m * f(xi)
		yp = f_prima(xi)
		if(abs(yp) < e_mach):
			print("division por cero")
			break
		xii = xi - y/yp
		if(((xii != 0) and (xi != 0) and (abs(xii - xi) / abs(xii) < tol)) or (abs(xii - xi) == 0)):
			break
		xi = xii
		listOfResult.append(xi)
	print("raiz encontrada: " + str(xi))
	lineal(listOfResult)
	superLineal(listOfResult)
	cuadratico(listOfResult)
	return xi
