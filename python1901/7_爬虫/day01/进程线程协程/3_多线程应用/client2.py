import socket


client = socket.socket()

client.connect(('127.0.0.1', 8888))

while True:
    data = b'client2'
    client.send(data)
    recv_data = client.recv(1024)
    print(recv_data)
