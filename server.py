import socket
import time
import os

def handle_request(client_connection):
    data = conn.recv(1024)
    content = data.decode('utf-8')

    time.sleep(15)
    response = '''HTTP/1.1 200 OK\r\n\r\nHello World!'''
    response = response.encode('utf-8')

    conn.sendall(response)
    conn.close()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind(('0.0.0.0', 8000))
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.listen()
    while True:
        conn, addr = sock.accept()
        print('connected by', addr)

        pid = os.fork()
        if pid == 0:  # child
            sock.close()  # close child copy
            handle_request(conn)
            conn.close()
            os._exit(0)  # child exits
        else:  # parent
            conn.close()  # close parent copy


