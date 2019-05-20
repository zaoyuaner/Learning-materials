import socket
import threading

server = socket.socket()

# 绑定地址
server.bind(('127.0.0.1', 8888))

# 监听
server.listen(5)


def process_client(client_socket):
    while True:
        data = client_socket.recv(1024)
        client_socket.send(data)


while True:
    client_socket, client_addr = server.accept() # 是一个阻塞的方法
    threading.Thread(target=process_client, args=(client_socket,)).start()

