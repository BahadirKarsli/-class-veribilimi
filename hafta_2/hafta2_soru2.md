# Soru 1

**Soru:** Hangisi ile fonksiyon oluşturulur?

    __init__ fonksiyon1():
    func fonksiyon1():
    def fonksiyon1():
    const fonksiyon1():
    class fonksiyon1():

**Cevap:**\
`def fonksiyon1():`

------------------------------------------------------------------------

# Soru 2

**Soru:** Aşağıdaki işlemlerin tür dönüşümü sonrası matematiksel
işlemlerde kullanılabilmesi ve tam sayı değer vermesi için boş bırakılan
yerlere ne gelmelidir?

``` python
a = .......................(input("vize notunuzu girin = "))
```

**Cevap:**\
`int(...)`

------------------------------------------------------------------------

# Soru 3

**Soru:** Aşağıdakilerden hangisi karar yapılarında kullanılan
deyimlerden birisi değildir?

    while
    continue
    if... :  elif....:  else:
    break
    def

**Cevap:**\
`def`

------------------------------------------------------------------------

# Soru 4 - Kavramlar

## Encapsulation (Kılıflama-Sarmalama) Nedir?

Encapsulation (kapsülleme), bir sınıfın verilerini dışarıdan doğrudan 
erişime kapatıp sadece belirli metotlar aracılığıyla erişilmesini sağlayarak 
veriyi koruma ilkesidir.

## Inheritance (Kalıtım) Nedir?

Inheritance (kalıtım), bir sınıfın başka bir sınıfın özelliklerini ve davranışlarını 
devralarak kod tekrarını azaltmasını ve yeniden kullanılabilirliği sağlamasını ifade eder.

------------------------------------------------------------------------
# Soru 5 - Hoca ve Öğrenci Sınıfı
Bu sınıflar arasında **inheritence**, **metotlara aşırı yüklenme**, **ezme**, **çok biçimlilik (polymorphism)** dahil tüm nesne tabanlı prensipleri gösteriniz.
```python
class Insan:
    def __init__(self, isim: str, yas: int, cinsiyet: str):
        self.isim = isim
        self.__yas = yas       # private (encapsulation)
        self.cinsiyet = cinsiyet

    # getter & setter (yas için)
    def get_yas(self):
        return self.__yas

    def set_yas(self, yeni_yas):
        if yeni_yas > 0:
            self.__yas = yeni_yas
        else:
            print("Yaş 0'dan küçük olamaz!")

    def bilgi_ver(self):
        return f"İsim: {self.isim}, Yaş: {self.__yas}, Cinsiyet: {self.cinsiyet}"


class Hoca(Insan):
    def __init__(self, isim, yas, cinsiyet, brans: str):
        super().__init__(isim, yas, cinsiyet)
        self.brans = brans

    # Polymorphism: Hoca için konus()
    def konus(self):
        return f"{self.isim} adlı hoca {self.brans} dersini anlatıyor."

class Ogrenci(Insan):
    def __init__(self, isim, yas, cinsiyet, sinif: str, okul_no: int):
        super().__init__(isim, yas, cinsiyet)
        self.sinif = sinif
        self.__okul_no = okul_no   # private (encapsulation)

    # getter & setter (okul_no için)
    def get_okul_no(self):
        return self.__okul_no

    def set_okul_no(self, yeni_no):
        if yeni_no > 0:
            self.__okul_no = yeni_no
        else:
            print("Okul numarası 0 veya negatif olamaz!")

    def katil(self):
        return f"{self.isim} adlı öğrenci {self.sinif} sınıfında derse katılıyor."

    # Polymorphism: Öğrenci için konus()
    def konus(self):
        return f"{self.isim} adlı öğrenci derste soru soruyor."
# İnsan nesnesi
i1 = Insan("Ahmet", 40, "Erkek")

# Hoca nesnesi
h1 = Hoca("Ayşe", 35, "Kadın", "Matematik")

# Öğrenci nesnesi
o1 = Ogrenci("Mehmet", 18, "Erkek", "12-A", 123)

# Bilgi verme
print(i1.bilgi_ver())
print(h1.bilgi_ver())
print(o1.bilgi_ver())

# Hoca konuşsun
print(h1.konus())

# Öğrenci katılsın ve konuşsun
print(o1.katil())
```

------------------------------------------------------------------------
# Soru 6 - Çalışan Sınıfları

Abstract sınıflar için `abc` modülünü
kullanıyoruz.
```python
from abc import ABC, abstractmethod

# Soyut Sınıf
class Ozgecmis(ABC):
    @abstractmethod
    def doldur(self):
        pass

# Ata Sınıf
class Calisan(Ozgecmis):
    def __init__(self, isim, soyisim):
        self.isim = isim
        self.soyisim = soyisim

    def doldur(self):
        print(f"{self.isim} {self.soyisim} için özgeçmiş dolduruluyor.")

# Alt Sınıflar
class MaviYaka(Calisan):
    def __init__(self, isim, soyisim):
        super().__init__(isim, soyisim)
        self.vardiya_sayisi = 3

    def calis(self):  # Metot ezme (Overriding)
        print("Mavi yaka fabrikada çalışıyor.")

class BeyazYaka(Calisan):
    def __init__(self, isim, soyisim):
        super().__init__(isim, soyisim)
        self.vardiya_sayisi = 2

    def calis(self):  # Metot ezme (Overriding)
        print("Beyaz yaka ofiste çalışıyor.")

# Nesne Türetme
mavi_yaka1 = MaviYaka("Mehmet", "Öztürk")
beyaz_yaka1 = BeyazYaka("Sıla", "Yılmaz")

# Kullanım
print("--- Çalışanlar ---")
mavi_yaka1.doldur()
mavi_yaka1.calis()
print(f"Vardiya sayısı: {mavi_yaka1.vardiya_sayisi}")

print("\n--- Çalışanlar ---")
beyaz_yaka1.doldur()
beyaz_yaka1.calis()
print(f"Vardiya sayısı: {beyaz_yaka1.vardiya_sayisi}")
```
