import socket
MSG_LEN = 20480

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8000))

while True:
    msg_send = input()
    client.send(msg_send.encode("utf8"))
    msg_receive = client.recv(MSG_LEN)
    print(msg_receive.decode("utf8"))
    if msg_receive.decode("utf8") == "bye":
        break
client.close()
