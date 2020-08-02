'''
Autores: 	Jose Cifuentes
			Oscar Juarez

31/07/2020
'''

import socket 
import pickle               
  
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

# Solicitamos el mensaje y lo enviamos 
mensaje=input("Ingrese el mensaje que desea enviar: ")

mensaje=pickle.dumps(mensaje)
client.send(mensaje) 

# Se cierra la conexion 
client.close()
