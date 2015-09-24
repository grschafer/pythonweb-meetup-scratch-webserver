import socket
import time

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind(('0.0.0.0', 8000))
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.listen()
    while True:
        conn, addr = sock.accept()
        print('connected by', addr)

        data = conn.recv(1024)
        content = data.decode('utf-8')
        lines = content.split('\r\n')
        method, path, protocol = lines[0].split()
        print('method:', method)
        print('path:', path)
        print('protocol:', protocol)
        headers = lines[1:-1]
        print('headers:\n\t' + '\n\t'.join(headers))

        time.sleep(15)
        response = '''HTTP/1.1 200 OK\r\n\r\nHello World!'''
        response = response.encode('utf-8')

        conn.sendall(response)
        conn.close()
