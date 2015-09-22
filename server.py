import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('0.0.0.0', 8000))
sock.listen(1)
while True:
    conn, addr = sock.accept()
    print('connected by', addr)
    while True:
        data = conn.recv(1024)
        if not data: break
        conn.sendall(data)
    conn.close()
sock.close()
