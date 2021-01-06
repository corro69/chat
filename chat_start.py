import PySimpleGUI as sg 
import pickle
import socket
from threading import Thread

pickle_in = open("server.dat", "rb")
server_info = pickle.load(pickle_in)

layout=[
    [sg.Text("Server:    "+ server_info[0])],
    [sg.Text("Chat Name:  "+ server_info[1])],
    [sg.Button(("Change Server IP and Chat ID"),size=(50,0))],
    [sg.Button(("Join Chat"),size=(50,0))]
]

window = sg.Window("Chat Start", layout, size=(250,150))

while True:
    event, values = window.read()

    if event == "Change Login Info":
        import chat_setup
    
    if event == "Join Chat":
        import chat_gui
        window.close()

    if event == sg.WIN_CLOSED or event =="Cancel":
        break
    
window.close()
