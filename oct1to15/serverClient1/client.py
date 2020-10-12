"""for client side"""
import socket
from threading import *


class ServerSide:

    def __init__(self):
        global conn, runstate

        runstate = True

        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # (internet ver 4, socket TCP/IP)
        conn.connect(('192.168.1.2', 8081))  # ((IP address, post))
        print("Connection Established\n")

        server_message = "<A Client has connected>\n"
        data = server_message.encode()
        conn.send(data)

        threadReceive = Thread(target=self.receiveData)
        threadSend = Thread(target=self.sendData)

        threadReceive.start()
        threadSend.start()

        threadReceive.join()
        threadSend.join()

    def sendData(self):
        global conn, runstate
        while runstate:
            client_message = "Client: " + input("You: ")
            if client_message == "Client: x":
                print("[You have disconnected]")
                runstate = False
            client_data = client_message.encode()
            conn.send(client_data)

    def receiveData(self):
        global conn, runstate
        while runstate:
            server_data = conn.recv(1024)
            server_message = server_data.decode()
            if server_message == "Server: x":
                print("[Server has disconnected]")
                runstate = False
            if runstate:
                print(server_message)


ServerSide()
