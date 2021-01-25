import socket
import thread
import sys


port = int(raw_input("enter port to bind to .... : "))
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("", port))
sock.listen(3)

while true:
    connection, address = sock.accept()
    data = connection.recv(512)
    sock.close()
