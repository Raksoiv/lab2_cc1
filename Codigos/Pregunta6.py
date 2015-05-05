def fixedPointModiefied(g, x0, tol, limit):
	"""Metodo de punto fijo modificado utilizando |g(x)|>1 y punto inicial x0
	Con una toleracia tol"""
	print("Punto Fijo")
	xi = x0
	listOfResult = []
	listOfResult.append(xi)
	for i in range(0, limit):
		xii = g(xi) - .99(xi - g(xi))
		if(((xii != 0) and (xi != 0) and (abs(xii - xi) / abs(xii) < tol)) or (abs(xii - xi) == 0)):
			break
		xi = xii
		listOfResult.append(xi)
	print("Raiz encontrada: " + str(xi))
	lineal(listOfResult)
	superLineal(listOfResult)
	cuadratico(listOfResult)
	return xi