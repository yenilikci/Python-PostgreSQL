from veritabani import *

class Sinavlar():
    
    def __init__(self):
        self.sinavAdi = ""
        self.sinavaGirenSayisi = ""
        self.sinavSuresi = ""

    def sinavEkle(self):
        print("\n---------- [Sınav Ekle] ----------")
        sinavAdi = input("Sınav Adı: ")
        sinavaGirenSayisi = input("Sınava Giren Öğrenci Sayısı: ")
        sinavSuresi = input("Sınav Süresi: ")
        sinavSql = "INSERT INTO sinavlar(sinavadi,sinavagirensayisi,sinavsuresi) VALUES ('{}','{}','{}')".format(sinavAdi,sinavaGirenSayisi,sinavSuresi)
        sinavEklemeIslemi = db.cursor()
        sinavEklemeIslemi.execute(sinavSql)
        db.commit()

    def sinavGuncelle(self):
        print("\n---------- [Sınav Güncelle] ----------")
        sinavId = input("Güncellenecek Sınav Id: ")
        sinavAdi = input("Sınav Adı: ")
        sinavaGirenSayisi = input("Sınava Giren Sayısı: ")
        sinavSuresi = input("Sınav Süresi: ")
        sinavSql = "UPDATE sinavlar SET sinavadi='{}',sinavagirensayisi='{}',sinavsuresi='{}' WHERE sinavid={}".format(sinavAdi,sinavaGirenSayisi,sinavSuresi,sinavId)
        sinavGuncellemeIslemi = db.cursor()
        sinavGuncellemeIslemi.execute(sinavSql)
        db.commit()

    def sinavListele(self):
        print("\n---------- [Sınav Adı-Süresi] ----------")
        sinavSql = "SELECT * FROM sinavlar"
        sinavListelemeIslemi = db.cursor()
        sinavListelemeIslemi.execute(sinavSql)
        sinavlar = sinavListelemeIslemi.fetchall()
        for sinav in sinavlar:
            print("Sınav Adı:",sinav[1],"Süresi:",sinav[2])

    def sinavSil(self):
        print("\n---------- [Sınav Sil] ----------")
        sinavId = input("Silinecek Sınav Id: ")
        sinavSql = "DELETE FROM sinavlar WHERE sinavid={}".format(sinavId)
        sinavSilmeIslemi = db.cursor()
        sinavSilmeIslemi.execute(sinavSql)
        db.commit()