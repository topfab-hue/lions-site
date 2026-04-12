/* ── LIONS FC — SHARED DATA ── */
var LIONS_SQUAD = [
  { num:27, pos:"Attaquant",        name:"Marcus Leone",   nat:"🇫🇷", goals:18, assists:7,  photo:"img/players/player1.png" },
  { num:10, pos:"Milieu offensif",  name:"João Silva",     nat:"🇧🇷", goals:12, assists:14, photo:"img/players/player3.png" },
  { num:9,  pos:"Avant-centre",     name:"Darius Kamara",  nat:"🇨🇮", goals:15, assists:3,  photo:"img/players/player1.png" },
  { num:7,  pos:"Ailier droit",     name:"Alexis Roux",    nat:"🇫🇷", goals:9,  assists:11, photo:"img/players/player2.png" },
  { num:11, pos:"Ailier gauche",    name:"Nabil Ouali",    nat:"🇲🇦", goals:7,  assists:9,  photo:"img/players/player4.png" },
  { num:8,  pos:"Milieu défensif",  name:"Lars Müller",    nat:"🇩🇪", goals:3,  assists:6,  photo:"img/players/player2.png" },
  { num:6,  pos:"Milieu central",   name:"Théo Martin",    nat:"🇫🇷", goals:4,  assists:8,  photo:"img/players/player2.png" },
  { num:14, pos:"Milieu central",   name:"Pablo Ruiz",     nat:"🇪🇸", goals:2,  assists:5,  photo:"img/players/player3.png" },
  { num:4,  pos:"Défenseur central",name:"Ricardo Vega",   nat:"🇪🇸", goals:2,  assists:1,  photo:"img/players/player3.png" },
  { num:5,  pos:"Défenseur central",name:"Mats Vogel",     nat:"🇩🇪", goals:1,  assists:2,  photo:"img/players/player2.png" },
  { num:3,  pos:"Latéral gauche",   name:"Kylian Ndiaye",  nat:"🇸🇳", goals:1,  assists:4,  photo:"img/players/player1.png" },
  { num:2,  pos:"Latéral droit",    name:"Antonio Greco",  nat:"🇮🇹", goals:0,  assists:3,  photo:"img/players/player3.png" },
  { num:1,  pos:"Gardien",          name:"Keita Diallo",   nat:"🇸🇳", goals:0,  assists:0,  photo:"img/players/player1.png" },
  { num:16, pos:"Gardien",          name:"Romain Lefort",  nat:"🇫🇷", goals:0,  assists:0,  photo:"img/players/player2.png" },
  { num:20, pos:"Attaquant",        name:"Hugo Ferreira",  nat:"🇵🇹", goals:5,  assists:2,  photo:"img/players/player3.png" },
  { num:17, pos:"Ailier droit",     name:"Samir Haddad",   nat:"🇩🇿", goals:4,  assists:5,  photo:"img/players/player4.png" },
  { num:23, pos:"Défenseur central",name:"Oluwaseun Ade",  nat:"🇳🇬", goals:0,  assists:1,  photo:"img/players/player1.png" },
  { num:19, pos:"Milieu offensif",  name:"Sofiane Barka",  nat:"🇫🇷", goals:3,  assists:4,  photo:"img/players/player4.png" }
];

var LIONS_MATCHES = [
  /* ─ LIGUE 1 ─ */
  { comp:"Ligue 1", round:"J1",  date:"2025-08-16", home:"Lions FC",         away:"AS Montagne",       sH:3, sA:1 },
  { comp:"Ligue 1", round:"J2",  date:"2025-08-23", home:"RC Bordeaux",      away:"Lions FC",          sH:0, sA:2 },
  { comp:"Ligue 1", round:"J3",  date:"2025-08-30", home:"Lions FC",         away:"OC Riviera",        sH:1, sA:1 },
  { comp:"Ligue 1", round:"J4",  date:"2025-09-13", home:"FC Strasbourg",    away:"Lions FC",          sH:2, sA:3 },
  { comp:"Ligue 1", round:"J5",  date:"2025-09-20", home:"Lions FC",         away:"SC Atlantique",     sH:4, sA:0 },
  { comp:"Ligue 1", round:"J6",  date:"2025-09-27", home:"Stade Nordique",   away:"Lions FC",          sH:1, sA:2 },
  { comp:"Ligue 1", round:"J7",  date:"2025-10-04", home:"Lions FC",         away:"FC Lyonnais",       sH:2, sA:2 },
  { comp:"Ligue 1", round:"J8",  date:"2025-10-18", home:"AS Capital",       away:"Lions FC",          sH:0, sA:1 },
  { comp:"Ligue 1", round:"J9",  date:"2025-10-25", home:"Lions FC",         away:"RC Marseillais",    sH:3, sA:0 },
  { comp:"Ligue 1", round:"J10", date:"2025-11-01", home:"FC Méditerranée",  away:"Lions FC",          sH:1, sA:3 },
  { comp:"Ligue 1", round:"J11", date:"2025-11-08", home:"Lions FC",         away:"US Bretagne",       sH:2, sA:1 },
  { comp:"Ligue 1", round:"J12", date:"2025-11-22", home:"OC Riviera",       away:"Lions FC",          sH:0, sA:0 },
  { comp:"Ligue 1", round:"J13", date:"2025-11-29", home:"Lions FC",         away:"Stade Nordique",    sH:1, sA:0 },
  { comp:"Ligue 1", round:"J14", date:"2025-12-06", home:"SC Atlantique",    away:"Lions FC",          sH:2, sA:4 },
  { comp:"Ligue 1", round:"J15", date:"2025-12-13", home:"Lions FC",         away:"AS Capital",        sH:2, sA:0 },
  { comp:"Ligue 1", round:"J16", date:"2025-12-20", home:"RC Marseillais",   away:"Lions FC",          sH:1, sA:2 },
  { comp:"Ligue 1", round:"J17", date:"2026-01-10", home:"Lions FC",         away:"RC Bordeaux",       sH:3, sA:1 },
  { comp:"Ligue 1", round:"J18", date:"2026-01-17", home:"AS Montagne",      away:"Lions FC",          sH:0, sA:2 },
  { comp:"Ligue 1", round:"J19", date:"2026-01-24", home:"Lions FC",         away:"FC Strasbourg",     sH:2, sA:1 },
  { comp:"Ligue 1", round:"J20", date:"2026-01-31", home:"US Bretagne",      away:"Lions FC",          sH:1, sA:1 },
  { comp:"Ligue 1", round:"J21", date:"2026-02-07", home:"Lions FC",         away:"FC Méditerranée",   sH:1, sA:0 },
  { comp:"Ligue 1", round:"J22", date:"2026-02-14", home:"FC Lyonnais",      away:"Lions FC",          sH:2, sA:3 },
  { comp:"Ligue 1", round:"J23", date:"2026-02-21", home:"Lions FC",         away:"AS Capital",        sH:3, sA:0 },
  { comp:"Ligue 1", round:"J24", date:"2026-02-28", home:"Lions FC",         away:"OC Riviera",        sH:0, sA:1 },
  { comp:"Ligue 1", round:"J25", date:"2026-03-07", home:"RC Bordeaux",      away:"Lions FC",          sH:1, sA:2 },
  { comp:"Ligue 1", round:"J26", date:"2026-03-14", home:"Lions FC",         away:"RC Marseillais",    sH:2, sA:0 },
  { comp:"Ligue 1", round:"J27", date:"2026-03-21", home:"SC Atlantique",    away:"Lions FC",          sH:0, sA:3 },
  { comp:"Ligue 1", round:"J28", date:"2026-04-04", home:"Lions FC",         away:"Stade Nordique",    sH:2, sA:1 },
  { comp:"Ligue 1", round:"J29", date:"2026-04-11", home:"US Bretagne",      away:"Lions FC",          sH:0, sA:2 },
  { comp:"Ligue 1", round:"J30", date:"2026-04-18", home:"Lions FC",         away:"FC Lyonnais",       sH:null, sA:null, time:"21:00" },
  { comp:"Ligue 1", round:"J31", date:"2026-04-25", home:"AS Capital",       away:"Lions FC",          sH:null, sA:null, time:"17:05" },
  { comp:"Ligue 1", round:"J32", date:"2026-05-02", home:"Lions FC",         away:"FC Méditerranée",   sH:null, sA:null, time:"21:00" },
  { comp:"Ligue 1", round:"J33", date:"2026-05-09", home:"OC Riviera",       away:"Lions FC",          sH:null, sA:null, time:"17:05" },
  { comp:"Ligue 1", round:"J34", date:"2026-05-23", home:"Lions FC",         away:"AS Montagne",       sH:null, sA:null, time:"21:00" },

  /* ─ COUPE DE FRANCE ─ */
  { comp:"Coupe de France", round:"16e de finale", date:"2026-01-03", home:"Lions FC",    away:"US Granville",      sH:4, sA:0 },
  { comp:"Coupe de France", round:"8e de finale",  date:"2026-01-25", home:"AS Troyes",   away:"Lions FC",          sH:1, sA:2 },
  { comp:"Coupe de France", round:"Quart de finale",date:"2026-02-18",home:"Lions FC",    away:"OC Riviera",        sH:2, sA:1 },
  { comp:"Coupe de France", round:"Demi-finale",   date:"2026-04-08", home:"FC Lyonnais", away:"Lions FC",          sH:0, sA:1 },
  { comp:"Coupe de France", round:"⭐ FINALE",      date:"2026-05-16", home:"Lions FC",    away:"SC Atlantique",     sH:null, sA:null, time:"21:00", venue:"Stade de France" },

  /* ─ UEFA CHAMPIONS LEAGUE ─ */
  { comp:"UEFA CL", round:"Phase de groupes J1", date:"2025-09-17", home:"Lions FC",         away:"Valencia CF",      sH:2, sA:0 },
  { comp:"UEFA CL", round:"Phase de groupes J2", date:"2025-10-01", home:"Sporting CP",      away:"Lions FC",         sH:1, sA:1 },
  { comp:"UEFA CL", round:"Phase de groupes J3", date:"2025-10-22", home:"Lions FC",         away:"BSC Young Boys",   sH:3, sA:1 },
  { comp:"UEFA CL", round:"Phase de groupes J4", date:"2025-11-05", home:"Valencia CF",      away:"Lions FC",         sH:2, sA:2 },
  { comp:"UEFA CL", round:"Phase de groupes J5", date:"2025-11-26", home:"Lions FC",         away:"Sporting CP",      sH:1, sA:0 },
  { comp:"UEFA CL", round:"Phase de groupes J6", date:"2025-12-10", home:"BSC Young Boys",   away:"Lions FC",         sH:0, sA:2 },
  { comp:"UEFA CL", round:"Huitièmes — Aller",   date:"2026-02-17", home:"Lions FC",         away:"Bayer Leverkusen", sH:2, sA:1 },
  { comp:"UEFA CL", round:"Huitièmes — Retour",  date:"2026-03-10", home:"Bayer Leverkusen", away:"Lions FC",         sH:1, sA:2 },
  { comp:"UEFA CL", round:"Quarts — Aller",      date:"2026-04-07", home:"Lions FC",         away:"Atlético Madrid",  sH:1, sA:0 },
  { comp:"UEFA CL", round:"⚡ Quarts — Retour",  date:"2026-04-15", home:"Atlético Madrid",  away:"Lions FC",         sH:null, sA:null, time:"21:00", venue:"Wanda Metropolitano" }
];

/* Ligue 1 standings */
var LIGUE1_TABLE = [
  { rank:1, club:"Lions FC",       pts:68, j:29, g:21, n:5,  p:3,  bp:62, bc:22, diff:"+40", form:["V","V","N","V","V"] },
  { rank:2, club:"OC Riviera",     pts:58, j:29, g:17, n:7,  p:5,  bp:48, bc:28, diff:"+20", form:["V","D","V","N","D"] },
  { rank:3, club:"FC Lyonnais",    pts:55, j:29, g:16, n:7,  p:6,  bp:55, bc:35, diff:"+20", form:["N","V","D","V","N"] },
  { rank:4, club:"AS Capital",     pts:50, j:29, g:14, n:8,  p:7,  bp:42, bc:30, diff:"+12", form:["D","V","D","V","D"] },
  { rank:5, club:"RC Bordeaux",    pts:48, j:29, g:13, n:9,  p:7,  bp:44, bc:36, diff:"+8",  form:["V","D","N","D","V"] },
  { rank:6, club:"Stade Nordique", pts:44, j:29, g:12, n:8,  p:9,  bp:38, bc:40, diff:"-2",  form:["D","N","V","D","D"] },
  { rank:7, club:"RC Marseillais", pts:42, j:29, g:11, n:9,  p:9,  bp:36, bc:38, diff:"-2",  form:["N","D","V","D","N"] },
  { rank:8, club:"SC Atlantique",  pts:38, j:29, g:10, n:8,  p:11, bp:32, bc:44, diff:"-12", form:["D","D","D","V","D"] },
  { rank:9, club:"US Bretagne",    pts:35, j:29, g:9,  n:8,  p:12, bp:30, bc:42, diff:"-12", form:["D","N","D","D","N"] },
  { rank:10,club:"FC Strasbourg",  pts:30, j:29, g:7,  n:9,  p:13, bp:28, bc:48, diff:"-20", form:["D","D","N","D","D"] },
  { rank:11,club:"FC Méditerranée",pts:27, j:29, g:6,  n:9,  p:14, bp:24, bc:52, diff:"-28", form:["D","D","D","N","D"] },
  { rank:12,club:"AS Montagne",    pts:22, j:29, g:5,  n:7,  p:17, bp:22, bc:60, diff:"-38", form:["D","D","D","D","N"] }
];

/* Helpers */
function lionsResult(m) {
  if (m.sH === null) return null;
  var isH = m.home === "Lions FC";
  var lG = isH ? m.sH : m.sA;
  var oG = isH ? m.sA : m.sH;
  if (lG > oG) return "V";
  if (lG < oG) return "D";
  return "N";
}

function isPast(m) {
  return new Date(m.date) < new Date();
}

function fmtDate(str) {
  var d = new Date(str);
  var days = ["Dim","Lun","Mar","Mer","Jeu","Ven","Sam"];
  var months = ["jan","fév","mar","avr","mai","jun","jul","aoû","sep","oct","nov","déc"];
  return days[d.getDay()] + " " + d.getDate() + " " + months[d.getMonth()] + " " + d.getFullYear();
}

function nextMatch() {
  var now = new Date();
  for (var i = 0; i < LIONS_MATCHES.length; i++) {
    var m = LIONS_MATCHES[i];
    if (new Date(m.date) > now && (m.home === "Lions FC" || m.away === "Lions FC")) return m;
  }
  return null;
}
