# KOCAELİ YUVAM ELEKTRİK — Marka Uyumlu Web Sitesi

**Hedef alan adı:** https://kocaeliyuvamelektrik.com  
**Sürüm:** 14 Kasım 2026 · Kırmızı / Elektrik Mavisi / Lacivert tema  
**İletişim:** Bayram Canseven · 0532 711 36 77  
**Hizmet merkezi:** Alikahya Fatih Mahallesi, Yuvam Akarca Toplu Konutları, İzmit / Kocaeli

## Yeni marka tasarımı

Site önceki turuncu ağırlıklı şablondan, seçtiğiniz **vektörel Kocaeli Yuvam Elektrik logosuna** uyumlu bir tasarıma geçirildi.

| Rol | Renk kodu | Kullanım |
| --- | --- | --- |
| Marka kırmızısı | `#D6010D` | Çatı, telefonla arama düğmesi, acil arıza vurgu çizgileri |
| Elektrik mavisi | `#004DBB` | YUVAM yazısı, hizmet ikonları, sayfa bağlantıları |
| Koyu lacivert | `#051839` | Başlıklar, üst bilgi şeridi ve alt sayfa bandı |
| Kırık beyaz | `#F5F8FC` | Sayfa arka planı ve ferah içerik alanları |

Tüm **31 HTML sayfasında** yeni logo üst menü ve alt bilgi alanında kullanılır. Ana sayfanın sağ görselinde logo daha büyük görünür. Logo `site/assets/yuvam-elektrik-logo.svg` dosyasından gelir; font veya piksele bağlı değildir. Markaya uygun `favicon.svg` ve sosyal paylaşım görseli de eklendi.

### İçerik kapsamı

- 19 hizmet sayfası (16 temel + 3 kurumsal/ticari), filtrelenebilir hizmet kataloğu
- Ana Sayfa, Hizmetler, Bölgeler, Hakkımızda, İletişim, SSS ve Gizlilik
- 4 bilgilendirici blog içeriği
- Tüm sayfalarda **0532 711 36 77** arama bağlantısı, mobilde sabit telefon düğmesi
- `sitemap.xml`, `robots.txt`, canonical URL, OpenGraph ve `Electrician` yapılandırılmış verisi

## Paket dosyaları

- `site/` — Hosting'e yüklenecek hazır site. Bunun **içeriğini** domainin web kök dizinine yükleyin.
- `site/index.html` — Ana sayfa.
- `site/assets/site.css` — Kullanılan tüm CSS; marka teması en sonda yer alır.
- `site/assets/yuvam-elektrik-logo.svg` — Güncel vektörel logo.
- `site/assets/favicon.svg` — Logonun ikonlaştırılmış versiyonu.
- `site/assets/yuvam-elektrik-sosyal-kart.png` — Web bağlantısı paylaşım görseli.
- `SITE_AYARLARI.json` — Domain, telefon, adres ve opsiyonel WhatsApp bilgileri.
- `build_site.py`, `content_data.py` — İçeriği ve sayfaları yeniden oluşturacak kaynak kod.
- `YUVAM_ELEKTRIK_TUM_WEB_ICERIKLERI.md` — Site metinleri ve SEO içerikleri.
- `ONIZLEMELER/` — Görsel ekran görüntüleri.

## Yayına alma

1. Alan adı `kocaeliyuvamelektrik.com` için hosting seçin; doğru DNS kayıtlarını tanımlayın ve HTTPS/SSL sertifikasını açın. **Dosyaların hazırlanması sitenin internette yayımlandığı anlamına gelmez.**
2. ZIP dosyasını açın. `site/` klasörünün **içindeki** dosyaları hosting hesabının `public_html` veya eşdeğer web kök dizinine yükleyin.
3. Tarayıcıda `https://kocaeliyuvamelektrik.com/`, `https://kocaeliyuvamelektrik.com/hizmetler/` ve `https://kocaeliyuvamelektrik.com/iletisim/` adreslerini kontrol edin.
4. Mobilde **0532 711 36 77** düğmesini gerçek telefon üzerinde test edin. Menüleri, hizmet kartlarını ve iletişim sayfasını da kontrol edin.
5. Google Search Console'a alan adını doğrulayarak `https://kocaeliyuvamelektrik.com/sitemap.xml` site haritasını gönderin. Google İşletme Profili'ne aynı web adresini ekleyin.
6. Gerçek iş, servis araçları, tabela ve ekip fotoğraflarını işletmenin izniyle daha sonra siteye ekleyebilirsiniz. Doğrulanmamış yorum, başarı sayısı veya belge kullanmayın.

## Site ayarlarının değiştirilmesi

`SITE_AYARLARI.json` içeriğinde gerçek telefon ve alan adı tanımlı:

```json
{
  "telefon_gorunen": "0532 711 36 77",
  "telefon_uluslararasi": "+905327113677",
  "whatsapp_uluslararasi": "",
  "alan_adi": "https://kocaeliyuvamelektrik.com"
}
```

**WhatsApp hattı teyit edilmediği için bağlantı gösterilmez**; yanlış iletişim bağlantısı oluşturulmaması için boş tutulmuştur. Daha sonra doğrulanırsa numarayı +90 biçiminde ekleyip `python build_site.py` çalıştırarak HTML dosyalarını yeniden üretin.

Alan adı tanımlı olduğu için bu pakette **sitemap ve indeksleme meta etiketleri yayına uygun** oluşturuldu. Ancak yayınlamadan önce domain/SSL/redirect ayarları doğrulanmalıdır.

## Güvenlik ve hizmet kapsamı notları

İşletmenin beyan ettiği hizmetler esas alınmıştır. 7/24 arıza talepleri için arama yapılabilir; **kesin servis varış zamanı vaat edilmez**. Kombi/doğalgaz ve klima devreleri için gereken yetkili servis işleri, sitenin elektrik bağlantı hizmetinden ayrı değerlendirilmelidir. Gizlilik/KVKK bilgilendirmesi işletmenin gerçek süreçlerine göre yayın öncesinde doğrulanmalıdır.

Kapsam dışı tutulan işler: **ofis tadilatı/dekorasyonu, telefon santrali kurulumu, korniş montajı**.

## Teknik kalite kontrol

Statik dosyalarda 31 sayfanın tüm iç bağlantıları ve arama bağlantıları kontrol edildi. Chromium ile **1440 px, 850 px, 390 px ve 360 px** ekranlarda görsel taşma, logo yükleme ve JavaScript konsol hatası kontrolü yapıldı. Mobil menü açılma testi ve hizmet arama filtresi testi geçti. Farklı gerçek cihazlarda ve yayın alan adında son kontrolleri de yapmanız önerilir.

## Google Analytics 4 ve çerez tercihi (15 Kasım 2026)

- Ölçüm kimliği: `G-7XXDVG2JWK`.
- Kod, `site/assets/site.js` içinde bulunur ve tüm sayfalarda ortak olarak yüklenir.
- Google Analytics betiği, ziyaretçi açıkça kabul etmeden indirilmez; tercih yerel depolamada saklanır.
- Alt bilgideki **Çerez tercihlerini değiştir** düğmesiyle onay geri çekilebilir.
- Telefon bağlantıları `phone_click`, iletişim sayfası ziyaretleri `contact_view` etkinliğini gönderir.
- GitHub Pages yayını `site/` dizinini kullandığı için kaynak `build_site.py` ve üretilmiş gizlilik sayfası birlikte güncellenmiştir.
- Google Analytics'te etiketin algılanması ve canlı ziyaret testleri için test tarayıcısında **Kabul et** seçilmelidir.
- KVKK, saklama süresi ve sınır ötesi aktarım yükümlülüklerinin gerçek uygulamaya göre hukuken değerlendirilmesi gerekir.
