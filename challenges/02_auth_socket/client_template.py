#!/usr/bin/env python3
"""
Reto 2: Auth Socket - cliente
El servidor manda un prompt pidiendo un código de acceso.
Tu script tiene que leer el prompt, mandar el código correcto, y leer la respuesta.
"""
import socket

HOST = "127.0.0.1"
PORT = 9002
ACCESS_CODE = "letmein"  # el mismo código que espera el server

# TODO 1: crea el socket y conéctate a (HOST, PORT)

# TODO 2: recibe el prompt inicial con .recv() e imprímelo

# TODO 3: manda ACCESS_CODE con .sendall() (recuerda .encode())

# TODO 4: recibe la respuesta final y muéstrala (ahí está la flag)
