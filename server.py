import socket
import threading
import tqdm



PORT = 5050
DISCONNECT_MESSAGE = "!DISCONNECT"
#SERVER = 127.0.0.1      # This is the hard coded IP address for my system 
SERVER = socket.gethostbyname(socket.gethostname())  # I have used this to dynamically change IP address if this program is used on another computer
ADDRESS = (SERVER, PORT)  # This to bind the server and port into a tuple 

print("Server is starting...")
print("Server IP :",SERVER)
print(f"Server listening on {ADDRESS} ")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)

server.listen()
client, addr = server.accept()



file_name = client.recv(1024).decode()
print(file_name)

#file_size = client.recv(1024).decode()
#print("Size of file :",file_size)

file = open(file_name, "wb")
file_bytes = b""

completed = False

pbar = tqdm.tqdm(unit="B", unit_scale=True, unit_divisor=1000) 


while not completed :
    data = client.recv(1024)
    
    if file_bytes[-5:] == b"<END>":
        completed = True
    else:
        file_bytes += data
    pbar.update(1024)
    
    
file.write(file_bytes)
file.close()
client.close()
server.close()
