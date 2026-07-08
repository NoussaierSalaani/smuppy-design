#!/bin/bash
# Double-cliquez ce fichier pour lancer la galerie des écrans Smuppy.
# (Sur Mac : clic droit > Ouvrir la première fois si le Gatekeeper bloque.)
cd "$(dirname "$0")" || exit 1
PORT=8799
echo "▶ Démarrage du serveur local des écrans Smuppy sur http://127.0.0.1:$PORT ..."
# ouvre le navigateur après 1,5 s
( sleep 1.5 && open "http://127.0.0.1:$PORT/index.html" ) &
# Python 3 (présent par défaut sur Mac récents) ; sinon fallback Node
if command -v python3 >/dev/null 2>&1; then
  python3 -m http.server "$PORT" --bind 127.0.0.1
elif command -v npx >/dev/null 2>&1; then
  npx --yes serve -l "$PORT" .
else
  echo "❌ Ni python3 ni npx trouvés. Installez Python 3 : https://www.python.org/downloads/"
  read -r -p "Appuyez sur Entrée pour fermer."
fi
