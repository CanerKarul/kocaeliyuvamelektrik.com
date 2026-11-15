# -*- coding: utf-8 -*-
"""Yuvam Elektrik - original Turkish content. No text copied from reference websites."""

SERVICES = [
{
 'slug':'elektrik-ariza-tespiti-ve-tamiri','name':'Elektrik Arıza Tespiti ve Tamiri','short':'Priz çalışmıyor, ışık yanmıyor veya elektrik sık sık kesiliyorsa arızanın nedenini birlikte belirleyelim.','icon':'bolt','category':'Arıza ve güvenlik',
 'lead':'İzmit’te ev, iş yeri ve apartmanlarda karşılaşılan elektrik arızaları için yerinde kontrol ve onarım hizmeti.',
 'body':'Bir odada elektrik olmaması, aydınlatmanın düzensiz çalışması, şalterin beklenmedik şekilde kapanması veya prizden koku gelmesi farklı nedenlerden kaynaklanabilir. Yuvam Elektrik, arızayı rastgele parça değiştirmek yerine sorunun kaynağını tespit ederek uygun müdahaleyi planlar. Gerekli kontrol ve onarımın kapsamı yerinde değerlendirmeden sonra açıklanır.',
 'signals':['Priz veya aydınlatma çalışmıyor','Elektrik kesintisi yalnızca belirli bir bölümde yaşanıyor','Şalter veya sigorta tekrar tekrar atıyor','Yanık kokusu ya da olağan dışı ısınma fark ediliyor'],
 'tasks':['Elektrik arıza kontrolü','Hat, bağlantı ve anahtar-priz değerlendirmesi','Arızalı parçanın uygun şekilde onarımı veya değişimi','İşlem sonrası güvenli kullanım kontrolü'],
 'note':'Kıvılcım, duman, yanık kokusu ya da elektrik çarpması riski varsa tesisata dokunmayın; güvenli bir noktadan yetkili yardım isteyin.'
},
{
 'slug':'elektrik-tesisati-bakimi-ve-yenileme','name':'Elektrik Tesisatı Bakımı ve Yenileme','short':'Eskiyen kablolar, yetersiz hatlar ve değişen kullanım ihtiyaçları için tesisat bakım ve yenileme.','icon':'cable','category':'Tesisat ve taahhüt',
 'lead':'İzmit’te konut ve iş yerleri için mevcut elektrik tesisatının kontrolü, bakımı ve ihtiyaç duyulan bölümlerin yenilenmesi.',
 'body':'Zaman içinde artan elektrikli cihaz sayısı ve eskimiş bağlantılar, mevcut tesisatın yeniden değerlendirilmesini gerektirebilir. Yuvam Elektrik; kablo hatları, bağlantı noktaları, anahtar-priz yerleşimi ve ilgili tesisat bölümlerini yapılan işe göre inceler. Amaç, kullanım ihtiyacına uygun ve düzenli bir çözüm oluşturmaktır. Yapılacak değişiklikler uygulama öncesinde konuşulur.',
 'signals':['Eski yapıdaki elektrik tesisatı yenilenecek','Odaların priz veya aydınlatma düzeni değişecek','Kablo ve bağlantılarda yıpranma şüphesi var','Tesisatta tekrarlayan arızalar görülüyor'],
 'tasks':['Mevcut tesisatın değerlendirilmesi','İhtiyaca göre hat ve kablo yenileme','Priz ve anahtar noktalarının düzenlenmesi','Bakım ve bağlantı kontrolü'],
 'note':'Tesisat değişikliklerinin kapsamı, mevcut sistem ve yürürlükteki teknik gereklilikler göz önünde bulundurularak belirlenir.'
},
{
 'slug':'priz-anahtar-ve-salter-montaji','name':'Priz, Anahtar ve Şalter Montajı','short':'Gevşeyen priz, çalışmayan anahtar veya yenilenmesi gereken şalterler için montaj ve onarım.','icon':'plug','category':'Montaj ve aydınlatma',
 'lead':'İzmit’te priz, anahtar ve şalter değişimi, yeni montaj ve bağlantı sorunlarına yönelik yerinde hizmet.',
 'body':'Gevşek prizler, çalışmayan ışık anahtarları ve yıpranmış şalterler günlük kullanımda rahatsızlık oluşturur; bazı durumlarda güvenlik riski de taşıyabilir. Yuvam Elektrik, mevcut noktayı kontrol ederek uygun ürünün doğru şekilde bağlanmasına ve montajın tamamlanmasına yardımcı olur. Yeni priz veya anahtar noktası talepleri, mevcut hat durumuna göre değerlendirilir.',
 'signals':['Priz yerinden oynuyor veya ısınıyor','Anahtar aydınlatmayı açıp kapatmıyor','Eski prizler yenilenecek','Yeni bir priz veya anahtar noktası isteniyor'],
 'tasks':['Priz değişimi ve montajı','Anahtar ve şalter kontrolü','Arızalı bağlantıların değerlendirilmesi','Yeni nokta için tesisat uygunluğu kontrolü'],
 'note':'Isınan, kararan veya kıvılcım çıkaran prizleri kullanmayı bırakın; kendi başınıza sökmeyin.'
},
{
 'slug':'avize-armatur-ve-aplik-montaji','name':'Avize, Armatür ve Aplik Montajı','short':'Avize, duvar apliği ve aydınlatma armatürlerinin güvenli bağlantı ve montajı.','icon':'bulb','category':'Montaj ve aydınlatma',
 'lead':'Yeni alınan avize, tavan armatürü ve duvar apliklerinin montajında Yuvam Elektrik yanınızda.',
 'body':'Aydınlatma ürünlerinde doğru bağlantı kadar ürünün yerleşimi ve sabitlenmesi de önemlidir. Yuvam Elektrik, avize, aplik ve armatür montajı öncesinde mevcut elektrik çıkışı ve montaj noktasını değerlendirir. Uygun olan ürünleri yerine monte eder, bağlantılarını tamamlar ve çalışmasını kontrol eder. Taşıyıcı yüzeyin yetersiz olduğu durumlarda gerekli ek işlemler önceden paylaşılır.',
 'signals':['Yeni avize veya aydınlatma ürünü alındı','Mevcut avize değiştirilecek','Duvar apliği monte edilecek','Armatür düzgün çalışmıyor'],
 'tasks':['Avize ve sarkıt montajı','Tavan armatürü montajı','Aplik bağlantısı ve montajı','Mevcut bağlantı noktasının kontrolü'],
 'note':'Ağır avizelerde montaj yüzeyinin taşıma kapasitesi ayrıca değerlendirilmelidir.'
},
{
 'slug':'led-spot-ve-ic-mekan-aydinlatma','name':'LED, Spot ve İç Mekân Aydınlatma','short':'Ev ve iş yerlerinde LED, spot ve iç mekân aydınlatma montajı ile arıza giderme.','icon':'bulb','category':'Montaj ve aydınlatma',
 'lead':'Salon, mutfak, koridor ve iş yeri gibi alanlarda kullanışlı iç mekân aydınlatma çözümleri.',
 'body':'Doğru aydınlatma hem kullanım konforunu hem de mekânın görünümünü etkiler. Mevcut LED ve spot aydınlatmanın arızası, yerleşim değişikliği veya yeni montaj taleplerinde Yuvam Elektrik bağlantı ve tesisat ihtiyacını değerlendirir. Ürün seçimi, güç ihtiyacı ve kullanım alanı dikkate alınarak uygulanabilir seçenekler konuşulur.',
 'signals':['Spot veya LED aydınlatma çalışmıyor','Yeni iç mekân ışıklandırması planlanıyor','Işıklar titriyor ya da düzensiz yanıyor','Mevcut armatürler yenilenecek'],
 'tasks':['LED ve spot montajı','Aydınlatma bağlantısı kontrolü','Arızalı armatür değişimi','Mevcut aydınlatma hattının değerlendirilmesi'],
 'note':'Ürün ve sürücü uyumluluğu, montaj öncesinde kontrol edilmelidir.'
},
{
 'slug':'dis-mekan-ve-cevre-aydinlatma','name':'Dış Mekân ve Çevre Aydınlatması','short':'Balkon, bahçe, bina girişi ve ortak alanlarda dış ortam aydınlatma kurulumu.','icon':'sun','category':'Montaj ve aydınlatma',
 'lead':'Bahçe, bina çevresi, giriş ve açık alanlar için kullanım amacına uygun aydınlatma montajı.',
 'body':'Dış mekân aydınlatması, görüş konforu ve alan kullanımını destekler. Bahçe, balkon, kapı önü, bina girişi ve çevre aydınlatma taleplerinde montaj noktaları ile kablo güzergâhı birlikte değerlendirilir. Dış ortam koşullarına uygun ürün seçimi ve bağlantı düzeni önemlidir. Yuvam Elektrik, mevcut tesisatın uygunluğuna göre kurulum ve yenileme işlemlerini planlar.',
 'signals':['Bahçe ya da bina girişine ışık isteniyor','Dış mekândaki aydınlatma çalışmıyor','Aplik veya projektör değişecek','Ortak alan aydınlatması yenilenecek'],
 'tasks':['Bahçe ve çevre aydınlatması montajı','Dış mekân aplik ve projektör bağlantısı','Arızalı aydınlatma noktalarının kontrolü','Mevcut dış hatların değerlendirilmesi'],
 'note':'Dış ortamda kullanılacak elektrik ekipmanları yerin koşullarına uygun koruma özelliklerinde seçilmelidir.'
},
{
 'slug':'sigorta-ve-kacak-akim-rolesi','name':'Sigorta ve Kaçak Akım Rölesi Kontrolü','short':'Sigorta atması, arızalı devre kesiciler ve kaçak akım rölesi sorunlarında kontrol ve onarım.','icon':'shield','category':'Arıza ve güvenlik',
 'lead':'Sık sık atan sigortalar ve kaçak akım rölesi sorunları için güvenli yerinde değerlendirme.',
 'body':'Elektrik sigortaları aşırı akım ve kısa devre gibi durumlarda devreyi korumaya yardımcı olur; kaçak akım röleleri ise uygun koşullarda kaçak akıma karşı ek koruma sağlar. Tekrarlayan açmaların nedeni birden fazla olabilir. Yuvam Elektrik, ilgili devreyi ve tesisatı değerlendirerek uygun onarım veya değişim ihtiyacını belirler. Sorunun kaynağı anlaşılmadan koruma elemanını daha yüksek değerli bir ürünle değiştirmek doğru bir çözüm değildir.',
 'signals':['Sigorta sürekli atıyor','Kaçak akım rölesi devreyi kapatıyor','Panoda eski veya yıpranmış elemanlar var','Belirli cihaz çalışınca elektrik kesiliyor'],
 'tasks':['Sigorta arızası değerlendirmesi','Kaçak akım rölesi kontrolü','Bağlantı ve devre incelemesi','Gerektiğinde uygun eleman değişimi'],
 'note':'Koruma elemanlarını devre dışı bırakmayın ve arızanın nedeni bilinmeden tekrar tekrar açmaya zorlamayın.'
},
{
 'slug':'elektrik-panosu-kurulum-ve-tadilati','name':'Elektrik Panosu Kurulum ve Tadilatı','short':'Elektrik panosu düzenleme, yıpranmış bileşenlerin kontrolü ve ihtiyaçlara uygun tadilat.','icon':'panel','category':'Arıza ve güvenlik',
 'lead':'Konut, küçük işletme ve ortak alan elektrik panoları için kontrol, düzenleme ve tadilat hizmeti.',
 'body':'Elektrik panosu; devrelerin dağıtımı ve koruma elemanlarının bulunduğu kritik bir noktadır. Düzensiz bağlantılar, eskimiş elemanlar veya değişen kullanım ihtiyaçları pano tadilatını gündeme getirebilir. Yuvam Elektrik, mevcut panoyu ve ihtiyacı değerlendirerek uygun düzenleme, bileşen yenileme ve bağlantı işlemlerini planlar. Gereken kapasite, koruma düzeni ve yetki kapsamı dikkate alınır.',
 'signals':['Panoda arıza veya ısınma şüphesi var','Sigortalar ve devreler düzenlenecek','Pano bileşenleri eskimiş','Tesisat yenilemesiyle pano düzeni değişecek'],
 'tasks':['Pano kontrolü ve arıza değerlendirmesi','Uygun pano düzenleme ve tadilatı','Sigorta/koruma elemanı değişimi','Bağlantı ve devre düzeninin gözden geçirilmesi'],
 'note':'Panolar yalnızca yetkin kişilerce, uygun güvenlik prosedürleriyle açılmalı ve üzerinde işlem yapılmalıdır.'
},
{
 'slug':'topraklama-hatti-ve-kontrolu','name':'Topraklama Hattı ve Kontrolü','short':'Topraklama hattı ihtiyacı ve mevcut bağlantıların uygunluğuna yönelik teknik değerlendirme.','icon':'shield','category':'Arıza ve güvenlik',
 'lead':'Topraklama bağlantıları ve ihtiyaç duyulan hat düzenlemeleri için yerinde inceleme.',
 'body':'Topraklama, elektrik tesisatının güvenliğinde rol oynayan temel unsurlardan biridir. Eksik, yıpranmış veya uygunluğu belirsiz bağlantılar uzman değerlendirmesi gerektirir. Yuvam Elektrik, mevcut hat durumu ve yapılacak işin kapsamına göre topraklama bağlantılarının kontrolü ve gerekli düzenlemeler için yardımcı olur. Resmî ölçüm, test veya rapor gerektiren işler ayrıca yetki ve mevzuat koşullarına göre ele alınmalıdır.',
 'signals':['Topraklama bağlantısından şüphe duyuluyor','Eski tesisat yenileniyor','Yeni hat düzenlemesi planlanıyor','Priz veya pano bağlantıları kontrol edilecek'],
 'tasks':['Mevcut topraklama bağlantısının değerlendirilmesi','Hat ihtiyacının belirlenmesi','Uygun kapsamda bağlantı düzenleme','Gerekli durumlarda yetkili ölçüm yönlendirmesi'],
 'note':'Topraklama işlemleri, sadece bir kablo eklemekten ibaret değildir; sistem bütünlüğü ve uygun testler önemlidir.'
},
{
 'slug':'internet-kablosu-cekme','name':'İnternet Kablosu Çekme','short':'Ev ve iş yerlerinde internet hattı, ağ kablosu ve bağlantı noktası düzenlemeleri.','icon':'wifi','category':'İletişim ve güvenlik',
 'lead':'İnternet modeminin bulunduğu nokta ile kullanım alanları arasında kablolama desteği.',
 'body':'Wi-Fi kapsamasının yetersiz kaldığı veya sabit bağlantının tercih edildiği alanlarda uygun ağ kablosu ve bağlantı noktaları önemlidir. Yuvam Elektrik, ev ve küçük işletmelerde internet kablosu çekimi, hat güzergâhı ve bağlantı sonlandırma taleplerine yardımcı olur. İnternet servis sağlayıcısının şebeke arızaları veya abonelik işlemleri bu hizmetin dışındadır.',
 'signals':['Modem başka odada, kablolu bağlantı isteniyor','İnternet kablosu hasarlı olabilir','Yeni ağ prizi/noktası talep ediliyor','Kablo güzergâhı düzenlenecek'],
 'tasks':['Ağ kablosu çekme','İç mekân kablo güzergâhı düzenleme','Uygun bağlantı noktası montajı','Kablo bağlantılarının kontrolü'],
 'note':'Dış şebeke bağlantısı ve operatör tarafındaki arızalar için ilgili internet servis sağlayıcısına başvurulmalıdır.'
},
{
 'slug':'telefon-hatti-ve-kablolama','name':'Telefon Hattı ve Kablolama','short':'Telefon hattı bağlantı, kablo yenileme ve iç tesisat düzenlemeleri.','icon':'phone','category':'İletişim ve güvenlik',
 'lead':'Konut ve küçük işletmelerde telefon iç hatlarının bağlantı ve kablolama ihtiyaçları.',
 'body':'Telefon hattının kullanım noktasına taşınması, kablonun yenilenmesi veya iç bağlantı arızasının kontrol edilmesi gerekebilir. Yuvam Elektrik, bina içi telefon kablolaması ve bağlantı noktalarına yönelik işler için yerinde inceleme yapar. Telefon santrali kurulumu hizmetlerimiz arasında değildir; operatör şebekesi kaynaklı sorunlarda servis sağlayıcısı ile iletişim kurulmalıdır.',
 'signals':['Telefon iç hattı çalışmıyor','Kablo veya priz değişecek','İç tesisat güzergâhı yenilenecek','Yeni telefon bağlantı noktası isteniyor'],
 'tasks':['Telefon hattı iç kablolaması','Bağlantı noktası kontrolü','Kablo yenileme ve düzenleme','Mevcut hattın değerlendirilmesi'],
 'note':'Telefon santrali kurulumu yapılmaz; operatör altyapısındaki arızalar kapsam dışıdır.'
},
{
 'slug':'uydu-anten-kurulum-ve-tamiri','name':'Uydu Anten Kurulumu ve Tamiri','short':'Uydu anten, LNB ve uydu bağlantı kablosu kurulumu ile arıza tespiti.','icon':'satellite','category':'İletişim ve güvenlik',
 'lead':'İzmit’te çanak anten ve uydu bağlantı sorunlarında kurulum, ayar ve tamir desteği.',
 'body':'Televizyonda sinyal kaybı, görüntü kesilmesi veya uydu tesisatındaki bağlantı sorunları günlük izleme deneyimini etkileyebilir. Yuvam Elektrik, çanak anten, kablo ve ilgili bağlantı bileşenlerini yapılan işe göre değerlendirerek kurulum veya onarım işlemlerini planlar. Çatı ve yüksek noktalar için güvenli erişim koşulları önceden incelenir.',
 'signals':['Televizyonda uydu sinyali yok','Kablo veya anten bağlantısı hasarlı','Çanak anten kurulacak veya ayarlanacak','Mevcut uydu sistemi kontrol edilecek'],
 'tasks':['Uydu anten kurulumu ve ayarı','Bağlantı kablosu ve konnektör kontrolü','LNB ve ilgili bileşenlerin değerlendirilmesi','Sinyal sorununun kaynağını inceleme'],
 'note':'Yüksekten çalışma gerektiren işlerde güvenli erişim ve hava koşulları uygun olmalıdır.'
},
{
 'slug':'goruntulu-diafon-ve-interkom','name':'Görüntülü Diafon ve İnterkom','short':'Görüntülü kapı konuşma sistemleri, diafon bağlantıları ve arıza giderme.','icon':'video','category':'İletişim ve güvenlik',
 'lead':'Apartman ve konutlar için görüntülü diafon, kapı konuşma sistemi ve bağlantı hizmetleri.',
 'body':'Kapıdan arayan kişinin görüntüsünü ve sesini almak, bina girişini kontrol etmek için görüntülü konuşma sistemleri kullanılır. Yuvam Elektrik, mevcut diafonun çalışmaması, cihaz değişimi veya yeni sistem montajı taleplerinde iç bağlantıları ve sistem uyumluluğunu değerlendirir. Çok daireli sistemlerde ortak altyapı ve bina yönetimi onayı gerekebilir.',
 'signals':['Görüntülü diafon ekranı açılmıyor','Ses veya görüntü gelmiyor','Kapı açma bağlantısı sorunlu','Yeni diafon veya interkom isteniyor'],
 'tasks':['Görüntülü diafon montajı','İç ünite ve bağlantı kontrolü','Uyumlu cihaz değişimi','Arıza değerlendirmesi ve kablo kontrolü'],
 'note':'Merkezi bina sistemlerine müdahalede yönetim onayı ve ürün uyumluluğu kontrol edilmelidir.'
},
{
 'slug':'kamera-sistemi-montaji','name':'Kamera Sistemi Montajı','short':'Konut, dükkân ve küçük işletmeler için güvenlik kamerası montajı ve bağlantıları.','icon':'camera','category':'İletişim ve güvenlik',
 'lead':'Kamera yerleşimi, kablo bağlantısı ve sistem montajında sahaya uygun uygulama.',
 'body':'Güvenlik kamerasının yararlı olabilmesi için doğru açı, güvenli montaj ve düzenli kablolama gerekir. Yuvam Elektrik, ev ve iş yeri için kamera montajı ve bağlantı taleplerini yerinde değerlendirir. Mevcut kayıt altyapısı, bağlantı imkânları ve ürün uyumluluğu montajdan önce konuşulur. Kamera kullanımında kişisel verilerin korunması ve mahremiyet kurallarına uyulmalıdır.',
 'signals':['Yeni kamera montajı yapılacak','Mevcut kamera yer değiştirecek','Kamera bağlantısı veya güç hattı sorunlu','Kablolar düzenlenecek'],
 'tasks':['Kamera montajı ve sabitleme','Güç ve veri kablosu düzenleme','Mevcut bağlantıların kontrolü','Gerekli cihaz uyumluluğunun değerlendirilmesi'],
 'note':'Kamera yerleşiminde ortak alan kuralları ve kişisel verilerin korunması yükümlülükleri gözetilmelidir.'
},
{
 'slug':'alarm-sistemi-kurulumu','name':'Alarm Sistemi Kurulumu','short':'Ev ve iş yerlerinde alarm sistemi bileşenlerinin montaj ve bağlantı desteği.','icon':'bell','category':'İletişim ve güvenlik',
 'lead':'Alarm sistemi ekipmanlarının montajı ve mevcut bağlantıların düzenlenmesi için yerinde destek.',
 'body':'Alarm sistemlerinde sensörlerin ve uyarı bileşenlerinin yerleşimi, sistemin amacına uygun çalışması açısından önem taşır. Yuvam Elektrik, kurulacak ürünün modeli ve altyapının durumuna göre bağlantı ve montaj işlerini değerlendirir. Uzaktan izleme aboneliği, güvenlik şirketi hizmeti veya sistemin üreticiye özel yetkilendirilmiş programlaması gerekiyorsa kapsam ayrıca netleştirilir.',
 'signals':['Yeni alarm ekipmanı monte edilecek','Bağlantı kabloları düzenlenecek','Mevcut sistemin bir bileşeni değiştirilecek','Alarm bağlantısında sorun görülüyor'],
 'tasks':['Alarm ekipmanı montajı','Kablolama ve bağlantı düzenleme','Uygun bileşen değişimi','Kurulum kapsamının cihaz modeline göre değerlendirilmesi'],
 'note':'Merkeze bağlı izleme ve özel yazılım hizmetleri montaj hizmetinden ayrı olabilir.'
},
{
 'slug':'gaz-dedektoru-kurulumu','name':'Gaz Dedektörü Kurulumu','short':'Gaz uyarı dedektörlerinin ürün talimatlarına uygun montaj ve bağlantısı.','icon':'shield','category':'Arıza ve güvenlik',
 'lead':'Ev ve uygun iş yerlerinde gaz dedektörü montaj ve elektrik bağlantı ihtiyaçlarına destek.',
 'body':'Gaz dedektörleri, uygun tasarım ve bakımla gaz sızıntısı gibi risklere karşı uyarı sağlamaya yardımcı olur. Yuvam Elektrik, cihaz türü, montaj yeri ve üretici talimatlarına göre yapılabilecek elektrik bağlantısı ve montajı değerlendirir. Gaz tesisatının onarımı veya resmî gaz tesisatı uygunluk işlemleri bu hizmetin parçası değildir; gerekli durumlarda yetkili gaz firması devreye girmelidir.',
 'signals':['Gaz dedektörü monte edilecek','Mevcut cihaz değiştirilecek','Elektrik bağlantısı düzenlenecek','Cihazın konumuyla ilgili teknik değerlendirme isteniyor'],
 'tasks':['Gaz dedektörü cihaz montajı','Gerekli elektrik bağlantısı','Ürün talimatlarına göre yerleşim değerlendirmesi','Montaj sonrası temel çalışma kontrolü'],
 'note':'Gaz kokusu alıyorsanız elektrik düğmelerine, fişlere veya telefonunuza gazlı ortamda müdahale etmeyin; güvenli alana çıkıp acil gaz hattını arayın.'
},
{
 'slug':'elektrik-taahhut-ve-uygulama','name':'Elektrik Taahhüt ve Uygulama İşleri','short':'Konut, iş yeri ve küçük ölçekli projelerde elektrik uygulama, yenileme ve montaj işleri.','icon':'building','category':'Tesisat ve taahhüt',
 'lead':'Planlı elektrik işleri için kapsamı önceden belirlenen yerinde uygulama ve taahhüt desteği.',
 'body':'Birden fazla elektrik işinin aynı projede yapılacağı durumlarda, iş sırasını ve malzeme ihtiyacını baştan planlamak önemlidir. Yuvam Elektrik, konut ve küçük işletmelerin elektrik tesisatı, pano, priz, anahtar ve aydınlatma uygulamalarını kapsamına göre değerlendirir. Uygulama öncesinde iş kalemleri, uygunluk ve süreç konuşulur. Proje çizimi, resmî onay veya özel yetki gerektiren işler ilgili yetkili kişilerce yürütülmelidir.',
 'signals':['Birden fazla tesisat işi aynı anda yapılacak','Küçük iş yeri elektrik düzeni yenilenecek','Montaj ve malzeme listesi çıkarılacak','Planlı yenileme için keşif isteniyor'],
 'tasks':['İş kapsamı ve uygulama planlaması','Elektrik tesisatı uygulamaları','Pano, aydınlatma, priz ve anahtar işleri','İş kalemleri için malzeme ihtiyacının belirlenmesi'],
 'note':'Resmî proje ve yetki gerektiren işler, mevzuat kapsamındaki uzman ve kurumlarla yürütülmelidir.'
},
]

FAQS = [
('Yuvam Elektrik hangi bölgelere hizmet veriyor?', 'Öncelikli hizmet bölgemiz İzmit’te Yuvam Akarca, Akarca Mahallesi, Alikahya, Fevzi Çakmak ve Yahya Kaptan çevresidir. İzmit’in diğer mahalleleri ile yakın merkez ilçelerdeki talepler için konumunuzu bildirerek uygunluğu öğrenebilirsiniz.'),
('Elektrik arızasında sizi nasıl çağırabilirim?', 'Telefonla arayıp yaşadığınız sorunu, mahalleyi ve mümkünse bina türünü belirtmeniz yeterlidir. Uygunluk, yapılabilecek ilk kontrol ve ziyaret planı görüşmede netleştirilir.'),
('Sigorta sürekli atıyorsa ne yapmalıyım?', 'Sigortanın tekrar tekrar atması aşırı yük, kısa devre veya başka bir arızanın işareti olabilir. Koruma elemanlarını devre dışı bırakmayın; sorunun kontrol edilmesi için elektrik ustasına başvurun.'),
('Priz değişimi ve avize montajı için de gelebiliyor musunuz?', 'Evet. Priz, anahtar, şalter, avize, aplik, armatür ve uygun aydınlatma ürünlerinin montajı hizmetlerimiz arasındadır.'),
('Fiyatı telefonda öğrenebilir miyim?', 'İşin türüne göre telefonda ön bilgi verilebilir. Kesin tutar; arızanın durumu, kullanılacak malzeme ve işin kapsamı değerlendirildikten sonra netleştirilir.'),
('Aynı gün gelebiliyor musunuz?', 'Müsaitlik ve konuma göre aynı gün ziyaret mümkün olabilir. Kesin saat ve uygunluk için telefonla bilgi alınız.'),
('Apartman ortak alanı ve diafon işleri yapıyor musunuz?', 'Evet. Ortak alan aydınlatmaları ve görüntülü diafon gibi sistemlerde uygun kapsamlı işler için destek verebiliriz. Ortak tesisata müdahalede bina yönetimi onayı gerekebilir.'),
('İnternet kesintisini giderebilir misiniz?', 'Bina veya daire içindeki internet kablosu, bağlantı noktası ve kablolama işleriyle ilgileniyoruz. Servis sağlayıcısının dış şebeke ya da abonelik kaynaklı kesintileri için ilgili operatöre başvurulmalıdır.'),
('Hizmet almadan önce fotoğraf gönderebilir miyim?', 'WhatsApp hattı aktifse sorunun veya montaj yapılacak yerin fotoğrafını gönderebilirsiniz. Fotoğraf ön değerlendirmeye yardımcı olabilir; kesin teşhis için yerinde inceleme gerekebilir.'),
('7/24 elektrik servisi hizmetiniz var mı?', 'Evet. Haftanın her günü 24 saat elektrik arıza, bakım ve montaj talepleri için telefonla iletişim ve yerinde servis sunuyoruz. Müdahale planı konuma ve işin kapsamına göre görüşülür.'),
]

BLOGS = [
{
 'slug':'sigorta-surekli-neden-atar','title':'Elektrik Sigortası Sürekli Neden Atar?','intro':'Tekrarlayan sigorta açmaları yalnızca can sıkıcı değil, incelenmesi gereken bir uyarı olabilir.',
 'sections':[
 ('Sigortanın görevi nedir?', 'Devre kesiciler, belirli aşırı akım ve kısa devre koşullarında devreyi ayırarak kablo ve tesisatın korunmasına yardımcı olur. Kaçak akım röleleri ise farklı bir koruma görevi üstlenir. Bu parçaların işlevleri birbirine karıştırılmamalıdır.'),
 ('Sık görülen nedenler', 'Aynı hatta çok fazla cihazın bağlı olması, hasarlı bir elektrikli cihaz, gevşek bağlantı veya tesisattaki bir arıza sigorta açmalarına yol açabilir. Nedenin hangisi olduğu ancak uygun kontrolle belirlenebilir.'),
 ('Ne zaman elektrikçi çağırmalı?', 'Sigorta tekrar tekrar atıyorsa, yanık kokusu varsa, panoda aşırı ısınma fark ediliyorsa veya yalnızca belirli bir cihaz devreye girdiğinde sorun oluşuyorsa profesyonel kontrol isteyin. Sigorta değerini yükselterek sorunu gizlemeye çalışmayın.'),
 ], 'cta':'İzmit’te sigorta arızası için Yuvam Elektrik’i arayın.'
},
{
 'slug':'priz-isiniyorsa-ne-yapilmali','title':'Priz Isınıyorsa Ne Yapılmalı?','intro':'Isınan, kararan veya kıvılcım çıkaran prizler sıradan bir kullanım sorunu olarak görülmemelidir.',
 'sections':[
 ('Neden ısınabilir?', 'Gevşek bağlantılar, yıpranmış kontaklar, uygun olmayan çoklayıcı kullanımı veya yüksek güç çeken cihazlar prizde ısınmaya katkıda bulunabilir. Görünüşten kesin neden çıkarmak mümkün değildir.'),
 ('Risk işaretleri', 'Plastik yüzeyde renk değişimi, yanık kokusu, cızırtı, çatırdama ya da fişin gevşek durması önemli uyarılardır.'),
 ('Güvenli yaklaşım', 'Prizi ve bağlı cihazları kullanmayı bırakın, hasarlı kısmı sökmeye çalışmayın. Duman veya yangın belirtisi varsa güvenli bölgeye geçip acil yardım isteyin. Yuvam Elektrik’ten yerinde kontrol için bilgi alabilirsiniz.'),
 ], 'cta':'Priz ve anahtar arızalarında Yuvam Elektrik’e ulaşın.'
},
{
 'slug':'avize-montajinda-dikkat-edilecekler','title':'Avize Montajı Öncesinde Nelere Dikkat Edilmeli?','intro':'Yeni bir avize satın aldığınızda montaj noktasının uygunluğu da ürün seçimi kadar önemlidir.',
 'sections':[
 ('Tavan ve montaj noktası', 'Ürünün ağırlığı, tavandaki bağlantı noktası ve montaj zemini uygun olmalıdır. Özellikle büyük avizelerde yalnızca elektrik bağlantısı değil mekanik sabitleme de değerlendirilmelidir.'),
 ('Elektrik uyumluluğu', 'Ürünün teknik gereksinimleri, mevcut aydınlatma hattı ve anahtar düzeniyle uyumlu olmalıdır. Gerekli düzenlemeler işlem öncesinde netleştirilmelidir.'),
 ('Montaj hizmeti almak', 'Yuvam Elektrik; avize, aplik ve armatür montajında mevcut noktayı kontrol ederek güvenli bağlantı ve sabitleme için yardımcı olur. Ürünün fotoğrafını ve konumunuzu ileterek ön bilgi alabilirsiniz.'),
 ], 'cta':'İzmit’te avize montajı için telefonla iletişime geçin.'
},
{
 'slug':'goruntulu-diafon-calismiyorsa','title':'Görüntülü Diafon Çalışmıyorsa Neler Kontrol Edilmeli?','intro':'Görüntülü kapı konuşma sistemlerinde sorun; iç ünite, bağlantı veya ortak bina altyapısından kaynaklanabilir.',
 'sections':[
 ('Belirtiler ne anlatır?', 'Ekranın açılmaması, sesin gelmemesi veya kapı açma işlevinin çalışmaması farklı arıza türleridir. Tek bir dairede mi yoksa tüm binada mı yaşandığı, sorunun kapsamını anlamada yardımcı olur.'),
 ('Sistem uyumu', 'Eski sistemlerde her yeni iç ünite, mevcut ortak hatla uyumlu olmayabilir. Marka, model ve bağlantı biçiminin kontrolü önemlidir.'),
 ('Profesyonel değerlendirme', 'Cihazı sökerek deneme yapmak yerine mevcut sistemin ve bağlantıların incelenmesini isteyin. Ortak altyapıya müdahale gerektiğinde bina yönetimi ile koordinasyon kurun.'),
 ], 'cta':'Diafon montajı ve arıza kontrolü için Yuvam Elektrik’i arayın.'
},
]

REGIONS = [
 ('Yuvam Akarca','İşletmemizin bulunduğu bölge; öncelikli servis odağı.'),
 ('Akarca Mahallesi','Yuvam Akarca ve yakın konut bölgelerindeki talepler.'),
 ('Alikahya Merkez','Elektrik arıza, montaj ve bakım talepleri.'),
 ('Alikahya Fatih','Konut ve iş yeri elektrik işleri.'),
 ('Alikahya Atatürk','Yerinde elektrik kontrol ve montaj talepleri.'),
 ('Alikahya Cumhuriyet','Ev, apartman ve iş yeri işleri.'),
 ('Fevzi Çakmak','Yuvam Akarca çevresi ve yakın yerleşimler.'),
 ('Yahya Kaptan','İzmit içindeki yakın servis bölgelerinden biri.'),
 ('Karadenizliler','Konuma göre servis uygunluğu telefonla teyit edilir.'),
]

HOMEPAGE_SECTION_COPY = {
 'hero_eyebrow':'İZMİT • YUVAM AKARCA • ALİKAHYA',
 'hero_title':'İzmit’te elektrikçi mi arıyorsunuz? Yuvam Elektrik yanınızda.',
 'hero_text':'Priz ve anahtar onarımından avize montajına, sigorta arızalarından elektrik tesisatı ve görüntülü diafon işlerine kadar ihtiyaç duyduğunuz elektrik hizmetlerinde Yuvam Elektrik’e ulaşın. İzmit’te Yuvam Akarca merkezli yerinde hizmet.',
 'about_title':'Mahallenize yakın, işine odaklanan elektrik hizmeti.',
 'about_text':'Yuvam Elektrik, Kocaeli’nin İzmit ilçesinde, Yuvam Akarca–Alikahya çevresinde elektrik arıza, bakım, montaj ve uygun kapsamlı taahhüt işleriyle ilgilenir. Bir priz değişimi kadar küçük işlerde de birden fazla kalemi içeren tesisat yenilemelerinde de önce ihtiyacı dinler, ardından uygulanabilir çözümü açıklar.',
 'price_text':'Elektrik işlerinde ücret; arızanın nedeni, montajın zorluğu, kullanılacak malzeme ve ulaşım koşullarına göre değişir. Telefonda sorununuzu anlatarak ön değerlendirme alabilir, işlem kapsamı netleştikten sonra fiyat bilgisi isteyebilirsiniz.'
}

# 14 Kasım 2026 — İşletmeden alınan güncel hizmet listesi ve kurumsal bilgiler.
# İlk 16 hizmet işletmenin listelediği başlıklardır. Son üç kayıt ise
# Hakkımızda metnindeki ticari/kurumsal hizmetlerden türetilmiştir.
_original_services = {item['slug']: dict(item) for item in SERVICES}

def _reuse(slug, *, name=None, short=None, lead=None, body=None, signals=None, tasks=None, note=None, category=None):
    v = _original_services[slug].copy()
    for k, value in dict(name=name, short=short, lead=lead, body=body, signals=signals, tasks=tasks, note=note, category=category).items():
        if value is not None: v[k] = value
    return v

def _new(slug,name,short,icon,category,lead,body,signals,tasks,note):
    return dict(slug=slug,name=name,short=short,icon=icon,category=category,
                lead=lead,body=body,signals=signals,tasks=tasks,note=note)

SERVICES = [
    _reuse('elektrik-ariza-tespiti-ve-tamiri',
        name='Elektrik Arıza Tespiti ve Tamiri',
        short='İzmit’te elektrik kesintisi, sigorta atması, priz ve tesisat sorunlarında yerinde arıza tespiti ve onarım.',
        lead='İzmit, Alikahya, Yuvam Akarca ve Yahya Kaptan’da 7/24 yerinde elektrik arıza tespiti ve tamiri. Günün her saati arayın; müdahale planını telefonda netleştirelim.',
        body='Evde, apartmanda veya iş yerinde ani elektrik kesintisi, atan sigorta, çalışmayan priz, yanık kokusu veya aydınlatma sorunu mu yaşıyorsunuz? Yuvam Elektrik’in 0532 711 36 77 numaralı hattını arayarak arızayı bildirebilirsiniz. Önce sorunun kapsamı ve adresiniz değerlendirilir; ardından müdahale uygunluğu hakkında bilgi verilir. Elektrik arızalarında güvenlik önceliğimizdir: tehlikeli tesisata müdahale etmeyin.',
        note='Duman, yangın veya elektrik çarpması riski varsa alandan uzaklaşın, 112’yi arayın. Gaz kokusu varsa elektrik anahtarlarına dokunmayın ve güvenli alandan gaz acil hattını arayın.'),
    _new('genel-elektrik-tamirleri','Genel Tamirler',
        'Ev, apartman ve iş yerlerinde küçük elektrik arızaları, bağlantı sorunları ve yerinde tamir işleri.',
        'bolt','Arıza ve bakım',
        'İzmit’te günlük hayatı aksatan elektrik kaynaklı küçük tamir ve onarım ihtiyaçlarına yerinde hizmet.',
        'Çalışmayan aydınlatma, gevşeyen priz, sorunlu bağlantı, arızalı düğme veya yıpranmış elektrik aksesuarları için çözüm üretmeden önce arızanın nedeni incelenir. Yuvam Elektrik, yapılan işe uygun malzeme ile onarım veya parça değişimini planlar. Birden fazla küçük işiniz varsa aramadan önce listelemeniz ziyaretin daha verimli planlanmasına yardımcı olur.',
        ['Odada bir aydınlatma noktası çalışmıyor','Priz veya anahtar arızası var','Mevcut bağlantının kontrol edilmesi gerekiyor','Birden fazla küçük elektrik işi aynı ziyarette yapılacak'],
        ['Arıza ve bağlantı kontrolü','Priz, anahtar ve aydınlatma onarımları','Arızalı ekipmanın uygun kapsamlı değişimi','İşlem sonrası temel çalışma kontrolü'],
        'Elektrik bağlantılarını enerjiyi güvenli şekilde ayırmadan açmayın veya onarmayın.'),
    _reuse('priz-anahtar-ve-salter-montaji', name='Anahtar Priz Montajı',
        short='Priz, anahtar ve şalter onarımı, değişimi ve yeni nokta montajı.'),
    _reuse('avize-armatur-ve-aplik-montaji', name='Aydınlatma Armatür ve Avize Montajı',
        short='Avize, aplik, tavan armatürü ve benzeri aydınlatmaların montaj ve bağlantıları.'),
    _reuse('led-spot-ve-ic-mekan-aydinlatma', name='LED Aydınlatma Montajı',
        short='LED, spot ve iç mekân ışıklandırmasında kurulum, yenileme ve bağlantı işleri.'),
    _reuse('dis-mekan-ve-cevre-aydinlatma', name='Dış Mekân Aydınlatma Montajı',
        short='Bahçe, bina önü, giriş, balkon ve ortak alan aydınlatmalarının montajı.'),
    _new('telefon-ve-internet-sistemleri-kurulumu','Telefon ve İnternet Sistemleri Kurulumu',
        'Daire ve bina içi telefon hattı, internet kablosu, data prizi ve bağlantı altyapısı.',
        'wifi','Telefon ve iletişim',
        'İzmit’te konut ve iş yerleri için telefon, internet ve ağ kablolaması konusunda yerinde destek.',
        'İnternetin belirli bir odada kullanılamaması, modem yerinin değişmesi, data prizi ihtiyacı veya bina içi telefon hattı yenilemesi gibi işler için Yuvam Elektrik’e ulaşabilirsiniz. Mevcut hatların durumu incelenerek kablo çekimi, soket ve priz bağlantısı, iç tesisat düzenlemeleri planlanır. İnternet operatörünün dış altyapısından veya abonelikten kaynaklanan arızalar ilgili sağlayıcının sorumluluğundadır.',
        ['Yeni odaya internet kablosu çekilecek','Data veya telefon prizi takılacak','Mevcut iç hat yenilenecek','Kablo bağlantısında kopukluk ya da temassızlık var'],
        ['İç mekân telefon hattı kablolaması','Ethernet/data kablosu çekimi','Data ve telefon prizi bağlantısı','Mevcut kablo ve konnektörlerin kontrolü'],
        'Telefon santrali kurulumu hizmet kapsamında değildir. İnternet servis sağlayıcısına ait dış hat ve abonelik işlemleri operatör tarafından yürütülür.'),
    _new('elektrik-tesisati-yenileme-ve-pano-tadilati','Elektrik Tesisatı Yenileme ve Pano Tadilatı',
        'Eski tesisatların yenilenmesi, dağıtım panolarının düzenlenmesi ve onarımı.',
        'panel','Tesisat ve pano',
        'İzmit’te ev, apartman, iş yeri ve ticari alanların tesisat yenileme ve pano tadilat talepleri.',
        'Eskimiş kablolar, kapasitesi yetersiz hatlar, düzensiz dağıtım panoları veya yeni kullanım ihtiyaçları güvenli bir tesisat değerlendirmesi gerektirir. Yuvam Elektrik, mevcut sistemi ve talep edilen değişiklikleri inceleyerek hat yenileme, pano düzenleme, sigorta ve bağlantı işleri için uygun uygulamayı planlar. Elektrik panolarında koruma elemanlarının gelişigüzel değiştirilmesi güvenlik riski doğurabilir.',
        ['Eski elektrik tesisatı yenilenecek','Pano içinde ısınma veya bağlantı sorunu var','Yeni kullanım için hat düzenlenecek','Mevcut dağıtım panosu yenilenecek'],
        ['Elektrik hattı kontrol ve yenilemesi','Pano tadilatı ve bağlantı düzenlemesi','Uygun sigorta ve koruma elemanı montajı','İş öncesi kapsam ve malzeme değerlendirmesi'],
        'Proje, onay, ölçüm raporu veya özel yetki gerektiren işler ilgili yetkili meslek mensuplarıyla yürütülmelidir.'),
    _reuse('uydu-anten-kurulum-ve-tamiri',name='Uydu Anten Tamiri ve Kurulumu',
        short='Çanak anten, LNB, kablo bağlantısı ve sinyal sorunlarında kurulum ve onarım.'),
    _new('tv-unitesi-ve-uydu-alicisi-kurulumu','TV Ünitesi ve Uydu Alıcısı Kurulumu',
        'Televizyon bağlantıları, uydu alıcısı kurulumu ve uygun duvar tipi TV ünitesi montajı.',
        'satellite','TV ve uydu',
        'İzmit’te televizyon, uydu alıcısı ve TV bağlantı düzeni için montaj desteği.',
        'Yeni televizyon veya uydu alıcısı takıldığında bağlantı kablolarının, anten hattının ve cihazların doğru şekilde düzenlenmesi gerekir. Yuvam Elektrik, TV ve uydu alıcısının uygun bağlantılarının tamamlanmasına, kabloların düzenlenmesine ve uygun duvar askı aparatı montajının değerlendirilmesine yardımcı olur. Mobilya imalatı veya geniş kapsamlı dekorasyon işleri bu hizmete dahil değildir.',
        ['Uydu alıcısı bağlanacak','Televizyon kabloları düzenlenecek','Uydu yayın bağlantısı kontrol edilecek','TV askı aparatı uygun duvara monte edilecek'],
        ['Uydu alıcısı bağlantısı ve ilk çalışma kontrolü','Anten kablosu kontrolü','Uygun duvar askı aparatı montajı','TV bağlantılarının ve kablolarının düzenlenmesi'],
        'Duvar tipinin ve askı aparatının televizyon ağırlığına uygunluğu montajdan önce değerlendirilmelidir.'),
    _reuse('sigorta-ve-kacak-akim-rolesi',name='Sigorta Tesisatı ve Tamiri',
        short='Sigorta arızası, sigorta kutusu, kaçak akım rölesi ve ilgili bağlantıların kontrolü.'),
    _new('panel-degisimi-ve-montaji','Panel Değişimi ve Montajı',
        'Arızalı LED aydınlatma panelleri ve uygun elektrik paneli bileşenlerinde değişim/montaj.',
        'panel','Aydınlatma ve pano',
        'İzmit’te panel tipi elektrik ve aydınlatma ekipmanlarının uygun kapsamda montajı ve yenilenmesi.',
        'Panel değişimi talebi farklı ürünleri ifade edebilir: LED aydınlatma paneli, yüzey tipi aydınlatma armatürü veya elektrik dağıtım panosuna ait bir parça. Telefonda panelin türünü belirtmeniz, mümkünse fotoğrafını paylaşmanız doğru hizmetin belirlenmesine yardımcı olur. Yuvam Elektrik ürün ve bağlantı uyumunu kontrol ederek uygun değişim ve montaj işlemlerini planlar.',
        ['LED panel yanmıyor veya titriyor','Eski aydınlatma paneli yenilenecek','Elektrik paneli bileşeni değişecek','Yeni panelin montajı isteniyor'],
        ['Panelin türünü ve mevcut bağlantısını inceleme','Uygun panel veya bileşen değişimi','Montaj ve elektrik bağlantısı','Temel çalışma ve güvenlik kontrolü'],
        'Elektrik dağıtım panolarına yalnızca ehil kişiler müdahale etmelidir; panelin türü işlem öncesinde kesinleştirilir.'),
    _reuse('goruntulu-diafon-ve-interkom',name='Görüntülü ve Sesli Diafon Sistemleri',
        short='Apartman ve dairelerde görüntülü/görüntüsüz diafon, iç ünite ve bağlantı işleri.'),
    _new('kombi-elektrik-baglantisi','Kombi Bağlantısı',
        'Kombinin elektrik beslemesi, uygun bağlantı noktası ve ilgili elektrik tesisatı işleri.',
        'plug','Cihaz bağlantıları',
        'Kombi için gereken elektrik bağlantısı ve besleme hattı düzenlemelerinde yerinde destek.',
        'Kombi yenilemelerinde veya kombinin yerinin değiştiği durumlarda elektrik bağlantısının uygunluğu önemlidir. Yuvam Elektrik, kombinin elektrik besleme noktası, bağlantı ve ilgili iç tesisat işlemlerini değerlendirir. Gaz tesisatı, baca, su bağlantısı ve cihazın ilk çalıştırılması üretici şartlarına ve ilgili yetkili servis uygulamalarına göre yürütülmelidir.',
        ['Kombi için elektrik prizi veya hat gerekiyor','Mevcut kombi elektrik bağlantısı sorunlu','Kombi yeri değiştiriliyor','Besleme hattının uygunluğu kontrol edilecek'],
        ['Elektrik besleme noktası kontrolü','Uygun elektrik hattı ve priz bağlantısı','Kombi enerji bağlantısı kapsamında elektrik işlemleri','İşlem sonrasında temel elektrik kontrolü'],
        'Doğalgaz, su ve baca bağlantısı ile kombi devreye alma işlemleri yetkili kuruluş veya servis gerektirir.'),
    _new('klima-kurulumu-elektrik-baglantisi','Klima Kurulumu',
        'Klima montajına hazırlık, elektrik hattı ve enerji bağlantısı çalışmalarında teknik destek.',
        'plug','Cihaz bağlantıları',
        'İzmit’te klima kurulumu için gerekli elektrik altyapısı ve cihaz besleme bağlantılarının hazırlanması.',
        'Yeni klima takılacağı zaman güvenli elektrik beslemesi, doğru koruma elemanları ve uygun kablo hattı önemlidir. Yuvam Elektrik, mevcut elektrik altyapısını değerlendirerek klima için gerekli enerji hattı, priz veya bağlantı noktası işlemlerini planlayabilir. Klima cihazının soğutucu akışkan hattı, vakum, gaz devresi ve yetkili servis gerektiren devreye alma işlemleri ayrıca uzman klima servisiyle yürütülür.',
        ['Yeni klima için elektrik hattı hazırlanacak','Klima beslemesi için ayrı hat gerekebilir','Eski bağlantı yenilenecek','Klima montajı öncesinde elektrik tesisatı kontrol edilecek'],
        ['Mevcut elektrik hattının uygunluk kontrolü','Gerekli enerji besleme hattının hazırlanması','Uygun priz ve koruma elemanı bağlantısı','Klima servisinin gerektirdiği elektrik altyapısı desteği'],
        'Klima gaz devresi ve soğutucu akışkan bağlantıları elektrik hizmeti kapsamında değildir; yetkili klima servisi gerektirir.'),
    _new('bina-ici-elektrik-tesisati','Bina İçi Elektrik Tesisatı',
        'Apartman, daire, merdiven ve ortak kullanım alanlarında elektrik tesisatı işleri.',
        'building','Tesisat ve pano',
        'İzmit’te binaların daire içi ve ortak alan tesisatları için bakım, yenileme ve uygulama desteği.',
        'Daireler, merdiven boşlukları, bina girişleri, depo ve ortak kullanım alanlarında elektrik ihtiyacı farklılaşabilir. Yuvam Elektrik, mevcut bina içi tesisatı değerlendirerek aydınlatma, kablo hattı, anahtar-priz, dağıtım ve bağlantı işlerini planlar. Ortak alan uygulamalarında bina yönetiminin onayı, yeni projelerde ise ilgili teknik şartlar dikkate alınır.',
        ['Apartman ortak alanında elektrik arızası var','Merdiven aydınlatması yenilenecek','Daire içi hat veya priz düzeni değişecek','Bina içinde ek elektrik noktası gerekiyor'],
        ['Bina içi elektrik hattı değerlendirmesi','Daire ve ortak alan kablolama işleri','Aydınlatma ve bağlantı montajı','İhtiyaca göre tesisat yenileme desteği'],
        'Ortak tesisata müdahalelerde yönetim onayı ve gerekli teknik yetkiler dikkate alınmalıdır.'),
    _new('kompanzasyon-panosu-ve-bakimi','Kompanzasyon Panosu ve Bakımı',
        'Ticari tesislerde kompanzasyon panosu ve ilgili elektrik bileşenlerinin kontrolü ve bakımı.',
        'panel','Ticari ve kurumsal',
        'Fabrika, şantiye ve ticari işletmelerin kompanzasyon panosu ihtiyaçlarında teknik inceleme.',
        'Elektrik tesislerinin güç faktörü düzenlemesinde kullanılan kompanzasyon panoları, işletmenin enerji kullanımı açısından önemlidir. Yuvam Elektrik, kompanzasyon panosundaki arıza, bakım ve yenileme taleplerinin kapsamını değerlendirir. Gerekli ölçüm, proje, işletme sorumluluğu veya özel yetki gerektiren işlemler ilgili yetkin uzmanlarla birlikte yürütülmelidir.',
        ['Kompanzasyon panosunda uyarı veya arıza var','Pano bileşenlerinin bakım ihtiyacı bulunuyor','Ticari tesis elektrik sistemi değerlendirilecek','Mevcut panoda tadilat planlanıyor'],
        ['Kompanzasyon panosu ön incelemesi','Bileşen ve bağlantı değerlendirmesi','Bakım ve yenileme planlaması','Gerekli yetki ve ölçüm ihtiyaçlarının belirlenmesi'],
        'Enerjili pano üzerinde işlem, uzman gözetimi ve gerekli iş güvenliği prosedürleri olmadan yapılmamalıdır.'),
    _new('ticari-alan-elektrik-bakim-taahhut','Ticari Alan Elektrik Bakım ve Taahhüt',
        'Fabrika, iş yeri, şantiye, restoran ve ticari yapılarda elektrik ağları, pano ve bakım işleri.',
        'building','Ticari ve kurumsal',
        'Kocaeli’de ticari işletmelerin elektrik tesisatı, bakım, uygulama ve taahhüt taleplerine yönelik çözümler.',
        'Fabrikalar, iş yerleri, şantiyeler, restoranlar ve diğer ticari alanlar farklı elektrik ihtiyaçlarına sahiptir. Yuvam Elektrik, pano kurulum ve tadilatı, tesisat, elektrik besleme hatları, makine enerji bağlantıları, kontrol ve planlı bakım konularındaki talepleri işin kapsamına göre değerlendirir. İşin büyüklüğü ve gerektirdiği teknik yetkiler baştan görüşülerek uygulama planı oluşturulur. İzmit dışındaki Kocaeli lokasyonlarında hizmet koşulları telefonla netleştirilir.',
        ['Yeni iş yeri elektrik tesisatı kurulacak','Şantiyede veya fabrikada elektrik bakım ihtiyacı var','Makine elektrik besleme bağlantısı planlanıyor','İşletme elektrik panoları yenilenecek'],
        ['Elektrik altyapı ve pano işleri','Makine enerji besleme hattı değerlendirmesi','Planlı elektrik bakım ve onarım','İş kapsamı, malzeme ve keşif görüşmesi'],
        'Resmî proje, elektrik mühendisliği, test raporu veya özel yetki gerektiren kısımlar ilgili yetkili profesyonellerce yürütülmelidir.'),
    _reuse('kamera-sistemi-montaji', name='Kamera ve Güvenlik Sistemleri',
        short='İş yeri, konut ve ortak alanlarda kamera sistemi bağlantı ve montajı.',
        category='Ticari ve kurumsal'),
]

REGIONS = [
 ('Yuvam Akarca','Ev ve iş yerlerine yerinde elektrik arıza, bakım ve montaj servisimizin öncelikli bölgesi.'),
 ('Alikahya Fatih','Yuvam Akarca Toplu Konutları ve çevresinde elektrik hizmetleri.'),
 ('Alikahya','Alikahya merkez ve mahallelerinde elektrik arıza ve montaj işleri.'),
 ('Yahya Kaptan','Konut, apartman ve iş yerlerinde elektrik bakım ve montaj.'),
 ('Fevzi Çakmak','İzmit içinde yakın hizmet bölgelerinden biri.'),
 ('Karadenizliler','İzmit içindeki elektrik arıza ve montaj talepleri.'),
 ('İzmit Merkez','İzmit’in diğer mahallelerinde konuma ve müsaitliğe göre servis.'),
 ('Kocaeli Diğer İlçeler','Kocaeli genelinde hizmet talepleri işin kapsamı, konum ve müsaitliğe göre görüşülür.'),
]

FAQS = [
 ('Yuvam Elektrik hangi bölgelere hizmet veriyor?', 'İzmit’te Yuvam Akarca, Alikahya ve Yahya Kaptan başta olmak üzere ev, apartman ve iş yerlerine yerinde elektrik servisi sunuyoruz. Kocaeli’nin diğer ilçelerindeki talepler için konum ve servis uygunluğunu telefonda görüşüyoruz.'),
 ('7/24 elektrik arızası ve diğer elektrik işleri için hizmet alabilir miyim?', 'Evet. Kocaeli Yuvam Elektrik haftanın 7 günü 24 saat elektrik arıza, bakım ve montaj hizmeti sunar. 0532 711 36 77 numarasından günün her saati ulaşabilirsiniz. İşin türüne ve konumuna göre yerinde servis planını telefonda netleştiriyoruz.'),
 ('Telefon numaranız nedir?', 'Bayram Canseven – Yuvam Elektrik: 0532 711 36 77. Acil elektrik arızası, bakım, montaj ve keşif talepleriniz için arayabilirsiniz.'),
 ('Dükkâna gelerek hizmet alabilir miyim?', 'Hayır. Artık fiziksel dükkânda müşteri kabul etmiyoruz. Elektrik arıza, bakım ve montaj hizmetlerini evinizde veya iş yerinizde, randevu ve servis uygunluğuna göre sunuyoruz.'),
 ('Priz değişimi, avize ve LED montajı yapıyor musunuz?', 'Evet. Priz, anahtar, şalter, avize, aydınlatma armatürü, LED ve dış mekân aydınlatma montajı hizmetlerimiz arasındadır.'),
 ('Kombi ve klima ile ilgili hangi işleri yapıyorsunuz?', 'Kombi ve klima cihazlarının elektrik besleme hattı ve bağlantı ihtiyaçları için destek veriyoruz. Doğalgaz bağlantısı, baca, soğutucu akışkan devresi ve ilgili cihaz devreye alma işleri yetkili servis kapsamındadır.'),
 ('TV ünitesi ve uydu alıcısı kuruyor musunuz?', 'Evet. Uygun duvar askı aparatı ve TV bağlantıları, uydu alıcısı kurulumu, uydu anten kontrolü ve kablo bağlantıları için arayabilirsiniz. Mobilya imalatı veya dekorasyon hizmeti sunmuyoruz.'),
 ('Elektrik sigortası sürekli atıyorsa ne yapmalıyım?', 'Şalter veya kaçak akım rölesi tekrar tekrar atıyorsa koruma elemanını devre dışı bırakmayın, nedenini kontrol ettirmek için elektrikçi çağırın.'),
 ('Hizmet fiyatını telefonla öğrenebilir miyim?', 'Sorunun türü ve bulunduğunuz mahalle üzerinden ön bilgi alabilirsiniz. Nihai ücret malzeme ihtiyacı, arıza kapsamı ve yerinde değerlendirmeyle belirlenir.'),
 ('Ticari işletmelere de hizmet veriyor musunuz?', 'Evet. Fabrika, şantiye, restoran ve iş yerlerinde elektrik panosu, kompanzasyon, enerji bağlantısı, arıza-bakım ve kamera sistemleri gibi talepleri kapsamına göre değerlendiriyoruz.'),
 ('Kamera ve diafon sistemi işleri yapıyor musunuz?', 'Evet. Görüntülü ve sesli diafon sistemleri ile uygun kamera ve güvenlik sistemi bağlantı, montaj ve bakım talepleri için bize ulaşabilirsiniz.'),
]

HOMEPAGE_SECTION_COPY = {
 'hero_eyebrow':'İZMİT • ALİKAHYA • YUVAM AKARCA',
 'hero_title':'İzmit’te elektrikçi mi arıyorsunuz? Evinize ve iş yerinize geliyoruz.',
 'hero_text':'Kocaeli Yuvam Elektrik; İzmit, Alikahya, Yuvam Akarca ve Yahya Kaptan çevresinde ev ve iş yerlerine haftanın 7 günü, 24 saat yerinde elektrik servisi sunar. Elektrik arızası, tesisat bakımı, sigorta, priz ve avize montajı için 7/24 arayabilirsiniz. Müdahale ve ziyaret planı konuma ve işin kapsamına göre görüşülür.',
 'about_title':'İzmit’te evinizin ve iş yerinizin elektrik çözüm ortağı.',
 'about_text':'Kocaeli Yuvam Elektrik, yıllardır İzmit ve çevresine hizmet veren yerel bir elektrik işletmesidir. Yuvam Akarca, Alikahya ve Yahya Kaptan başta olmak üzere ev, apartman ve iş yerlerine adresinde servis sunar; dükkânda müşteri kabul etmez. Elektrik arıza, bakım, tesisat, montaj, pano ve uygun kapsamlı ticari işler için önce ihtiyacı dinler, sonra hizmet ve randevu planını netleştirir.',
 'price_text':'Elektrik arıza ve montaj hizmetlerinde ücret; arızanın niteliği, kullanılacak malzemeler, tesisatın mevcut durumu ve işin kapsamına göre değişir. 0532 711 36 77 numarasını arayarak ön bilgi alabilir, gerekli durumlarda yerinde inceleme sonrası net teklif isteyebilirsiniz.'
}
