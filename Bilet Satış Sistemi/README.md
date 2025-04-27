
# Etkinlik ve Bilet Satış Sistemi

Bu proje, Python'un Tkinter kütüphanesini kullanarak geliştirilen basit bir etkinlik ve bilet satış platformudur.  
Kullanıcılar etkinlikler oluşturabilir, bu etkinliklere bilet alabilir ve bilet satın alan kişileri görüntüleyebilir.



##  Proje Özellikleri

- Etkinlik ekleme (Ad, Tarih, Mekan, Bilet sayısı ile)
- Mevcut etkinlikleri listeleme
- Etkinliklere bilet satın alma (Kullanıcı adı ve bilet adedi ile)
- Bilet alan kişileri listeleme
- Kalan bilet sayılarını yönetme
- Kullanıcı dostu basit Tkinter arayüzü


##  Kurulum

1. Python 3 kurulu olduğundan emin olun.
2. Tkinter kütüphanesi Python ile birlikte gelir, ekstra yüklemeye gerek yoktur.
3. Proje dosyasını `.py` uzantısıyla bilgisayarınıza kaydedin.



## Kullanım

Terminal veya Komut İstemi'nde çalıştırabilirsiniz:


python bilet_satis_sistemi.py


Program açıldığında karşınıza 5 adet buton çıkacaktır:

| Buton                  | Görevi |
|-------------------------|--------|
| **Etkinlik Ekle**        | Yeni etkinlik oluşturur. |
| **Bilet Satın Al**       | Var olan etkinliklerden bilet satın almanızı sağlar. |
| **Etkinlikleri Göster**  | Tüm etkinlikleri ve kalan bilet sayılarını listeler. |
| **Bilet Alanları Göster**| Seçilen etkinlikte kimlerin bilet aldığı gösterilir. |
| **Çıkış**                | Programdan güvenli şekilde çıkış yapar. |

---

## Program Akışı

1. Öncelikle bir etkinlik eklenir. (Ad, tarih, mekan, bilet sayısı girilir.)
2. Daha sonra bir etkinlik seçilir ve kaç bilet alınmak istendiği girilir.
3. Satın alma başarılı olursa kalan bilet sayısı azalır.
4. İstenirse bilet alan kullanıcılar görüntülenebilir.



## Notlar

- Eğer istenenden az bilet kaldıysa sistem hata mesajı verir.
- Bir etkinlikte biletler biterse daha fazla satış yapılamaz.
- Bu proje öğrenme ve geliştirme amaçlı sade bir şekilde tasarlanmıştır.



## Lisans

Bu proje herhangi bir lisans kısıtlaması olmaksızın eğitim ve kişisel kullanım için serbesttir.


