import socket
import json

def create_json():
    hems = {
        "name": "house1",
        "appliances": ["a1", "a2", "a3"],
        "number": 10
    }
    return json.dumps(hems)

def send_message():

    data = create_json()

    addr = ("localhost", 7000)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.connect(addr)
        sock.sendall(bytes(create_json(), encoding="utf-8"))
        received = sock.recv(1024)
        received = received.decode("utf-8")
        sock.close()

    finally:
        print("Not Connect")
        sock.close()

    print("Sent:     {}".format(data))
    print("Received: {}".format(received))

send_message()

