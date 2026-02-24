class Makanan:
    def __init__(self,nama, rasa, harga):
        self.nama=nama
        self.rasa=rasa
        self.harga=harga
    def deskripsi(self):
        print(self.nama, self.rasa, self.harga)
    def rasaMakanan(self):
        print("rasanya", self.rasa, "sekali")
    def changeHarga(self, new_harga):
        self.harga=new_harga
        print("harga di diskon jadi", self.harga)
m1=Makanan("ayam", "enak", 10000)
m1=Makanan("dendeng", "lezat", 5000)
m1=Makanan("rendang", "enakkk", 12000)
m1.deskripsi()
m1.rasaMakanan()
m1.changeHarga(5000)


