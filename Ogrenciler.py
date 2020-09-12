from veritabani import *

class Ogrenciler():
    def __init__(self):
        self.ogrAdi = ""
        self.ogrSoyadi = ""
        self.ogrNo = ""
        self.ogrSinif = ""
        self.ogrSube = ""

    def ogrenciEkle(self):
        print("---------- [Öğrenci Ekle] ----------")
        ogrAdi = input("Öğrenci Adı: ")
        ogrSoyadi = input("Öğrenci Soyadı: ")
        ogrNo = input("Öğrenci Numarası: ")
        ogrSinif = input("Öğrenci Sınıfı: ")
        ogrSube = input("Öğrenci Şubesi: ")
        ogrSql = "INSERT INTO ogrenciler(ogrenciadi,ogrencisoyadi,ogrencinumarasi,ogrencisinif,ogrencisube) VALUES ('{}','{}','{}','{}','{}')".format(ogrAdi,ogrSoyadi,ogrNo,ogrSinif,ogrSube)
        ogrEklemeIslemi = db.cursor()
        ogrEklemeIslemi.execute(ogrSql)
        db.commit()

    def ogrenciGuncelle(self):
        print("\n---------- [Öğrenci Güncelle] ----------")
        ogrId = input("Güncellenecek Öğrenci Id: ")
        ogrAdi = input("Öğrencinin Adı: ")
        ogrSoyadi = input("Öğrencinin Soyadı: ")
        ogrNo = input("Öğrencinin Numarası: ")
        ogrSinif = input("Öğrencinin Sınıfı: ")
        ogrSube = input("Öğrencinin Şubesi: ")
        ogrSql = "UPDATE ogrenciler SET ogrenciadi='{}',ogrencisoyadi='{}',ogrencinumarasi='{}',ogrencisinif='{}',ogrencisube='{}' WHERE ogrenciid={}".format(ogrAdi,ogrSoyadi,ogrNo,ogrSinif,ogrSube,ogrId)
        ogrGuncellemeIslemi = db.cursor()
        ogrGuncellemeIslemi.execute(ogrSql)
        db.commit()

    def ogrenciListele(self):
        print("\n---------- [Öğrenci İsim-Soyisimleri] ----------")
        ogrSql = "SELECT * FROM ogrenciler"
        ogrListelemeIslemi = db.cursor()
        ogrListelemeIslemi.execute(ogrSql)
        ogrenciler = ogrListelemeIslemi.fetchall()
        for ogrenci in ogrenciler:
            print("İsim:",ogrenci[1],"Soyisim:",ogrenci[2])


    def ogrenciSil(self):
        print("\n---------- [Öğrenci Sil] ----------")
        ogrId = input("Silinecek Öğrenci Id: ")
        ogrSql = "DELETE FROM ogrenciler WHERE ogrenciid={}".format(ogrId)
        ogrSilmeIslemi = db.cursor()
        ogrSilmeIslemi.execute(ogrSql)
        db.commit()




        