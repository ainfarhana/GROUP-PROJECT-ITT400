import time
import socket
import sys
new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#host_name = socket.gethostname()
#s_ip = socket.gethostbyname(host_name)

port = 8080

new_socket.bind(("", port))
print("Request has been successful!")
print("This is your IP: ", '192.168.56.102')

name = input('Enter name: ')

new_socket.listen(1)


conn, add = new_socket.accept()

print("Received connection from ", add[0])
print('Connection Established. Connected From: ',add[0])

client = (conn.recv(1024)).decode()
print(client + ' has joined...')
conn.send(name.encode())
while True:
    message = input('Me : ')
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(client, ':', message)
