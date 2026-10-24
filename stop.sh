#!/bin/bash
# Detiene los 4 servicios de reto levantados por setup.sh

if [ -f .pids/servers.pid ]; then
    while read -r pid; do
        if kill "$pid" 2>/dev/null; then
            echo "[+] Detenido PID $pid"
        fi
    done < .pids/servers.pid
    rm -f .pids/servers.pid
    echo "Listo."
else
    echo "No hay servidores registrados (¿ya corriste ./setup.sh?)."
fi
