# Soru-1
# Araba adlı iki parametre alan bir tane de fonksiyonu olan bir sınıf yazdık
class Araba:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

    def bilgileri_yazdir(self):
        print(f"Marka: {self.marka}, Model: {self.model}")


# Kullanım
araba1 = Araba("Toyota", "Corolla")
araba1.bilgileri_yazdir()


# Soru-2
class Dikdortgen:
    def __init__(self, uzunluk, genislik):
        self.uzunluk = uzunluk
        self.genislik = genislik

    def alanhesapla(self):
        print(self.uzunluk * self.genislik)


diktortgen1 = Dikdortgen(15, 20)
diktortgen1.alanhesapla()


# Soru-3
class Kare:
    def __init__(self, kenar):
        self.kenar = kenar

    # J satır I sutun parametreleri
    def kenaryazdir(self):
        for i in range(self.kenar):
            for j in range(self.kenar):
                if (j == 0) or (j == (self.kenar - 1)):
                    print("*", end="")
                elif (i == 0) or (i == self.kenar - 1):
                    print("*", end="")
                else:
                    print(" ", end="")
            print()


kare1 = Kare(5)
kare1.kenaryazdir()


# Soru-4
class HesapMakinesi:
    def topla(self, sayi1, sayi2, sayi3=None):
        if sayi3 is not None:
            return sayi1 + sayi2 + sayi3
        else:
            return sayi1 + sayi2


# HesapMakinesi sınıfından bir nesne oluşturma
hesap_makinesi = HesapMakinesi()

# İki sayı ile toplama
sonuc1 = hesap_makinesi.topla(10, 20)
print("İki sayının toplamı:", sonuc1)

# Üç sayı ile toplama
sonuc2 = hesap_makinesi.topla(10, 20, 30)
print("Üç sayının toplamı:", sonuc2)


# Soru-5
class Merhaba:
    def merhaba_yazdir(self):
        print("Merhaba Dünya")


# Merhaba sınıfından bir nesne oluşturma ve metodu çağırma
merhaba = Merhaba()
merhaba.merhaba_yazdir()

