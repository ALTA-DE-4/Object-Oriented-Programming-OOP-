class BangunRuang:
    def __init__(self):
        pass

    def hitung_volume(self):
        pass

class Kubus(BangunRuang):
    def __init__(self, sisi):
        self.sisi = sisi

    def hitung_volume(self):
        return self.sisi**3

class Balok(BangunRuang):
    def __init__(self, panjang, lebar, tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi

    def hitung_volume(self):
        return self.panjang * self.lebar * self.tinggi

class Tabung(BangunRuang):
    def __init__(self, jari_jari, tinggi):
        self.jari_jari = jari_jari
        self.tinggi = tinggi

    def hitung_volume(self):
        return 22/7 * self.jari_jari**2 * self.tinggi

# Input langsung di dalam kode
sisi_kubus = 10
panjang_balok = 3
lebar_balok = 6
tinggi_balok = 10
jari_jari_tabung = 7
tinggi_tabung = 10

kubus = Kubus(sisi_kubus)
balok = Balok(panjang_balok, lebar_balok, tinggi_balok)
tabung = Tabung(jari_jari_tabung, tinggi_tabung)

volume_kubus = kubus.hitung_volume()
volume_balok = balok.hitung_volume()
volume_tabung = tabung.hitung_volume()

print("\nOutput:")
print("Volume")
print(f"Kubus: {volume_kubus}")
print(f"Balok: {volume_balok}")
print(f"Tabung: {volume_tabung}")
