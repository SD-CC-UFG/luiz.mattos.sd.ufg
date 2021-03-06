import socket
import pickle
import threading

class Cliente:
    def __init__(self):
        self.sock = None
        self.ip = None
        self.port = None
        self.s = None

    def newSocket(self):
        self.sock.close()
        self.criaSocketTcp()

    def criaSocketTcp(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def criaSocketUdp(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def requestAdress(self, servidor):
        self.setCamposSocket('127.0.0.1',9996)

        if self.s is None: self.criaSocketTcp()
        else: self.newSocket()

        self.conect()

        if servidor is None: msg = input()
        else: msg = servidor

        msgSerializada = pickle.dumps(msg)

        self.s.send(msgSerializada)

        msgSerializada = self.s.recv(1024)

        msg = pickle.loads(msgSerializada)

        print ("Resposta do server: ",msg)

        self.host, self.port = msg

        self.newSocket()

        self.conect()

    def comunica(self):
        while True:
            msg = input("Digite sua mensagem: ")

            if msg == 'exit': break
            elif msg == 'mySQL' or msg == 'HTTP': self.requestAdress(msg)
            else:
                print ("MSG QUE IRA PRO DNS: ",msg)

                msgSerializada = pickle.dumps(msg)

                self.s.send(msgSerializada)

                msgSerializada = self.s.recv(1024)

                msg = pickle.loads(msgSerializada)

                print ("Resposta do server: ", msg)

    def setCamposSocket(self, h, p):
        self.host = h
        self.port = p
        self.dest = (self.host, self.port)

    def conect(self):
        dest = (self.host,self.port)
        self.s.connect(dest)

    def exit(self):
        self.s.close()

cliente = Cliente()

cliente.requestAdress(None)

cliente.comunica()

cliente.exit()