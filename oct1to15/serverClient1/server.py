"""for server side"""
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # (internet ver 4, socket TCP/IP)
server_socket.bind(('0.0.0.0', 8081))  # ((IP address, post))
server_socket.listen()  # continuously listens to requests on binded (address,port)
print("Waiting for connection...")
connection_socket, address = server_socket.accept()  # if a request is found, the request is accepted. Returns
print("connection Established with",address)

client_message = connection_socket.recv(1024)
client_message = client_message.decode()
print(client_message)

while True:
    server_message = "Server:" + input(">>")
    data = server_message.encode()
    connection_socket.send(data)
    if server_message == 'Server:x':
        print("[You have disconnected]")
        break