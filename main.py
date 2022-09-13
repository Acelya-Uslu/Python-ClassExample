class Araba():
    marka = "Renault"
    renk="Kırmızı"
    fiyat=50.000
    model="Clio"

    def bilgileriYazdır(self): # objenin adı ne olursa olsun self atansın diyoruz
        print(self.marka , self.fiyat, self.renk)


araba=Araba()
print(araba.fiyat)
print(araba.model)
print(araba.renk)

#Bir sınıftan  obje türettiğim zaman init fonksiyonu tetikleniyor.


print("*****************")
araba.bilgileriYazdır()