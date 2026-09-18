# Reto 2 — Auth Socket

**Categoría:** Python / Sockets (interacción)
**Puerto:** 9002

## Objetivo
El servicio pide un código de acceso por texto plano antes de soltar la flag.
Tu cliente debe leer el prompt, mandar el código correcto y leer la respuesta.

## Pistas
- El server manda el prompt primero: tienes que `.recv()` antes de mandar nada.
- `.sendall()` espera bytes, no strings — usa `.encode()`.
- El código de acceso está en el propio `client_template.py` (a propósito: en un
  reto real lo sacarías por fuerza bruta, wordlist, o leyendo el binario/fuente).

## Cómo probar
```bash
python3 client_template.py
```
