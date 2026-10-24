#!/bin/bash
# PARTE 3 - Panel del club (web, SQLi)   Uso: bash parte3.sh
cd "$(dirname "$0")" || exit 1
BASE="$(pwd)"; PORT=9102
command -v python3 >/dev/null || { echo "[X] Falta python3. Instala: sudo apt install python3"; exit 1; }
mkdir -p "$BASE/.run"
[ -f "$BASE/.run/reto3.pid" ] && kill "$(cat "$BASE/.run/reto3.pid")" 2>/dev/null && sleep 1
if ! python3 -c "
import socket,sys
s=socket.socket(); s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
try: s.bind(('127.0.0.1',$PORT))
except OSError: sys.exit(1)"; then
  echo "[X] El puerto $PORT esta ocupado. Ejecuta 'bash stop.sh' y reintenta."; exit 1
fi
nohup python3 "$BASE/retos/3_panel/app.py" > "$BASE/.run/reto3.log" 2>&1 &
echo $! > "$BASE/.run/reto3.pid"
sleep 1
kill -0 "$(cat "$BASE/.run/reto3.pid")" 2>/dev/null || { echo "[X] No arranco. Mira .run/reto3.log"; exit 1; }
cat <<MSG
[OK] PARTE 3 lista: Panel del club
  Abre en el navegador DE TU VM: http://127.0.0.1:$PORT
  Solo entra el presidente.
  Flag con formato HTF{...}. Para apagar: bash stop.sh
MSG
