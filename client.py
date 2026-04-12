'''Authors: Noelia Doman and Sam Rios
Class: CIS457
Assignment: Group Chat
This application allows interaction between multiple users in an
interactive application'''

from threading import Thread
import socket
import os

class Client:
    # When a client is made, it connects to the server, and asks for a username
    def __init__(self, HOST, PORT):
        self.socket = socket.socket()
        self.socket.connect((HOST, PORT))
        self.name = input("Enter your name: ")

        self.talk_to_server()
    
    # First, the name will be sent to the server. Then, it will constantly 
    # listen for messages on a new thread. 
    def talk_to_server(self):
        self.socket.send(self.name.encode())
        Thread(target = self.receive_message).start()
        self.send_message()

    # When user input is received, it will send that message to the server with client's name
    def send_message(self):
        while True:
            try:
                client_input = input(f"{self.name}: ")
                client_message = self.name + ": " + client_input
                self.socket.send(client_message.encode())
            except (ConnectionError, OSError):
                print("\nConnection lost. Exiting gracefully.")
                self.socket.close()
                os._exit(0)
    # Will forever listen out for messages. If the message is empty, close the program. 
    def receive_message(self):
        while True:
            try:
                server_message = self.socket.recv(1024).decode()
                if not server_message.strip():
                    os._exit(0)
                print("\r" + " " * 100, end="")
                print("\r" + server_message)
                print(f"{self.name}: ", end="", flush=True)
            except (ConnectionError, OSError):
                print("Server has shut down. Exiting gracefully.")
                self.socket.close()
                os._exit(0)

if __name__ == '__main__':
    Client('127.0.0.1', 7632)
