# Cours 1 minute · C'est quoi l'IA ?

Pilote d'une série de cours vidéo d'une minute, animés entièrement en JavaScript sur canvas (aucune dépendance, aucune image, aucune police distante).

- `index.html` : page autonome. En haut du script, l'objet `SCRIPT` (texte, timings, scènes, palette) ; en dessous le moteur (horloge, sous-titres, transitions, primitives) puis les visuels (`VISUALS`).
- Nouvel épisode : réécrire `SCRIPT`, réutiliser ou ajouter des fonctions dans `VISUALS`.
- `?t=12` dans l'URL, ou `window.__seek(12)`, fige l'image à 12 s (vérification / captures).
