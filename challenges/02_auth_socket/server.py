#!/usr/bin/env python3
"""
Reto 2: Auth Socket
El servidor pide un código de acceso por texto plano.
Si mandas el correcto, te da la flag.
"""
import socket

HOST = "0.0.0.0"
PORT = 9002
ACCESS_CODE = "letmein"
FLAG = "HTF{s3nd_r3cv_1s_a_c0nv3rsat10n}"


def handle(conn):
    conn.sendall(b"=== HTF Auth Service ===\n")
    conn.sendall(b"ACCESS CODE: ")
    data = conn.recv(1024).decode(errors="ignore").strip()
    if data == ACCESS_CODE:
        conn.sendall(f"Acceso concedido.\n{FLAG}\n".encode())
    else:
        conn.sendall(b"Acceso denegado.\n")


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(5)
        print(f"[02_auth_socket] escuchando en {HOST}:{PORT}")
        while True:
            conn, addr = s.accept()
            with conn:
                handle(conn)


if __name__ == "__main__":
    main()
