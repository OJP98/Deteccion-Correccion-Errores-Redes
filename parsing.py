from bitarray import bitarray

# Función que recibe un string para convertirlo a bitarray
def ConvertStringToBitarray(message):
	binary = ''.join(bin(ord(x))[2:].zfill(8) for x in message)
	return bitarray(binary)

# Función que recibe un bitarray para convertirlo a string con decodificación 'utf-8'
def ConvertBitarrayToString(array):
	return array.tobytes().decode("utf-8")
