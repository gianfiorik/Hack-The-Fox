#!/usr/bin/env python3
# Reto 2: "El portero matematico" - puerto 9101 (solo 127.0.0.1)
import socketserver, random, base64

HOST, PORT = "127.0.0.1", 9101
FLAG = base64.b64decode("SFRGe3B5dGhvbl9tYXNfcmFwaWRvX3F1ZV90dX0=").decode()

class Handler(socketserver.StreamRequestHandler):
    def handle(self):
        a, b = random.randint(100, 999), random.randint(100, 999)
        self.wfile.write(f"Portero: ¿Cuánto es {a} + {b}? Tienes 3 segundos.\n> ".encode())
        self.request.settimeout(3)
        try:
            resp = self.rfile.readline().decode().strip()
        except Exception:
            self.wfile.write(b"\nMuy lento. Fuera.\n")
            return
        if resp == str(a + b):
            self.wfile.write(f"Correcto. Pasa: {FLAG}\n".encode())
        else:
            self.wfile.write(b"Incorrecto. Fuera.\n")

class Server(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True

if __name__ == "__main__":
    with Server((HOST, PORT), Handler) as s:
        print(f"[reto 2] escuchando en {HOST}:{PORT}")
        s.serve_forever()
