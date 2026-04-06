# Group Chat application using Python TCP sockets

Info:
A simple group chat that can handle multiple users with raw TCP sockets and pythons "threading" module. 
Rules:
Unable to use SocketIO, no external dependencies outside of Pythons standard library.
---
## Files:
server.py - chat server which runs on a dedicated host
client.py - chat client which runs on each participant's machine
---
## How-To use application:

### 1. Start the server 
'''bash
python3 sever.py
'''

The sever listens on ***port _*** by default. 

### 2. Connect a client on a different host

'''bash
python3 clent.py <server_ip>
'''

---
Enter username 
---

## Requirements
- Python
- Standard library
- Works on linux


