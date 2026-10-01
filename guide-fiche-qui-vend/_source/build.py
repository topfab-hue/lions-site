import re,sys
D='/home/user/lions-site/guide-fiche-qui-vend/'
src=open(D+'_source/guide.src.html',encoding='utf-8').read()

css=src.split('<style>\n',1)[1].split('</style>',1)[0]
body=src.split('<body>',1)[1].split('<script>',1)[0]
js='<script>'+src.split('<script>',1)[1].split('</script>',1)[0]+'</script>'

# retire les @font-face du source (ajoutés selon le mode)
css=re.sub(r"@font-face\{[^}]*\}\n?","",css)

ZMAP={'.scrim':99980,'.panel':99990,'.modal':99995,'.tip':99999,'.toast':99999,'.fab':99970}
KF=sorted(set(re.findall(r'@keyframes (\w+)',css)))

def split_top(t):
    out=[];i=0;n=len(t)
    while i<n:
        j=t.find('{',i)
        if j<0:
            if t[i:].strip():out.append((t[i:].strip(),None))
            break
        head=t[i:j].strip();d=1;k=j+1
        while k<n and d:
            d+= (t[k]=='{')-(t[k]=='}');k+=1
        out.append((head,t[j+1:k-1]));i=k
    return out

def split_sel(s):
    parts=[];d=0;cur=''
    for ch in s:
        if ch=='(':d+=1
        if ch==')':d-=1
        if ch==',' and d==0:parts.append(cur);cur=''
        else:cur+=ch
    parts.append(cur);return [p.strip() for p in parts if p.strip()]

ROOTSEL=':is(#lfqv,#lfqv-ov)'
def prefix_sel(s):
    if s in(':root','html','body'):return ROOTSEL
    return ROOTSEL+' '+s

def process(t):
    res=[]
    for head,inner in split_top(t):
        if inner is None:continue
        if head.startswith('@media') or head.startswith('@supports'):
            res.append(head+'{'+process(inner)+'}')
        elif head.startswith('@keyframes'):
            name=head.split()[1]
            res.append('@keyframes lfqv-'+name+'{'+inner+'}')
        elif head.startswith('@'):
            res.append(head+'{'+inner+'}')
        else:
            sels=split_sel(head)
            if sels==['html']:continue  # scroll-behavior géré en JS / par mode
            if inner.strip()=='' :continue
            for s in sels:
                if s in ZMAP:
                    inner=re.sub(r'z-index:\d+','z-index:%d'%ZMAP[s],inner)
            res.append(','.join(prefix_sel(s) for s in sels)+'{'+inner+'}')
    return '\n'.join(res)

def rem2px(m):
    v=float(m.group(1))*16
    return ('%g'%round(v,2))+'px'
css=re.sub(r'(-?\d*\.?\d+)rem',rem2px,css)
scoped=process(css)
def fix_anim(m):
    v=m.group(1)
    for n in KF:v=re.sub(r'(?<![\w-])%s(?![\w-])'%n,'lfqv-'+n,v)
    return 'animation:'+v
scoped=re.sub(r'animation:([^;}]*)',fix_anim,scoped)

extra="""
#lfqv{overflow-x:clip}
#lfqv-ov{font-size:15px;line-height:1.7}
#lfqv [id]{scroll-margin-top:120px}
#lfqv.standalone{background:var(--bg);min-height:100vh}
#lfqv.embed{background:transparent}
#lfqv.embed .nav,#lfqv.embed .drawer,#lfqv.embed .prog{display:none!important}
#lfqv.embed .hero{padding-top:56px}
#lfqv-ov.standalone .toc{display:none}
#lfqv-ov .fab{transition:bottom .5s cubic-bezier(.22,.8,.24,1),transform .35s,box-shadow .35s}
#lfqv-ov.has-toc .toast{bottom:132px}
@media(max-width:1180px){#lfqv-ov.has-toc .fab{bottom:118px}}
#lfqv.embed [id]{scroll-margin-top:130px}
"""
scoped+=extra

SPLIT=body.index('<button class="pill dark fab"')
body_main,body_ov=body[:SPLIT],body[SPLIT:]
# JS : tout est limité au conteneur, jamais au document entier
js=js.replace("const $=(s,r=document)=>r.querySelector(s), $$=(s,r=document)=>[...r.querySelectorAll(s)];",
"const ROOT=document.getElementById('lfqv'),OV=document.getElementById('lfqv-ov');\nif(OV&&OV.parentNode!==document.body)document.body.appendChild(OV);\nconst $=(s,r)=>r?r.querySelector(s):(ROOT.querySelector(s)||(OV&&OV.querySelector(s)));\nconst $$=(s,r)=>r?[...r.querySelectorAll(s)]:[...ROOT.querySelectorAll(s),...(OV?OV.querySelectorAll(s):[])];\n[ROOT,OV].filter(Boolean).forEach(h=>h.addEventListener('click',e=>{const a=e.target.closest('a[href^=\"#\"]');if(!a)return;const id=a.getAttribute('href').slice(1);const t=id&&ROOT.querySelector('#'+id);if(!t)return;e.preventDefault();t.scrollIntoView({behavior:'smooth',block:'start'})}));",1)
assert 'const ROOT' in js

FA_LOCAL="""@font-face{font-family:'HVOliveandFigs';src:url('fonts/HVOliveandFigs-Regular.otf') format('opentype');font-weight:400;font-style:normal;font-display:swap}
@font-face{font-family:'HVOliveandFigs';src:url('fonts/HVOliveandFigs-Italic.otf') format('opentype');font-weight:400;font-style:italic;font-display:swap}
"""
FA_LOCAL+="@font-face{font-family:'SnellRoundhand';src:url('fonts/SnellRoundhand-Regular.ttf') format('truetype');font-weight:400;font-style:normal;font-display:swap}\n"
U='https://www.kezacreation.com/wp-content/uploads/2025/06/'
FA_SITE="""@font-face{font-family:'HVOliveandFigs';src:url('%sHVOliveandFigs-Regular.otf') format('opentype');font-weight:400;font-style:normal;font-display:swap}
@font-face{font-family:'HVOliveandFigs';src:url('%sHVOliveandFigs-Italic.otf') format('opentype');font-weight:400;font-style:italic;font-display:swap}
"""%(U,U)
FA_SITE+="@font-face{font-family:'SnellRoundhand';src:url('https://www.kezacreation.com/wp-content/uploads/2025/07/SnellRoundhand-01.ttf') format('truetype');font-weight:400;font-style:normal;font-display:swap}\n"

head_meta=src.split('<style>',1)[0]
# standalone
gf='<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600&display=swap" rel="stylesheet">'
standalone=head_meta+'<style>\nhtml{scroll-behavior:smooth}\nbody{margin:0;background:#F7F4F2}\n'+FA_LOCAL+scoped+'\n</style>\n</head>\n<body>\n<div id="lfqv" class="standalone">'+body_main+'</div>\n<div id="lfqv-ov" class="standalone">'+body_ov+'</div>\n'+js+'\n</body>\n</html>\n'
open(D+'index.html','w',encoding='utf-8').write(standalone)

# fragment pour WordPress
bm=body_main.replace('<h1 class="ttl">','<h2 class="ttl">').replace('</h1>','</h2>')
embed=(gf+"\n<style>\n"+FA_SITE+scoped+"\n</style>\n<div id=\"lfqv\" class=\"embed\">"+bm+"</div>\n<div id=\"lfqv-ov\" class=\"embed\">"+body_ov+"</div>\n"+js+"\n")
open(D+'embed.html','w',encoding='utf-8').write(embed)
print(len(standalone),len(embed))
