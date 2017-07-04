import socket

class MySocketServer():
    def __init__(self):
        self.s = socket.socket()
        self.host = socket.gethostname()
        self.port = 12345
        self.s.bind((self.host, self.port))
        print("bind to host %s, port %s" % (self.host, self.port))

    def start(self):
        self.s.listen(5)
        while True:
            c, addr = self.s.accept()
            print("Connection from %s" % str(addr))
            while True:
                message = c.recv(1024)
                print(message)
                if message == "BYE":
                    print("BYE received")
                    c.close()
                    break


    def close(self):
        self.s.close()


if __name__ == '__main__':
    server = MySocketServer()

    server.start()

    server.close()


