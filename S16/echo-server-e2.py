import http.server
import socketserver
import termcolor
from pathlib import Path
import jinja2 as j

def read_html_file(filename):
    contents = Path("html/" + filename).read_text()
    contents = j.Template(contents)
    return contents

PORT = 8080

socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')
        if self.path == "/":
            contents = Path('html/form-2.html').read_text()
        elif self.path.startswith("/echo") and self.path.endswith("on"):
            msg = self.path[1:]
            msg = msg[9:-7].upper()
            contents = read_html_file("form-e2.html").render(context={"todisplay": msg})
        elif self.path.startswith("/echo") and not self.path.endswith("on"):
            msg = self.path[1:]
            msg = msg[9:]
            contents = read_html_file("form-e1.html").render(context={"todisplay": msg})
        else:
            contents = Path("html/error.html").read_text()
            self.send_response(404)

        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()
        self.wfile.write(str.encode(contents))
        return

Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()