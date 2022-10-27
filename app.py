from http.server import BaseHTTPRequestHandler, HTTPServer
import time
hName = "localhost"
Port = 8080


class wser (BaseHTTPRequestHandler):
    def do_GET (self):
        self.send_response (200)
        self.send_header ("Content-type", "text/html")
        self.end_headers ()
        self.wfile.write (bytes ("<html><head><title>CSM rocks</title></head>", "utf-8"))
        self.wfile.write (bytes ("<body>", "utf-8"))
        self.wfile.write (bytes ("<p>Hello CSM 2022</p>", "utf-8"))
        self.wfile.write (bytes ("</body></html>", "utf-8"))


if __name__ == "__main__":
    wser = HTTPServer ((hName, Port), wser)
    wser.serve_forever()
