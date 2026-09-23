# Cours 1 minute · C'est quoi l'IA ?

Pilote d'une série de cours vidéo d'une minute, animés entièrement en JavaScript sur canvas (aucune dépendance, aucune image, aucune police distante).

- `index.html` : page autonome. En haut du script, l'objet `SCRIPT` (actes, 14 plans minutés, texte de chaque plan, palette) ; en dessous le moteur (horloge, sous-titres, fondus enchaînés, primitives) puis les visuels (`VISUALS`), un par type de plan.
- Nouvel épisode : réécrire `SCRIPT`, réutiliser ou ajouter des fonctions dans `VISUALS`.
- `?t=12` dans l'URL, ou `window.__seek(12)`, fige l'image à 12 s (vérification / captures).
