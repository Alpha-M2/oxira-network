import socket
import threading
import json


class Node:
    def __init__(self, host, port):
        self.sock = socket.socket()
        self.sock.bind((host, port))
        self.sock.listen()

    def start(self):
        # Start accept loop in a daemon thread and return the Thread for testing
        t = threading.Thread(target=self.accept, daemon=True)
        t.start()
        return t

    def accept(self):
        while True:
            try:
                conn, _ = self.sock.accept()
                data = conn.recv(4096)
                # Attempt to decode JSON; if invalid, report and continue
                try:
                    print("Received:", json.loads(data))
                except json.JSONDecodeError:
                    print("Received invalid JSON")
            except OSError:
                # Socket closed or other I/O error; exit loop cleanly
                break
