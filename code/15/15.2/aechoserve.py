# aechoserv.py
# Asynchronous echo server

from socket import *
import asyncio

async def echo_server(address, loop):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(1)
    sock.setblocking(False)
    while True:
        client, addr = await loop.sock_accept(sock)
        print('Connection from', addr)
        loop.create_task(echo_handler(client, loop))

async def echo_handler(client, loop):
    while True:
        data = await loop.sock_recv(client, 10000)
        if not data:
            break
        await loop.sock_sendall(client, b'Got:' + data)
    print('Connection closed')
    client.close()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(echo_server(('',25000), loop))
