class Araba():
    def __init__(self,marka,fiyat,renk):
        self.gelenMarka=marka
        self.gelenFiyat=fiyat
        self.gelenRenk=renk

    def bilgileriYazdır(self):
        print(self.gelenMarka,self.gelenFiyat, self.gelenRenk)


araba1=Araba("reno",50,"mavi")
araba2=Araba("fiat",30,"kırmızı")

araba1.bilgileriYazdır()
