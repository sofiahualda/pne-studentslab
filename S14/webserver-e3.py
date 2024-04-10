import http.server
import socketserver
import termcolor
from pathlib import Path

PORT = 8081

socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')
        slices = self.requestline.split('/')
        resource = slices[1]

        read_index = Path("index.html").read_text()
        read_blue = Path("blue.html").read_text()
        read_error = Path("error.html").read_text()
        read_green = Path("green.html").read_text()
        read_pink = Path("pink.html").read_text()

        if resource == " HTTP" or resource == "index.html HTTP":
            contents = read_index
        elif resource == ("blue.html HTTP"):
            contents = read_blue
        elif resource == "error.html HTTP":
            contents = read_error
        elif resource == "green.html HTTP":
            contents = read_green
        elif resource == "pink.html HTTP":
            contents = read_pink

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