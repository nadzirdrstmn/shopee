import http.server
import socketserver


class MyHandler(http.server.SimpleHTTPRequestHandler):
    def handle_one_request(self):
        print(self.client_address[0])
        return super().handle_one_request()


httpd = socketserver.TCPServer(("", 8080), MyHandler)

while True:
    httpd.handle_request()
