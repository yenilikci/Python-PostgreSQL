from Ogrenciler import *
from Ogretmenler import *
from Sinavlar import *
from Dersler import *
from Devamsizlik import *
from Demirbaslar import *
from Yemekhane import *
from Siniflar import *
from Subeler import *

while(True):
    print("""
    _______________________________________________________________
                    
                    Okul/Kurs Bilgi Takip Uygulaması
    _______________________________________________________________
    
    Yapılabilecek İşlemler:
    1)Öğrenciler İle İlgili İşlemler
    2)Öğretmenler İle İlgili İşlemler
    3)Dersler İle İlgili İşlemler
    4)Sınavlar İle İlgili İşlemler
    5)Devamsızlık Kayda Geç
    6)Demirbaş Kayda Geç
    7)Sınıf Ekle
    8)Şube Ekle
    9)Yemekhane Menüsüne Yemek Ekle
    0)Çıkış
    """)
    menuSecim = int(input("Yukarıdaki işlemlerden birini seçiniz: "))
    if(menuSecim == 1):
        ogrenciler = Ogrenciler()
        print("""
        Aşağıdaki Listeden Bir İşlem Seçiniz:
        a)Öğrenci Ekle
        b)Öğrenci Güncelle
        c)Öğrenci Listele
        d)Öğrenci Sil
        """)
        ogrI = input("Seçiminiz: ")
        if(ogrI == "a" or ogrI == "A"):
            ogrenciler.ogrenciEkle()
        elif(ogrI == "b" or ogrI == "B"):
            ogrenciler.ogrenciGuncelle()
        elif(ogrI == "c" or ogrI == "C"):
            ogrenciler.ogrenciListele()
        elif(ogrI == "d" or ogrI == "D"):
            ogrenciler.ogrenciSil()

    elif(menuSecim == 2):
        ogretmenler = Ogretmenler()
        print("""
        Aşağıdaki Listeden Bir İşlem Seçiniz:
        a)Öğretmen Ekle
        b)Öğretmen Güncelle
        c)Öğretmen Listele
        d)Öğretmen Sil
        """)
        ogrtmI = input("Seçiminiz: ")
        if(ogrtmI == "a" or ogrtmI == "A"):
            ogretmenler.ogretmenEkle()
        elif(ogrtmI == "b" or ogrtmI == "B"):
            ogretmenler.ogretmenGuncelle()
        elif(ogrtmI == "c" or ogrtmI == "C"):
            ogretmenler.ogretmenListele()
        elif(ogrtmI == "d" or ogrtmI == "D"):
            ogretmenler.ogretmenSil()        

    elif(menuSecim == 3):
        dersler = Dersler()
        print("""
        Aşağıdaki Listeden Bir İşlem Seçiniz:
        a)Ders Ekle
        b)Ders Güncelle
        c)Ders Listele
        d)Ders Sil
        """)
        dersI = input("Seçiminiz: ")
        if(dersI == "a" or dersI == "A"):
            dersler.dersEkle()
        elif(dersI == "b" or dersI == "B"):
            dersler.dersGuncelle()
        elif(dersI == "c" or dersI == "C"):
            dersler.dersListele()
        elif(dersI == "d" or dersI == "D"):
            dersler.dersSil() 

    elif(menuSecim == 4):
        sinavlar = Sinavlar()
        print("""
        Aşağıdaki Listeden Bir İşlem Seçiniz:
        a)Sınav Ekle
        b)Sınav Güncelle
        c)Sınav Listele
        d)Sınav Sil
        """)
        sinavI = input("Seçiminiz: ")
        if(sinavI == "a" or sinavI == "A"):
            sinavlar.sinavEkle()
        elif(sinavI == "b" or sinavI == "B"):
            sinavlar.sinavGuncelle()
        elif(sinavI == "c" or sinavI == "C"):
            sinavlar.sinavListele()
        elif(sinavI == "d" or sinavI == "D"):
            sinavlar.sinavSil() 

    elif(menuSecim == 5):
        devamsizlik = Devamsizlik()
        devamsizlik.devamsizlikEkle()

    elif(menuSecim == 6):
        demirbaslar = Demirbaslar()
        demirbaslar.demirbasEkle()

    elif(menuSecim == 7):
        siniflar = Siniflar()
        siniflar.sinifEkle()

    elif(menuSecim == 8):
        subeler = Subeler()
        subeler.subeEkle()

    elif(menuSecim == 9):
        yemekhanemenu = Yemekhane()
        yemekhanemenu.menuyeYemekEkle()

    elif(menuSecim == 0):
        print("Uygulama Sonlanıyor...")
        exit()
    else:
        print("Listede Olan Bir İşlemi Seçiniz!")