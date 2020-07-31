'''
Autores: 	Jose Cifuentes
			Oscar Juarez

31/07/2020
'''

import socket                
  
cliente = socket.socket()          
  
# Definimos el puerto al que queremos conectarnos
port = 12345                
  
# Hacemos la conexion local
cliente.connect(('127.0.0.1', port)) 
  
# Recibimos la informacion del servidor
print (cliente.recv(1024)) 

# Cerramos la conexion
cliente.close()