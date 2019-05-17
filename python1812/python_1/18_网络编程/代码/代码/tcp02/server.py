import  socket

server = socket.socket()

server.bind(("10.36.131.32",6666))

server.listen(5)

conn,address = server.accept()

print("连接成功")

while True:
    clientData = conn.recv(1024)
    result = clientData.decode("utf-8")
    print("客户端对服务端说：",result)

    if result == "bye" or result == "再见":
        break

    sendData = input("请输入要给回复客户端的数据：")
    conn.send(sendData.encode("utf-8"))

server.close()






