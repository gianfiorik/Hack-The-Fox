#!/bin/bash
# PARTE 5 - Foto sospechosa (misc)   Uso: bash parte5.sh
cd "$(dirname "$0")" || exit 1
command -v exiftool >/dev/null || echo "[!] Te falta exiftool. Instala: sudo apt install libimage-exiftool-perl"
DEST="$HOME/ctf_parte5"; mkdir -p "$DEST"
cp retos/5_misc/foto.jpg "$DEST/foto.jpg"
cat <<MSG
[OK] PARTE 5 lista: Foto sospechosa
  Tu archivo: $DEST/foto.jpg
  Flag con formato HTF{...}. Para limpiar: bash stop.sh
MSG
