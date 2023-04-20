import socket
import os

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
#SERVER = 127.0.0.1      # This is the hard coded IP address for my system 
SERVER = socket.gethostbyname(socket.gethostname())  # I have used this to dynamically change IP address if this program is used on another computer
ADDRESS = (SERVER, PORT)  


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)

file = open("test_image.png","rb")
#file_size = os.path.getsize("test_image.png")

client.send("receiving_file.png".encode())
#client.send(str(file_size).encode())


data = file.read()
client.sendall(data)
client.send(b"<END>")

file.close()
client.close()