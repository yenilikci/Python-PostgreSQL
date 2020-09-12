from veritabani import *

class Devamsizlik():
    
    def __init__(self):
        self.ogrenciNo = ""
        self.devamsizlikGunu = ""

    def devamsizlikEkle(self):
        print("\n---------- [Devamsızlık Ekle] ----------")
        ogrenciNo = input("Devamsızlık Yapan Öğrenci No: ")
        devamsizlikGunu = input("Kaç Gün Devamsızlık Yaptı: ")
        devamsizlikSql = "INSERT INTO devamsizlik(ogrencino,devamsizlikgunu) VALUES ('{}','{}')".format(ogrenciNo,devamsizlikGunu)
        devamsizlikEklemeIslemi = db.cursor()
        devamsizlikEklemeIslemi.execute(devamsizlikSql)
        db.commit()