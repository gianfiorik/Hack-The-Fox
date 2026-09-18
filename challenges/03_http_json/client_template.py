#!/usr/bin/env python3
"""
Reto 3: HTTP JSON - cliente
Usa requests para pegarle al endpoint y sacar la flag del JSON.
"""
import requests

URL = "http://127.0.0.1:9003/api/status"

# TODO 1: haz un requests.get(URL)

# TODO 2: convierte la respuesta a dict con .json()

# TODO 3: imprime el dict completo primero para ver dónde vive la flag

# TODO 4: navega el dict (["debug"]["flag"] o similar) e imprime solo la flag
