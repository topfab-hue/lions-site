# La Fiche Qui Vend : guide interactif KezaCréation

## Intégration dans YOOtheme (WordPress)

1. Ouvrez la page dans le **Builder YOOtheme** et ajoutez un élément **Html** dans une section.
2. Ouvrez le fichier `embed.html`, copiez **tout son contenu** et collez-le dans le champ de l'élément Html.
3. Enregistrez. Aucun autre réglage n'est nécessaire.

Conseils :
- Mettez la section en pleine largeur ou en conteneur standard : le guide gère lui-même sa largeur (740 px).
- Le titre « La Fiche Qui Vend » est un titre de niveau 2 : gardez votre propre titre de page en niveau 1.
- Les polices HVOliveandFigs et SnellRoundhand sont chargées depuis votre site (`/wp-content/uploads/2025/06/` et `/2025/07/`). Ne déplacez pas ces fichiers.
- Le guide utilise du JavaScript : l'élément Html doit pouvoir contenir des scripts (compte administrateur).
- Tout le style est isolé : il ne modifie rien sur le reste de la page.

## Fichiers

- `embed.html` : version à coller dans YOOtheme.
- `index.html` : version autonome (une page complète), avec les polices dans `fonts/`.
- `_source/guide.src.html` + `_source/build.py` : source unique. Après une modification de la source, lancer `python3 _source/build.py` regénère `index.html` et `embed.html`.
