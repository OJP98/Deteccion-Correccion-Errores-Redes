from bitarray import bitarray
from random import randint, choices, choice
import pickle

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
			errorType = choice(["replace"])

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



# _____________EJEMPLO_____________

# EMISOR:
cadena = "Hola_mundo"

# Armar bitarray
array_de_bits = ConvertStringToBitarray(cadena)
print("La cadena original es:", array_de_bits)

# Simular ruido y serializar data
array_de_bits_con_ruido = SimulateNoise(array_de_bits, 1) # probabilidad que 1/100 bits cambie
archivo_serializado = SerializeData(array_de_bits_con_ruido)

print("Se va enviar de forma empaquetada:", array_de_bits_con_ruido)

	# ENVIAMOS CON SOCKETS EL ARCHIVO SERIALIZADO

# RECEPTOR:
	# RECIBIMOS ARCHIVO SERIALIZADO CON SOCKETS
informacion_recibida = LoadData(archivo_serializado) # Esto desenpaqueta un bitarray
print("Se recibe:", informacion_recibida)
	# DETECTAMOS Y CORREGIMOS ERRORES CON ALGORITMOS
informacion_corregida = ConvertBitarrayToString(informacion_recibida) # Aún no hay correción de errores, esto puede dar una cadena rara
print(informacion_corregida)
