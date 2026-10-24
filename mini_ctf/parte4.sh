#!/bin/bash
# PARTE 4 - Mensaje en dos capas (cripto)   Uso: bash parte4.sh
cd "$(dirname "$0")" || exit 1
DEST="$HOME/ctf_parte4"; mkdir -p "$DEST"
cp retos/4_cripto/mensaje.txt "$DEST/mensaje.txt"
cat <<MSG
[OK] PARTE 4 lista: Mensaje en dos capas
  Tu archivo: $DEST/mensaje.txt
  Herramientas sugeridas: CyberChef o la terminal.
  Flag con formato HTF{...}. Para limpiar: bash stop.sh
MSG
