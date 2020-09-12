from veritabani import *

class Subeler():

    def __init__(self):
        self.subeAdi = ""
        self.subeMevcut = ""
    
    def subeEkle(self):
        print("\n---------- [Şube Ekle] ----------")
        subeAdi = input("Şube Adı: ")
        subeMevcut = input("Şubede Bulunan Öğrenci Sayısı: ")
        subeSql = "INSERT INTO subeler(subeadi,subemevcut) VALUES ('{}','{}')".format(subeAdi,subeMevcut)
        subeEklemeIslemi = db.cursor()
        subeEklemeIslemi.execute(subeSql)
        db.commit()

