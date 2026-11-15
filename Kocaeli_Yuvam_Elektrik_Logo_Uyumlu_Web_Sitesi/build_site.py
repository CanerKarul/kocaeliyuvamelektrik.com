# -*- coding: utf-8 -*-
"""Yuvam Elektrik: multi-page responsive static site + editorial content.
Run: python build_site.py (from this directory). Site folder is recreated.
"""
from __future__ import annotations
import html, json, re, textwrap, shutil
from pathlib import Path
from urllib.parse import quote
from xml.sax.saxutils import escape as xml_escape
from content_data import SERVICES, BLOGS, FAQS, REGIONS, HOMEPAGE_SECTION_COPY as HC

ROOT = Path(__file__).resolve().parent
SITE = ROOT/'site'
CONFIG = json.loads((ROOT/'SITE_AYARLARI.json').read_text(encoding='utf-8'))
PHONE = CONFIG.get('telefon_uluslararasi','').strip()
WHATSAPP = CONFIG.get('whatsapp_uluslararasi','').strip() # Bilinmeyen WhatsApp hattı otomatik varsayılmaz.
VISIBLE_PHONE = CONFIG.get('telefon_gorunen','').strip() or 'Telefon numarası eklenecek'
DOMAIN = CONFIG.get('alan_adi','').strip().rstrip('/')
PUBLISHED = bool(PHONE and DOMAIN)
BRAND = CONFIG.get('isletme_adi','Yuvam Elektrik')
PHONE_MISSING = not bool(PHONE)

SEO_SERVICE_DESCRIPTIONS = {
    'elektrik-ariza-tespiti-ve-tamiri': 'İzmit, Alikahya, Yuvam Akarca ve Yahya Kaptan’da 7/24 elektrik arıza tespiti ve yerinde tamir. Günün her saati bize ulaşabilirsiniz.',
    'sigorta-ve-kacak-akim-rolesi': 'İzmit’te sigorta sürekli atıyor veya kaçak akım rölesi devreyi kapatıyor mu? Yuvam Elektrik ile güvenli arıza değerlendirmesi için iletişime geçin.',
    'priz-anahtar-ve-salter-montaji': 'İzmit, Alikahya ve Yuvam Akarca’da priz, anahtar ve şalter montajı veya bağlantı kontrolü için Yuvam Elektrik’e ulaşın.',
    'avize-armatur-ve-aplik-montaji': 'İzmit’te avize, aplik ve armatür montajı için Yuvam Elektrik’e ulaşın. Alikahya ve Yahya Kaptan için servis uygunluğunu görüşün.',
    'goruntulu-diafon-ve-interkom': 'İzmit’te görüntülü diafon çalışmıyor mu? Ses, görüntü ve kapı açma arızaları için Yuvam Elektrik ile montaj ve onarım seçeneklerini görüşün.',
}
SEO_TITLE_OVERRIDES = {
    'elektrik-ariza-tespiti-ve-tamiri':'İzmit Elektrik Arıza Tamiri | Yuvam Elektrik',
    'elektrik-tesisati-yenileme-ve-pano-tadilati':'İzmit Elektrik Tesisatı Yenileme | Yuvam Elektrik',
    'goruntulu-diafon-ve-interkom':'İzmit Görüntülü Diafon Montajı | Yuvam Elektrik',
    'telefon-ve-internet-sistemleri-kurulumu':'İzmit Telefon ve İnternet Tesisatı | Yuvam Elektrik',
    'ticari-alan-elektrik-bakim-taahhut':'İzmit İş Yeri Elektrik Bakımı | Yuvam Elektrik',
}
BLOG_SEO_TITLES = {
    'avize-montajinda-dikkat-edilecekler':'Avize Montajı Öncesi Kontrol | Yuvam Elektrik',
    'goruntulu-diafon-calismiyorsa':'Görüntülü Diafon Arızası | Yuvam Elektrik',
}

BLOG_RELATED_SERVICE = {
    'komsularda-elektrik-var-evde-yok':'elektrik-ariza-tespiti-ve-tamiri',
    'sigorta-surekli-neden-atar': 'sigorta-ve-kacak-akim-rolesi',
    'priz-isiniyorsa-ne-yapilmali': 'priz-anahtar-ve-salter-montaji',
    'avize-montajinda-dikkat-edilecekler': 'avize-armatur-ve-aplik-montaji',
    'goruntulu-diafon-calismiyorsa': 'goruntulu-diafon-ve-interkom',
}

ICONS={
 'bolt':'<path d="m13 2-3 8H5l6 12 3-8h5L13 2Z"/>',
 'cable':'<path d="M7 13a4 4 0 0 1 4-4h2a4 4 0 0 1 4 4v1a4 4 0 0 1-4 4H9"/><path d="M5 9V4M9 9V4M15 18v3m4-3v3"/>',
 'plug':'<path d="M12 22v-5m-5-5V3m10 9V3M5 12h14v2a7 7 0 0 1-14 0v-2Z"/>',
 'bulb':'<path d="M9 18h6m-5 4h4M9 14a6 6 0 1 1 6 0c-.8.7-1 1.4-1 3h-4c0-1.6-.2-2.3-1-3Z"/>',
 'sun':'<circle cx="12" cy="12" r="4"/><path d="M12 2v2m0 16v2M4.9 4.9l1.4 1.4m11.4 11.4 1.4 1.4M2 12h2m16 0h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>',
 'shield':'<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10Z"/><path d="m9 12 2 2 4-4"/>',
 'panel':'<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18m-12 4h6m-3-4v12"/>',
 'wifi':'<path d="M2 8.8a15 15 0 0 1 20 0M5 12a11 11 0 0 1 14 0m-11 3a6 6 0 0 1 8 0"/><circle cx="12" cy="19" r="1"/>',
 'phone':'<path d="M22 16.9V20a2 2 0 0 1-2.2 2A18 18 0 0 1 2 4.2 2 2 0 0 1 4 2h3.1a2 2 0 0 1 2 1.7l.5 3.1a2 2 0 0 1-.6 1.8l-1.7 1.7a14 14 0 0 0 6.4 6.4l1.7-1.7a2 2 0 0 1 1.8-.6l3.1.5a2 2 0 0 1 1.7 2Z"/>',
 'satellite':'<path d="M2 16a10 10 0 0 0 13-13L2 16Zm0 0 6 6m8-12 5-5M14 2l8 8"/>',
 'video':'<rect x="3" y="3" width="18" height="18" rx="3"/><path d="m10 8 6 4-6 4V8Z"/>',
 'camera':'<path d="M5 7h3l2-3h4l2 3h3a2 2 0 0 1 2 2v10H3V9a2 2 0 0 1 2-2Z"/><circle cx="12" cy="13" r="3"/>',
 'bell':'<path d="M18 8a6 6 0 0 0-12 0c0 7-3 7-3 9h18c0-2-3-2-3-9Z"/><path d="M10 21h4"/>',
 'building':'<rect x="3" y="6" width="18" height="15" rx="1"/><path d="M8 21v-5h8v5M7 10h2m6 0h2M7 13h2m6 0h2M8 6V3h8v3"/>',
 'map':'<path d="m3 6 6-3 6 3 6-3v15l-6 3-6-3-6 3V6Zm6-3v15m6-12v15"/>',
 'check':'<path d="m4 12 5 5L20 6"/>',
 'arrow':'<path d="M5 12h14m-6-6 6 6-6 6"/>',
 'menu':'<path d="M4 6h16M4 12h16M4 18h16"/>',
 'message':'<path d="M21 11.5a8.4 8.4 0 0 1-9 8.4 9.6 9.6 0 0 1-4.1-.9L3 21l2.1-4.7A8.4 8.4 0 1 1 21 11.5Z"/>',
}

def e(s): return html.escape(str(s),quote=True)

def icon(name, size=24):
    return f'<svg aria-hidden="true" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round">{ICONS.get(name, ICONS["bolt"])}</svg>'

def phone_href(prefix): return 'tel:'+PHONE if PHONE else prefix+'iletisim/'
def whatsapp_href(prefix, label='Merhaba, Yuvam Elektrik hizmetleri hakkında bilgi almak istiyorum.'):
    if not WHATSAPP: return prefix+'iletisim/'
    digits=re.sub(r'\D','',WHATSAPP)
    return 'https://wa.me/'+digits+'?text='+quote(label)

def wa_btn(label='WhatsApp ile Yazın', prefix='___ROOT___', text=None):
    if not WHATSAPP: return ''
    target = whatsapp_href(prefix, text) if text else whatsapp_href(prefix)
    return btn(label, target, 'btn-whatsapp', svg='message')

def btn(label, href, kind='btn-primary', extra='', svg=None):
    attr=' rel="noopener noreferrer" target="_blank"' if href.startswith('https://wa.me') else ''
    ic=icon(svg,19) if svg else ''
    return f'<a class="btn {kind} {extra}" href="{e(href)}"{attr}>{ic}{e(label)}</a>'

def site_logo(prefix):
    # Markanın onaylı, tamamen vektörel orijinal logosu. Header/footer aynı dosyayı kullanır.
    return f'<a class="brand" href="{prefix or "./"}" aria-label="Kocaeli Yuvam Elektrik ana sayfa"><img class="brand-logo" src="{prefix}assets/yuvam-elektrik-logo.svg?v=20261115-r2" width="139" height="96" alt="Kocaeli Yuvam Elektrik" decoding="async"></a>'

def nav(prefix, active):
    links=[('Ana Sayfa','','home'),('Hizmetler','hizmetler/','services'),('Bölgeler','hizmet-bolgeleri/','regions'),('Hakkımızda','hakkimizda/','about'),('Blog','blog/','blog'),('İletişim','iletisim/','contact')]
    return ''.join(f'<a href="{prefix+path if path else (prefix or "./")}"'+(' aria-current="page"' if key==active else '')+f'>{e(label)}</a>' for label,path,key in links)

def shared_header(prefix,active):
    top=''.join([
      '<div class="topbar"><div class="container"><span>📍 Yuvam Akarca · Alikahya · Yahya Kaptan · İzmit</span>',
      '<span class="topbar-second"><b class="live-dot"></b> Ev ve iş yerlerine 7/24 yerinde elektrik servisi</span></div></div>'
    ])
    ribbon=('<div class="preview-ribbon"><div class="container">TASLAK: SEO yayını için alan adını SITE_AYARLARI.json dosyasına ekleyin.</div></div>' if not PUBLISHED else '')
    return f'''{top}{ribbon}<header class="site-header"><div class="container header-inner">{site_logo(prefix)}<nav class="nav-links" data-mobile-menu aria-label="Ana menü">{nav(prefix,active)}</nav><div class="nav-actions"><div class="header-phone">7/24 Elektrik Servisi<strong>{e(VISIBLE_PHONE)}</strong></div>{btn('Hemen Ara',phone_href(prefix),svg='phone')}<button class="menu-toggle" data-menu-toggle aria-label="Menüyü aç/kapat" aria-expanded="false">{icon('menu',23)}</button></div></div></header>'''

# İşletmenin doğrulanmış Google Haritalar profili (CID, kamusal adres değil).
GBP_MAPS_URL = "https://www.google.com/maps?cid=17157529544399427815"

def shared_footer(prefix):
    fphone=phone_href(prefix)
    wa_footer = f'<a href="{e(whatsapp_href(prefix))}" target="_blank" rel="noopener noreferrer">WhatsApp ile mesaj gönder</a>' if WHATSAPP else ''
    wa_mobile = wa_btn('WhatsApp',prefix)
    one_col = ' style="grid-template-columns:1fr"' if not WHATSAPP else ''
    return f'''<footer class="footer"><div class="container"><div class="footer-cols"><div>{site_logo(prefix)}<p>İzmit’te Alikahya ve Yahya Kaptan başta olmak üzere elektrik arıza, bakım, onarım, montaj ve taahhüt hizmetleri.</p><p>Her gün 24 saat elektrik arıza, bakım ve montaj için yerinde servis. Gece ve gündüz arayın; müdahale planını konum ve işin kapsamına göre görüşelim.</p></div><div><h3>Yuvam Elektrik</h3><nav class="footer-links" aria-label="Alt menü"><a href="{prefix}hakkimizda/">Hakkımızda</a><a href="{prefix}hizmetler/">Tüm Hizmetler</a><a href="{prefix}hizmet-bolgeleri/">Hizmet Bölgeleri</a><a href="{prefix}blog/">Faydalı Bilgiler</a><a href="{prefix}sikca-sorulan-sorular/">Sık Sorulan Sorular</a><a href="{prefix}gizlilik/">Gizlilik Bilgilendirmesi</a></nav></div><div><h3>İletişim</h3><div class="footer-links"><span>Bayram Canseven</span><a href="{e(fphone)}">{e(VISIBLE_PHONE)}</a><a href="{GBP_MAPS_URL}" target="_blank" rel="noopener noreferrer">Google Haritalar’da işletme profilimiz</a><span>{e(CONFIG.get('konum','Alikahya Fatih Mah. Yuvam Akarca Toplu Konutları, İzmit / Kocaeli'))}</span><span>{e(CONFIG.get('calisma_saatleri',''))}</span>{wa_footer}</div></div></div><div class="footer-bottom"><span>© Yuvam Elektrik • İzmit, Kocaeli</span><span>Elektrik tesisatına yetkisiz müdahale etmeyin.</span></div></div></footer><div class="mobile-action-bar" aria-label="Hızlı iletişim"{one_col}>{btn('0532 711 36 77 • Telefonla Ara',fphone,svg='phone')}{wa_mobile}</div><script src="{prefix}assets/site.js" defer></script>'''

def schema_org(kind='local',service=None):
    # Hizmet bölgesi işletmesi: müşterilere açık olmayan eski dükkânın sokak adresini yayımlamayız.
    base={"@context":"https://schema.org","@type":"Electrician","name":BRAND,"description":"İzmit, Alikahya ve Yuvam Akarca çevresinde ev ve iş yerlerine yerinde elektrik arıza, tesisat ve montaj servisi. İzmit genelinde haftanın 7 günü 24 saat yerinde elektrik arıza, bakım ve montaj hizmeti.","areaServed":[{"@type":"Place","name":n+", İzmit, Kocaeli"} for n,_ in REGIONS[:7]],"address":{"@type":"PostalAddress","addressLocality":"İzmit","addressRegion":"Kocaeli","addressCountry":"TR"}}
    # Kullanıcı tarafından doğrulanan yeni çalışma düzeni: haftanın her günü 24 saat.
    base["openingHoursSpecification"]=[
        {"@type":"OpeningHoursSpecification",
         "dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
         "opens":"00:00","closes":"23:59"}
    ]
    if DOMAIN: base['url']=DOMAIN+'/'
    base['sameAs']=[GBP_MAPS_URL]
    base['hasMap']=GBP_MAPS_URL
    if PHONE: base['telephone']=PHONE
    if kind=='service' and service:
        return {"@context":"https://schema.org","@type":"Service","name":service['name'],"description":service['lead'],"provider":{k:v for k,v in base.items() if k!='@context'},"areaServed":{"@type":"Place","name":"İzmit, Kocaeli, Türkiye"}}
    return base

def seo_breadcrumbs(relpath, page_title, canonical):
    """BreadcrumbList uses actual site navigation instead of URL-only labels."""
    if not (DOMAIN and canonical and relpath):
        return None
    steps=[('Ana Sayfa', DOMAIN+'/')]
    if relpath.startswith('hizmetler/') and relpath != 'hizmetler/':
        steps.append(('Hizmetler', DOMAIN+'/hizmetler/'))
    elif relpath.startswith('blog/') and relpath != 'blog/':
        steps.append(('Blog', DOMAIN+'/blog/'))
    steps.append((page_title.split(' | ', 1)[0], canonical))
    return {
        '@context': 'https://schema.org',
        '@type': 'BreadcrumbList',
        'itemListElement': [
            {'@type':'ListItem','position':i,'name':name,'item':url}
            for i,(name,url) in enumerate(steps,start=1)
        ],
    }

def make_page(path,title,description,body,active=None,schema=None):
    file=SITE/path
    file.parent.mkdir(parents=True,exist_ok=True)
    depth=len(Path(path).parts)-1
    prefix='../'*depth
    relpath=str(path).replace('index.html','').replace('\\','/')
    canonical=f'{DOMAIN}/{relpath}' if DOMAIN else None
    crumb=seo_breadcrumbs(relpath,title,canonical)
    crumb_json=json.dumps(crumb,ensure_ascii=False).replace('</', '<\\/') if crumb else ''
    head='\n'.join([
       '<!doctype html><html lang="tr"><head><meta charset="utf-8">',
       '<meta name="viewport" content="width=device-width, initial-scale=1">',
       f'<title>{e(title)}</title>',
       f'<meta name="description" content="{e(description[:159])}">',
       '<meta name="theme-color" content="#061A3D">',
       '<meta name="robots" content="index,follow">' if PUBLISHED else '<meta name="robots" content="noindex,nofollow">',
       f'<link rel="canonical" href="{e(canonical)}">' if canonical else '',
       f'<meta property="og:title" content="{e(title)}">',
       f'<meta property="og:description" content="{e(description[:159])}">',
       '<meta property="og:type" content="website">',
       '<meta property="og:site_name" content="Kocaeli Yuvam Elektrik">',
       '<meta property="og:locale" content="tr_TR">',
       f'<meta property="og:image" content="{e(DOMAIN)}/assets/yuvam-elektrik-sosyal-kart.png">' if DOMAIN else '',
       f'<link rel="icon" type="image/svg+xml" href="{prefix}assets/favicon.svg">',
       f'<meta property="og:url" content="{e(canonical)}">' if canonical else '',
       f'<link rel="stylesheet" href="{prefix}assets/site.css">',
       f'<script type="application/ld+json">{json.dumps(schema,ensure_ascii=False).replace("</", "<\\/")}</script>' if schema else '',
       f'<script type="application/ld+json">{crumb_json}</script>' if crumb_json else '',
       '</head><body>'
    ])
    output=head+shared_header(prefix,active)+body.replace('___ROOT___',prefix)+shared_footer(prefix)+'</body></html>'
    file.write_text(output,encoding='utf-8')
    return str(path)

def page_heading(eyebrow,title,subtitle):
    return f'<section class="page-heading"><div class="container"><span class="eyebrow"><span class="dot"></span>{e(eyebrow)}</span><h1>{e(title)}</h1><p>{e(subtitle)}</p></div></section>'

def section_head(tag,title,desc=None):
    return '<div class="section-head"><div>'+f'<span class="eyebrow"><span class="dot"></span>{e(tag)}</span><h2>{e(title)}</h2>'+(f'<p>{e(desc)}</p>' if desc else '')+'</div></div>'

def cards(services):
    s='<div class="service-grid">'
    for svc in services:
        s+=f'''<article class="service-card" data-service-search="{e(svc['name']+' '+svc['short']+' '+svc['category'])}"><div class="service-card-top"><span class="icon-bubble">{icon(svc['icon'])}</span><span class="category-pill">{e(svc['category'])}</span></div><h3>{e(svc['name'])}</h3><p>{e(svc['short'])}</p><a class="text-link" href="___ROOT___hizmetler/{e(svc['slug'])}/">Hizmeti incele {icon('arrow',16)}</a></article>'''
    return s+'</div>'

def faq_html(faqs):
    return '<div class="faq-list">'+''.join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q,a in faqs)+'</div>'

def contact_banner(prefix_marker='___ROOT___'):
    return f'''<div class="contact-band"><div><span class="eyebrow eyebrow-inverse">YUVAM ELEKTRİK • İZMİT</span><h2>Elektrikle ilgili bir sorununuz mu var?</h2><p>Ne tür bir iş olduğunu ve bulunduğunuz mahalleyi telefonda anlatın. Uygun hizmet ve ziyaret planını birlikte netleştirelim.</p></div>{btn('Hemen Telefonla Ara',phone_href(prefix_marker),svg='phone',extra='btn-lg')}</div>'''

def homepage():
    issue_map=[('bolt','Elektrik arızası var','elektrik-ariza-tespiti-ve-tamiri'),('shield','Sigorta sürekli atıyor','sigorta-ve-kacak-akim-rolesi'),('bulb','Avize/aydınlatma takılacak','avize-armatur-ve-aplik-montaji'),('video','Görüntülü diafon çalışmıyor','goruntulu-diafon-ve-interkom')]
    issues=''.join(f'<a class="issue" href="___ROOT___hizmetler/{slug}/"><span class="icon-bubble">{icon(ic)}</span><strong>{e(label)}</strong><small>Çözümü incele →</small></a>' for ic,label,slug in issue_map)
    steps=[('01','Sorununuzu anlatın','Arıza, montaj veya tesisat ihtiyacınızı telefonla kısaca paylaşın.'),('02','Konumu netleştirelim','Mahallenize ve işin türüne göre ziyaret uygunluğunu görüşelim.'),('03','Uygun çözümü planlayalım','İşin kapsamı, malzeme ve ücret bilgisi değerlendirmeyle netleşsin.')]
    step_h=''.join(f'<div class="step"><div class="step-number">{n}</div><h3>{e(t)}</h3><p>{e(b)}</p></div>' for n,t,b in steps)
    reg=''.join(f'<span class="region-chip">{e(n)}</span>' for n,_ in REGIONS)
    bcards=''.join(f'<a class="blog-card" href="___ROOT___blog/{b["slug"]}/"><span class="eyebrow"><span class="dot"></span>FAYDALI BİLGİ</span><h3>{e(b["title"])}</h3><p>{e(b["intro"])}</p><span class="text-link">Yazıyı oku {icon("arrow",16)}</span></a>' for b in BLOGS[:2])
    hero=f'''<section class="hero"><div class="container hero-grid"><div class="hero-copy"><div class="eyebrow"><span class="dot"></span>{e(HC['hero_eyebrow'])}</div><h1>{e(HC['hero_title'])}</h1><p class="lead">{e(HC['hero_text'])}</p><div class="hero-actions">{btn('0532 711 36 77 · Hemen Ara',phone_href('___ROOT___'),'btn-primary btn-lg',svg='phone')}{btn('Hizmetleri İncele','___ROOT___hizmetler/','btn-outline btn-lg',svg='arrow')}</div><div class="micro-info"><span><b class="small-check">✓</b> İzmit’te yerinde servis</span><span><b class="small-check">✓</b> Ev ve iş yeri</span><span><b class="small-check">✓</b> 7/24 yerinde servis</span></div></div><div class="hero-visual"><div class="circuit"></div><div class="hero-visual-content"><div class="hero-visual-header"><span class="hero-visual-label">KOCAELİ • İZMİT</span><span class="hero-alert"><b class="live-dot"></b> 7/24 SERVİS</span></div><div class="hero-logo-card"><img src="___ROOT___assets/yuvam-elektrik-logo.svg?v=20261115-r2" alt="Kocaeli Yuvam Elektrik logosu" width="400" height="277" fetchpriority="high"></div><div class="hero-visual-contact"><div><small>DOĞRUDAN ELEKTRİK USTASINA ULAŞIN</small><strong>0532 711 36 77</strong></div><a href="{phone_href('___ROOT___')}" aria-label="Yuvam Elektrik'i telefonla ara">{icon('phone',21)}</a></div></div></div></div></section>''' 
    return hero+f'''<section class="section section-white"><div class="container simple-page prose"><h2>İzmit’te 7/24 elektrikçi ve yerinde arıza servisi</h2><p>Kocaeli Yuvam Elektrik olarak yıllardır İzmit’te elektrik arıza, tesisat, sigorta, priz ve aydınlatma işleriyle ilgileniyoruz. Yuvam Akarca, Alikahya ve Yahya Kaptan başta olmak üzere evinize, apartmanınıza veya iş yerinize geliyoruz; fiziksel dükkânda müşteri kabul etmiyoruz.</p><p><strong>Çalışma saatlerimiz:</strong> Pazartesi–Pazar, günün 24 saati. <strong>Yerinde servis:</strong> Elektrik arıza, bakım ve montaj için 7/24 bize ulaşabilirsiniz; müdahale planını işin türüne ve bulunduğunuz adrese göre görüşüyoruz.</p><p>Evde elektrik kesintisi, sürekli atan sigorta, ısınan priz veya çalışmayan aydınlatma gibi sorunlarda doğru kontrol için <a href="___ROOT___hizmetler/elektrik-ariza-tespiti-ve-tamiri/">İzmit elektrik arıza tespiti ve tamiri</a> hizmetimizi inceleyin. <a href="___ROOT___hizmetler/sigorta-ve-kacak-akim-rolesi/">Sigorta ve kaçak akım rölesi kontrolü</a> hakkında da bilgi alabilirsiniz.</p><p>Komşularınızda elektrik varken yalnızca sizin dairenizde kesinti yaşanıyorsa <a href="___ROOT___blog/komsularda-elektrik-var-evde-yok/">komşularda elektrik varken evde kesinti rehberimizi</a> okuyun. Kablo veya elektrik panosuna müdahale etmeyin; acil bir tehlikede güvenli yere çıkıp 112’yi arayın.</p><p><strong>Ustanızla doğrudan görüşün:</strong> Bayram Canseven’e <a href="{e(phone_href('___ROOT___'))}">0532 711 36 77</a> numarasından ulaşabilirsiniz. Daha önce hizmet almış müşterilerin değerlendirmelerini <a href="{GBP_MAPS_URL}" target="_blank" rel="noopener noreferrer">Google Haritalar’daki işletme profilimizden</a> inceleyebilirsiniz.</p></div></section><section class="section section-white"><div class="container">{section_head('Hızlı çözüm','Hangi konuda elektrikçi arıyorsunuz?','En sık karşılaşılan taleplerden birini seçin ya da bizi doğrudan arayın.')}<div class="issue-grid">{issues}</div></div></section><section class="section"><div class="container">{section_head('Hizmetlerimiz','İzmit’te elektrik işleriniz için tek iletişim noktası.','Arızadan montaja, tesisattan haberleşme sistemlerine kadar sunduğumuz hizmetler.')}{cards(SERVICES[:8])}<div style="margin-top:24px">{btn('Tüm Hizmetleri Gör','___ROOT___hizmetler/','btn-outline',svg='arrow')}</div></div></section><section class="section section-white"><div class="container">{section_head('Nasıl ilerliyoruz?','Telefon edin, ihtiyacınızı birlikte netleştirelim.') }<div class="step-grid">{step_h}</div></div></section><section class="section section-soft"><div class="container about-grid"><div><span class="eyebrow"><span class="dot"></span>YUVAM ELEKTRİK HAKKINDA</span><h2>{e(HC['about_title'])}</h2><p class="lead">{e(HC['about_text'])}</p><div class="check-grid"><div class="check-item"><b>✓</b> Yerel hizmet odağı</div><div class="check-item"><b>✓</b> Farklı elektrik işlerinde destek</div><div class="check-item"><b>✓</b> İşin kapsamını önceden görüşme</div><div class="check-item"><b>✓</b> Telefonla doğrudan iletişim</div></div><a href="___ROOT___hakkimizda/" class="text-link">Hakkımızda daha fazla bilgi {icon('arrow',16)}</a></div><div class="about-panel"><span>YUVAM AKARCA / ALİKAHYA</span><h3>Uzağı aramayın. Önce mahallenizdeki elektrik ustasına sorun.</h3><p>İzmit’te evinize, apartmanınıza veya iş yerinize uygun hizmeti telefonla görüşelim.</p></div></div></section><section class="section"><div class="container">{section_head('Ticari ve kurumsal işler','İş yerinizin elektrik altyapısı için de yanınızdayız.','Fabrika, şantiye, restoran ve diğer ticari işletmelerde pano, bakım, kompanzasyon ve kamera sistemi taleplerinizi değerlendiriyoruz.')}{cards(SERVICES[16:])}</div></section><section class="section section-white"><div class="container">{section_head('Hizmet bölgeleri','Yuvam Akarca ve Alikahya çevresinde yanınızdayız.','Alikahya ve Yahya Kaptan başta olmak üzere İzmit genelinde elektrik arıza, bakım ve montaj hizmetleri sunuyoruz.')}<div class="region-grid">{reg}</div><p class="region-note">İzmit genelinde hizmet veriyoruz. Kocaeli’nin diğer ilçelerindeki işler için konum, kapsam ve servis uygunluğunu telefonda görüşebilirsiniz.</p><a class="text-link" href="___ROOT___hizmet-bolgeleri/">Hizmet alanını incele {icon('arrow',16)}</a></div></section><section class="section section-soft"><div class="container">{section_head('Fiyatlandırma','Elektrik işlerinde fiyat nasıl belirleniyor?')}<p style="max-width:870px;color:#526779">{e(HC['price_text'])}</p>{btn('İşiniz İçin Ön Bilgi Alın',phone_href('___ROOT___'),'btn-primary',svg='phone')}</div></section><section class="section section-white"><div class="container">{section_head('Sık sorulan sorular','Aramadan önce merak edilenler')}{faq_html(FAQS[:6])}<div style="margin-top:20px"><a class="text-link" href="___ROOT___sikca-sorulan-sorular/">Tüm soruları görüntüle {icon('arrow',16)}</a></div></div></section><section class="section"><div class="container">{section_head('Bilgi köşesi','Elektrik hakkında faydalı bilgiler') }<div class="blog-grid">{bcards}</div></div></section><section class="section section-white"><div class="container">{contact_banner()}</div></section>'''

def service_page(s):
    # Anlamlı konu bağlantıları: kullanıcıyı aynı kategorideki diğer işlere götürür.
    related=[v for v in SERVICES if v['slug']!=s['slug'] and v['category']==s['category']][:3]
    if len(related)<3:
        related += [v for v in SERVICES if v['slug']!=s['slug'] and v not in related][:3-len(related)]
    related_html='<h2>İlgili elektrik hizmetleri</h2><ul>'+''.join(
        f'<li><a href="___ROOT___hizmetler/{e(v["slug"])}/">{e(v["name"])}</a></li>'
        for v in related
    )+'</ul>' if related else ''
    signals=''.join(f'<li>{e(x)}</li>' for x in s['signals'])
    tasks=''.join(f'<li>{e(x)}</li>' for x in s['tasks'])
    calltxt='Merhaba, '+s['name']+' için İzmit’te hizmet almak istiyorum.'
    aside=f'''<aside class="aside-box"><span class="eyebrow"><span class="dot"></span>DOĞRUDAN İLETİŞİM</span><h3>{e(s['name'])} için arayın</h3><p>İşin yapılacağı mahalleyi ve ihtiyacınızı anlatın. Servis uygunluğunu birlikte görüşelim.</p><div class="aside-phone">{e(VISIBLE_PHONE)}</div>{btn('Telefonla Ara',phone_href('___ROOT___'),svg='phone')}{wa_btn('WhatsApp Mesajı','___ROOT___',calltxt)}<div class="aside-mini">İzmit genelinde hizmet • Kocaeli’nin diğer ilçelerinde servis uygunluğu telefonla teyit edilir.</div></aside>'''
    ariza_extra = ''
    heading = s['name']
    if s['slug'] == 'elektrik-ariza-tespiti-ve-tamiri':
        heading = 'İzmit’te Elektrik Arıza Tespiti ve Tamiri'
        ariza_extra = ('<h2>İzmit’te elektrik arızası için yerinde servis nasıl işler?</h2>'
                       '<p>İzmit, Yuvam Akarca, Alikahya ve Yahya Kaptan çevresinde ev, apartman ve iş yerlerindeki elektrik sorunlarını telefonla dinliyoruz. Hangi bölümde elektrik olmadığı, sigortanın ne zaman attığı veya priz ve aydınlatma sorunlarının nasıl başladığı gibi bilgilerle servis planını netleştiriyoruz. Arızanın nedeni ve yapılacak işin kapsamı yerinde kontrol sonrası belirlenir.</p>'
                       '<h2>Binada elektrik varken dairemde elektrik yoksa ne yapmalıyım?</h2>'
                       '<p>Diğer dairelerde elektrik varken yalnızca sizin evinizde kesinti olması, daire içi koruma elemanlarından gelen besleme hattına kadar farklı nedenlerle ilişkili olabilir. Sigorta yeniden atıyorsa tekrar tekrar açmayı denemeyin; pano veya kabloları sökmeyin. Olası nedenler için <a href="___ROOT___blog/komsularda-elektrik-var-evde-yok/">komşularda elektrik varken evde kesinti rehberimizi</a> inceleyebilirsiniz.</p>'
                       '<h2>İzmit’te acil elektrikçi çağırmadan önce hangi bilgileri vermeliyim?</h2>'
                       '<p>Yuvam Akarca, Alikahya, Yahya Kaptan ve İzmit genelinde arıza bildiriminde bulunduğunuzda mahalleyi, binanın türünü, elektrik kesintisinin sadece sizin dairenizde mi yoksa ortak alanlarda da mı yaşandığını ve sigortanın atıp atmadığını söylemeniz ilk değerlendirmeyi kolaylaştırır. Yanık kokusu, kıvılcım ya da duman varsa bunu özellikle belirtin; tehlikeli tesisata yaklaşmayın.</p>'
                       '<h2>Gece acil elektrik arızasında ulaşabilir miyim?</h2>'
                       '<p>Evet. İzmit’te 7/24 acil elektrikçi ihtiyacı, elektrik arıza, bakım ve montaj talepleri için haftanın her günü hizmet sunuyoruz. Gece veya gündüz 0532 711 36 77 numarasından arayabilirsiniz; müdahale zamanını konuma ve işin kapsamına göre telefonda netleştiriyoruz. Belirli bir varış süresi veya her arızanın anında çözüleceği garantisi verilmez.</p>'
                       '<h2>Elektrik arıza tespiti ve onarım ücreti nasıl belirlenir?</h2>'
                       '<p>Ön görüşmede arıza belirtisi ve adres bilgisi değerlendirilir. Gerekli yerinde kontrollerden sonra olası kablo, sigorta, bağlantı ve malzeme değişimi kapsamına göre ücret netleştirilir. Fiyatı etkileyen koşullar açıklanmadan sabit bir tamir bedeli vaat etmiyoruz. Sigorta sürekli atıyorsa <a href="___ROOT___hizmetler/sigorta-ve-kacak-akim-rolesi/">sigorta ve kaçak akım rölesi kontrolü</a> hizmetimizi de inceleyebilirsiniz.</p>')
    return page_heading('İZMİT • YUVAM ELEKTRİK',heading,s['lead'])+f'''<section class="section section-white"><div class="container service-layout"><article class="prose"><p class="lead">{e(s['body'])}</p>{ariza_extra}<h2>Hangi durumlarda arayabilirsiniz?</h2><ul class="detail-list">{signals}</ul><h2>Bu hizmet kapsamında neler yapıyoruz?</h2><ul>{tasks}</ul><h2>Yuvam Elektrik ile süreç nasıl ilerliyor?</h2><p>İlk görüşmede bulunduğunuz mahalleyi, yaşadığınız sorunu ve varsa kullanılan ürünün modelini soruyoruz. Yapılacak işin kapsamına göre servis uygunluğunu görüşüyor, gerekli kontrol ve montaj işlemleri için plan oluşturuyoruz. Kullanılacak malzeme veya ek işlem ihtiyacı ortaya çıkarsa uygulama öncesinde bilgi vermeyi hedefliyoruz.</p><div class="info-note"><strong>Güvenlik notu:</strong> {e(s['note'])}</div><h2>İzmit’te {e(s['name'].lower())} için iletişim</h2><p>Yuvam Akarca ve Alikahya Fatih’te bulunan Yuvam Elektrik, Alikahya ve Yahya Kaptan başta olmak üzere İzmit genelinde hizmet verir. Kocaeli’nin diğer ilçelerindeki planlı işler için uygunluğu telefonda görüşebilirsiniz.</p>{related_html}<p><a class="text-link" href="___ROOT___hizmetler/">← Diğer elektrik hizmetlerini görün</a></p></article>{aside}</div></section>'''

def other_page():
    about=page_heading('HAKKIMIZDA','Kocaeli Yuvam Elektrik: Elektrik işlerinizde çözüm ortağınız.','Alikahya ve Yahya Kaptan başta olmak üzere İzmit’in tamamında arıza, bakım, montaj ve taahhüt hizmetleri.')+f'''<section class="section section-white"><div class="container simple-page prose"><h2>Yuvam Elektrik hakkında</h2><p>{e(HC['about_text'])}</p><p>Elektrik arızaları, deneyim ve titiz çalışma gerektirir. Yuvam Elektrik olarak iş güvenliğini ve doğru uygulamayı önemser; sorunu dinleyip uygun çözümün kapsamını anlaşılır biçimde aktarmaya çalışırız. Anahtar-priz değişiminden bina içi tesisat yenilemeye, avize ve LED aydınlatmadan sigorta ve pano işlerine kadar farklı ihtiyaçlara cevap veririz.</p><h2>Konut, apartman ve ticari işletmelere hizmet</h2><p>Ev ve apartmanlardaki günlük arızaların yanında fabrika, iş yeri, şantiye, restoran ve eğlence mekânları gibi ticari alanlarda elektrik altyapısı, dağıtım ve kompanzasyon panosu, enerji besleme hatları, kamera güvenlik sistemleri, kontrol, bakım ve onarım taleplerini değerlendiririz. İşin kapsamına ve gerekli teknik yetkilere göre uygulama planı oluştururuz.</p><h2>Hizmet anlayışımız</h2><p>Hedefimiz, müşteri memnuniyetini ön planda tutarak ihtiyaçlara uygun, güvenli ve sürdürülebilir çözümler üretmek. Teknolojideki gelişmeleri ve güncel uygulamaları takip ederek, malzeme seçimini işin teknik gerekliliklerine uygun yapmaya özen gösteriyoruz.</p><h2>Nerelere hizmet veriyoruz?</h2><p><strong>İzmit, Alikahya, Yuvam Akarca ve Yahya Kaptan</strong> çevresindeki ev, apartman ve iş yerlerine yerinde elektrik servisi sunuyoruz. Fiziksel dükkânda müşteri kabul etmiyoruz. İzmit dışındaki Kocaeli taleplerini de işin kapsamı, konum ve planlamaya göre değerlendirebiliyoruz.</p><h2>Doğrudan iletişim</h2><p><strong>Bayram Canseven — Yuvam Elektrik</strong><br>Telefon: <a href="{e(phone_href('___ROOT___'))}">{e(VISIBLE_PHONE)}</a></p></div></section><section class="section"><div class="container">{contact_banner()}</div></section>'''
    regions=page_heading('HİZMET BÖLGELERİ','İzmit’in tamamında elektrik hizmeti','Alikahya, Yuvam Akarca ve Yahya Kaptan çevresindeki ev ve iş yerlerine adresinde servis sunuyoruz.')+f'''<section class="section section-white"><div class="container">{section_head('İzmit genelinde hizmet','Öncelikli bölgelerimiz ve servis kapsamımız')}<div class="area-list">{''.join(f'<article class="area-card"><h3>{e(a)}</h3><p>{e(b)}</p></article>' for a,b in REGIONS)}</div><div class="callout" style="margin-top:30px"><h3>İzmit dışındaki bir konumda mısınız?</h3><p>Kocaeli’nin diğer ilçelerindeki işler için de arayabilirsiniz. İşin niteliği, mesafe ve müsaitliğe göre ziyaret planı telefonda belirlenir.</p>{btn('Servis Uygunluğunu Sorun',phone_href('___ROOT___'),svg='phone')}</div></div></section>'''
    optional_wa = (f'''<div class="contact-tile"><span class="icon-bubble">{icon('message',26)}</span><h3>WhatsApp üzerinden yazın</h3><p>Arıza veya montaj işinize ilişkin kısa bilgi ve güvenli bir noktadan çekilmiş fotoğraf gönderebilirsiniz.</p>{wa_btn('WhatsApp Mesajı Gönder','___ROOT___')}</div>''' if WHATSAPP else f'''<div class="contact-tile"><span class="icon-bubble">{icon('map',26)}</span><h3>Konum ve servis bölgemiz</h3><p>İzmit, Alikahya, Yuvam Akarca ve Yahya Kaptan çevresinde yerinde elektrik servisi.</p><p>Alikahya, Yahya Kaptan ve İzmit geneli için arayın. Kocaeli diğer ilçelerindeki planlı işler için uygunluğu telefonda görüşelim.</p>{btn('Servis Hakkında Ara',phone_href('___ROOT___'),svg='phone')}</div>''')
    contact=page_heading('İLETİŞİM','Yuvam Elektrik’e hemen ulaşın.','7/24 elektrik arıza talebi, bakım, montaj ve keşif görüşmeleri için Bayram Canseven’i doğrudan arayın.')+f'''<section class="section section-white"><div class="container"><h2>7/24 elektrik servisi için iletişim</h2><div class="contact-grid"><div class="contact-tile"><span class="icon-bubble">{icon('phone',26)}</span><h3>Telefonla iletişim</h3><p><strong>Bayram Canseven — Yuvam Elektrik</strong></p><p>Elektrik arızası, bakım, montaj veya taahhüt işinizi kısaca anlatın. Mahallenizi belirterek servis uygunluğunu öğrenebilirsiniz.</p><h2>{e(VISIBLE_PHONE)}</h2>{btn('Telefonla Hemen Ara',phone_href('___ROOT___'),'btn-primary btn-lg',svg='phone')}</div>{optional_wa}</div><div class="callout" style="margin-top:24px"><h3>Hizmet bölgemiz ve çalışma düzeni</h3><p>{e(CONFIG.get('konum','Alikahya Fatih Mah. Yuvam Akarca Toplu Konutları, İzmit / Kocaeli'))}</p><p>Ev ve iş yerlerine adresinde hizmet veriyoruz; fiziksel dükkânda müşteri kabul etmiyoruz.</p><p><strong>İletişim ve çalışma saatleri:</strong> {e(CONFIG.get('calisma_saatleri','7/24 telefonla talep alınır.'))}</p><p style="margin-bottom:0"><strong>Aramadan önce:</strong> Mahalle ve sokak, arızanın türü, varsa marka-model ve uygun olduğunuz zamanı belirtmeniz yeterlidir.</p></div></div></section>'''
    privacy=page_heading('YASAL BİLGİLENDİRME','Gizlilik Bilgilendirmesi','Web sitesi kullanımı ve iletişim sırasında paylaşılan bilgiler hakkında genel açıklamalar.')+f'''<section class="section section-white"><div class="container simple-page prose legal"><h2>1. Site ve iletişim</h2><p>Bu internet sitesi Yuvam Elektrik hizmetlerini tanıtmak ve ziyaretçilerin telefon veya WhatsApp üzerinden işletmeye ulaşmasını kolaylaştırmak amacıyla hazırlanmıştır.</p><h2>2. İletişim verileri</h2><p>Ziyaretçinin telefon görüşmesi veya WhatsApp üzerinden kendi isteğiyle paylaştığı ad, telefon numarası, adres, fotoğraf ve hizmet talebi bilgileri, talebin değerlendirilmesi ve iletişimin sürdürülmesi için işlenebilir. WhatsApp hizmetine geçişte ilgili sağlayıcının gizlilik kuralları geçerlidir.</p><h2>3. Teknik kayıtlar, çerezler ve analiz</h2><p>Bu web sitesi, yalnızca ziyaretçinin onayı sonrasında Google Analytics 4 (ölçüm kimliği G-7XXDVG2JWK) teknolojisini yükler. Onay verildiğinde ziyaret edilen sayfalar, site etkileşimleri ve telefonla arama bağlantısına tıklamalar gibi olaylar ölçülür; telefon görüşmesinin içeriği veya görüşmenin gerçekleşip gerçekleşmediği ölçülmez. Analitik çerezleri reddedebilirsiniz. Tercihiniz tarayıcınızın yerel depolamasında saklanır; sayfanın altındaki Çerez tercihlerini değiştir düğmesinden kararınızı değiştirebilirsiniz. Onayınızı geri çektiğinizde bu tarayıcıdaki analitik veri gönderimi durdurulur. Analitik veriler Google hizmetlerine aktarılabilir ve yurt dışında işlenebilir. Barındırma sağlayıcısı teknik erişim kayıtları tutabilir. Google hizmetinin veri işleme ayrıntıları için Google gizlilik politikasını inceleyebilirsiniz.</p><h2>4. İlgili kişi başvuruları</h2><p>Veri işleme süreçleri hakkında sorularınız için sitede gösterilen işletme telefon numarasından iletişime geçebilirsiniz. KVKK kapsamındaki veri sorumlusu kimliği, başvuru kanalı, işleme hukuki sebepleri ve saklama süreleri yayın öncesinde işletmenin fiilî süreçlerine göre ayrıca tamamlanmalıdır.</p></div></section>'''
    return about,regions,contact,privacy

def write_editorial_document():
    md=['# YUVAM ELEKTRİK — WEB SİTESİ TÜM İÇERİKLERİ', '', 'Özgün Türkçe içerik paketi | İzmit / Yuvam Akarca / Alikahya', '', '## 1. Konumlandırma ve pazarlama hedefi', '',
       '**Ana marka mesajı:** Elektrik İşlerinde Güvenilir Çözüm Ortağınız.',
       '**Temel hedef:** İzmit çevresinde elektrikçi arayan ziyaretçilerin telefonla arayarak hizmet talebi oluşturması.',
       '**Birincil eylem:** 0532 711 36 77 numarasını ara. **İkincil eylem:** Hizmetleri incele. WhatsApp hattı teyit edilmeden WhatsApp eylemi gösterilmez.',
       '**İşletme odağı:** Alikahya Fatih / Yuvam Akarca; Alikahya ve Yahya Kaptan başta olmak üzere İzmit geneli.',
       '**Kapsam dışı:** Ofis tadilatı ve ofis dekorasyonu; telefon santrali kurulumu; korniş montajı.',
       '', '## 2. Ana sayfa tam metinleri', '',
       f'**SEO Başlık:** İzmit Elektrikçi | 7/24 Arıza ve Montaj – Yuvam Elektrik',
       '**SEO Açıklaması:** İzmit’te 7/24 elektrik arıza, priz, avize, sigorta, pano ve tesisat işleri. Alikahya, Yahya Kaptan ve İzmit geneli. 0532 711 36 77.',
       '', f'# {HC["hero_title"]}', '', HC['hero_text'], '',
       '**Birincil buton:** Telefonla Hemen Ara', '**İkincil buton:** Hizmetleri İncele', '',
       '### Hangi konuda elektrikçi arıyorsunuz?',
       'Elektrik arızası var • Sigorta sürekli atıyor • Avize/aydınlatma takılacak • Görüntülü diafon çalışmıyor', '',
       '### Hizmetlerimiz',
       'Arızadan montaja, tesisattan haberleşme sistemlerine kadar sunduğumuz hizmetler.', '',
       '### Nasıl ilerliyoruz?',
       '1. Sorununuzu anlatın: Arıza, montaj veya tesisat ihtiyacınızı telefonla kısaca paylaşın.',
       '2. Konumu netleştirelim: Mahallenize ve işin türüne göre ziyaret uygunluğunu görüşelim.',
       '3. Uygun çözümü planlayalım: İşin kapsamı, malzeme ve ücret bilgisi değerlendirmeyle netleşsin.', '',
       '### Hakkımızda', HC['about_title'], '', HC['about_text'], '',
       '### Elektrik işlerinde fiyat nasıl belirleniyor?', HC['price_text'], '',
       '### Alt çağrı', 'Elektrikle ilgili bir sorununuz mu var? Ne tür bir iş olduğunu ve bulunduğunuz mahalleyi telefonda anlatın. Uygun hizmet ve ziyaret planını birlikte netleştirelim.', '',
       '## 3. Hizmet sayfaları — özgün ve yayınlanabilir metinler', '']
    for i,s in enumerate(SERVICES,1):
        md.extend([f'### 3.{i} {s["name"]}', '',f'**URL:** /hizmetler/{s["slug"]}/',
           f'**SEO Başlık:** {s["name"]} | İzmit – Yuvam Elektrik',
           f'**SEO Açıklaması:** {s["lead"][:145]}',
           '',f'**H1:** {s["name"]}', '', s['lead'], '',s['body'],'',
           '**Ne zaman aramalısınız?**', '']+[f'- {a}' for a in s['signals']]+['','**Yapılan işler:**','']+[f'- {a}' for a in s['tasks']]+['','**Çalışma süreci metni:** İlk görüşmede mahalleyi, yaşanan sorunu ve varsa ürün modelini soruyoruz. İşin kapsamına göre servis uygunluğunu görüşüyor ve işlem planı oluşturuyoruz. Gerekli malzeme veya ek işlem ihtiyacını uygulamadan önce netleştiriyoruz.','',f'**Güvenlik notu:** {s["note"]}','','**CTA:** Bu hizmet için Yuvam Elektrik’i hemen arayın.',''])
    md.extend(['## 4. Hizmet bölgeleri', '', 'Öncelikli mahalleler:']+[f'- **{a}:** {b}' for a,b in REGIONS]+['','Alikahya ve Yahya Kaptan başta olmak üzere İzmit geneline servis sunulur. Kocaeli’nin diğer ilçelerindeki talepler için konum, işin niteliği ve müsaitlik telefonda değerlendirilir.','',
      '## 5. Hakkımızda sayfası','','Yuvam Elektrik, Kocaeli İzmit’te Alikahya Fatih Mahallesi, Yuvam Akarca Toplu Konutları bölgesinde faaliyet gösterir. Alikahya ve Yahya Kaptan başta olmak üzere İzmit geneline elektrik arıza, bakım, montaj, tesisat ve taahhüt hizmetleri sunar.','','Konut, apartman ve iş yerlerinin yanında fabrika, şantiye, restoran ve diğer ticari alanlarda elektrik panosu, kompanzasyon, makine enerji besleme hatları, elektrik kontrol ve bakım işleri ile kamera güvenlik sistemlerinin uygun kapsamlı uygulamalarını değerlendiriyoruz.','','Elektrik işlerinde önce güvenliğe, uygun malzeme seçimine ve ihtiyaca göre doğru çözüme odaklanırız. İşin kapsamı ve gereken teknik yetkilere göre müdahale planlarız. Doğrudan iletişim: Bayram Canseven – 0532 711 36 77.','',
      '## 6. Sık sorulan sorular','','Sitede hazır soru-cevaplar:'])
    for q,a in FAQS: md.extend(['',f'**{q}**','',a])
    md.extend(['','## 7. Blog yazıları',''])
    for b in BLOGS:
        md.extend([f'### {b["title"]}','','**URL:** /blog/'+b['slug']+'/','','**Giriş:** '+b['intro'],''])
        for h,p in b['sections']: md.extend([f'**{h}**','',p,''])
        md.extend(['**CTA:** '+b['cta'],''])
    md.extend(['## 8. İletişim sayfası','','**Başlık:** Elektrik işiniz için Yuvam Elektrik’i arayın.','',
     'Alikahya ve Yahya Kaptan başta olmak üzere İzmit genelindeki hizmet talepleriniz için 0532 711 36 77 numarasından Bayram Canseven’e ulaşabilirsiniz.','','**Telefon bölümü:** Elektrik arızası, bakım, montaj veya taahhüt işinizi kısaca anlatın. Mahallenizi söyleyerek uygunluk ve süreç hakkında bilgi alın.','',
     '**WhatsApp bölümü:** Ayrı bir WhatsApp hattı teyit edilmedikçe sayfada bağlantı gösterilmez. Tehlikeli arızaya fotoğraf çekmek için yaklaşmayın.','',
     '**Telefon:** 0532 711 36 77 — Bayram Canseven.', '\n**İşletme konumu:** Alikahya Fatih Mah. Yuvam Akarca Toplu Konutları, İzmit / Kocaeli.', '**Telefonla sorulacak dört bilgi:** mahalle, iş türü, varsa ekipman modeli, istenen tarih.','','## 9. SEO içerik stratejisi','','**Ana arama niyeti:** İzmit elektrikçi, Yuvam Akarca elektrikçi, Alikahya elektrikçi.','',
     '**Hizmet aramaları:** İzmit elektrik arıza, İzmit avize montajı, İzmit priz değişimi, İzmit sigorta arızası, İzmit görüntülü diafon tamiri, İzmit uydu anten kurulumu, İzmit elektrik panosu tadilatı, İzmit kamera montajı.','',
     '**Önerilen site mimarisi:** Ana Sayfa → Hizmetler → 16 temel + 3 kurumsal hizmet sayfası → Hizmet Bölgeleri → Hakkımızda → SSS → Blog → İletişim → Gizlilik.','',
     '**Yerel SEO prensibi:** Ayrı mahalle sayfaları yalnızca gerçekten faydalı ve farklı yerel bilgi varsa eklenmelidir; aynı metnin mahalle adını değiştirerek çoğaltılması önerilmez.','',
     '## 10. Tasarım ve dönüşüm rehberi','','- Mobilde ekranın altında sabit “0532 711 36 77 • Telefonla Ara” düğmesi; WhatsApp yalnızca doğrulanırsa eklenir.','- Masaüstü üst menüde telefon numarası ve belirgin “Hemen Ara” düğmesi.','- Ana ekranda Yuvam Akarca / İzmit konumu ve net hizmet vaadi.','- Ziyaretçi sorununu dört hızlı seçimden bulabilmeli.','- Her hizmet sayfasında ayrı çağrı butonu ve mahalle odaklı bilgi.','- Sahte değerlendirmeler, doğrulanmamış başarı sayıları, uydurma belgeler ve kesin geliş süresi vaatleri kullanılmamalıdır.','- Fotoğraflar mümkünse gerçek ustanın, gerçek uygulamaların ve iş bitimlerinin fotoğrafları olmalıdır.','- Markaya uygun tasarım renkleri: kırmızı #D6010D; elektrik mavisi #004DBB; koyu lacivert #051839; kırık beyaz #F5F8FC. Gerçek vektörel logo tüm sayfalarda kullanılır.','',
     '## 11. Google İşletme Profili metni','','**İşletme açıklaması önerisi:** Yuvam Elektrik, Kocaeli İzmit Alikahya Fatih Mahallesi Yuvam Akarca bölgesinde faaliyet gösterir. Alikahya ve Yahya Kaptan başta olmak üzere İzmit genelinde 7/24 elektrik arıza talepleri, sigorta ve pano arızası, priz ve anahtar montajı, avize, LED ve dış mekân aydınlatması, tesisat yenileme, uydu anten ve diafon sistemleri için hizmet sunar. Konut, apartman ve ticari işletmeler için elektrik bakım, montaj ve taahhüt işleriyle ilgilenir. İletişim: 0532 711 36 77.','','**Google İşletme Profili:** Gerçek işletme adını ve iletişim telefonunu kullanın. Müşteriler adreste karşılanmıyorsa Google’ın hizmet bölgesi işletmesi adres görünürlüğü kurallarını uygulayın.','',
     '## 12. Yayın öncesi tamamlanması gereken bilgiler','','1. Telefon doğrulandı: 0532 711 36 77; WhatsApp kullanımı ayrıca teyit edilmelidir.','2. Domain/alan adı: https://kocaeliyuvamelektrik.com (yayına alınırken DNS/SSL doğrulanmalı).','3. İşletme konumu: Alikahya Fatih Mah. Yuvam Akarca Toplu Konutları, İzmit / Kocaeli. Fiziksel müşteri kabul edilip edilmediği teyit edilmeli.','4. 7/24 arıza talebi beyanı var; fiili müdahale koşulları/ziyaret saatleri işletme tarafından netleştirilmeli.','5. Bayram Canseven iletişim kişisidir; mesleki belge ve teknik yetki bilgileri (varsa) doğrulanıp eklenmeli.','6. Gerçek iş fotoğrafları, tabela/logo, örnek işler ve izinli müşteri yorumları.','7. Veri işleme süreçlerine uygun KVKK/çerez bilgisi.','',
     '## 13. Kapsam dışı hizmetler','','- Ofis tadilatı ve ofis dekorasyonu','- Telefon santrali kurulumu','- Korniş montajı','',
     '## 14. Kaynak ve özgünlük notu','','Örnek site hizmet başlıkları için incelendi: https://www.uygarelektrikci.com/ . Metinler özgün yazılmıştır; örnek sitenin telifli metinleri kopyalanmamıştır. Mahalle kapsamı için İzmit Belediyesi ve yerel kamu kaynakları kontrol edilmiştir. Google’ın mobil uyumluluk ve işletme profili rehberleri temel alınmıştır.'])
    (ROOT/'YUVAM_ELEKTRIK_TUM_WEB_ICERIKLERI.md').write_text('\n'.join(md),encoding='utf-8')

def build():
    if (SITE/'hizmetler').exists(): shutil.rmtree(SITE/'hizmetler')
    paths=[]
    paths.append(make_page(Path('index.html'), 'İzmit Elektrikçi | 7/24 Elektrik Arıza – Yuvam Elektrik', 'İzmit, Alikahya, Yuvam Akarca ve Yahya Kaptan’da ev ve iş yerlerine 7/24 elektrik arıza, bakım, priz, avize ve tesisat servisi. Hemen arayın.',homepage(),'home',schema_org()))
    serv_body=page_heading('HİZMETLERİMİZ','Elektrik arızasından montaja, aradığınız hizmet burada.','İzmit’te ev ve iş yerlerine haftanın 7 günü 24 saat yerinde elektrik arıza, bakım, montaj ve tesisat servisi. Günün her saati arayın; servis planını görüşelim.')+f'''<section class="section section-white"><div class="container"><h2>Elektrik arıza, bakım ve montaj hizmetleri</h2><div class="service-filter"><label class="sr-only" for="serviceFilter">Hizmetlerde ara</label><input id="serviceFilter" type="search" data-service-filter placeholder="Örn. priz, avize, uydu, sigorta..." autocomplete="off"><small>Hizmeti yazarak hızlıca bulun.</small></div>{cards(SERVICES[:16])}<div style="margin:35px 0 20px">{section_head('Kurumsal hizmetler','Ticari işletmeler için elektrik çözümlerimiz')}</div>{cards(SERVICES[16:])}<p class="no-result" data-no-results>Bu aramayla eşleşen hizmet bulunamadı. Yine de ihtiyacınız için bizi arayabilirsiniz.</p></div></section><section class="section"><div class="container">{contact_banner()}</div></section>'''
    paths.append(make_page(Path('hizmetler/index.html'),'Elektrik Hizmetleri | İzmit – Yuvam Elektrik','İzmit’te elektrik arızası, priz ve avize montajı, elektrik panosu, sigorta, diafon, uydu, kamera ve kablolama hizmetlerini inceleyin.',serv_body,'services'))
    for s in SERVICES:
        paths.append(make_page(Path('hizmetler')/s['slug']/'index.html',SEO_TITLE_OVERRIDES.get(s['slug'],s['name']+' | İzmit – Yuvam Elektrik'),SEO_SERVICE_DESCRIPTIONS.get(s['slug'],s['lead']),service_page(s),'services',schema_org('service',s)))
    about,regions,contact,privacy=other_page()
    paths.append(make_page(Path('hakkimizda/index.html'),'Hakkımızda | İzmit Yuvam Elektrik','Yuvam Elektrik İzmit Alikahya’da. Bayram Canseven: 0532 711 36 77. Alikahya ve Yahya Kaptan başta olmak üzere İzmit genelinde elektrik hizmetleri.',about,'about'))
    paths.append(make_page(Path('hizmet-bolgeleri/index.html'),'Hizmet Bölgeleri | Yuvam Akarca ve Alikahya Elektrikçi','Yuvam Elektrik Alikahya ve Yahya Kaptan başta olmak üzere İzmit’in tamamında hizmet sunar; Kocaeli genelinde planlı ticari işler için arayın.',regions,'regions'))
    paths.append(make_page(Path('iletisim/index.html'),'İletişim | Yuvam Elektrik İzmit','Bayram Canseven – Yuvam Elektrik: 0532 711 36 77. İzmit ve çevresinde haftanın her günü 24 saat elektrik arıza, bakım ve montaj servisi.',contact,'contact'))
    paths.append(make_page(Path('gizlilik/index.html'),'Gizlilik Bilgilendirmesi | Yuvam Elektrik','Kocaeli Yuvam Elektrik web sitesinde iletişim taleplerinin işlenmesi, çerezler ve kişisel verilerin korunması hakkında bilgilendirme.',privacy))
    faq=page_heading('SIK SORULAN SORULAR','Elektrik hizmetlerimiz hakkında merak edilenler','Hizmet alanı, arıza, montaj, fiyatlandırma ve ziyaret planlamasına ilişkin kısa yanıtlar.')+f'<section class="section section-white"><div class="container faq-page">{faq_html(FAQS)}</div></section><section class="section"><div class="container">{contact_banner()}</div></section>'
    paths.append(make_page(Path('sikca-sorulan-sorular/index.html'),'Sık Sorulan Sorular | İzmit Yuvam Elektrik','Yuvam Elektrik’in İzmit’te sunduğu elektrik arıza, montaj, fiyat ve hizmet bölgesi konularında sık sorulan sorular.',faq))
    blogs_h=''.join(f'<a class="blog-card" href="___ROOT___blog/{b["slug"]}/"><span class="eyebrow"><span class="dot"></span>FAYDALI BİLGİ</span><h3>{e(b["title"])}</h3><p>{e(b["intro"])}</p><span class="text-link">Yazıyı oku {icon("arrow",16)}</span></a>' for b in BLOGS)
    blog=page_heading('ELEKTRİK REHBERİ','Ev ve iş yerleri için faydalı elektrik bilgileri','Elektrik arızası belirtileri ve doğru hizmet seçimiyle ilgili kısa, anlaşılır rehberler.')+f'<section class="section section-white"><div class="container"><h2>Elektrik arızası ve güvenli kullanım rehberleri</h2><div class="blog-grid">{blogs_h}</div></div></section>'
    paths.append(make_page(Path('blog/index.html'),'Elektrik Rehberi | İzmit Yuvam Elektrik','Sigorta arızası, priz ısınması, avize montajı ve diafon sorunları için Yuvam Elektrik blog yazılarını inceleyin.',blog,'blog'))
    for b in BLOGS:
        parts=''.join(f'<h2>{e(h)}</h2><p>{e(p)}</p>' for h,p in b['sections'])
        related_service=next((v for v in SERVICES if v['slug']==BLOG_RELATED_SERVICE.get(b['slug'])),None)
        related_html=(f'<h2>Bu konuda yerinde hizmet</h2><p>İzmit’te bu konuyla ilgili profesyonel destek için <a href="___ROOT___hizmetler/{e(related_service["slug"])}/">{e(related_service["name"])}</a> sayfamızı inceleyebilirsiniz.</p>' if related_service else '')
        blogbody=page_heading('YUVAM ELEKTRİK • BİLGİ KÖŞESİ',b['title'],b['intro'])+f'<section class="section section-white"><div class="container service-layout"><article class="prose"><p class="lead">{e(b["intro"])}</p>{parts}<div class="info-note">Bu yazı genel bilgilendirme amaçlıdır. Elektrik tesisatına yetkisiz müdahale etmeyin; güvenlik riski varsa ilgili acil yardım kanallarına başvurun.</div>{related_html}<p><a class="text-link" href="___ROOT___blog/">← Diğer faydalı yazılara dön</a></p></article><aside class="aside-box"><h3>{e(b["cta"])}</h3><p>Yuvam Akarca ve İzmit yakın çevresindeki talepler için bize ulaşın.</p>{btn('Telefonla Ara',phone_href('___ROOT___'),svg='phone')}{wa_btn('WhatsApp','___ROOT___')}</aside></div></section>'
        paths.append(make_page(Path('blog')/b['slug']/'index.html',BLOG_SEO_TITLES.get(b['slug'],b['title']+' | Yuvam Elektrik'),b['intro'],blogbody,'blog'))
    if PUBLISHED:
        locs=''.join(f'  <url><loc>{xml_escape(DOMAIN+"/"+p.replace("index.html", ""))}</loc></url>\n' for p in paths)
        (SITE/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+locs+'</urlset>\n',encoding='utf-8')
        (SITE/'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n',encoding='utf-8')
    else:
        (SITE/'robots.txt').write_text('User-agent: *\nDisallow: /\n# Önizleme: telefon ve alan adı eklenince dosyaları yeniden oluşturun.\n',encoding='utf-8')
        if (SITE/'sitemap.xml').exists(): (SITE/'sitemap.xml').unlink()
    write_editorial_document()
    print(f'Olusturuldu: {len(paths)} HTML sayfasi; hizmetler: {len(SERVICES)}; blog: {len(BLOGS)}; yayina hazir: {PUBLISHED}')

if __name__=='__main__': build()
