'''
Autores: 	Jose Cifuentes
			Oscar Juarez

31/07/2020
'''

import socket     
import pickle               
  
cliente = socket.socket()          
  
# Definimos el puerto al que queremos conectarnos
port = 12345                
  
# Hacemos la conexion local
cliente.connect(('127.0.0.1', port)) 
  
# Recibimos la informacion del servidor
mensaje=cliente.recv(1024)
print("Mensaje serializado: "+str(mensaje))
print ("Mensaje : "+str(pickle.loads(mensaje))) 

# Cerramos la conexion
cliente.close()