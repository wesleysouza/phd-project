import socket
import json

def server_running():
    # get hostname
    host = "localhost"
    port = 7000
    connection_number = 0

    server_socket = socket.socket();
    server_socket.bind((host, port))

    while True:
        server_socket.listen(2)
        conn, address = server_socket.accept()
        print("Connection from " + str(address) + "\n")
        connection_number += 1
        print("Connection number: " + str(connection_number) + "\n")

        data_json = conn.recv(1024).decode()
        data = json.loads(data_json)
        print("DATA RECEIVED: \n")
        print(data)
        conn.sendall(bytes(data_json, encoding="utf-8"))
        conn.close()

server_running()