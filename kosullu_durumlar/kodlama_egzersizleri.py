"""
Programlama Ödevi - Koşullu Durumlar
"""


def problem1():
    """
    Problem 1
        Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın ve şu kurallara göre ekrana şu yazıları yazdırın.

        Beden Kitle İndeksi: Kilo / Boy(m) *  Boy(m)

        BKİ 18.5'un altındaysa -------> Zayıf

        BKİ 18.5 ile 25 arasındaysa ------> Normal

        BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu

        BKİ 30'un üstündeyse -------------> Obez
    """
    boy = float(input("Lütfen Boyunuzu Giriniz: "))
    kilo = float(input("Lütfen Kilonuzu Giriniz: "))

    beden_kitle_endeksi = kilo / boy * boy  # bki =  kilo / (boy ** 2)

    if beden_kitle_endeksi < 18.5:
        print("Zayıf")
    elif beden_kitle_endeksi < 25:
        print("Normal")
    elif beden_kitle_endeksi < 30:
        print("Fazla Kilolu")
    else:
        print("Obez")


def problem2():
    """
    Problem 2
        Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın.
    """
    x = float(input("Lütfen Birinci Giriniz: "))
    y = float(input("Lütfen İkinci Giriniz: "))
    z = float(input("Lütfen Üçüncü Giriniz: "))

    if x > y and x > z:
        print(f"En büyüz x: {x}")
    elif y > x and y > z:
        print(f"En büyük y: {y}")
    elif z > x and z > y:
        print(f"En büyük z: {z}")
    else:
        print("Değerlerden hepsi veya birkaçı eşittir.")


def problem3():
    """
    Problem 3
        Kullanıcının girdiği vize1,vize2,final notlarına notlarına göre harf notunu hesaplayın.

        Vize1 toplam notun %30'una etki edecek.

        Vize2 toplam notun %30'una etki edecek.

        Final toplam notun %40'ına etki edecek.


        Toplam Not >=  90 -----> AA

        Toplam Not >=  85 -----> BA

        Toplam Not >=  80 -----> BB

        Toplam Not >=  75 -----> CB

        Toplam Not >=  70 -----> CC

        Toplam Not >=  65 -----> DC

        Toplam Not >=  60 -----> DD

        Toplam Not >=  55 -----> FD

        Toplam Not <  55 -----> FF
    """
    vize1 = int(input("Lütfen Vize 1 Notunu Giriniz: "))
    vize2 = int(input("Lütfen Vize 2 Notunu Giriniz: "))
    final = int(input("Lütfen Final Notunu Giriniz: "))

    genel_not = vize1 * 3/10 + vize2 * 3/10 + final * 4/10

    if (genel_not >= 90):
        print("AA")
    elif (genel_not >= 85):
        print("BA")
    elif (genel_not >= 80):
        print("BB")
    elif (genel_not >= 75):
        print("CB")
    elif (genel_not >= 70):
        print("CC")
    elif (genel_not >= 65):
        print("DC")
    elif (genel_not >= 60):
        print("DD")
    else:
        print("FF")


def problem4():
    """
    Problem 4
        Şimdi de geometrik şekil hesaplama işlemi yapalım. İlk olarak kullanıcıdan üçgenin mi dörtgenin mi tipini bulmak istediğini sorun.

        Eğer kullanıcı "Dörtgen" cevabını verirse , 4 tane kenar isteyip bu dörtgenin kare mi , dikdörtgen mi yoksa sıradan bir dörtgen mi olduğunu bulmaya çalışın.

        Eğer kullanıcı "Üçgen" cevabını verirse , 3 tane kenar isteyip bu üçgenin ikizkenar mı , eşkenar mı yoksa sıradan bir üçgen mi olduğunu bulmaya çalışın. Eğer verilen kenarlar bir üçgen belirtmiyorsa, ekrana "Üçgen belirtmiyor" şeklinde bir yazı yazın.o

        Üçgen belirtme şartını bilmiyorsunuz internetten bakabilirsiniz.

        Ayrıca , bu problemde mutlak değer bulmaya ihtiyacınız olacak. Bunun için, Pythonda hazır bir fonksiyon olan abs() fonksiyonunu kullanabilirsiniz. Kullanımı şu şekildedir ;
    """

    sekil = input("Hangi şeklin tipini öğrenmek istiyorsunuz?")

    if (sekil == "Dörtgen"):
        print("Lütfen kenarları sırayla giriniz.")
        a = int(input("Kenar-1:"))
        b = int(input("Kenar-2:"))
        c = int(input("Kenar-3:"))
        d = int(input("Kenar-4:"))

        if (a == b and a == c and a == d):
            print("Kare")
        elif (a == c and b == d):
            print("Dikdörtgen")
        else:
            print("Dörtgen")
    elif (sekil == "Üçgen"):
        a = int(input("Kenar-1:"))
        b = int(input("Kenar-2:"))
        c = int(input("Kenar-3:"))
        if (abs(a+b) > c and abs(a+c) > b and abs(b+c) > a):
            if (a == b and a == c):
                print("Eşkenar Üçgen...")
            elif ((a == b and a != c) or (a == c and a != b) or (b == c and b != a)):
                print("İkizkenar Üçgen....")
            else:
                print("Çeşitkenar Üçgen...")
        else:
            print("Üçgen belirtmiyor...")

    else:
        print("Geçersiz Şekil...")


if __name__ == "__main__":
    # problem1()
    # problem2()
    # problem3()
    problem4()
