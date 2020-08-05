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
  
cliente = socket.socket()          
  
# Definimos el puerto al que queremos conectarnos
port = 12345                
  
# Hacemos la conexion local
cliente.connect(('127.0.0.1', port)) 
  

# Recibimos la informacion del servidor
mensaje = cliente.recv(1024)

start = time.time()

try:
	if(sys.argv[1]=='CRC'):
		print(pickle.loads(mensaje))
		print(ConvertBitarrayToBinaryString(pickle.loads(mensaje)))
		mensajeString=ConvertBitarrayToBinaryString(pickle.loads(mensaje))
		print(CRC.check(mensajeString))
		print()
		print("Mensaje "+CRC.getText(mensajeString))

	elif sys.argv[1] == "hamming":
		cadena_con_ruido = pickle.loads(mensaje)

		# Corregir texto binario con ruido (SOLO PARA HAMMING)
		cadena_corregida = DetectAndReplaceError(cadena_con_ruido)

		# Convertir texto en codigo hamming a texto binario
		cadena_string = ConvertHammingToMessage(cadena_corregida)

		mensaje_recibido = ConvertBitarrayToString(cadena_string)
		print("Mensaje recibido: ", mensaje_recibido)

except Exception as e:
	print ("Mensaje : "+str(ConvertBitarrayToString(pickle.loads(mensaje)))) 




# Cerramos la conexion
cliente.close()
end = time.time()

print("Tiempo de interpretación del mensaje: "+str(end - start))