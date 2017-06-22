# echoserv.py

from socket import *
import threading

def echo_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(1)
    while True:
        client, addr = sock.accept()
        print('Connection from', addr)
        # echo_handler(client)
        t = threading.Thread(target=echo_handler,
                             args=(client,))
        t.start()

def echo_handler(client):
    while True:
        data = client.recv(100000)
        if not data:
            break
        client.sendall(b'Got:' + data)
    print('Connection closed')
    client.close()

if __name__ == '__main__':
    echo_server(('',25000))
