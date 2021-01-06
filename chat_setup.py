import PySimpleGUI as sg 
import pickle
import socket
from threading import Thread

layout=[
    [sg.Text("Server IP"), sg.InputText(), sg.OK()],
    [sg.Text("Name"), sg.InputText(), sg.OK()],
    [sg.Output(size=(50,5),key = 'OUTPUT')],
    [sg.Button("Done")]
]

window = sg.Window("Chat Setup", layout, size=(300,150))

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
        window.close()

    if event == sg.WIN_CLOSED or event =="Cancel":
        break
    
window.close()
