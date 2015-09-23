import socket
from collections import namedtuple

Request = namedtuple('Request', ['method', 'path', 'headers'])

def hello_view(request):
    return '''HTTP/1.1 200 OK\r\n\r\nHello World!'''

def echo_headers(request):
    lines = ''.join('<p>{}</p>'.format(h) for h in request.headers)
    return '''HTTP/1.1 200 OK\r\n\r\n<html>{}</html>'''.format(lines)

def make_404(request):
    return '''HTTP/1.1 404 Not Found\r\n\r\nResource doesn't exist'''

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

        request = Request(method, path, headers)
        if path == '/':
            response = hello_view(request)
        elif path == '/headers':
            response = echo_headers(request)
        else:
            response = make_404(request)
        response = response.encode('utf-8')

        conn.sendall(response)
        conn.close()
