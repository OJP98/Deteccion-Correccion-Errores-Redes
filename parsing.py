from bitarray import bitarray
from random import randint, choices, choice

# Función que recibe un string para convertirlo a bitarray
def ConvertStringToBitarray(message):
	binary = ''.join(bin(ord(x))[2:].zfill(8) for x in message)
	return bitarray(binary)

# Función que recibe un bitarray para convertirlo a string con decodificación 'utf-8'
def ConvertBitarrayToString(array):
	return array.tobytes().decode("utf-8")

# Función que simula ruido en un bitarray basado en una tasa de errores por bits.
def SimulateNoise(array, rate = None):
	if rate == None: rate = 1

	for bit in array:
		createNoise = choices([True, False], weights=(rate, 100-rate))

		if createNoise[0]:
			position = randint(0, len(array)-1)
			errorType = choice(["add", "remove", "replace"])

			# Se agrega un bit
			if errorType == "add":
				array = array[:position] + str(randint(0, 1)) + array[position:]
			# Se quita un bit
			elif errorType == "remove": 
				array = array[:position] + array[position+1:]
			# Se reemplaza un bit
			else:
				if array[position]:
					array = array[:position-1] + "0" + array[position:]
				else:
					array = array[:position-1] + "1" + array[position:]

	return array
