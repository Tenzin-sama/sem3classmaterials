"""for server side"""
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # (internet ver 4, socket TCP/IP)
server_socket.bind(('0.0.0.0', 8081))  # ((IP address, post))
server_socket.listen()  # continuously listens to requests on binded (address,port)
print("Waiting for connection...")
connection_socket, address = server_socket.accept()  # if a request is found, the request is accepted. Returns
print("connection Established with",address)
# print(connection_socket)
# print("")
# print(address)
server_message = "Sever: Thank you for sending the request."
data = server_message.encode()
connection_socket.send(data)
"""
HW:
establish two-way communication,
meaning client can send data to server as well
"""

client_message = connection_socket.recv(1024)
client_message = client_message.decode()
print(client_message)

input()
"""Abandoned: Refer to 'serverClient1' folder for actual work on this assignment"""
