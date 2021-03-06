""" testing new scripts here """
"""for client side"""

import socket
from threading import *

class ServerSide:
    global conn
    def __init__(self):
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # (internet ver 4, socket TCP/IP)
        conn.connect(('192.168.1.2', 8081))  # ((IP address, post))
        print("Connection Established\n")

        server_message = "<You have connected with Server>\n"
        data = server_message.encode()
        conn.send(data)

        threadReceive = Thread(target=self.receiveData)
        threadSend = Thread(target=self.sendData)

        threadReceive.start()
        threadSend.start()

        threadReceive.join()
        threadSend.join()


    def sendData(self):
        while True:
            client_message = "Client: " + input()
            if client_message == "Client: x":
                print("[You have disconnected]")
                break
            client_data = client_message.encode()
            conn.send(client_data)

    def receiveData(self, conn):
        while True:
            server_data = conn.recv(1024)
            server_message = server_data.decode()
            if server_message == "Server: x":
                print("[Server has disconnected]")
                break
            print(server_message)

ServerSide()