'''Authors: Noelia Doman and Sam Rios
Class: CIS457
Assignment: Group Chat
This application allows interaction between multiple users in an
interactive application'''

import threading
import socket

# dictionary mapping socket for username

clients = {}
clients_lock = threading.Lock()

def broadcast(message): #send message to all clients
    with clients_lock:
        for client in clients:
            clients[client].send(message)
        #error code needed?

def handle_client():
    # first message to username to everyone
    username =
    if not username:
        username = "Anonymous"

print(f"{username} joined the chat")
broadcast(f"{username} joined the chat")
