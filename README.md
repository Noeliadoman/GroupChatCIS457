# Group Chat application using Python TCP sockets

Info:
- A simple group chat that can handle multiple users with raw TCP sockets and pythons "threading" module. 
- Rules:
- Unable to use SocketIO, no external dependencies outside of Pythons standard library.
---
## Files:
- server.py - chat server which runs on a dedicated host
- client.py - chat client which runs on each participant's machine
---
## Overall Design of Chat Server

### 1. Purpose
The chat server is responsible for managing multiple client connections simultaneously, receiving messages from connected clients, and broadcasting those messages to all other active clients in real time.

### Chat Server Design
The server is implemented as a single python class that owns the listening socket, the shared client list anda  threading socket. A new thread is created for each connected client, allowing the server to handle multiple clients. 

### Chat Client Design
The client is implemented as a single python class that owns the TKinter GUI, the TCP socket and a background thread for receiving messages. All socket I/O happens off the main thread; all GUI updates are dispatched back to the main thread using root.after().

## Team Responsilibity & Developer Coordination 
### Task Breakdown:
- Noelia Doman: design and implement the server class, implemented thread-safe client list management using thread.Lock, implemented broadcast_message() with concurrent-safe list snapshot, wrote server-side error handling
- Sam Rois - Designed and implemented the Client class, built the TKinter GUI, implemented the two-thread architecture, fixed lambda closure bug

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


