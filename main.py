# 11
class Oqituvchi:
    def __init__(self, ism, fan, tajriba):
        self.ism = ism
        self.fan = fan
        self.tajriba = tajriba

    def malumot(self):
        return self.ism, self.fan, self.tajriba

    def tajriba_oshir(self, yil):
        self.tajriba += yil


# 12
class Mahsulot:
    def __init__(self, nom, narx):
        self.nom = nom
        self.narx = narx

class Supermarket:
    def __init__(self):
        self.mahsulotlar = []

    def mahsulot_qosh(self, mahsulot):
        self.mahsulotlar.append(mahsulot)

    def arzon_mahsulot(self):
        return min(self.mahsulotlar, key=lambda m: m.narx).nom


# 13
class Televizor:
    def __init__(self, brend, ovoz=10, kanal=1):
        self.brend = brend
        self.ovoz = ovoz
        self.kanal = kanal

    def ovoz_oshir(self, q):
        self.ovoz += q

    def kanal_ozgartir(self, k):
        self.kanal = k


# 14
class Osimlik:
    def __init__(self, nom, turi):
        self.nom = nom
        self.turi = turi

class Bog:
    def __init__(self):
        self.osimliklar = []

    def osimlik_qosh(self, osimlik):
        self.osimliklar.append(osimlik)

    def tur_osimliklari(self, turi):
        return [o.nom for o in self.osimliklar if o.turi == turi]


# 15
class Sayohatchi:
    def __init__(self, ism):
        self.ism = ism
        self.manzillar = []

    def manzil_qosh(self, manzil):
        self.manzillar.append(manzil)

    def sayohatlar_soni(self):
        return len(self.manzillar)
