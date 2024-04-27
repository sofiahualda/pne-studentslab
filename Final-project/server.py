import http.server
import socketserver
import termcolor
from pathlib import Path
import jinja2 as j
from urllib.parse import parse_qs, urlparse


def read_html_file(filename):
    contents = Path("html/" + filename).read_text()
    contents = j.Template(contents)
    return contents

PORT = 8080

socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)

        GENES = ["U5", "ADA", "FRAT1", "RNU6_269P", "FXN"]
        termcolor.cprint(self.requestline, 'green')
        if self.path == "/":
            contents = Path('html/index.html').read_text()
        elif self.path[:-1] == "/ping":
            contents = Path("html/ping.html").read_text()
        elif self.path[:4] == "/get":
            for gene in GENES:
                index = GENES.index(gene)
                if 0 <= index <= 4:
                    if self.path.endswith(f"{index}"):
                        sequence = Path("..", "sequences", gene + ".txt").read_text().splitlines()
                        sequence = sequence[1:]
                        msg = ""
                        for line in sequence:
                            msg += line
                        contents = read_html_file("get.html").render(context={"todisplay": str(msg), "sequence": str(index)})
        elif self.path[:5] == "/gene":
            for gene in GENES:
                if self.path.endswith(f"{gene}"):
                    sequence = Path("..", "sequences", gene + ".txt").read_text().splitlines()
                    sequence = sequence[1:]
                    msg = ""
                    for line in sequence:
                        msg += line
                    contents = read_html_file("gene.html").render(context={"todisplay": str(msg), "gene": str(gene)})
        elif self.path.startswith("/operation"):
            msg = arguments['msg'][0]
            if self.path.endswith("Info"):
                total_len = len(msg)
                a_a = f"A: {msg.count('A')} ({((msg.count('A') / total_len) * 100):.1f}%)"
                a_c = f"C: {msg.count('C')} ({((msg.count('C') / total_len) * 100):.1f}%)"
                a_g = f"G: {msg.count('G')} ({((msg.count('G') / total_len) * 100):.1f}%)"
                a_t = f"T: {msg.count('T')} ({((msg.count('T') / total_len) * 100):.1f}%)"
                info_msg = f"Total length: {len(msg)}\n {a_a}\n {a_c}\n {a_g}\n {a_t}"
                contents = read_html_file("operation.html").render(context={"result": info_msg, "operation": "info", "sequence": msg})
            elif self.path.endswith("Comp"):
                complement = ""
                for base in msg:
                        if base == "A":
                            complement += "T"
                        elif base == "G":
                            complement += "C"
                        elif base == "C":
                            complement += "G"
                        elif base == "T":
                            complement += "A"
                contents = read_html_file("operation.html").render(context={"result": complement, "operation": "comp", "sequence": msg})
            elif self.path.endswith("Rev"):
                seq_n = msg[:len(msg)]
                reverse = seq_n[::-1]
                contents = read_html_file("operation.html").render(context={"result": reverse, "operation": "rev", "sequence": msg})


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