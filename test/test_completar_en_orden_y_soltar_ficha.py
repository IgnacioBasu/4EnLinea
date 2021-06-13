from src.tarea1 import completarTableroEnOrden

#Para poder llevar a cabo el testeo de la funcion de soltar en orden las fichas hay que usar la funcion de soltar fichas
#Por lo anterior podemos decir que testeando la funcion de completarTableroEnOrden tambien testeamos la de soltarFichaEnColumna
#La funcion completarTableroEnOrden hace uso de la funcion soltarFichaEnColumna(sin esta no funciona)
def test_tablero_en_orden_y_soltar_ficha():
	tab = [
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
		]

	secuencia = [1,2,3,4]

	assert [
	[0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0],
	[1, 2, 1, 2, 0, 0, 0],
	]                           == completarTableroEnOrden(secuencia, tab)