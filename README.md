# Mini CTF HTF — "Primera Sangre"

5 partes, flags con formato `HTF{...}`. Todo corre en TU propia VM (nada sale a la red).
El instructor te asigna una parte (o varias): ejecuta **solo** el script de la tuya.

## Preparar

```bash
unzip mini_ctf_estudiantes.zip
cd mini_ctf
bash parteN.sh      # cambia N por tu parte, ejemplo: bash parte3.sh
```

> No pegues scripts en la terminal: ejecútalos como archivo (`bash parte3.sh`).

Para apagar todo y limpiar al terminar: `bash stop.sh`

## Partes

| Parte | Reto | Cómo lo preparas | Dónde lo resuelves | Pts |
|---|---|---|---|---|
| 1 | Archivo fantasma | `bash parte1.sh` | carpeta `~/ctf_oficina` | 50 |
| 2 | El portero matemático | `bash parte2.sh` | `nc 127.0.0.1 9101` (plantilla en `retos/2_portero/`) | 100 |
| 3 | Panel del club | `bash parte3.sh` | http://127.0.0.1:9102 en el navegador de tu VM | 100 |
| 4 | Mensaje en dos capas | `bash parte4.sh` | `~/ctf_parte4/mensaje.txt` | 100 |
| 5 | Foto sospechosa | `bash parte5.sh` | `~/ctf_parte5/foto.jpg` | 100 |

`bash setup.sh` prepara las 5 partes de una vez (solo para quien las haga todas).

## Reglas

- Equipos de 3 o 4 personas.
- **Regla de honor:** no abras `servidor.py`, `app.py` ni los `parte*.sh` hasta que termine el CTF.
- Cada pista usada resta 10 puntos.
- Si algo falla: `bash stop.sh` y luego vuelve a ejecutar tu `parteN.sh`.
