import socket


class FileServerClient:
    def __init__(self, address, port):
        """
        Create tcp/ip socket
        And connect to the address:port
        """
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((address, port))

    def __del__(self):
        self.sock.close()

    def write(self, message):
        """
        Send files to file server over tcp connection
        """
        try:
            self.sock.send((str(message) + "\r\n").encode())
            self.sock.recv(1)
        except Exception:
            return False

        return True
