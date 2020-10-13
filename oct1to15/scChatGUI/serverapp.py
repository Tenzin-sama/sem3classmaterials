"""for server side"""
import socket
from threading import *
from tkinter import *


class ServerGUI:

    def __init__(self):

        global conn, runstate  # shared variable across all modules

        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('192.168.1.2', 8081))  # ((IP address, post))
        server_socket.listen()  # continuously listens to requests on binded (address,port)
        print("Waiting for connection...")
        conn, address = server_socket.accept()
        # print("Connection Established with", address, "\n")  # after a client connects

        runstate = True  # to dictate whether to continue running or stop

        server_message = "<You have connected with Server>\n"
        data = server_message.encode()
        conn.send(data)

        # using threads to run both receive and send in parallel
        threadReceive = Thread(target=self.receiveData)
        threadSend = Thread(target=self.sendData)

        threadReceive.start()
        threadSend.start()

        # when the threaded functions have stopped
        threadReceive.join()
        input("Log: Receive has stopped. Press enter twice to end the program\n")
        threadSend.join()
        print("Log: Send has stopped. Program has ended")
        server_socket.close()

    def sendData(self):
        """funtion to send data to client"""
        global conn, runstate
        while runstate:
            server_message = "Server: " + input()
            if server_message == 'Server: x':
                print("[You have disconnected]")
                print("...please wait...\n")
                runstate = False
            server_data = server_message.encode()
            conn.send(server_data)

    def receiveData(self):
        """function to receive data from client"""
        global conn, runstate
        while runstate:
            client_data = conn.recv(1024)
            client_message = client_data.decode()
            if client_message == "Client: x":  # if client has disconnected
                print("[Client has disconnected]")
                runstate = False
            if runstate:
                print(client_message)


ServerGUI()
