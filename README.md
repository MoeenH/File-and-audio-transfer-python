
# Socket Programming Assignment

Socket Programming
Objective: The objective of this assignment is to implement a socket programming solution that
can transfer files between two hosts.



Bonus Part:
• Open Server-audio.py file for the audio streaming question

## Authors

- [@MoeenH](https://www.github.com/MoeenH)


## Deployment

To deploy the first part of the project:



```bash
  pip install socket  #Library to establish connection
  pip install tqdm  #Library to print a progress bar

  python server.py #run this file first

  python client.py #run this file after server.py


```
```python
  # in server.py and client.py you can hardcode your ip and port
  file = open("(FILE PATH)","rb")   
  client.send("(FILE NAME AT DESTINATION)".encode())

  # Or else you can use this to automatically get the ip of the system
  SERVER = socket.gethostbyname(socket.gethostname())

```

To deploy the second part of the assignment:

```bash
   pip install vidstream # a opensource library available to stream audio and video

```
Now the Server-audio.py will be run on different systems. to run on the same network use the local ip address.
-to run over the internet use public ip and relevant port.

```python
  receiver = AudioReceiver (ip, 5050) 
  receive_thread = threading.Thread(target=receiver.start_server)

  sender = AudioSender (ip2, 5555)
  sender_thread = threading.Thread(target=sender.start_stream)

  # the other host would have the same script but the ip and ports will be swapped, in order to establish connection between both the devices

  receiver = AudioReceiver (ip2, 5555) 
  receive_thread = threading.Thread(target=receiver.start_server)

  sender = AudioSender (ip, 5050)
  sender_thread = threading.Thread(target=sender.start_stream)


```

