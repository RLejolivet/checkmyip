#!/usr/bin/python3

import http.server
import json

# Script version
version = "1.0.0"


# HTTP listener method. Starts an HTTP server on specified port
def http_listener(port, talker):
    print("Starting HTTPServer")
    with http.server.HTTPServer(('', port), talker) as httpd:
        httpd.serve_forever()


# HTTP Request Handler
class MyIPRequestHandler(http.server.BaseHTTPRequestHandler):
    server_version = f"CheckMyIP/{version}"

    def do_GET(self):
        (host, port) = self.client_address
        proto = "http"

        if self.headers["X-Real-IP"] is not None:
            host = self.headers["X-Real-IP"]

        if self.headers["X-Forwarded-For"] is not None:
            host = self.headers["X-Forwarded-For"].split(",")[0].strip()

        if self.headers["X-Forwarded-Proto"] is not None:
            proto = self.headers["X-Forwarded-Proto"]

        response_body_raw = (json.dumps({
            "ip": host,
            "port": port,
            "proto": proto
        }) + "\n").encode("utf-8")

        self.send_response(200, "OK TOP")
        self.send_header("Content-Type", "application/json; encoding=utf8")
        self.send_header("Content-Length", str(len(response_body_raw)))
        self.end_headers()

        self.wfile.write(response_body_raw)


if __name__ == "__main__":
    http_listener(80, MyIPRequestHandler)
