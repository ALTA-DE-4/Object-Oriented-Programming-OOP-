class Kalkulator:
    def __init__(self):
        pass

    def penjumlahan(self, a, b):
        return a + b

    def pengurangan(self, a, b):
        return a - b

    def perkalian(self, a, b):
        return a * b

    def pembagian(self, a, b):
        if b == 0:
            return "pilih angka lain"
        else:
            return a / b


kalkulator = Kalkulator()

hasil_penjumlahan = kalkulator.penjumlahan(3, 4)
hasil_pengurangan = kalkulator.pengurangan(15, 4)
hasil_perkalian = kalkulator.perkalian(10, 10)
hasil_pembagian = kalkulator.pembagian(12, 3)

# Menampilkan hasil
print("Penjumlahan:", hasil_penjumlahan)
print("Pengurangan:", hasil_pengurangan)
print("Perkalian:", hasil_perkalian)
print("Pembagian:", hasil_pembagian)

