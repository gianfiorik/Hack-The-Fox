# Reto 1 — Banner Grab

**Categoría:** Python / Sockets (warm-up)
**Puerto:** 9001

## Objetivo
Escribir un cliente TCP en Python (`client_template.py`) que se conecte al servicio
y capture la flag que manda apenas se abre la conexión. No hay que enviar nada.

## Pistas
- `socket.socket(socket.AF_INET, socket.SOCK_STREAM)` crea el socket.
- `.connect((HOST, PORT))` abre la conexión.
- `.recv(1024)` lee bytes; acuérdate de hacer `.decode()`.

## Cómo probar
```bash
python3 client_template.py
```
