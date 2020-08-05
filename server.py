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
mensaje=input("Ingrese el mensaje que desea enviar: ")

start = time.time()
# Armar bitarray
try:
	if(sys.argv[1]=='CRC'):
		array_de_bits = CRC.construirMensaje(mensaje)
except Exception as e:
	array_de_bits = ConvertStringToBitarray(mensaje)

print("La cadena original es:", array_de_bits)

# Simular ruido y serializar data
array_de_bits_con_ruido = SimulateNoise(array_de_bits, 1) # probabilidad que 1/100 bits cambie

mensaje=pickle.dumps(array_de_bits_con_ruido)

client.send(mensaje) 

# Se cierra la conexion 
client.close()
end = time.time()

print("Tiempo de envío de mensaje: "+ str(end-start))