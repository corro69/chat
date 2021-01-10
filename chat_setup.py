import PySimpleGUI as sg 
import pickle
import socket
from threading import Thread

layout=[
    [sg.Text("Server IP"), sg.InputText(), sg.OK()],
    [sg.Text("Name"), sg.InputText(), sg.OK()],
    [sg.Output(size=(40,3),key = 'OUTPUT')],
    [sg.Button("Done")]
]

window = sg.Window("Chat Setup", layout, size=(300,200))

while True:
    event, values = window.read()

    if event == "OK":

        x = values[0]
        y = values[1]
        server_info = (x,y)
        pickle_out = open("server.dat","wb")
        pickle.dump(server_info, pickle_out)
        pickle_out.close()

        print(server_info)

    if event == "Done":
        x = values[0]
        y = values[1]
        server_info = (x,y)
        pickle_out = open("server.dat","wb")
        pickle.dump(server_info, pickle_out)
        pickle_out.close()
        window.close()
        import chat_start

    if event == sg.WIN_CLOSED:
        break
    
window.close()