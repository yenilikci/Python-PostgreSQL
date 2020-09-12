from veritabani import *

class Demirbaslar():

    def __init__(self):
        self.demirbasAdi = ""

    def demirbasEkle(self):
        print("\n---------- [Demirbaş Ekle] ----------")
        demirbasAdi = input("Demirbaş Adı: ")
        demirbasSql = "INSERT INTO demirbaslar(demirbasadi) VALUES ('{}')".format(demirbasAdi)
        demirbasEklemeIslemi = db.cursor()
        demirbasEklemeIslemi.execute(demirbasSql)
        db.commit()