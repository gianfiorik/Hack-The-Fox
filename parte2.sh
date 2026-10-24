#!/bin/bash
# PARTE 2 - El portero matematico (sockets)   Uso: bash parte2.sh
cd "$(dirname "$0")" || exit 1
BASE="$(pwd)"; PORT=9101
for cmd in python3 nc; do
  command -v "$cmd" >/dev/null || { echo "[X] Falta $cmd. Instala: sudo apt install python3 netcat-openbsd"; exit 1; }
done
mkdir -p "$BASE/.run"
# si ya estaba corriendo, lo reiniciamos
[ -f "$BASE/.run/reto2.pid" ] && kill "$(cat "$BASE/.run/reto2.pid")" 2>/dev/null && sleep 1
if ! python3 -c "
import socket,sys
s=socket.socket(); s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
try: s.bind(('127.0.0.1',$PORT))
except OSError: sys.exit(1)"; then
  echo "[X] El puerto $PORT esta ocupado. Ejecuta 'bash stop.sh' y reintenta."; exit 1
fi
nohup python3 "$BASE/retos/2_portero/servidor.py" > "$BASE/.run/reto2.log" 2>&1 &
echo $! > "$BASE/.run/reto2.pid"
sleep 1
kill -0 "$(cat "$BASE/.run/reto2.pid")" 2>/dev/null || { echo "[X] No arranco. Mira .run/reto2.log"; exit 1; }
cat <<MSG
[OK] PARTE 2 lista: El portero matematico
  Servicio:  nc 127.0.0.1 $PORT
  Plantilla: $BASE/retos/2_portero/cliente_plantilla.py
  Tienes 3 segundos para responder, asi que a mano no alcanza.
  Flag con formato HTF{...}. Para apagar: bash stop.sh
MSG
