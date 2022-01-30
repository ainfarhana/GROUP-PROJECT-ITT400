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
