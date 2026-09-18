# Semana 2 — Python aplicado a Seguridad + Git

**Hack The Fox — UCB**

## Estructura

```
semana2-ctf/
├── setup.sh                 # verifica python3/requests/git, levanta los 4 retos
├── stop.sh                  # detiene los 4 retos
├── git_cheatsheet.md         # material del segmento de Git (viernes, 5-10 min)
├── challenges/
│   ├── 01_banner_grab/       # socket TCP, sin interacción (warm-up)
│   ├── 02_auth_socket/       # socket TCP, con interacción (send/recv)
│   ├── 03_http_json/         # requests.get() + parseo de JSON
│   └── 04_http_chained_auth/ # login -> token -> flag (requests encadenado)
└── solutions/                 # SOLO instructor, no se comparte ni se sube a git
```

Cada carpeta en `challenges/` tiene:
- `server.py` — el servicio del reto (ya corre solo, no hay que tocarlo)
- `client_template.py` — el esqueleto que los estudiantes completan
- `README.md` — objetivo, pistas, cómo probar

## Viernes (virtual, 20:00) — preparación

1. Recap rápido de semana 1 (permisos, SUID, procesos, portscan).
2. Concepto: sockets en Python (`connect`, `send`, `recv`).
3. Concepto: `requests` — GET, POST, JSON, headers.
4. Git en 5-10 min (`git_cheatsheet.md`).
5. Setup del ambiente: cada estudiante corre `./setup.sh` en su máquina y
   confirma que los 4 puertos (9001-9004) responden.

## Sábado (presencial, 12:15) — CTF hands-on

Los 4 retos ya están corriendo (si no, `./setup.sh` los levanta). Los
estudiantes completan los `client_template.py` de cada uno, en orden de
dificultad creciente, y reportan la flag capturada.

| Reto | Puerto | Skill principal |
|---|---|---|
| 01_banner_grab | 9001 | socket connect + recv |
| 02_auth_socket | 9002 | socket send + recv (interacción) |
| 03_http_json | 9003 | requests.get() + parseo de dict/JSON |
| 04_http_chained_auth | 9004 | requests.post() + headers + flujo encadenado |

Al terminar cada reto, commitear el `client_template.py` resuelto (renombrado
o no, a criterio del estudiante) al repo del club.

## Notas para el instructor

- `solutions/soluciones.py` tiene las 4 soluciones de referencia — no compartir.
- Los servers son stdlib puro (`socket`, `http.server`) para no depender de
  Flask ni nada externo del lado del servidor; solo el cliente necesita `requests`.
- Recordatorio de siempre: **nunca pegar scripts multilínea directo en zsh
  interactivo** — guardarlos con `nano` y ejecutarlos como archivo.
