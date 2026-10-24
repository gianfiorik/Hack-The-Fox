#!/bin/bash
# Prepara TODAS las partes (para instructor o para quien haga varias).
cd "$(dirname "$0")" || exit 1
for n in 1 2 3 4 5; do bash "parte$n.sh" || exit 1; echo; done
