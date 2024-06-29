class OngkosKirim:
    def __init__(self, panjang, lebar, tinggi, berat):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
        self.berat = berat
        self.standar_harga = 5000
        self.min_volume = 50

    def hitung_volume(self):
        return self.panjang * self.lebar * self.tinggi

    def hitung_harga(self):
        volume = self.hitung_volume()
        if volume < self.min_volume:
            volume = self.min_volume
        return self.standar_harga * self.berat

# Input
panjang = 5
lebar = 2
tinggi = 4
berat = 1

ongkoskirim = OngkosKirim(panjang, lebar, tinggi, berat)
harga = ongkoskirim.hitung_harga()
print("Harga: Rp", harga)