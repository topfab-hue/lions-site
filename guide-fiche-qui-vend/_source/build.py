import re,sys,os,base64
D=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/'
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
#lfqv.js .rv{opacity:0;transform:translateY(16px);transition:opacity .9s cubic-bezier(.22,.8,.24,1),transform .9s cubic-bezier(.22,.8,.24,1)}
#lfqv.js .rv.in{opacity:1;transform:none}
#lfqv-ov.standalone .toc{display:none}
#lfqv-ov .fab{transition:bottom .5s cubic-bezier(.22,.8,.24,1),transform .35s,box-shadow .35s}
#lfqv.embed [id]{scroll-margin-top:130px}
#lfqv-ov .fab{bottom:calc(20px + var(--lf-dodge,0px))}
#lfqv-ov .toc{bottom:calc(14px + env(safe-area-inset-bottom,0px) + var(--lf-dodge,0px))}
#lfqv-ov .toast{bottom:calc(84px + var(--lf-dodge,0px))}
#lfqv-ov.has-toc .toast{bottom:calc(132px + var(--lf-dodge,0px))}
@media(max-width:1180px){#lfqv-ov.has-toc .fab{bottom:calc(118px + var(--lf-dodge,0px))}}
#lfqv-ov.lf-tall .toc,#lfqv-ov.lf-tall .fab{display:none}
#lfqv .sr,#lfqv-ov .sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
"""
scoped+=extra

body=re.sub(r'<!--.*?-->','',body,flags=re.S)
SPLIT=body.index('<button type="button" class="pill dark fab"')
body_main,body_ov=body[:SPLIT],body[SPLIT:]
# JS : tout est limité au conteneur, jamais au document entier
js=js.replace("const $=(s,r=document)=>r.querySelector(s), $$=(s,r=document)=>[...r.querySelectorAll(s)];",
"const ROOT=document.getElementById('lfqv'),OV=document.getElementById('lfqv-ov');\nif(OV&&OV.parentNode!==document.body)document.body.appendChild(OV);\nconst $=(s,r)=>r?r.querySelector(s):(ROOT.querySelector(s)||(OV&&OV.querySelector(s)));\nconst $$=(s,r)=>r?[...r.querySelectorAll(s)]:[...ROOT.querySelectorAll(s),...(OV?OV.querySelectorAll(s):[])];\n[ROOT,OV].filter(Boolean).forEach(h=>h.addEventListener('click',e=>{const a=e.target.closest('a[href^=\"#\"]');if(!a)return;const id=a.getAttribute('href').slice(1);const t=id&&ROOT.querySelector('#'+id);if(!t)return;e.preventDefault();t.scrollIntoView({behavior:'smooth',block:'start'})}));",1)
js=js.replace('&&','&& ')
assert '&&' not in js.replace('&& ','')

# --- garde-fou WordPress : un '&' hors entité valide à l'intérieur d'un faux "tag" <...> serait réécrit en &#038;
import re as _re
def _risky(t):
    out=[]
    for m in _re.finditer(r"<[A-Za-z/!][^<>]*>",t):
        for a in _re.finditer(r"&(?!(amp|lt|gt|quot|nbsp|#39|#038);)",m.group(0)):
            out.append(m.group(0)[:80]);break
    return out
_r=_risky(js)
assert not _r,'Risque WordPress (& dans un faux tag) : %s'%_r[:3]
assert 'const ROOT' in js
assert '<img' not in js,'<img en clair dans le script'

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
MONT=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'montserrat.b64')).read().strip()
FA_MONT="@font-face{font-family:'LFQV Montserrat';src:url(data:font/woff2;base64,"+MONT+") format('woff2');font-weight:100 900;font-style:normal;font-display:swap}\n"
gf=''
standalone=head_meta+'<style>\nhtml{scroll-behavior:smooth}\nbody{margin:0;background:#F7F4F2}\n'+FA_MONT+FA_LOCAL+scoped+'\n</style>\n</head>\n<body>\n<div id="lfqv" class="standalone">'+body_main+'</div>\n<div id="lfqv-ov" class="standalone">'+body_ov+'</div>\n'+js+'\n</body>\n</html>\n'
open(D+'index.html','w',encoding='utf-8').write(standalone)

# fragment WordPress : script en base64
raw=js[len('<script>'):-len('</script>')]
b64=base64.b64encode(raw.encode('utf-8')).decode()
jsb='<script>(function(){try{(new Function(decodeURIComponent(escape(atob("'+b64+'")))))()}catch(e){if(window.console)console.error("LFQV",e)}})();</script>'
bm=body_main
embed=(gf+"\n<style>\n"+FA_MONT+FA_SITE+scoped+"\n</style>\n<div id=\"lfqv\" class=\"embed\">"+bm+"</div>\n<div id=\"lfqv-ov\" class=\"embed\">"+body_ov+"</div>\n"+jsb+"\n")
open(D+'embed.html','w',encoding='utf-8').write(embed)
print(len(standalone),len(embed))
