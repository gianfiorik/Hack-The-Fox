# Git en 5 minutos — HTF Semana 2

Desde esta semana, cada script/writeup se sube al repo del club. No hay sesión
dedicada a Git — es un hábito que arranca hoy y se repite cada semana.

## Lo mínimo para sobrevivir

```bash
git init                     # convierte la carpeta actual en un repo (ya lo hace setup.sh)
git status                   # qué cambió, qué está listo para commitear
git add archivo.py           # marca un archivo para el próximo commit
git add .                    # marca todo lo que cambió
git commit -m "mensaje"      # guarda el snapshot con un mensaje
git log --oneline            # historial corto de commits
```

## Conectar con el repo del club (una sola vez por máquina)

```bash
git remote add origin <URL-del-repo-del-club>
git branch -M main
git push -u origin main      # primera vez
git push                     # las siguientes veces
```

## Si ya existe el repo y quieres bajarlo

```bash
git clone <URL-del-repo-del-club>
```

## Reglas simples para el club

- Un commit por reto resuelto o por avance real, no un solo commit gigante al final.
- Mensajes cortos y en español, describiendo qué se hizo: `"resuelto reto 3 - http json"`.
- `solutions/` nunca se sube (ya está en `.gitignore`) — ahí solo va el material del instructor.
- Si algo se rompe con `git push` (conflictos, permisos), se pregunta en el grupo
  antes de forzar nada (`--force` está prohibido salvo que el inge lo autorice).
