import socket
import threading

PORT = 5050

#SERVER = 127.0.0.1      # This is the hard coded IP address for my system 
SERVER = socket.gethostbyname(socket.gethostname())  # I have used this to dynamically change IP address if this program is used on another computer
ADDRESS = (SERVER, PORT)  # This to bind the server and port into a tuple 

print("Server IP :",SERVER)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)