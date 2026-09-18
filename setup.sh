#!/bin/bash
# HTF - Semana 2: Setup de ambiente (Python + Git)
#
# IMPORTANTE: no pegues este script directo en una terminal zsh interactiva.
# Guárdalo con nano (ya viene guardado si clonaste el repo), dale permisos
# de ejecución, y corrélo así:
#
#   chmod +x setup.sh
#   ./setup.sh

set -e

echo "=== HTF Semana 2: Setup ==="
echo ""

# 1. Verificar Python3
if ! command -v python3 &> /dev/null; then
    echo "[!] python3 no encontrado. Instálalo antes de continuar."
    exit 1
fi
echo "[+] python3: $(python3 --version)"

# 2. Verificar/instalar requests
if ! python3 -c "import requests" &> /dev/null 2>&1; then
    echo "[*] Instalando requests..."
    pip3 install requests --break-system-packages 2>/dev/null || pip3 install --user requests
else
    echo "[+] requests ya está instalado"
fi

# 3. Verificar git + inicializar repo si no existe
if ! command -v git &> /dev/null; then
    echo "[!] git no encontrado. Instálalo antes de continuar."
    exit 1
fi
echo "[+] git: $(git --version)"

if [ ! -d .git ]; then
    git init
    cat > .gitignore << 'EOF'
__pycache__/
*.pyc
.venv/
solutions/
*.log
.pids/
EOF
    echo "[+] Repo git inicializado (.gitignore creado, solutions/ ignorado)"
else
    echo "[+] Ya existe un repo git en esta carpeta"
fi

# 4. Levantar los 4 servicios de reto en background
mkdir -p .pids
rm -f .pids/servers.pid

for dir in challenges/*/; do
    name=$(basename "$dir")
    if [ -f "${dir}server.py" ]; then
        python3 "${dir}server.py" > "${dir}server.log" 2>&1 &
        pid=$!
        echo "$pid" >> .pids/servers.pid
        echo "[+] $name arrancado (PID $pid)"
    fi
done

echo ""
echo "=== Listo ==="
echo "Servicios de reto corriendo en los puertos 9001-9004."
echo "Para detenerlos: ./stop.sh"
