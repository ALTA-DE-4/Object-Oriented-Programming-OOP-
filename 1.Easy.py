class BangunDatar:
    def __init__(self, sisi1, sisi2=None):
        self.sisi1 = sisi1
        self.sisi2 = sisi2

    def hitung_luas(self):
        pass

    def hitung_keliling(self):
        pass

class Persegi(BangunDatar):
    def __init__(self, sisi):
        super().__init__(sisi)

    def hitung_luas(self):
        return self.sisi1**2

    def hitung_keliling(self):
        return 4 * self.sisi1

class Segitiga(BangunDatar):
    def __init__(self, alas, tinggi):
        super().__init__(alas, tinggi)

    def hitung_luas(self):
        return 0.5 * self.sisi1 * self.sisi2

    def hitung_keliling(self):
        return self.sisi1 + self.sisi2 + (self.sisi1**2 + self.sisi2**2)**0.5

class PersegiPanjang(BangunDatar):
    def __init__(self, panjang, lebar):
        super().__init__(panjang, lebar)

    def hitung_luas(self):
        return self.sisi1 * self.sisi2

    def hitung_keliling(self):
        return 2 * (self.sisi1 + self.sisi2)

# Luas
persegi = Persegi(4)
luas_persegi = persegi.hitung_luas()
print("Output:")
print("Luas")
print("Persegi: ", luas_persegi)

segitiga = Segitiga(3, 4)
luas_segitiga = segitiga.hitung_luas()
print("Segitiga: ", luas_segitiga)

persegi_panjang = PersegiPanjang(7, 8)
luas_persegi_panjang = persegi_panjang.hitung_luas()
print("Persegi Panjang: ", luas_persegi_panjang)

# Keliling
persegi = Persegi(4)
keliling_persegi = persegi.hitung_keliling()
print("Keliling")
print("Persegi: ", keliling_persegi)

segitiga = Segitiga(3, 4)
keliling_segitiga = segitiga.hitung_keliling()
print("Segitiga: ", keliling_segitiga)

persegi_panjang = PersegiPanjang(7, 8)
keliling_persegi_panjang = persegi_panjang.hitung_keliling()
print("Persegi Panjang: ", keliling_persegi_panjang)
