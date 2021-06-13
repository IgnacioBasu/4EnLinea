from src.tarea1 import contenidoFila

def test_contenido_columna():
	tab = [
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
		[1, 2, 1, 2, 1, 2, 1],
		]

	assert [1, 2, 1, 2, 1, 2, 1] == contenidoFila(6, tab)