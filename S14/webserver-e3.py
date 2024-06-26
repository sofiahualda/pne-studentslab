import http.server
import socketserver
import termcolor
from pathlib import Path

PORT = 8080

socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')

        slices = self.requestline.split('/')
        resource = self.path
        if resource == "/" or resource == "/index.html":
            contents = Path("index.html").read_text()
        elif resource == "/blue.html":
            contents = Path("blue.html").read_text()
        elif resource == "/green.html":
            contents = Path("green.html").read_text()
        elif resource == "/pink.html":
            contents = Path("pink.html").read_text()
        else:
            contents = Path("error.html").read_text()
            self.send_response(404)

        self.send_response(200)

        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', str(len(contents.encode())))

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