#!/usr/bin/env python3
# Reto 3: "Panel del club" - puerto 9102 (solo 127.0.0.1)
import sqlite3, base64, html
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

HOST, PORT = "127.0.0.1", 9102
FLAG = base64.b64decode("SFRGe2NvbWlsbGFfc2ltcGxlX3BvZGVyX3RvdGFsfQ==").decode()

db = sqlite3.connect(":memory:", check_same_thread=False)
db.execute("CREATE TABLE users (user TEXT, pass TEXT, perfil TEXT)")
db.executemany("INSERT INTO users VALUES (?,?,?)", [
    ("invitado", "invitado", "Bienvenido, invitado. No hay nada secreto aqui."),
    ("presidente", "x9Qv#r2!kLm8-HTF-no-adivinable", f"Panel del presidente. Secreto del club: {FLAG}"),
])

PAGE = """<html><body style="font-family:sans-serif;background:#1c1226;color:#eee;text-align:center;margin-top:80px">
<h1>Panel del club HTF</h1>{body}</body></html>"""
FORM = """<form method="POST" action="/login">
<p>Usuario: <input name="user"></p><p>Clave: <input name="pass" type="password"></p>
<p><button>Entrar</button></p></form>{msg}"""

class H(BaseHTTPRequestHandler):
    def _send(self, body, code=200):
        self.send_response(code)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(PAGE.format(body=body).encode())

    def do_GET(self):
        self._send(FORM.format(msg=""))

    def do_POST(self):
        n = int(self.headers.get("Content-Length", 0))
        d = parse_qs(self.rfile.read(n).decode())
        u, p = d.get("user", [""])[0], d.get("pass", [""])[0]
        q = f"SELECT perfil FROM users WHERE user='{u}' AND pass='{p}'"   # vulnerable a proposito
        try:
            row = db.execute(q).fetchone()
        except Exception as e:
            self._send(FORM.format(msg=f"<p>Error SQL: {html.escape(str(e))}</p>"))
            return
        if row:
            self._send(f"<p>{row[0]}</p>")
        else:
            self._send(FORM.format(msg="<p>Credenciales incorrectas.</p>"))

    def log_message(self, *a):
        pass

if __name__ == "__main__":
    print(f"[reto 3] escuchando en http://{HOST}:{PORT}")
    HTTPServer((HOST, PORT), H).serve_forever()
