"""
Kodlama Egzersizi - Temel Python Objeleri ve Veri Yapıları
"""


def oyuncu_kaydetme():
    print("Oyuncu Kaydetme Programı")

    ad = input("Oyuncunun Adı: ")
    soyad = input("Oyuncunun Soyadı: ")
    takim = input("Oyuncunun Takımı: ")

    bilgiler = [ad, soyad, takim]
    print("Bilgiler Kaydediliyor...")

    print("\nOyuncunun Adı: {0}\nOyuncunun Soyadı: {1}\nOyuncunun Takımı: {2}\n".format(
        bilgiler[0], bilgiler[1], bilgiler[2]))

    print("Bilgiler Kaydedildi...")


def kok_bulma():
    """
    2. dereceden bir bilinmeyenli denklemin köklerini bulma

    Denklem: ax^2 + bx + c

    Deltayı Hesaplama: b ** 2 - 4 * a * c

    Birinci Kök: (-b - delta ** 0.5) / (2*a)
    İkinci Kök:  (-b + delta ** 0.5) / (2*a)
    """
    a = int(input('a: '))
    b = int(input('b: '))
    c = int(input('c: '))

    delta = b ** 2 - 4 * a * c

    x1 = (-b - delta ** 0.5) / (2*a)
    x2 = (-b + delta ** 0.5) / (2*a)

    print(f"Birinci Kök: {x1}, İkinci Kök: {x2}")


if __name__ == "__main__":
    # oyuncu_kaydetme()
    kok_bulma()
