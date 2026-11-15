document.addEventListener('DOMContentLoaded',function(){
  const toggle=document.querySelector('[data-menu-toggle]');
  const menu=document.querySelector('[data-mobile-menu]');
  if(toggle&&menu){toggle.addEventListener('click',function(){let v=menu.classList.toggle('is-open');toggle.setAttribute('aria-expanded',String(v));});menu.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{menu.classList.remove('is-open');toggle.setAttribute('aria-expanded','false');}));}
  const input=document.querySelector('[data-service-filter]');
  if(input){const cards=[...document.querySelectorAll('[data-service-search]')];const empty=document.querySelector('[data-no-results]');input.addEventListener('input',function(){const q=(input.value||'').toLocaleLowerCase('tr-TR').trim();let visible=0;cards.forEach(c=>{const show=c.dataset.serviceSearch.toLocaleLowerCase('tr-TR').includes(q);c.hidden=!show;if(show)visible++;});if(empty)empty.style.display=visible?'none':'block';});}
});

/* Google Analytics 4 — yalnızca açık analitik çerez izni sonrasında etkinleştirilir. */
(function () {
  'use strict';
  const measurementId = 'G-7XXDVG2JWK';
  const preferenceKey = 'yuvam_analytics_consent_v1';
  let preference = null;
  let analyticsLoaded = false;

  try {
    const saved = localStorage.getItem(preferenceKey);
    if (saved === 'accepted' || saved === 'rejected') preference = saved;
  } catch (error) {
    // Tarayıcı depolaması kullanılamasa da varsayılan durum izinsizdir.
  }

  window.dataLayer = window.dataLayer || [];
  window.gtag = window.gtag || function () { window.dataLayer.push(arguments); };
  window.gtag('consent', 'default', {
    analytics_storage: 'denied',
    ad_storage: 'denied',
    ad_user_data: 'denied',
    ad_personalization: 'denied'
  });

  function isContactPage() {
    return /^\/iletisim(?:\/|\/index\.html)?$/.test(window.location.pathname);
  }

  function enableAnalytics() {
    if (analyticsLoaded || preference !== 'accepted') return;
    analyticsLoaded = true;
    window.gtag('consent', 'update', {
      analytics_storage: 'granted',
      ad_storage: 'denied',
      ad_user_data: 'denied',
      ad_personalization: 'denied'
    });
    window.gtag('js', new Date());
    window.gtag('config', measurementId, {
      allow_google_signals: false,
      allow_ad_personalization_signals: false
    });
    const tag = document.createElement('script');
    tag.async = true;
    tag.src = 'https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(measurementId);
    document.head.appendChild(tag);
    if (isContactPage()) {
      window.gtag('event', 'contact_view', { page_type: 'contact' });
    }
  }

  function eraseAnalyticsCookies() {
    const names = document.cookie.split(';').map(x => x.trim().split('=')[0])
      .filter(name => name === '_ga' || name.startsWith('_ga_') || name === '_gid' || name === '_gat');
    const hostname = window.location.hostname;
    for (const name of names) {
      for (const suffix of ['', '; Domain=' + hostname, '; Domain=.' + hostname]) {
        document.cookie = name + '=; Max-Age=0; Path=/; SameSite=Lax' + suffix;
      }
    }
  }

  function choose(value) {
    const wasLoaded = analyticsLoaded;
    preference = value;
    try { localStorage.setItem(preferenceKey, value); } catch (error) {}
    if (value === 'accepted') {
      enableAnalytics();
    } else {
      eraseAnalyticsCookies();
      if (wasLoaded) {
        window.gtag('consent', 'update', { analytics_storage: 'denied' });
        window.location.reload();
      }
    }
  }

  if (preference === 'accepted') enableAnalytics();

  document.addEventListener('DOMContentLoaded', function () {
    document.addEventListener('click', function (event) {
      const target = event.target;
      const link = target && target.closest ? target.closest('a[href^="tel:"]') : null;
      if (link && analyticsLoaded && preference === 'accepted') {
        window.gtag('event', 'phone_click', { contact_method: 'phone_link' });
      }
    });

    const banner = document.createElement('section');
    banner.className = 'analytics-consent';
    banner.setAttribute('role', 'region');
    banner.setAttribute('aria-labelledby', 'analytics-consent-title');
    banner.hidden = preference !== null;
    banner.innerHTML = '<div class="analytics-consent-copy">' +
      '<strong id="analytics-consent-title">Çerez tercihiniz</strong>' +
      '<p>Site ziyaretlerini ve telefonla arama bağlantısı tıklamalarını ölçmek için Google Analytics kullanmak istiyoruz. ' +
      'Yalnızca kabul ederseniz analitik çerezler etkinleştirilir. ' +
      '<a href="/gizlilik/">Gizlilik bilgilendirmesi</a></p></div>' +
      '<div class="analytics-consent-actions">' +
      '<button type="button" data-consent-reject>Reddet</button>' +
      '<button type="button" data-consent-accept>Kabul et</button></div>';
    document.body.appendChild(banner);

    banner.querySelector('[data-consent-accept]').addEventListener('click', function () {
      choose('accepted');
      banner.hidden = true;
    });
    banner.querySelector('[data-consent-reject]').addEventListener('click', function () {
      choose('rejected');
      banner.hidden = true;
    });

    const footer = document.querySelector('.footer-bottom');
    if (footer) {
      const edit = document.createElement('button');
      edit.type = 'button';
      edit.className = 'analytics-preferences-button';
      edit.textContent = 'Çerez tercihlerini değiştir';
      edit.addEventListener('click', function () {
        banner.hidden = false;
        banner.querySelector('[data-consent-reject]').focus();
      });
      footer.appendChild(edit);
    }
  });
}());
