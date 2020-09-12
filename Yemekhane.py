from veritabani import *

class Yemekhane():

    def __init__(self):
        self.yemekAdi = ""
        self.yemekFiyati = ""
        
    def menuyeYemekEkle(self):
        print("\n---------- [Menüye Yemek Ekle] ----------")
        yemekAdi = input("Yemek Adı: ")
        yemekFiyati = input("Yemek Fiyati: ")
        yemekSql = "INSERT INTO yemekhanemenu(yemekadi,yemekfiyat) VALUES ('{}','{}')".format(yemekAdi,yemekFiyati)
        yemekEklemeIslemi = db.cursor()
        yemekEklemeIslemi.execute(yemekSql)
        db.commit()