# Smuppy — Galerie des écrans & maquettes (design)

Tous les écrans HTML + maquettes (PNG Figma) de l'app Smuppy, à visualiser **localement**.

> ⚠️ Repo de **design uniquement** (artefacts visuels). Ce n'est pas le code de l'app.
> Privé — ne pas partager en dehors de l'équipe (écrans pré-lancement).

## 🚀 Lancer la galerie (le plus simple)

1. **Cloner** le repo :
   ```bash
   git clone https://github.com/NoussaierSalaani/smuppy-design.git
   cd smuppy-design
   ```
2. **Double-cliquer** le lanceur :
   - **Mac** : `START-MAC.command` (si Gatekeeper bloque : clic droit → *Ouvrir*)
   - **Windows** : `START-WINDOWS.bat`

   → Le navigateur s'ouvre tout seul sur `http://127.0.0.1:8799/index.html`.

### Lancement manuel (si les scripts ne marchent pas)
Depuis le dossier du repo :
```bash
python3 -m http.server 8799 --bind 127.0.0.1
# ou, sans Python : npx --yes serve -l 8799 .
```
Puis ouvrir **http://127.0.0.1:8799/index.html**

> Il faut passer par un serveur local : ouvrir les `.html` en `file://` casse certaines
> pages (chargement d'assets/JSON bloqué par le navigateur).

## 🗺️ Points d'entrée

| Page | Chemin |
|------|--------|
| **Index maître — tous les écrans** | `index.html` (= `ALL_FOUND_SCREENS_LOCAL.html`) |
| Profile (le plus abouti) | `PROFILE_FINAL/index.html` |
| Profile — rendu réel | `PROFILE_REAL/index.html` |
| Maquettes V2 validées | `V2UI_VALIDATED_MAQUETTES.html` |
| Run V2 (redesign) | `RUN_V2_REDESIGN/` |

Les dossiers `PROFILE_FIGMA*`, `LOT*`, etc. contiennent des PNG : naviguez via
`http://127.0.0.1:8799/<dossier>/`.

## Pré-requis
- **Python 3** (déjà présent sur Mac récents) **ou** Node.js (`npx`).
