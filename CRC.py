import binascii
OVERHEAD=16
'''
	Esta funcion calcula el valor 
	de verificacion adujunta del mensaje
'''
def construirMensaje(mensaje):
	
	binarioTemp=''
	binario=''
	#Traducimos el mensaje a binario 
	#y lo rellenamos con 8 bits
	for i in mensaje:
		binario+=bin(ord(i))[2:].zfill(8)

	#print(binario)
	#Agregamos 16 bits en blanco
	binarioTemp=binario
	binarioTemp+=bin(0)[2:].zfill(OVERHEAD)

	#Calculamos cuanto hace falta
	#para que nuestro mensaje modular
	# 65521 sea igual a 0
	sumaInicial=int(binarioTemp,2)
	modular=sumaInicial%65521
	resta=65521-modular

	#Finalmente esa diferencia la 
	#agregamos a nuestro mensaje
	binario+=bin(resta)[2:].zfill(OVERHEAD)
	#print(binarioTemp)
	#print(binario)

	return binario

'''
	Este metodo determina si
	hay errores o no
'''
def check(binario):
	#Si es modular 65521 entonces
	#Sabemos que no hay errores
	if((int(binario,2)%65521)==0):
		return('No hay error')
	else:
		return('Si hay error')

def getText(binario):
	bin_data =binario[0:len(binario)-OVERHEAD]
	n = int(bin_data, 2)	
	return(binascii.unhexlify('%x' % n).decode())


'''
binario=construirMensaje("Que onda papu")
print(check(binario))
print(getText(binario))
'''