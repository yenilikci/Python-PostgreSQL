from veritabani import *

class Dersler():

    def __init__(self):
        self.dersAdi = ""
        self.dersBrans = ""
    
    def dersEkle(self):
        print("\n---------- [Ders Ekle] ----------")
        dersAdi = input("Ders Adı: ")
        dersBrans = input("Ders Branş: ")
        dersSql = "INSERT INTO dersler(dersadi,dersbrans) VALUES ('{}','{}')".format(dersAdi,dersBrans)
        dersEklemeIslemi = db.cursor()
        dersEklemeIslemi.execute(dersSql)
        db.commit()
    
    def dersGuncelle(self):
        print("\n---------- [Ders Güncelle] ----------")
        dersId = input("Güncellenecek Ders Id: ")
        dersAdi = input("Ders Adı: ")
        dersBrans = input("Ders Branş: ")
        dersSql = "UPDATE dersler SET dersadi='{}',dersbrans='{}' WHERE dersid={}".format(dersAdi,dersBrans,dersId)
        dersGuncellemeIslemi = db.cursor()
        dersGuncellemeIslemi.execute(dersSql)
        db.commit()
    
    def dersListele(self):
        print("\n---------- [Ders Adı-Branş] ----------")
        dersSql = "SELECT * FROM dersler"
        dersListeleIslemi = db.cursor()
        dersListeleIslemi.execute(dersSql)
        dersler = dersListeleIslemi.fetchall()
        for ders in dersler:
            print("İsim:",ders[1],"Branş:",ders[2])
    
    def dersSil(self):
        print("\n---------- [Ders Sil] ----------")
        dersId = input("Silinecek Ders Id: ")
        dersSql = "DELETE FROM dersler WHERE dersid={}".format(dersId)
        dersSilmeIslemi = db.cursor()
        dersSilmeIslemi.execute(dersSql)
        db.commit()