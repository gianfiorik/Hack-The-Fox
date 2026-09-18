# Reto 4 — HTTP Chained Auth

**Categoría:** Python / Requests (encadenado)
**Puerto:** 9004

## Objetivo
Simula un flujo real de API: primero te logueas (`POST /api/login`) para obtener
un token de sesión, y luego usas ese token en un header para pedir la flag
(`GET /api/flag`). Es el mismo patrón que verán en la mayoría de retos web con
autenticación por token.

## Credenciales
```json
{"user": "htf", "pass": "ctf2026"}
```

## Pistas
- `requests.post(url, json=CREDS)` manda el body como JSON automáticamente.
- El token viene en la respuesta del login — sácalo con `.json()["token"]`.
- Para mandar headers: `requests.get(url, headers={"X-Session-Token": token})`.

## Cómo probar
```bash
python3 client_template.py
```
