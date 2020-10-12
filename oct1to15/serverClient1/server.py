"""for server side"""
import socket
from threading import *


class ServerSide:

    def __init__(self):
        global conn, runstate
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('192.168.1.2', 8081))  # ((IP address, post))
        server_socket.listen()  # continuously listens to requests on binded (address,port)
        print("Waiting for connection...")
        conn, address = server_socket.accept()
        print("Connection Established with", address, "\n")

        runstate = True

        server_message = "<You have connected with Server>\n"
        data = server_message.encode()
        conn.send(data)

        threadReceive = Thread(target=self.receiveData)
        threadSend = Thread(target=self.sendData)

        threadReceive.start()
        threadSend.start()

        threadReceive.join()
        print("Receive has stopped")
        threadSend.join()
        print("Send has stopped")

    def sendData(self):
        global conn, runstate
        while runstate:
            server_message = "Server: " + input("You: ")
            if server_message == 'Server: x':
                print("[You have disconnected]")
                runstate = False
            server_data = server_message.encode()
            conn.send(server_data)

    def receiveData(self):
        global conn, runstate
        while runstate:
            client_data = conn.recv(1024)
            client_message = client_data.decode()
            if client_message == "Client: x":
                print("[Client has disconnected]")
                runstate = False
            if runstate:
                print(client_message)


ServerSide()
