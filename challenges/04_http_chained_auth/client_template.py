#!/usr/bin/env python3
"""
Reto 4: HTTP Chained Auth - cliente
Dos pasos: login para sacar un token, luego usar el token para pedir la flag.
"""
import requests

BASE = "http://127.0.0.1:9004"
CREDS = {"user": "htf", "pass": "ctf2026"}

# TODO 1: haz requests.post(BASE + "/api/login", json=CREDS)

# TODO 2: saca el token del JSON de respuesta

# TODO 3: haz requests.get(BASE + "/api/flag", headers={"X-Session-Token": token})

# TODO 4: imprime la flag del JSON de respuesta
