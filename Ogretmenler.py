from veritabani import *

class Ogretmenler():
    def __init__(self):
        self.ogrtmAdi = ""
        self.ogrtmSoyadi = ""
        self.ogrtmBrans = ""

    def ogretmenEkle(self):
        print("\n---------- [Öğretmen Ekle] ----------")
        ogrtmAdi = input("Öğretmen Adı: ")
        ogrtmSoyadi = input("Öğretmen Soyadı: ")
        ogrtmBrans = input("Öğretmen Branş: ")
        ogrtmSql = "INSERT INTO ogretmenler(ogretmenadi,ogretmensoyadi,ogretmenbrans) VALUES ('{}','{}','{}')".format(ogrtmAdi,ogrtmSoyadi,ogrtmBrans)
        ogrtmEklemeIslemi = db.cursor()
        ogrtmEklemeIslemi.execute(ogrtmSql)
        db.commit()

    def ogretmenGuncelle(self):
        print("\n---------- [Öğretmen Güncelle] ----------")
        ogrtmId = input("Güncellenecek Öğretmen Id: ")
        ogrtmAdi = input("Öğretmenin Adı: ")
        ogrtmSoyadi = input("Öğretmenin Soyadı: ")
        ogrtmBrans = input("Öğretmenin Branşı: ")
        ogrtmSql = "UPDATE ogretmenler SET ogretmenadi='{}',ogretmensoyadi='{}',ogretmenbrans='{}' WHERE ogretmenid={}".format(ogrtmAdi,ogrtmSoyadi,ogrtmBrans,ogrtmId)
        ogrtmGuncellemeIslemi = db.cursor()
        ogrtmGuncellemeIslemi.execute(ogrtmSql)
        db.commit()

    def ogretmenListele(self):
        print("\n---------- [Öğretmen İsim-Soyisimleri] ----------")
        ogrtmSql = "SELECT * FROM ogretmenler"
        ogrtmListelemeIslemi = db.cursor()
        ogrtmListelemeIslemi.execute(ogrtmSql)
        ogretmenler = ogrtmListelemeIslemi.fetchall()
        for ogretmen in ogretmenler:
            print("İsim:",ogretmen[1],"Soyisim:",ogretmen[2])

    def ogretmenSil(self):
        print("\n---------- [Öğretmen Sil] ----------")
        ogrtmId = input("Silinecek Öğretmen Id: ")
        ogrtmSql = "DELETE FROM ogretmenler WHERE ogretmenid={}".format(ogrtmId)
        ogrtmSilmeIslemi = db.cursor()
        ogrtmSilmeIslemi.execute(ogrtmSql)
        db.commit()