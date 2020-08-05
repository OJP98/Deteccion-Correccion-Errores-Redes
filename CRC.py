import binascii

def construirMensaje(mensaje):
	
	binarioTemp=''
	binario=''
	for i in mensaje:
		binario+=bin(ord(i))[2:].zfill(8)

	#print(binario)
	binarioTemp=binario
	binarioTemp+=bin(0)[2:].zfill(8)
	binarioTemp+=bin(0)[2:].zfill(8)

	sumaInicial=int(binarioTemp,2)
	modular=sumaInicial%65521
	resta=65521-modular

	binario+=bin(resta)[2:].zfill(16)
	#print(binarioTemp)
	#print(binario)

	return binario

def check(binario):
	if((int(binario,2)%65521)==0):
		return('No hay error')
	else:
		return('Si hay error')

def getText(binario):
	bin_data =binario[0:len(binario)-16]
	n = int(bin_data, 2)	
	return(binascii.unhexlify('%x' % n).decode())


'''
binario=construirMensaje("Que onda papu")
print(check(binario))
print(getText(binario))
'''