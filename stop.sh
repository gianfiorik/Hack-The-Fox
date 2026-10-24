#!/bin/bash
# Apaga los servidores y limpia todo lo creado por las partes.
cd "$(dirname "$0")" || exit 1
for n in 2 3; do
  f=".run/reto$n.pid"
  [ -f "$f" ] && kill "$(cat "$f")" 2>/dev/null && echo "parte $n detenida"
  rm -f "$f"
done
rm -rf "$HOME/ctf_oficina" "$HOME/ctf_parte4" "$HOME/ctf_parte5"
echo "Listo."
