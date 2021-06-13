from src.tarea1 import TableroValido

def test_tablero_valido_si():
	secuencia = [1,2,3,6]

	assert  True == TableroValido(secuencia)

def test_tablero_valido_no():
	secuencia = [1,2,3,8]

	assert  False == TableroValido(secuencia)