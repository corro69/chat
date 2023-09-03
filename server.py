import socket
from threading import Thread

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5002
seperator_token = "<SEP>"
client_sockets = set()
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((SERVER_HOST, SERVER_PORT))
s.listen(5)
print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

def listen_for_client(cs):
    connected = True
    while connected:
        try:
            msg = cs.recv(1024).decode()
        except Exception as e:
            print(f"[!] Error: {e}")
         #   client_sockets.remove(cs)
            break
        if msg == '!EXIT':
         #   client_sockets.remove(cs)
            break
        else:
            msg = msg.replace(seperator_token, ": ")
            client_socket.send(msg.encode())

while True:
    client_socket, client_address = s.accept()
    print(f"[+] {client_address} connected.")
    client_sockets.add(client_socket)
    t = Thread(target=listen_for_client, args=(client_socket,))
    t.daemon = True
    t.start()

#for cs in client_sockets:
#    cs.close()
#cs.close()