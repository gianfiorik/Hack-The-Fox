# Reto 3 — HTTP JSON

**Categoría:** Python / Requests
**Puerto:** 9003

## Objetivo
`GET /api/status` devuelve un JSON. La flag está anidada en algún campo — no está
a simple vista, hay que explorar la estructura del dict en Python.

## Pistas
- `requests.get(url).json()` te da directo un `dict`.
- Imprime el dict completo primero (`print(data)`) antes de intentar navegarlo.
- También puedes probar con `curl http://127.0.0.1:9003/api/status` para comparar,
  pero el entregable es el script en Python.

## Cómo probar
```bash
python3 client_template.py
```
