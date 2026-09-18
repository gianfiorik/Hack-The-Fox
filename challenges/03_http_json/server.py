#!/usr/bin/env python3
"""
Reto 3: HTTP JSON
GET /api/status devuelve un JSON. La flag está anidada en la respuesta.
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

PORT = 9003
FLAG = "HTF{r3qu3sts_g3t_json_ez}"


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api/status":
            body = json.dumps({
                "service": "htf-api",
                "status": "ok",
                "uptime": "133742s",
                "debug": {"flag": FLAG},
            }).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        pass  # silencia logs para no ensuciar la terminal


if __name__ == "__main__":
    print(f"[03_http_json] escuchando en http://0.0.0.0:{PORT}")
    HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
