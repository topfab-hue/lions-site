# Lions FC — Site Web

## Vue d'ensemble

Site web statique pour Lions FC, club de football fictif français. Aucun outil de build, aucun framework, aucun gestionnaire de paquets — HTML/CSS/JS vanilla pur, servi par un serveur de fichiers statiques.

## Structure du projet

```
lions-site/
├── index.html          # Page d'accueil (1307 lignes) — animation canvas, sections héros/stats/effectif/galerie
├── agenda.html         # Calendrier des matchs, résultats, classement Ligue 1
├── effectif.html       # Profils joueurs + fiche staff
├── billetterie.html    # Achat de billets pour les matchs à venir
├── club.html           # Histoire et présentation du club
├── contact.html        # Formulaire et informations de contact
├── lions-data.js       # Couche de données partagée (chargée par <script src>)
├── frames/             # 142 images JPG numérotées (frame_0001.jpg … frame_0142.jpg) pour l'animation canvas
├── img/
│   ├── players/        # Photos joueurs : player1.png … player4.png, coach_main.png
│   └── staff/          # (répertoire présent, contenu variable)
└── .claude/
    └── launch.json     # Config serveur de développement
```

## Lancer le projet en local

```bash
python3 -m http.server 9090
```

Le fichier `.claude/launch.json` configure ce serveur sur le port 9090 (avec `autoPort: true` pour éviter les conflits). Ouvrir `http://localhost:9090` dans un navigateur.

## Système de design

### Palette de couleurs

| Variable CSS       | Valeur hex          | Usage                          |
|--------------------|---------------------|-------------------------------|
| `--navy`           | `#0D1B2A`           | Fond principal                |
| `--navy2`          | `#152235`           | Fond secondaire / survols     |
| `--gold`           | `#C9A344`           | Couleur accent principale     |
| `--gold2`          | `#E8BE5A`           | Accent or clair               |
| `--text`           | `#F0EDE6`           | Texte principal               |
| `--text-2`         | `#7A8A9A`           | Texte secondaire / sous-titres|
| `--border`         | `rgba(201,163,68,.12)` | Séparateurs discrets        |

### Effet "Liquid Glass" (iOS 26)

Le site utilise un système de glassmorphism cohérent défini via ces variables CSS :

```css
--glass-bg:          rgba(14,26,42,.48)
--glass-bg-light:    rgba(255,255,255,.045)
--glass-border:      rgba(255,255,255,.10)
--glass-border-gold: rgba(201,163,68,.22)
--glass-blur:        blur(36px) saturate(180%) brightness(1.08)
--glass-blur-heavy:  blur(52px) saturate(200%) brightness(1.06)
--glass-spec:        inset 0 1px 0 rgba(255,255,255,.14), inset 0 -1px 0 rgba(0,0,0,.12)
--glass-spec-gold:   inset 0 1px 0 rgba(201,163,68,.18), inset 0 -1px 0 rgba(0,0,0,.1)
--glass-shadow:      0 8px 40px rgba(0,0,0,.55), 0 1px 0 rgba(255,255,255,.07)
--glass-shadow-lg:   0 20px 70px rgba(0,0,0,.65), 0 1px 0 rgba(255,255,255,.08)
--glass-radius:      18px
--glass-radius-sm:   14px
--pill-radius:       100px
```

Toujours appliquer `backdrop-filter` + `-webkit-backdrop-filter` ensemble pour la compatibilité Safari.

### Typographie

Aucune web font externe. Pile système uniquement : `'Helvetica Neue', Helvetica, Arial, sans-serif`.

Conventions de texte :
- Eyebrows / labels : `font-size: ~.55-.68rem`, `letter-spacing: 5-7px`, `text-transform: uppercase`, couleur `--gold`
- Titres de section : `font-size: ~.55rem`, `font-weight: 700`, `letter-spacing: 7px`, `text-transform: uppercase`
- Corps de texte : `font-size: ~.88-1rem`, couleur `--text-2`
- CTA / boutons : `font-weight: 800-900`, `letter-spacing: .18em`

### Architecture CSS

**Important** : les CSS custom properties du `:root` sont dupliquées dans chaque fichier HTML (dans le `<style>` inline). Il n'y a pas de feuille de style partagée. Lors de l'ajout ou de la modification d'une variable, **mettre à jour tous les fichiers HTML concernés**.

`index.html` contient le `:root` complet avec toutes les variables glass. Les autres pages utilisent une version abrégée (sans les variables rarement utilisées comme `--glass-bg-light`).

## Couche de données : `lions-data.js`

Ce fichier exporte trois tableaux globaux et quatre fonctions utilitaires utilisés par plusieurs pages via `<script src="lions-data.js">`.

### Tableaux

- **`LIONS_SQUAD`** — 18 joueurs. Champs : `num`, `pos`, `name`, `nat` (emoji drapeau), `goals`, `assists`, `photo` (chemin relatif vers `img/players/`)
- **`LIONS_MATCHES`** — Tous les matchs de la saison (Ligue 1, Coupe de France, UEFA CL). Champs : `comp`, `round`, `date` (ISO 8601), `home`, `away`, `sH`, `sA` (scores, `null` = à venir), `time` (optionnel), `venue` (optionnel)
- **`LIGUE1_TABLE`** — Classement de Ligue 1. Champs : `rank`, `club`, `pts`, `j`, `g`, `n`, `p`, `bp`, `bc`, `diff`, `form` (tableau de 5 éléments : `"V"`, `"N"`, `"D"`)

### Fonctions utilitaires

| Fonction | Signature | Description |
|---|---|---|
| `lionsResult(m)` | `match → "V"\|"N"\|"D"\|null` | Résultat de Lions FC pour un match (null si à venir) |
| `isPast(m)` | `match → boolean` | Vrai si la date du match est passée |
| `fmtDate(str)` | `"YYYY-MM-DD" → string` | Formatte en "Lun 16 aoû 2025" |
| `nextMatch()` | `() → match\|null` | Premier match à venir de Lions FC |

Pour ajouter un match, l'insérer dans `LIONS_MATCHES` en respectant l'ordre chronologique. Pour mettre à jour un résultat, remplir `sH` et `sA` (remplacer `null`).

## Fonctionnalités clés de `index.html`

### Animation canvas (scroll-driven)
- 142 frames JPEG dans `/frames/frame_XXXX.jpg` (numérotation à 4 chiffres avec zéros)
- Chargées dans un tableau `frames[]`, progression affichée dans le loader
- Le scroll sur `#hero` avance/recule dans les frames via `requestAnimationFrame`
- Le canvas se redimensionne au `resize` en tenant compte du `devicePixelRatio`

### Navbar pill
- Commence en full-width transparent, passe en "pill" glassmorphism au scroll (`#nav.pill`)
- Transition déclenchée à `scrollY > 80`

### Éléments UI communs (présents sur toutes les pages)
- `#scroll-prog` — barre de progression en haut (2px, dégradé or)
- `#cursor-glow` — lueur de 400px suivant le curseur (radial gradient)
- `#nav` — navbar fixe avec logo + liens + CTA "Billetterie"
- `<footer>` — footer avec logo, liens, réseaux sociaux et copyright

### Animations d'entrée
Pattern CSS standard : `opacity: 0; transform: translateY(Xpx); animation: fadeUp Xs Xs forwards;`
Les éléments révélés au scroll utilisent `IntersectionObserver` qui ajoute la classe `.visible`.

## Conventions de code

### HTML
- Langue : `<html lang="fr">` — tout le contenu UI est en **français**
- Chaque page est autonome : CSS inline dans `<head>`, JS inline avant `</body>`
- `lions-data.js` est chargé en premier si la page l'utilise, avant le script inline
- Attributs `loading="lazy"` sur les images non critiques

### JavaScript
- Vanilla JS uniquement (ES5/ES6 selon les fichiers — `index.html` utilise ES6, les autres ES5 avec `var`)
- Aucune dépendance externe (pas de jQuery, pas de lodash, rien)
- Les images Unsplash sont utilisées pour la galerie et le fond du héros (URLs directes)
- Pas de module system — tout est en global scope

### Images
- Photos joueurs : `img/players/player1.png` … `player4.png` (réutilisées pour plusieurs joueurs)
- Les entrées `LIONS_SQUAD` référencent `photo` avec un chemin depuis la racine
- Les frames d'animation sont numérotées `frame_0001.jpg` … `frame_0142.jpg`

## Déploiement

Le site est hébergé sur **OVH** via déploiement Git (non via FTP).

Le workflow GitHub Actions FTP (`.github/workflows/disabled/`) est **désactivé** — ne pas le réactiver. Le déploiement se fait directement depuis le repository OVH.

Le fichier `lions-hero.mp4` est exclu du déploiement FTP (trop lourd) — conserver cette exclusion si le workflow était réactivé.

## Workflow de développement

1. Lancer le serveur local : `python3 -m http.server 9090`
2. Modifier directement les fichiers HTML/JS
3. Rafraîchir le navigateur (pas de hot reload)
4. Pour les données : modifier uniquement `lions-data.js`
5. Commit et push sur `main` → déploiement automatique OVH

## Pièges courants

- **CSS dupliqué** : modifier `--glass-*` ou les couleurs nécessite de mettre à jour le `:root` dans chaque fichier HTML séparément.
- **Scores `null`** : un match à venir a `sH: null, sA: null`. Ne jamais mettre `0` si le match n'a pas eu lieu.
- **Frames manquantes** : si une frame est absente, `drawFrame()` retourne silencieusement (`img.complete` est false). Les 142 frames doivent toutes être présentes.
- **Pas de build** : il n'y a pas de `npm run build`, pas de minification, pas de transpilation. Ce qui est dans le repo est ce qui est servi.
- **Responsive** : le breakpoint mobile principal est `768px`. La navbar se simplifie (`.nav-links { display: none }`), les grilles passent en colonne unique.
