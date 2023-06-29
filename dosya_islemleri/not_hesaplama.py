def not_hesapla(satir):
    """
    Not Hesaplama
    :return: None
    """
    satir = satir[:-1]

    liste = satir.split(",")

    isim = liste[0]
    not1 = int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])

    son_not = not1 * (3/10) + not2 * (3/10) + not3 * (4/10)

    if (son_not >= 90):
        harf = "AA"
    elif (son_not >= 85):
        harf = "BA"
    elif (son_not >= 80):
        harf = "BB"
    elif (son_not >= 75):
        harf = "CB"
    elif (son_not >= 70):
        harf = "CC"
    elif (son_not >= 65):
        harf = "DC"
    elif (son_not >= 60):
        harf = "DD"
    elif (son_not >= 55):
        harf = "FD"
    else:
        harf = "FF"

    return isim + "-----------" + harf + "\n"
   

with open("dosya_islemleri/dosya.txt","r",encoding="utf-8") as file:
    eklenecekler_listesi = []
    kalanlar_listesi = []
    gecenler_listesi = []
    for i in file:
        not_hesaplama_sonucu = not_hesapla(i)
        eklenecekler_listesi.append(not_hesapla(i))
        
        if "FF" in not_hesaplama_sonucu:
            kalanlar_listesi.append(not_hesaplama_sonucu)
        else:
            gecenler_listesi.append(not_hesaplama_sonucu)

        with open("kalanlar.txt", "w", encoding="utf-8") as kalanlar_dosyasi:
            for kalan in kalanlar_listesi:
                kalanlar_dosyasi.write(kalan)

        with open("geçenler.txt", "w", encoding="utf-8") as gecenler_dosyasi:
            for gecen in gecenler_listesi:
                gecenler_dosyasi.write(gecen)
    print(eklenecekler_listesi)
    with open("notlar.txt","w",encoding="utf-8") as file2:
        for i in eklenecekler_listesi:
            file2.write(i)
