#!/bin/bash
# PARTE 1 - Archivo fantasma (Linux)   Uso: bash parte1.sh
OFICINA="$HOME/ctf_oficina"
rm -rf "$OFICINA"; mkdir -p "$OFICINA/documentos" "$OFICINA/fotos"
echo "Lista de compras del club: pizza, gaseosas, cables." > "$OFICINA/documentos/compras.txt"
echo "Reunion el sabado 12:15. No faltar." > "$OFICINA/documentos/recordatorio.txt"
echo "Si buscas algo, mira con mas cuidado." > "$OFICINA/README"
echo "nada por aqui" > "$OFICINA/fotos/vacio.txt"
echo "HTF{ls_a_es_tu_amigo}" > "$OFICINA/.nota_secreta"
cat <<MSG
[OK] PARTE 1 lista: Archivo fantasma
  Enunciado: el admin dejo una nota en el servidor, pero no aparece con ls.
  Tu carpeta de trabajo: $OFICINA
  Flag con formato HTF{...}. Para limpiar: bash stop.sh
MSG
