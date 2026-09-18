#!/usr/bin/env python3
"""
Reto 1: Banner Grab
No hay truco: el server manda la flag apenas te conectas.
Objetivo: escribir un cliente TCP en Python que se conecte y la lea.
"""
import socket

HOST = "0.0.0.0"
PORT = 9001
FLAG = "HTF{s0ck3ts_1s_ju5t_a_f1l3}"


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(5)
        print(f"[01_banner_grab] escuchando en {HOST}:{PORT}")
        while True:
            conn, addr = s.accept()
            with conn:
                banner = f"Bienvenido al servicio HTF-01\n{FLAG}\n"
                conn.sendall(banner.encode())


if __name__ == "__main__":
    main()
