import socket
import time
import sys

class Server:
    """
    Server as described in RFC 868 is waiting for connection and then sends 32-bit
    binary number containing number of seconds elapsed from 1st of January 1970

    Example:
	serever = Server()
    """
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(('localhost', 37)) # dont forget to change IP address to corresponding one
        print('Listening on port 37')
        self.operate()

    def operate(self):
        while True:
            data, address = self.sock.recvfrom(1)
            self.sock.sendto(bin(int(time.time()))[2:].encode(), address)
            print("Remote host {} connected, Response: {}".format(address[0], bin(int(time.time()))[2:]))
            print("Remote host {} disconnected.".format(address[0]))


class Client:
    """
    Client side for obtaining time in format specified at RFC 868
    
	Example:
	Client(time_server=("X.X.X.X", Y))
    """
    def __init__(self, time_server):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.sendto(b'', time_server)
        
        try:
            data, server = self.sock.recvfrom(32)
        except Exception as e:
            print(e)
            self.sock.close()
            sys.exit()
        
        self.sock.close()
        print("Received time: {}".format(data.decode()))

Client(time_server=('localhost', 37))