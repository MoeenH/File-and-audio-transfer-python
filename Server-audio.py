from vidstream import AudioSender
from vidstream import AudioReceiver

import threading

import socket

ip = socket.gethostbyname(socket.gethostname())

receiver = AudioReceiver (ip, 5050)
receive_thread = threading.Thread(target=receiver.start_server)

sender = AudioSender ('', 5555)
sender_thread = threading.Thread(target=sender.start_stream)

receive_thread.start()
sender_thread.start()
