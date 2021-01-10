import PySimpleGUI as sg 
import socket
import random
from threading import Thread
from datetime import datetime
import pickle
import os
import base64
import hashlib
from Crypto.Cipher import AES
from Crypto import Random

pickle_in = open("server.dat", "rb")
server_info = pickle.load(pickle_in)

SERVER_HOST = server_info[0]
SERVER_PORT = 5002
seperator_token = "<SEP>"
name  = server_info[1]
password = ("password")

s = socket.socket()
print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
s.connect((SERVER_HOST, SERVER_PORT))
print("[+] Connected.")
print("[+] Joined chat as " + name)

BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]

def listening_for_messages():
    while True:
        message = s.recv(1024)
        #print(message)
        decrypted = decrypt(message, password)
        print (bytes.decode(decrypted))
        
def encrypt(raw, password):
    private_key = hashlib.sha256(password.encode("utf-8")).digest()
    raw = pad(raw)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(raw))

def decrypt(enc, password):
    private_key = hashlib.sha256(password.encode("utf-8")).digest()
    enc = base64.b64decode(enc)
    iv = enc[:16]
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(enc[16:]))

t = Thread(target=listening_for_messages)
t.daemon = True
t.start()

layout=[
    [sg.Output(size=(50,15), key = 'OUTPUT')],
    [sg.Text(name,size=(0,0)), sg.InputText(do_not_clear=False), sg.OK()]
]

window = sg.Window("Chat", layout, size=(400,350))

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        s.shutdown()
        s.close()
        break
        
    to_send = values[0]

    date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    to_send = encrypt(name + ": " + to_send, password)

    s.send(to_send)

s.close()

window.close()
