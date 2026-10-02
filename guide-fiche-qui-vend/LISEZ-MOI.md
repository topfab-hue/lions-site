# La Fiche Qui Vend : guide interactif KezaCréation

## Intégration dans YOOtheme (WordPress)

1. Ouvrez la page dans le **Builder YOOtheme** et ajoutez un élément **Html** dans une section.
2. Ouvrez le fichier `embed.html`, copiez **tout son contenu** et collez-le dans le champ de l'élément Html.
3. Enregistrez. Aucun autre réglage n'est nécessaire.

Conseils :
- Mettez la section en pleine largeur ou en conteneur standard : le guide gère lui-même sa largeur (740 px).
- Le titre « La Fiche Qui Vend » du guide est le titre de niveau 1 (H1) de la page : n'en ajoutez pas un second.
- Les polices HVOliveandFigs et SnellRoundhand sont chargées depuis votre site (`/wp-content/uploads/2025/06/` et `/2025/07/`). Ne déplacez pas ces fichiers.
- Le guide utilise du JavaScript : l'élément Html doit pouvoir contenir des scripts (compte administrateur).
- La police Montserrat est intégrée au fichier : aucun appel à Google Fonts (pas de transfert de données vers un tiers).
- Tout le style est isolé : il ne modifie rien sur le reste de la page.

## Fichiers

- `embed.html` : version à coller dans YOOtheme.
- `index.html` : version autonome (une page complète), avec les polices dans `fonts/`.
- `_source/guide.src.html` + `_source/build.py` : source unique. Après une modification de la source, lancer `python3 _source/build.py` regénère `index.html` et `embed.html`.

## Si une partie de la page ne s'affiche pas

WordPress peut transformer certains caractères du code (par exemple `&&` en `&#038;&#038;`, ou la balise d'image) et casser le JavaScript. Dans `embed.html`, le script est donc encodé en base64 : WordPress ne peut plus en modifier le texte. Le contenu reste visible même si le script échoue. Après toute mise à jour, recollez **tout** le contenu de `embed.html` (en remplaçant l'ancien) et videz le cache du site.

## Défilement doux du site (Lenis)

Le site kezacreation.com utilise la bibliothèque Lenis, qui capte la molette sur toute la page. Le panneau d'aide et la fenêtre de bienvenue portent l'attribut `data-lenis-prevent` pour garder leur propre défilement. Ne pas le retirer.

## Atelier : photos, aperçu et note

- Les photos sont lues dans le navigateur de la personne. Rien n'est envoyé sur un serveur. Une version réduite (720 px) est mémorisée sur l'appareil pour retrouver la fiche au retour.
- La note sur 100 est calculée localement à partir de règles simples (longueur, mots vagues, occasion, matière, destinataire, nombre de mots, FAQ, mots-clés, photos). Elle est indicative.
- Les règles et les barèmes sont dans `_source/guide.src.html` (fonctions `scoreTitle` et `ficheScore`). Après modification : `python3 _source/build.py`.

## Vie privée

Vos visiteuses saisissent du texte et des photos dans l'atelier : tout reste dans leur navigateur (localStorage). Le bouton « Effacer toutes mes données » du panneau d'aide supprime tout. Mentionnez-le dans votre politique de confidentialité si besoin.
