# Konstruksi kelas abstrak
from abc import ABC, abstractmethod

# Mengambil nilai pi dari modul math
from math import pi

# Membuat kelas dasar bangun 2 dimensi (bangun datar)
# dimana setiap kelas yang menggunakan induk kelas bangun 2 dimensi
# wajib mendefinisikan perhitungan luas dan keliling
class Bangun2D(ABC):
    @abstractmethod
    def luas(self):
        pass

    @abstractmethod
    def keliling(self):
        pass

class Persegi(Bangun2D):
    def __init__(self, sisi = 0):
        self.sisi = sisi

    def luas(self):
        print("Luas Persegi:", (self.sisi * self.sisi))
    
    def keliling(self):
        print("Keliling Persegi:", (4 * self.sisi))

class Lingkaran(Bangun2D):
    def __init__(self, r):
        self.r = r
    
    def luas(self):
        print("Luas Lingkaran:", (pi * self.r**2))

    def keliling(self):
        print("Keliling Lingkaran:", (2 * pi * self.r))

lingkaran = Lingkaran(20)
lingkaran.keliling()
