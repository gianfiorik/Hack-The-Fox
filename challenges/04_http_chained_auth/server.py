#!/usr/bin/env python3
"""
Reto 4: HTTP Chained Auth
POST /api/login con {"user": "htf", "pass": "ctf2026"} -> {"token": "..."}
GET  /api/flag  con header X-Session-Token: <token>    -> {"flag": "..."}
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import secrets

PORT = 9004
FLAG = "HTF{ch41n_y0ur_r3qu3sts_l1k3_4_pr0}"
USER, PASS = "htf", "ctf2026"
VALID_TOKENS = set()


class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/api/login":
            length = int(self.headers.get("Content-Length", 0))
            try:
                data = json.loads(self.rfile.read(length))
            except json.JSONDecodeError:
                data = {}
            if data.get("user") == USER and data.get("pass") == PASS:
                token = secrets.token_hex(8)
                VALID_TOKENS.add(token)
                self._json(200, {"token": token})
            else:
                self._json(401, {"error": "credenciales inválidas"})
        else:
            self.send_response(404)
            self.end_headers()

    def do_GET(self):
        if self.path == "/api/flag":
            token = self.headers.get("X-Session-Token")
            if token in VALID_TOKENS:
                self._json(200, {"flag": FLAG})
            else:
                self._json(403, {"error": "token inválido o ausente"})
        else:
            self.send_response(404)
            self.end_headers()

    def _json(self, code, obj):
        body = json.dumps(obj).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        pass


if __name__ == "__main__":
    print(f"[04_http_chained_auth] escuchando en http://0.0.0.0:{PORT}")
    HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
