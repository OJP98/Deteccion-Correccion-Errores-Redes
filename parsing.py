from bitarray import bitarray
from random import randint, choices, choice
from math import log2
import pickle

# Función que recibe un string para convertirlo a un string binario
def ConvertToBinaryString(message):
	return ''.join(bin(ord(x))[2:].zfill(8) for x in message)

# Función que recibe un bitarray para convertirlo a string con decodificación 'utf-8'
def ConvertBitarrayToString(array):
	array = bitarray(array)
	return array.tobytes().decode("utf-8")

# Función para convertir un bitarray a un string binario
def ConvertBitarrayToBinaryString(array):
	result = ""
	for val in array:
		if val:
			result = result + "1"
		else:
			result = result + "0"
	return result

# Función que simula ruido en una cadena binaria basado en una tasa de errores por bits.
def SimulateNoise(data, rate = None):
	if rate == None: rate = 1
	amountErr = 0

	for bit in data:
		createNoise = choices([True, False], weights=(rate, 100-rate))

		if createNoise[0]:
			amountErr += 1
			position = randint(1, len(data)-1)
			if data[position] == "1":
				data = data[:position] + "0" + data[position+1:]
			else:
				data = data[:position] + "1" + data[position+1:]

	print("Cantidad de errores en la cadena con ruido:", amountErr)
	return data


# Fucnión que serializa un bitarray con pickle y devuelve el nombre del archivo
def SerializeData(data):
	filename = "serialized_data"
	with open(filename, "wb") as file:
		pickle.dump(data, file)

	return filename

# Función que deserializa data con pickle y devuelve la data del archivo
def LoadData(data):
	received_data = pickle.load(open(data,"rb"))
	# Debería devolver un bitarray
	return received_data


# HAMING CODE IMPLEMENTATION

# Calulcar los bits redundantes de un string binario
def RedundantBits(data):
	# En base a la fórmula explicada en: https://www.geeksforgeeks.org/hamming-code-in-computer-network/
	for iteration in range(len(data)):
		if 2**iteration >= len(data) + iteration + 1:
			return iteration

# Crea el string de datos con los bits redundantes
def CreateSerializedData(data, bits):

	counter_from_0 = 0
	counter_from_1 = 1
	serialized_data = ""
	# Se recorre el array
	for bit in range(1, len(data) + bits+1):
		# Si la posición es par, se agrega un 0
		if bit == 2**counter_from_0:
			serialized_data = serialized_data + "0"
			counter_from_0 += 1
		# De lo contrario, se usa la posición de la data original
		else:
			serialized_data = serialized_data + data[-counter_from_1]
			counter_from_1 += 1

	return ''.join(reversed(serialized_data))

# Determina y devuelve los bits de paridad de un string de datos
def DetermineParityBits(data, parity):
  
	# For finding rth parity bit, iterate over 
	# 0 to r - 1 
	for i in range(parity): 
		result = 0

		for j in range(0, len(data)): 
			j += 1
			# a = AND bitwise
			a = j & 2**i
			if a == 2**i:
				# b = XOR
				b = data[j * -1]
				result = result ^ int(b) 
  
		# Se inserta el bit de paridad
		newPosition = len(data) - (2**i)
		data = data[:newPosition] + str(result) + data[newPosition+1:] 
	return data 

# Convierte un mensaje binario a codigo hamming
def ConvertBinaryStringToHamming(message):
	redundantBits = RedundantBits(message)
	data = CreateSerializedData(message, redundantBits)
	return DetermineParityBits(data, redundantBits)


# Convierte un codigo hamming a un mensaje cualquiera
def ConvertHammingToMessage(hamming):
	n = len(hamming)
	iterations = log2(n)

	for i in range(round(iterations)+1):
		newPosition = n - 2**i
		hamming = hamming[:newPosition] + hamming[newPosition + 1:]

	return hamming

# Detecta y corrige errores con el codigo hamming
def DetectAndReplaceError(data):
	data = ConvertBitarrayToBinaryString(data)
	redundantBits = RedundantBits(data)

	position = 0

	for i in range(redundantBits):
		contBits = 0
		for j in range(1, len(data) + 1):
			# Hacer un bitwise AND
			if j & (2**i) == 2**i:
				# XOR con el valor previo
				contBits = contBits ^ int(data[j * -1])

		# Se crea un numero binario juntando los bits de paridad
		position = position + contBits * (10**i)

	# Posicion del error
	position = int(str(position), 2)

	# Corregir el error encontrado
	if position != 0:
		eliminar = len(data) - position
		data = data[:eliminar] + str((int(data[eliminar]) + 1) % 2) + data[eliminar + 1:]

	return data


# _____________EJEMPLO_____________

cadena = "Hola"

# Convertir texto binario
cadena_binaria = ConvertToBinaryString(cadena)
print("Mensaje en binario:", cadena_binaria)

# Convertir texto binario a codigo hamming
cadena_hamming = ConvertBinaryStringToHamming(cadena_binaria)
print("Mensaje en codigo hamming:", cadena_hamming)

# Simular ruido en texto binario
cadena_con_ruido = SimulateNoise(cadena_hamming, 1)
print("Mensaje con ruido:", cadena_con_ruido)

# Convertir a bitarray
cadena_con_ruido = bitarray(cadena_con_ruido)

# Serializar archivo con pickle
file = SerializeData(cadena_con_ruido)

# ENVIAR Y RECIBIR MENSAJE
print("\n\nENVIAR Y RECIBIR MENSAJE CON SOCKETS\n\n")

# Recibir cadena con ruido de pickle
cadena_con_ruido = LoadData(file)
print("Mensaje recibido (con ruido):", cadena_con_ruido)

# Corregir texto binario con ruido (SOLO PARA HAMMING)
cadena_corregida = DetectAndReplaceError(cadena_con_ruido)
print("Mensaje en binario corregido:", cadena_corregida)

# Convertir texto en codigo hamming a texto binario
cadena_string = ConvertHammingToMessage(cadena_corregida)
print("Mensaje de hamming a texto binario:", cadena_string)

mensaje_recibido = ConvertBitarrayToString(cadena_string)
print("Mensaje recibido: ", mensaje_recibido)