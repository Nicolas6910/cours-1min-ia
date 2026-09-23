# Cours 1 minute · C'est quoi l'IA ?

Cours vidéo d'une minute animé en JavaScript sur canvas, épisode 1 d'une série.

- `src.html` : source. En haut, l'objet `SCRIPT` (actes, 14 plans minutés, textes) ; puis le système de design
  (palette `C`, échelle typographique `TS`, grille `G`), le moteur, les visuels (`VISUALS`) et le lecteur.
- `build.py` : produit `index.html` en y embarquant les polices (Inter 400/600/700/800 et Noto Sans Mono, sous-ensembles WOFF, licence SIL OFL, voir `fonts/`).
- Nouvel épisode : réécrire `SCRIPT`, réutiliser ou ajouter des visuels, puis `python3 build.py`.
- `?t=12` dans l'URL, ou `window.__seek(12)`, fige l'image à 12 s (vérification / captures).
