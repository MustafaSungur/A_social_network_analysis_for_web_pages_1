# A_social_network_analysis_for_web_pages_1

* Dokuz Eylül Üniversitesi web sayfalarına yönelik bir sosyal ağ analizi ve bu sonuçların görselleştirmesi yapıldı. 
* https://www.deu.edu.tr/ana sayfası ve altındaki tüm sayfalar ve buradaki tüm veriler kapsamdadır.
* Sözcük (özel ad, eylem, nesne, kavram, vb. hepsi olabilir) bazlı frekans analizi 	yapıldı; her sözcüğün ilgili
tüm sayfalarda toplam kaç kere geçtiği (frekansı) ve 	kaç farklı web sayfasında geçtiği gösterildi.
* Bu analizler sonucu tüm sözcükler frekans değerine göre en yüksekten en düşüğe tabloda sıralananıp sonuc.csv dosyasına kaydedildi.
* Bu analize ilişkin sonuçlar, veri görselleştirmesi yapılarak uygun bir grafik oluşturulup Grafiks dosaysına ekran görüntüleri mevcuttur.

* !! Sitelerden Kelimeleri çekmek ve ayıklamak çoz uzun sürüyor. Bunun için soru_1.py dosyasındaki yorum satırına alınmış kısım da kelimeleri ayıkladıktan sonra
zemberek kütüphanesi ile köklerine ayırdım. köklerine ayrılan kelimeler içinde ki stop words'leri filtreledikten sonra Words klasörü içinde ki text dosyalarına yazdırdım. 
* Her bir text dosyası farklı sayfalardan alnın kelimelerdir.
* Frekansları, kelimeleri text dosyalarından çekerek hesapladım.
