
# Socket Programming Assignment

Socket Programming
Objective: The objective of this assignment is to implement a socket programming solution that
can transfer files between two hosts.

Bonus: An extra credit will be given if the solution can broadcast audio from the server to the
client, like a phone call.

Instructions:

• You can use C++, Java, or Python for this assignment.

• You are allowed to use any library or framework for socket programming in your chosen
programming language.

• Your solution should consist of two programs: a client program and a server program.

• The client program should be able to connect to the server program over a network and
send a file to the server.

• The server program should be able to receive the file sent by the client and save it on its
local filesystem.

• Your solution should be able to handle large files.

• Your solution should implement error checking and handling to ensure that files are
transferred correctly.

• Your solution should handle the case when the server is offline or cannot be reached.

• Your code should be well-documented, with clear and concise comments explaining the
purpose and function of each section of code.

Bonus:
• If your solution can broadcast audio from the server to the client, you will receive extra
credit.

• The audio broadcasting feature should work in real-time, with minimal latency.

• Your solution should implement error checking and handling to ensure that audio is
transmitted correctly.
## Authors

- [@MoeenH](https://www.github.com/MoeenH)


## Deployment

To deploy this project:

```bash
  python server.py

  python client.py


```
```python
  
  file = open("(FILE PATH)","rb")
  client.send("(FILE NAME AT DESTINATION)".encode())


```


