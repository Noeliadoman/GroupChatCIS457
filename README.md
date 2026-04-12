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
# Overall Design of Chat Server

### Purpose
The chat server is responsible for managing multiple client connections simultaneously, receiving messages from connected clients, and broadcasting those messages to all other active clients in real time.
#### Data Strcutures
- Self.clients - list of dict - holds one entry per active client.
- self.lock - threading.Lock - prevents when threads can add or remove clients simultaneously.
- self.socket - socket.socket - server's TCP listening socket.
- client dict - {'client_name': str, 'client_socket': socket}
#### Operations
- Constructor - __init__ - creates and brinds the TCP socket
- listen - listen() - on new connections it gets client name, the lock to append the client record, broadcasts a join message and starts a thread.
- hanlde_new_client - handle_new_client(client) - loops on recv(1024). Broadcasts a leave message and removes client when prompted. 
- broadcast_message - broadcast_message(sender, msg) - sends msg to every client whose name is different than the senders. 
#### Concurrency Model
Each client is served by its own daemon thread. The threading.Lock ensures the shared clients list is never modified by two threads simultaneously. broadcast_message() copies the list before iterating, so a disconnect mid-broadcast does not corrupt the loop.

### Chat Server Design
The server is implemented as a single python class that owns the listening socket, the shared client list anda  threading socket. A new thread is created for each connected client, allowing the server to handle multiple clients. 

### Chat Client Design
The client is implemented as a single python class that owns the TKinter GUI, the TCP socket and a background thread for receiving messages. All socket I/O happens off the main thread; all GUI updates are dispatched back to the main thread using root.after().
#### Data Strcutures
- Self.socket - socket.socket - TCP socket connected to HOST:PORT.
- self.name - str - display name entered at startup via simpledialog.prevents when threads can add or remove clients simultaneously.
- self.root - tk.Tk - Root tkinter window.
- self.chat_text - tk.Text - Read-only scrollable text area showing conversation history
- self.input_text - tk.Text - Editable input box where the user types messages.
- self.send_button - tk.Button - Clicking this calls send_message().
- self.chat_scroll - tk.Scrollbar - Vertical scrollbar
#### Operations
- Constructor - __init__ - Builds all tkinter widgets. Registers on_close with WM_DELETE_WINDOW. Connects the socket. Prompts for a username and sends it to the server. Starts the receive daemon thread. Calls root.mainloop().
- on_enter - on_enter(event) - Bound to the Return key on input_text. Calls send_message() then returns 'break' to suppress tkinter's default newline insertion.
- send_message - send_message() - Reads and strips input_text. Formats the payload as 'name: message'. 
- receive_message - receive_message() - sthread loop. Blocks on recv(1024). Schedules update_chat() via root.after() using a default-argument lambda (msg=server_message) to correctly capture the current value.
- update_chat = update_chat(message) - Runs on the main thread via root.after(). 
- on_close - on_close() - Called when the user closes the window.
#### Concurrency Model
Each client is served by its own daemon thread. The threading.Lock ensures the shared clients list is never modified by two threads simultaneously. broadcast_message() copies the list before iterating, so a disconnect mid-broadcast does not corrupt the loop.


## Team Responsilibity & Developer Coordination 
### Task Breakdown:
#### Noelia Doman: 
- design and implement the server class
- implemented thread-safe client list management using thread.Lock
- implemented broadcast_message() with concurrent-safe list snapshot
- wrote server-side error handling
- documentation
#### Sam Rois 
- Designed and implemented the Client class
- built the TKinter GUI
- implemented the two-thread architecture
- fixed lambda closure bug
- Implemented the two-thread architecture 
- SSH tunnel setup and testing
- implemented WM_DELETE_WINDOW socket cleanup via on_close()
- documentation

## Workflow:
We used Git for version control.

