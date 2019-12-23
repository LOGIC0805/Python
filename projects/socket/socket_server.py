import socket
import threading
MSG_LEN = 20480

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8000))
server.listen()


def handle_sock(sock, address):
    while True:
        msg_receive = sock.recv(MSG_LEN)
        print(msg_receive.decode("utf8"))
        # sock.send("Hello {}!".format(msg_receive.decode("utf8")).encode("utf8"))
        if msg_receive.decode("utf8") != "bye":
            msg_send = input()
            sock.send(msg_send.encode("utf8"))
        else:
            msg_send = "bye"
            sock.send(msg_send.encode("utf8"))
            break
    sock.close()


while True:
    sock, address = server.accept()
    client_thread = threading.Thread(target=handle_sock, args=(sock, address))
    client_thread.start()
# server.close()
