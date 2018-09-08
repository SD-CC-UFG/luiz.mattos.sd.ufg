import socket
import threading
import pickle
import time

HOST = ''              # Endereco IP do Servidor
PORT = 9996            # Porta que o Servidor esta

def conectado(con, cliente):
	print ("Cliente conectado server DNS")
	
	msgSerializada = con.recv(1024)
	msg = pickle.loads(msgSerializada)
	
	print ("MENSAGEM RECEBIDA DO CLIENTE: ",msg)
		
	if msg == 'mySQL':
		msg = ('127.0.0.1',9997)
	elif msg == 'HTTP':
		msg = ('127.0.0.1',9998)
	elif msg == 'CHAT':
		msg = ('127.0.0.1',9999)
	else: msg = ('127.0.0.1',9996)
	
	
	msgSerializada = pickle.dumps(msg)
	
	print ("MSG QUE SERA ENVIADA: ",msg)
	
	con.send(msgSerializada)
	
	
	con.close()
	
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

orig = (HOST, PORT)
 
s.bind(orig)
s.listen(1)

while True:
	con, cliente = s.accept()
	t = threading.Thread(target=conectado ,args=(con, cliente))
	t.start()

s.close()