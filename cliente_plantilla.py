#!/usr/bin/env python3
# Plantilla del reto 2. Completa los TODO.
import socket

HOST, PORT = "127.0.0.1", 9101

s = socket.create_connection((HOST, PORT))
pregunta = s.recv(1024).decode()
print(pregunta)

# TODO 1: extrae los dos numeros de 'pregunta'
# TODO 2: calcula la suma
# TODO 3: envia la respuesta terminada en "\n" con s.send(...)
# TODO 4: recibe y muestra lo que responda el portero

s.close()
