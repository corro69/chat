import PySimpleGUI as sg 

import socket
import random
from threading import Thread
from datetime import datetime
from colorama import Fore, init, Back

init()

colors = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTBLACK_EX,
    Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX,
    Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX,
    Fore.LIGHTYELLOW_EX, Fore.MAGENTA, Fore.RED, Fore.WHITE, Fore.YELLOW
]

client_color = random.choice(colors)

#SERVER_HOST = "127.0.0.1"
SERVER_HOST = input("Server IP: ")
SERVER_PORT = 5002
seperator_token = "<SEP>"

s = socket.socket()
print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
s.connect((SERVER_HOST, SERVER_PORT))
print("[+] Connected.")

name  = input("Enter your name: ")

def listening_for_messages():
    while True:
        message = s.recv(1024).decode()
        print(message + "\n")

t = Thread(target=listening_for_messages)
t.daemon = True
t.start()



layout=[
    [sg.Output(size=(50,18), key = 'OUTPUT')],
    [sg.Text(size=(0,0)), sg.InputText(), sg.OK()]
]

window = sg.Window("Chat", layout, size=(400,350))

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED or event =="Cancel":
        break
    if event == "OK":
        chat_message = values[0]
    
    to_send = values[0]
    if to_send.lower() == 'q':
        s.shutdown(socket.SHUT_RDWR)
        break
    
    date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #to_send = f"{client_color}[{date_now}] {name}{seperator_token}{to_send}{Fore.RESET}"
    to_send = f"{name}{seperator_token}{to_send}"
    s.send(to_send.encode())

s.close()

window.close()