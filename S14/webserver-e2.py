import http.server
import socketserver
import termcolor
from pathlib import Path

PORT = 8081

socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.read_index = Path("index.html").read_text()
        self.read_error = Path("error.html").read_text()
        termcolor.cprint(self.requestline, 'green')
        slices = self.requestline.split('\n')
        req_line = slices[0]
        req_line_parts = req_line.split("/")
        resource = req_line_parts[1]
        if resource == " HTTP" or "index.html HTTP" in resource:
            contents = self.read_index
        else:
            contents = self.read_error
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
