import socket

class MySocketClient():
    def __init__(self):
        self.s = socket.socket()
        self.host = socket.gethostname()
        self.port = 12345
        self.s.connect((self.host, self.port))

    def send(self, message):
        self.s.send(message)

    def close(self):
        self.s.close()


if __name__ == '__main__':
    client = MySocketClient()

    line = ""

    while line <> "BYE":
        line = raw_input("Enter message to be sent:")
        client.send(line)
        if line == "BURST":
            for i in range(1000):
                s = str(i) + '\n'
                print(s)
                client.send(s)


    client.close()


