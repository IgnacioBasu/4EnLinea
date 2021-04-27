
def tableroVacio():
	return [
			[0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0],
			]


def contenidoColumna(nro_columna, tablero):
	columna = []
	for  fila in tablero:
		celda = fila[nro_columna-1]
		columna.append(celda)
	return columna

def contenidoFila(nro_fila, tablero):
	fila = []
	for columna in tablero[nro_fila-1]:
		fila.append(columna)
	return fila

def Columnas(tablero):
	colu = []
	for columna in range(0,7):
		colu.append(contenidoColumna(columna,tablero))
	return colu

def Filas(tablero):
	fil = []
	for fila in tablero:
		fil.append(fila)
	return fil

#La secuencia es el numero de columan donde se suelta la ficha, si es par al jugador 2 sino al 1
def completarTableroEnOrden(secuencia, tablero):
	
	y=1 #Comienza en 1 para que luego pueda comenzar el jugador 1
	for columna in secuencia:
		if (y % 2) ==0:  #Esta linea define que jugador va a ir, si "y" es par va a ir el jugador 2 de lo contrario el 1
			fichaNumero=2
			soltarFichaEnColumna(fichaNumero, columna, tablero)
			y=y+1  #Lo usamos para pasar el turno al jugador 2 ya que "y" sera par 
		else:
			fichaNumero=1
			soltarFichaEnColumna(fichaNumero, columna, tablero)
			y=y+1 #Lo usamos para pasar el turno al jugador 1 ya que "y" sera impar 
			
	return tablero

    
def soltarFichaEnColumna(ficha, columna, tablero):   
	for fila in range(6, 0, -1):
		if tablero[fila - 1][columna - 1] == 0:
			tablero[fila - 1][columna - 1] = ficha
			return 

def dibujarTablero(tablero):
	for fila in tablero:
		for celda in fila:
			if celda == 0:
				print(' 0 ',end=' ')
			
			else:
				print(' %s ' % celda, end=' ')
		print(' ')

def TableroValido(secuencia):
	for columna in secuencia:
		if columna < 1 or columna > 7:
		 return False
	return True


secuencia= [2,2,3,5]
tablero = []
if TableroValido(secuencia):
	tablero = completarTableroEnOrden(secuencia, tableroVacio())
	dibujarTablero(tablero)

else:
	print("Las columnas deben ser del 1 al 7")

print(contenidoColumna(2,tablero))
print(contenidoFila(5,tablero))

print("Las columnas son: ")
print(Columnas(tablero))

print("Las filas son: ")
print(Filas(tablero))


     
	