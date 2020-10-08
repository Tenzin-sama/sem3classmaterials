"""for client side"""
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # (internet ver 4, socket TCP/IP)
client_socket.connect(('127.0.0.1', 8081))  # ((IP address, post))
print("Connection Established\n")

data=client_socket.recv(1024)
message=data.decode()
print('Received message from server:')
print(message)

client_message = "Client: Hello!"
data = client_message.encode()
client_socket.send(data)
