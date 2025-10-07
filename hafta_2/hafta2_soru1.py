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
print(o1.konus())

# Getter - Setter testleri
print("Öğrencinin okul numarası:", o1.get_okul_no())
o1.set_okul_no(456)
print("Güncellenmiş okul numarası:", o1.get_okul_no())

print("Hoca'nın yaşı:", h1.get_yas())
h1.set_yas(36)
print("Güncellenmiş yaş:", h1.get_yas())
