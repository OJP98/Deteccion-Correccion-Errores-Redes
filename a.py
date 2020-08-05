import binascii

mensaje = 'Que onda como vas? Soy la mera verga en persona'
binarioTemp=''
binario=''
for i in mensaje:
	binario+=bin(ord(i))[2:].zfill(8)

print(binario)
binarioTemp=binario
binarioTemp+=bin(0)[2:].zfill(8)
binarioTemp+=bin(0)[2:].zfill(8)

sumaInicial=int(binarioTemp,2)
modular=sumaInicial%65521
resta=65521-modular

binario+=bin(resta)[2:].zfill(16)
print(binarioTemp)
print(binario)

# initializing binary data 
bin_data =binario[0:len(binario)-16]

print(int(binario,2)%65521)
n = int(bin_data, 2)

print(binascii.unhexlify('%x' % n).decode())