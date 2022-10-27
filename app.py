import time
from http.server import BaseHTTPRequestHandler

hostName = "localhost"
serverPort = 8080 #You can choose any available port; by default, it is 8000
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self): #the do_GET method is inherited from BaseHTTPRequestHandler
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>CSM rocks!</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>Hello CSM team.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))
        
if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))  #Server starts
try:
    webServer.serve_forever()
except KeyboardInterrupt:
    pass
webServer.server_close()  #Executes when you hit a keyboard interrupt, closing the server
print("Server stopped.")
