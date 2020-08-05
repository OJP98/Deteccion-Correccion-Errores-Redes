'''
Autores: 	Jose Cifuentes
			Oscar Juarez

31/07/2020
'''

import socket 
import pickle   
import CRC
import sys
import time
from parsing import *
from bitarray import bitarray

  
server = socket.socket()          
print ("Se crea el socket correctamente")
  
#Definimos el puerto donde el servidor va a estar esperando conexiones
port = 12345                
  
server.bind(('', port))         
print ("Servidor escuchando en el puerto: %s" %(port) )
  
# Definimos el socket en modo escucha 
server.listen(5)                
   
# Establecer conexion con un cliente
client, addr = server.accept()      
print ('Cliente conectado de: ', addr) 
print()

# Solicitamos el mensaje y lo enviamos 
mensaje = input("Ingrese el mensaje que desea enviar: ")
tasa_de_errores = int(input("Ingrese la tasa de errores por bit: "))

start = time.time()
# Armar bitarray
try:
	if(sys.argv[1]=='CRC'):
		array_de_bits = CRC.construirMensaje(mensaje)

	elif sys.argv[1] == "hamming":
		cadena_binaria = ConvertToBinaryString(mensaje)
		array_de_bits = ConvertBinaryStringToHamming(cadena_binaria)

except Exception as e:
	array_de_bits = ConvertStringToBitarray(mensaje)

print("La cadena original es:", array_de_bits)

# Simular ruido y serializar data
array_de_bits_con_ruido = SimulateNoise(array_de_bits, tasa_de_errores) # probabilidad que 1/100 bits cambie
print("La cadena con ruido es:", array_de_bits_con_ruido)

bitarray_con_ruido = bitarray(array_de_bits_con_ruido)
print(bitarray_con_ruido)

mensaje = pickle.dumps(bitarray_con_ruido)

client.send(mensaje) 

# Se cierra la conexion 
client.close()
end = time.time()

print("Tiempo de envío de mensaje: "+ str(end-start))