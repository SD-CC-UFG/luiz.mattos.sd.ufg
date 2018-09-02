import socket
import pickle
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = '127.0.0.1'
PORT = 9996
dest = (HOST, PORT)

s.connect(dest)

def waitingResponse():
	data = s.recv(1024)
	
	msg = pickle.loads(data)
	
	print ("RESPOSTA RECEBIDA: ", msg)
	

while True:
	msg = input("DIGITAE: ")
	
	msgSerializada = pickle.dumps(msg)

	s.send(msgSerializada)
	
	t = threading.Thread(target=waitingResponse , args = ())
	t.start()
	
	if msg == 'exit': break
	 
s.close()