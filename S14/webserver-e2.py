import http.server
import socketserver
import termcolor
from pathlib import Path

PORT = 8081

socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        read_index = Path("index.html").read_text()
        termcolor.cprint(self.requestline, 'green')
        slices = self.requestline.split('/')
        resource = slices[1]
        if resource == " HTTP" or resource == "index.html":
            contents = read_index
        else:
            contents = "Resource not available"

        self.send_response(200)

        self.send_header('Content-Type', 'text/plain')
        self.send_header('Content-Length', len(contents.encode()))

        self.end_headers()

        self.wfile.write(contents.encode())

        return



Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()
