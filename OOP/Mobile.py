class Mobile:
    """
    Class adalah cetakan, template atau blue print untuk membuat sebuah object.
    """
    def __init__(self, tipe, roda, kecepatan):
        # Konstruktor dari class Mobile
        self.tipe = tipe
        self.roda = roda
        self.kecepatan = kecepatan
    
    def melaju(self):
        print("Melaju dengan kecepatan:", self.kecepatan, "km/jam")
    
    def klakson(self):
        print("Pim .... Pim .... Pim ...")
    
    def berbelok(self, belok):
        print("Berbelok ke", belok)

mobileWuling = Mobile("sedan", 4, 200)
mobileWuling.melaju()
mobileWuling.klakson()
mobileWuling.berbelok("Kanan")
print("Tipe mobile", mobileWuling.tipe)
