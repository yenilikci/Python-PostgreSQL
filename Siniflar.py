from veritabani import *

class Siniflar():

    def __init__(self):
        self.sinifAdi = ""
        self.sinifSube = ""

    def sinifEkle(self):
        print("\n---------- [Sınıf Ekle] ----------")
        sinifAdi = input("Sınıf Adı: ")
        sinifSube = input("Sınıf Şube: ")
        sinifSql = "INSERT INTO siniflar(sinifadi,sinifsube) VALUES ('{}','{}')".format(sinifAdi,sinifSube)
        sinifEklemeIslemi = db.cursor()
        sinifEklemeIslemi.execute(sinifSql)
        db.commit()
