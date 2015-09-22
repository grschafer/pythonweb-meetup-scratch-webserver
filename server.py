import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('0.0.0.0', 8000))
sock.listen(1)
while True:
    conn, addr = sock.accept()
    print('connected by', addr)

    data = conn.recv(1024)
    print('received', data)

    response = b'''\
HTTP/1.1 200 OK

Hello World!
'''
    conn.sendall(response)
    conn.close()
sock.close()
