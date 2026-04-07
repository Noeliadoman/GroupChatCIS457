'''Authors: Noelia Doman and Sam Rios
Class: CIS457
Assignment: Group Chat
This application allows interaction between multiple users in an
interactive application'''

import threading
import socket

HOST = ''
port =

def receive_message(sock):
    while True:
        data = sock.recv(1024)
        if not data:
            print("Connection closed")
            break

def main():

    host =
    port =

    username = input("Enter your user name: ").strip()
    if not username:
        username = "Anonymous"

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    # send username to everyone

    #start background thread to receive messages