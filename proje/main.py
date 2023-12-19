import os
def ana_ekran():
    os.system("cls")
    print("1 - Yönetici girişi")
    print("2 - Üye girişi")
    print("3 - Kayıt ol")
    print("0 - Çıkış yap")

def yönetici_ekran():
    os.system("cls")
    print("1 - Üyeleri görüntüle")
    print("2 - Ürünleri görüntüle")
    print("3 - Ürün ekle")
    print("4 - Ürün sil")
    print("5 - Şifreni değiştir")
    print("0 - Geri dön")

def üye_ekran():
    os.system("cls")
    print("1 - Ürün satın al")
    print("2 - Ürünleri görüntüle")
    print("3 - Cüzdanına para ekle")
    print("4 - Profiline göz at")
    print("5 - Şifreni değiştir")
    print("0 - Geri dön")

def kayıt_ol():
    os.system("cls")
    with open("üyeler.txt","a+",encoding="utf-8") as dosya:
        with open("üyepara.txt","a+",encoding="utf-8") as üyep:
            sayac = 0
            while sayac == 0:
                kullanıcı_adı = str(input("Kullanıcı adı giriniz : "))
                kontrol = kullanıcı_kontrol(kullanıcı_adı)
                if kontrol == 0:
                    sayac += 1
            ad = str(input("Adınızı giriniz : "))
            soyad = str(input("Soyadınızı giriniz : "))
            şifre = str(input("Şifrenizi giriniz : "))
            dosya.write(kullanıcı_adı + " " + ad + " " + soyad + " " + şifre + " " + "0\n")
            üyep.write(kullanıcı_adı + " " + "0" + " 0\n")

def kullanıcı_kontrol(kullanıcı_adı):
    sayac = 0
    with open("üyeler.txt","r",encoding="utf-8") as dosya:
        for satir in dosya:
            if satir[0] == kullanıcı_adı:
                sayac += 1
    return sayac

def yönetici_kontrol(password):
    sayac = 0
    with open("yöneticişifre.txt","r",encoding="utf-8") as dosya:
        şifre = dosya.read()
        if şifre == password:
            sayac += 2
    return sayac

def üye_kontrol(kullanici,password):
    sayac = 0
    with open("üyeler.txt","r",encoding="utf-8") as dosya:
        for satir in dosya:
            satir = satir.split(" ")
            if kullanici == satir[0]:
                ad = satir[0]
                şifre = satir[3]
    if ad == kullanici and str(şifre) == str(password):
        sayac += 2
    return sayac

def kod_kontrol(ürün_kodu):
    sayac = 0
    with open("ürünler.txt","r",encoding="utf-8") as dosya:
        for satir in dosya:
            satir = satir.split(" ")
            if satir[0] == ürün_kodu:
                sayac += 1
    return sayac

def üyeleri_görüntüle():
    os.system("cls")
    with open("üyeler.txt","r",encoding="utf-8") as dosya:
        for satir in dosya:
            satir = satir.split(" ")
            print("----------------")
            print(f"Kullanıcı adı : {satir[0]}")
            print(f"Adı           : {satir[1]}")
            print(f"Soyadı        : {satir[2]}")
            print("----------------")

def ürünleri_görüntüle():
    os.system("cls")
    with open("ürünler.txt","r",encoding="utf-8") as dosya:
        for satir in dosya:
            satir = satir.split(" ")
            print("----------------")
            print(f"Ürünün kodu   : {satir[0]}")
            print(f"Ürünün adı    : {satir[1]}")
            print(f"Ürünün fiyatı : {satir[2]}")
            print("----------------")


def ürün_ekle():
    os.system("cls")
    with open("ürünler.txt","a+",encoding="utf-8") as dosya:
        ürün_kodu = input("Eklemek istediğiniz ürünün kodu : ")
        sayac = kod_kontrol(ürün_kodu)
        while sayac != 0:
            print("Ürün kodu kullanılıyor !")
            ürün_kodu = input("Eklemek istediğiniz ürünün kodu : ")
            sayac = kod_kontrol(ürün_kodu)
        ürün_ad = input("Eklemek istediğiniz ürünün adı : ")
        ürün_fiyat = input("Eklemek istediğiniz ürünün fiyatı : ")
        dosya.write(ürün_kodu + " " + ürün_ad + " " + ürün_fiyat + " " + "0\n")


def ürün_sil1():
    os.system("cls")
    with open("ürünler.txt","r",encoding="utf-8") as dosya:
        with open("ürüngecici.txt","w",encoding="utf-8") as gecici:
            ürünleri_görüntüle()
            print("\n")
            silinecek_ürün = str(input("Lütfen silmek istediğiniz ürünün kodunu giriniz : "))
            for satir in dosya:
                satir = satir.split(" ")
                if silinecek_ürün == satir[0]:
                    continue
                else:
                    gecici.write(satir[0] + " " + satir[1] + " " + satir[2] + "\n")

def ürün_sil2():
    with open("ürünler.txt","w",encoding="utf-8") as dosya:
        with open("ürüngecici.txt","r",encoding="utf-8") as gecici:
            okunacak = gecici.read()
            dosya.write(okunacak)

def üye_şifre_değiştir1():
    i = 0
    with open("üyeler.txt","r",encoding="utf-8") as dosya:
        with open("üyegecici.txt","w",encoding="utf-8") as gecici:
            dosya.seek(0)
            for satir in dosya:
                i += 1
            dosya.seek(0)
            for i in range(1,i+1):
                okunacak = dosya.readline()
                gecici.write(okunacak)

def üye_şifre_değiştir2(kullanici):
    os.system("cls")
    with open("üyegecici.txt","r",encoding="utf-8") as gecici:
        with open("üyeler.txt","w",encoding="utf-8") as dosya:
            yeni_sifre = input("Lütfen yeni şifrenizi giriniz : ")
            for satir in gecici:
                satir = satir.split(" ")
                if satir[0] == kullanici:
                    dosya.write(kullanici + " " + satir[1] + " " + satir[2] + " " + str(yeni_sifre) + " " + "0\n")
                elif satir[0] != kullanici:
                    dosya.write(satir[0] + " " + satir[1] + " " + satir[2] + " " + satir[3] + " " + "0\n")


def yönetici_değiştir():
    os.system("cls")
    with open("yöneticişifre.txt" ,"w+",encoding="utf-8") as dosya:
        yeni_şifre = str(input("Lütfen yeni şifrenizi giriniz : "))
        dosya.write(yeni_şifre)

def para_ekle1():
    with open("üyepara.txt","r",encoding="utf-8") as dosya:
        with open("üyeparagecici.txt","w",encoding="utf-8") as gecici:
            i = 0
            dosya.seek(0)
            for satir in dosya:
                i += 1
            dosya.seek(0)
            for i in range(1,i+1):
                okunacak = dosya.readline()
                gecici.write(okunacak)


def para_ekle2(kullanici):
    os.system("cls")
    with open("üyeparagecici.txt","r",encoding="utf-8") as gecici:
        with open("üyepara.txt","w",encoding="utf-8") as dosya:
            eklenecek_para = int(input("Lütfen eklemek istediğiniz miktarı giriniz : "))
            for satir in gecici:
                satir = satir.split(" ")
                if kullanici == satir[0]:
                    para = satir[1]
                    yeni_miktar = eklenecek_para + int(para)
                    dosya.write(kullanici + " " + str(yeni_miktar) + " " + "0\n")
                elif kullanici != satir[0]:
                    dosya.write(satir[0] + " " + satir[1] + " " + "0\n")


def profile_görüntüle(kullanici):
    os.system("cls")
    with open("üyeler.txt","r",encoding="utf-8") as dosya:
        with open("üyepara.txt","r",encoding="utf-8") as üyep:
            for i in üyep:
                i = i.split(" ")
                if i[0] == kullanici:
                    para = i[1]
            for satir in dosya:
                satir = satir.split(" ")
                if satir[0] == kullanici:
                    print(f"Kullanıcı adı : {kullanici}")
                    print(f"Ad            : {satir[1]}")
                    print(f"Soyad         : {satir[2]}")
                    print(f"Cüzdanım      : {para}")

def satın_al1():
    os.system("cls")
    with open("ürünler.txt","r",encoding="utf-8") as dosya:
        liste = []
        ücret = []
        ürünleri_görüntüle()
        giriş = "0"
        while giriş != "0001":
            sayı = str(input("Lütfen satın almak istediğiniz ürünün kodunu giriniz : "))
            if sayı != "0001":
                liste.append(sayı)
            elif sayı == "0001":
                giriş = "0001"
        for i in liste:
            satın_al2(i)
def satın_al2(i):
    ücret = []
    with open("ürünler.txt","r",encoding="utf-8") as dosya:
        for satir in dosya:
            satir = satir.split(" ")
            if satir[0] == i:
                ücret.append(satir[2])
        for a in ücret:
            satın_al3(a)

def satın_al3(a):
    toplam.append(a)

def para_kontrol(kullanici,para):
    with open("üyepara.txt","r",encoding="utf-8") as dosya:
        for satir in dosya:
            satir = satir.split(" ")
            if satir[0] == kullanici:
                cüzdan = satir[1]
        if int(cüzdan) >= int(para):
            cekilecek_miktar = int(cüzdan) - int(para)
            parayı_cek1()
            parayı_cek2(cekilecek_miktar)
        elif int(cüzdan) < int(para):
            print("Satın alım için lütfen cüzdanınıza para ekleyin")

def parayı_cek1():
    with open("üyepara.txt","r",encoding="utf-8") as dosya:
        with open("üyeparagecici.txt","w",encoding="utf-8") as gecici:
            i = 0
            dosya.seek(0)
            for satir in dosya:
                i += 1
            dosya.seek(0)
            for i in range(1,i+1):
                okunacak = dosya.readline()
                gecici.write(okunacak)

def parayı_cek2(cekilecek_miktar):
    with open("üyeparagecici.txt","r",encoding="utf-8") as gecici:
        with open("üyepara.txt","w",encoding="utf-8") as dosya:
            for satir in gecici:
                satir = satir.split(" ")
                if kullanici == satir[0]:
                    yeni_miktar = cekilecek_miktar
                    dosya.write(kullanici + " " + str(yeni_miktar) + " " + "0\n")
                elif kullanici != satir[0]:
                    dosya.write(satir[0] + " " + satir[1] + " " + "0\n")
            print("Satın alım başarılı !")



# KAYNAK KODLARI     -     KAYNAK KODLARI     -     KAYNAK KODLARI       -        KAYNAK KODLARI     -     KAYNAK KODLARI     -     KAYNAK KODLARI       -
# KAYNAK KODLARI     -     KAYNAK KODLARI     -     KAYNAK KODLARI       -        KAYNAK KODLARI     -     KAYNAK KODLARI     -     KAYNAK KODLARI       -
# KAYNAK KODLARI     -     KAYNAK KODLARI     -     KAYNAK KODLARI       -        KAYNAK KODLARI     -     KAYNAK KODLARI     -     KAYNAK KODLARI       -
# KAYNAK KODLARI     -     KAYNAK KODLARI     -     KAYNAK KODLARI       -        KAYNAK KODLARI     -     KAYNAK KODLARI     -     KAYNAK KODLARI       -



çıkış_1 = 0

while çıkış_1 == 0:
    ana_ekran()
    ilk_secenek = int(input("\nGirdi  : "))

    if ilk_secenek == 0:
        çıkış_1 = 1
        print("Çıkış yapıldı !")


    elif ilk_secenek == 1:
        password = str(input("Lütfen şifrenizi giriniz : "))
        kontrol = yönetici_kontrol(password)
        if kontrol == 2:
            çıkış_2 = 0

            while çıkış_2 == 0:
                yönetici_ekran()
                ikinci_secenek = int(input("\nGirdi  : "))

                if ikinci_secenek == 1:
                    sayac = 0
                    while sayac == 0:
                        üyeleri_görüntüle()
                        giriş = int(input("Lütfen menüye dönmek için '0' a basınız  : "))
                        if(giriş == 0):
                            sayac += 1

                elif ikinci_secenek == 2:
                    sayac = 0
                    while sayac == 0:
                        ürünleri_görüntüle()
                        giriş = int(input("Lütfen menüye dönmek için '0' a basınız  : "))
                        if (giriş == 0):
                            sayac += 1

                elif ikinci_secenek == 3:
                    ürün_ekle()
                    sayac = 0
                    while sayac == 0:
                        giriş = int(input("Lütfen menüye dönmek için '0' a basınız  : "))
                        if giriş == 0:
                            sayac += 1

                elif ikinci_secenek == 4:
                    ürün_sil1()
                    ürün_sil2()
                    sayac = 0
                    while sayac == 0:
                        print("İşlem başarılı\n")
                        giriş = int(input("Lütfen menüye dönmek için '0' a basınız  : "))
                        if (giriş == 0):
                            sayac += 1

                elif ikinci_secenek == 5:
                    yönetici_değiştir()
                    sayac = 0
                    while sayac == 0:
                        print("İşlem başarılı\n")
                        giriş = int(input("Lütfen menüye dönmek için '0' a basınız  : "))
                        if (giriş == 0):
                            sayac += 1

                elif ikinci_secenek == 0:
                    çıkış_2 += 1

    elif ilk_secenek == 2:
        kullanici = str(input("Kullanıcı adınızı giriniz : "))
        password = str(input("Şifrenizi giriniz : "))
        kontrol = üye_kontrol(kullanici,password)
        if kontrol == 2:
            çıkış_2 = 0

            while çıkış_2 == 0:
                üye_ekran()
                ikinci_secenek = int(input("\nGirdi  : "))

                if ikinci_secenek == 0:
                    çıkış_2 += 1

                elif ikinci_secenek == 1:
                    toplam = []
                    para = 0
                    satın_al1()
                    for j in toplam:
                        para = int(j) + para
                    para_kontrol(kullanici,para)


                elif ikinci_secenek == 2:
                    sayac = 0
                    while sayac == 0:
                        ürünleri_görüntüle()
                        giriş = int(input("Lütfen menüye dönmek için '0' a basınız  : "))
                        if (giriş == 0):
                            sayac += 1

                elif ikinci_secenek == 3:
                    para_ekle1()
                    para_ekle2(kullanici)
                    sayac = 0
                    while sayac == 0:
                        print("İşlem başarılı !\n")
                        giriş = int(input("Lütfen menüye dönmek için '0' a basınız  : "))
                        if (giriş == 0):
                            sayac += 1

                elif ikinci_secenek == 4:
                    profile_görüntüle(kullanici)
                    sayac = 0
                    while sayac == 0:
                        giriş = int(input("Lütfen menüye dönmek için '0' a basınız  : "))
                        if (giriş == 0):
                            sayac += 1

                elif ikinci_secenek == 5:
                    üye_şifre_değiştir1()
                    üye_şifre_değiştir2(kullanici)
                    sayac = 0
                    while sayac == 0:
                        print("İşlem başarılı")
                        giriş = int(input("Lütfen menüye dönmek için '0' a basınız  : "))
                        if (giriş == 0):
                            sayac += 1

    elif ilk_secenek == 3:
        kayıt_ol()
