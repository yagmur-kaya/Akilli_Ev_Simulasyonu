# Akıllı Ev Simülasyonu 
Bu projeyi nesne tabanlı programlama (OOP) öğrenmeye başladığım zaman pratik yapmak amacıyla yazdım. 
Akıllı ev simülasyonu yaparken perde,klima ve fırını  kontrol etmeyi amaçladım.Tabii ki daha öğrenme aşamasında olduğum için çok fazla özellik ekleyemedim kendimi geliştirdikçe daha fazla parametre ve fonksiyon eklemeyi düşünüyorum
## Cihazlar
 Klima: 
-Derece ayarlayabilir
 -Derece gösterebilir
Perde:
-Açma,kapatma ve yarıya indirme işlemlerini yapabilir.
Fırın:
-Sıcaklık ayarlama yapabilir.
-Sıcaklık gösterme yapabilir.
-Pişirme modu (alt üst,fanlı,grill,buz çözme) seçebilir.
Süre belirleyebilir.
 ## Amaç
Bu proje sayesinde:
- Python'da sınıf yapısı ve kalıtımı pekiştirdim.
- Gerçek dünya senaryolarını kodla modellemeyi öğrendim.
- GitHub üzerinden projelerimi paylaşma pratiği kazandım.
#Örnek kullanım 
klima_=klima()
print(klima_.derece_ayarla(22))
print(klima_.derece_goster()) 

perde_=perde()
perde_.yariya_indir()
perde_.durum_goruntule()
print(perde_.durum_goruntule())

firin_=firin()
firin_.ac()
firin_.sicaklik_ayarla(180)
firin_.fanli_()
firin_.sicaklik_goster(25)


print(firin_.sicaklik_ayarla(220))
print(firin_.sicaklik_goster(25))
print(firin_.grill_())
print(firin_.buz_cozme())
print(firin_.pisir(30))
