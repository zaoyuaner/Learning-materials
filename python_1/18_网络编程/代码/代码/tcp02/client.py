import  socket

client = socket.socket()

client.connect(("10.36.131.32",6666))

while True:
    sendData = input("请输入要发送给服务端的数据：")
    client.send(sendData.encode("utf-8"))

    serverData = client.recv(1024)
    result = serverData.decode("utf-8")
    print("服务端回复：",result)

    if result == "bye":
        break

client.close()
