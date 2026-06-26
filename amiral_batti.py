#ELANUR USSEN 
import random
print("---------------AMİRAL BATTI OYUNUNA HOSGELDİNİZ----------------------\n\n")
while True:
    boyut = int(input("OYUN ALANINN BOYUTUNU GIRIN(EN AZ 10x10):"))
    while True:
        if boyut < 10:
            print("LUTFEN 10X10 DAN BUYUK BIR BOYUT GIRINIZ:")
            boyut = int(input("OYUN ALANINN BOYUTUNU GIRIN(EN AZ 10x10):"))
            continue
        else:
            break

    print("\n")
    oyun_alani = []
    for i in range(boyut):
        satir = []
        for j in range(boyut):
            satir.append("?")
        oyun_alani.append(satir)

    kontrol1 = 0
    atissayisi2 = 0
    yalanci_y = 0
    yalanci_x = 0
    gemi_koordinatlari = []
    gemiler = []
    secilenkonumlar = []
    yonler = ["yatay", "dikey"]
    gemi_boyutlari = [1, 2, 3, 4]
    yler = []
    xler = []
    for gemi_boyutu in gemi_boyutlari:
        while True:
            gemi_yonu = random.choice(["yatay", "dikey"])

            if gemi_yonu == "yatay":
                x_koordinati = random.randint(0, boyut - gemi_boyutu)
                y_koordinati = random.randint(0, boyut - 1)
                gemi_koordinatlari = [(x_koordinati + i, y_koordinati) for i in range(gemi_boyutu)]
            else:
                x_koordinati = random.randint(0, boyut - 1)
                y_koordinati = random.randint(0, boyut - gemi_boyutu)
                gemi_koordinatlari = [(x_koordinati, y_koordinati + i) for i in range(gemi_boyutu)]

            uyusuyor_mu = False
            for gemi in gemiler:
                for koordinat in gemi_koordinatlari:
                    if koordinat in gemi:
                        uyusuyor_mu = True
                        break
                if uyusuyor_mu:
                    break

            if not uyusuyor_mu:
                gemiler.append(gemi_koordinatlari)
                break


    print("1-GIZLI MOD\n2-ACIK MOD")
    secim = int(input("LUTFEN ISTEDIGINIZ BIR MODU SECİNİZ:"))
    rtr2 = 0
    if secim == 2:
        for gemi_koordinatlari in gemiler:
            for koordinat in gemi_koordinatlari:
                x, y = koordinat
                oyun_alani[y][x] = gemi_boyutlari[len(gemi_koordinatlari) - 1]
        print("\n")
        for i in range(boyut):
            for j in range(boyut):
                print(oyun_alani[i][j], end="")
            print()
        print("\n")

        secilenkonumlar = []
        yanlishakki = (boyut ** 2) // 3
        ıkıncıyanlıs=yanlishakki
        print("BASLANGIC TAHMIN ETME HAKKINIZ:", yanlishakki)
        while yanlishakki > 0:
            ctr = 0
            while True:
                tahminix = int(input(f"LUTFEN SUTUN NUMARASI GIRIN(INDEXLER 0-{boyut-1} ARASINDADIR):"))
                tahminiy = int(input(f"LUTFEN SATIR NUMARASI GIRIN(INDEXLER 0-{boyut-1} ARASINDADIR):"))
                if (tahminiy < 0 or tahminiy > boyut-1) or (tahminix < 0 or tahminix > boyut-1):
                    print(f"LUTFEN 0-{boyut-1} ARASI BIR DEGER GIRINIZ")
                    continue
                else:
                    break
            for konumlar in secilenkonumlar:
                for konum in konumlar:
                    if tahminiy == konum[1] and tahminix == konum[0]:
                        print("DAHA ONCE BU KONUMU SECTINIZ LUTFEN BASKA BIR KONUM SECINIZ")
                        print(f"KALAN YANLIS HAKKINIZ:{yanlishakki}")

                        for i in range(boyut):
                            for j in range(boyut):
                                print(oyun_alani[i][j], end="")
                            print()
                        print("\n")
                        ctr = 1
                        break
            dahaoncekonumlar = [(tahminix, tahminiy)]
            secilenkonumlar.append(dahaoncekonumlar)
            if oyun_alani[tahminiy][tahminix] == '?' or oyun_alani[tahminiy][tahminix] == '*':
                if oyun_alani[tahminiy][tahminix] == '?':
                    print("MAALESEF ISABET EDEMEDINIZ")
                    oyun_alani[tahminiy][tahminix] = '*'
                    yanlishakki -= 1
                    atissayisi2 += 1
                    print(f"KALAN YANLIS HAKKINIZ:{yanlishakki}")
                    for i in range(boyut):
                        for j in range(boyut):
                            print(oyun_alani[i][j], end="")
                        print()
                    print("\n")
            else:
                if ctr == 0:
                    oyun_alani[tahminiy][tahminix] = 'X'
                    print("TEBRIKLER BIR GEMI PARCASINI VURDUNUZ!\n")
                    atissayisi2 += 1
                    for i in range(boyut):
                        for j in range(boyut):
                            print(oyun_alani[i][j], end="")
                        print()


            for gemi_koordinatlari in gemiler:
                for koordinat in gemi_koordinatlari:
                    if tahminiy == koordinat[1] and tahminix == koordinat[0]:
                        gemi_koordinatlari.remove((tahminix, tahminiy))
                        if len(gemi_koordinatlari) == 0:
                            print("TEBRIKLER BIR GEMIYI BATIRDINIZ!")
                            kontrol1+=1
                            break

            if kontrol1 == 4:
                print("TUM GEMILER BATIRILDI")
                puan = ıkıncıyanlıs - atissayisi2
                print(f"TEBRIKLER {puan}PUANLA OYUNU KAZANDINIZ")
                print("1-YENİ OYUN\n2-CIKIS")
                tercih = int(input("SECIMINIZI YAPINIZ:"))
                if tercih == 1:
                    yanlishakki = (boyut ** 2) // 3
                    atissayisi2 = 0
                    break
                else:
                    yanlishakki = 0
                    rtr = 1
                    break

            if yanlishakki == 0  and kontrol != 4:
                print("OYUNU KAYBETTINIZ")
                print("1-YENİ OYUN\n2-CIKIS")
                tercih = int(input("SECIMINIZI YAPIN:"))
                if tercih == 1:
                    yanlishakki = (boyut ** 2) // 3
                    atissayisi = 0
                    break
                else:
                    yanlishakki = 0
                    rtr = 1
                    break
    if rtr2==1:
        break
    rtr = 0
    if secim == 1:

        yanlishakki = (boyut**2)//3
        ıkıncıyanlıs=yanlishakki
        puan = 0
        atissayisi = 0
        print("\nBASLANGIC TAHMIN ETME HAKKINIZ:", yanlishakki)
        kontrol = 0
        while yanlishakki > 0:
            ctr = 0
            while True:
                tahminix = int(input(f"LUTFEN SUTUN NUMARASI GIRIN(INDEXLER 0-{boyut-1} ARASINDADIR):"))
                tahminiy = int(input(f"LUTFEN SATIR NUMARASI GIRIN(INDEXLER 0-{boyut-1} ARASINDADIR):"))
                if (tahminiy < 0 or tahminiy > boyut-1) or (tahminix < 0 or tahminix > boyut-1):
                    print(f"LUTFEN 0-{boyut-1} ARASI BIR SAYI GIRINIZ")
                    continue
                else:
                    break
            for konumlar in secilenkonumlar:
                for konum in konumlar:
                    if tahminiy == konum[1] and tahminix == konum[0]:
                        print("DAHA ONCE BU KONUMU SECTINIZ,LUTFEN FARKLI BIR KONUM SECINIZ")

                        ctr = 1

            dahaoncekonumlar = [(tahminix, tahminiy)]
            secilenkonumlar.append(dahaoncekonumlar)
            if ctr == 0:
                if gemi_koordinatlari in gemiler:
                    isabet = False
                    for gemi_koordinatlari in gemiler:
                        for koordinat in gemi_koordinatlari:
                            if tahminiy == koordinat[1] and tahminix == koordinat[0]:
                                print("TEBRIKLER BIR GEMI PARCASINI BATIRDINIZ :)\n")
                                atissayisi += 1
                                oyun_alani[tahminiy][tahminix] = 'X'
                                for i in range(boyut):
                                    for j in range(boyut):
                                        print(oyun_alani[i][j], end="")
                                    print()

                                gemi_koordinatlari.remove((tahminix, tahminiy))
                                if len(gemi_koordinatlari) == 0:
                                    print("TEBRIKLER BIR GEMIYI BATIRDINIZ :)\n")
                                    kontrol += 1
                                isabet = True
                                break

            if oyun_alani[tahminiy][tahminix] == '?' or oyun_alani[tahminiy][tahminix] == '*':
                if oyun_alani[tahminiy][tahminix] == '?':
                    print("MAALESEF ISABET ETTIREMEDINIZ!")
                    atissayisi += 1
                    oyun_alani[tahminiy][tahminix] = '*'
                    yanlishakki -= 1
                print(f"KALAN YANLIS HAKKINIZ:{yanlishakki}")
                for i in range(boyut):
                    for j in range(boyut):
                        print(oyun_alani[i][j], end="")
                    print()
                print("\n")

            if kontrol == 4:
                print("TUM GEMILER BATIRILDI")
                puan = ıkıncıyanlıs - atissayisi
                print(f"TEBRIKLER {puan} PUANLA OYUNU KAZANDINIZ")
                print("1-YENİ OYUN\n2-CIKIS")
                tercih = int(input("SECIMINIZI YAPIN:"))
                if tercih == 1:
                    yanlishakki = (boyut ** 2) // 3
                    atissayisi = 0
                    break
                else:
                    yanlishakki = 0
                    rtr=1
                    break

            if yanlishakki == 0 and kontrol != 4:
                print("OYUNU KAYBETTINIZ")
                print("1-YENİ OYUN\n2-CIKIS")
                tercih = int(input("SECIMINIZI YAPINIZ:"))
                if tercih == 1:
                    yanlishakki = (boyut ** 2) // 3
                    atissayisi = 0
                    break
                else:
                    yanlishakki = 0
                    rtr=1
                    break
    if rtr==1:
       break
##son