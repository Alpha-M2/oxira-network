import socket
import threading
import json


class Node:
    def __init__(self, host, port):
        self.sock = socket.socket()
        self.sock.bind((host, port))
        self.sock.listen()

    def start(self):
        threading.Thread(target=self.accept).start()

    def accept(self):
        while True:
            conn, _ = self.sock.accept()
            data = conn.recv(4096)
            print("Received:", json.loads(data))
