'''Authors: Noelia Doman and Sam Rios
Class: CIS457
Assignment: Group Chat
This application allows interaction between multiple users in an
interactive application'''

from threading import Thread
import socket
import tkinter as tk
import tkinter.simpledialog as simpledialog


class Client:
    def __init__(self, HOST, PORT):
        self.root = tk.Tk()
        self.root.title("Group Chat Client")
        
        # Chat display
        self.chat_text = tk.Text(self.root, height=20, width=50, state='disabled')
        self.chat_scroll = tk.Scrollbar(self.root, command=self.chat_text.yview)
        self.chat_text.config(yscrollcommand=self.chat_scroll.set)
        self.chat_text.pack(side=tk.LEFT, fill=tk.Y)
        self.chat_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Input
        self.input_text = tk.Text(self.root, height=3, width=50)
        self.input_text.pack()
        
        # Send button
        self.send_button = tk.Button(self.root, text="Send", command=self.send_message)
        self.send_button.pack()
        
        # Bind enter
        self.input_text.bind('<Return>', self.on_enter)
        self.root.protocol('WM_DELETE_WINDOW', self.on_close)
        
        # Connect
        self.socket = socket.socket()
        self.socket.connect((HOST, PORT))
        self.name = simpledialog.askstring("Name", "Enter your name:")
        if not self.name:
            self.name = "Anonymous"
        self.socket.send(self.name.encode())
        Thread(target=self.receive_message, daemon=True).start()
        
        self.root.mainloop()
    
    def on_enter(self, event):
        self.send_message()
        return 'break'
    
    def send_message(self):
        message = self.input_text.get("1.0", tk.END).strip()
        if message:
            client_message = self.name + ": " + message
            try:
                self.socket.send(client_message.encode())
                self.input_text.delete("1.0", tk.END)
                self.root.after(0, lambda: self.update_chat("Me: " + message))
            except (ConnectionError, OSError):
                self.root.quit()
    
    def receive_message(self):
        while True:
            try:
                server_message = self.socket.recv(1024).decode()
                if not server_message.strip():
                    self.root.quit()
                    break
                self.root.after(0, lambda: self.update_chat(server_message))
            except (ConnectionError, OSError):
                self.root.after(0, lambda: self.root.quit())
                break
    
    def on_close(self):
        try:
            self.socket.send((self.name + ": exit").encode())
        except (ConnectionError, OSError):
            pass
        finally:
            try:
                self.socket.close()
            except:
                pass
            self.root.destroy()
    
    def update_chat(self, message):
        self.chat_text.config(state='normal')
        self.chat_text.insert(tk.END, message + '\n')
        self.chat_text.config(state='disabled')
        self.chat_text.see(tk.END)

if __name__ == '__main__':
    Client('127.0.0.1', 5000)