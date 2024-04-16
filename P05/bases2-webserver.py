import http.server
import socketserver
import termcolor
from pathlib import Path
import os

PORT = 8080

socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')

        resource = self.path
        if resource == "/" or resource == "/index.html":
            contents = Path("html/index.html").read_text()
        elif resource == "/info/A.html":
            contents = Path("html/info/A.html").read_text()
        elif resource == "/info/C.html":
            contents = Path("html/info/C.html").read_text()
        elif resource == "/info/G.html":
            contents = Path("html/info/G.html").read_text()
        elif resource == "/info/T.html":
            contents = Path("html/info/T.html").read_text()
        else:
            resource = self.path[1:]
            try:
                file_name = os.path.join("html/" + resource)
                contents = Path(file_name).read_text()
                self.send_response(200)
            except FileNotFoundError:
                contents = Path("html/error.html").read_text()
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