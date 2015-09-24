from http.server import HTTPServer, SimpleHTTPRequestHandler

class MyRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write('Hello World!'.encode('utf-8'))

server_address = ('', 8000)
httpd = HTTPServer(server_address, MyRequestHandler)
httpd.serve_forever()

