from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(b"Hello from minimal Python app on OpenShift!")

if __name__ == "__main__":
    server_address = ('', 8080)  # Must listen on 8080 for OpenShift
    httpd = HTTPServer(server_address, SimpleHandler)
    print("Starting minimal Python app on port 8080...")
    httpd.serve_forever()

