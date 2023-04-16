"""
Programlama Ödevi - Temel Python Objeleri ve Veri Yapıları
"""


def problem1():
    """
    Problem 1
    - Kullanıcıdan aldığınız 3 tane sayıyı çarparak ekrana yazdırın. Ekrana yazdırma işlemini *format* metoduyla yapmaya çalışın.
    """

    a = int(input('Lütfen birinci sayıyı giriniz: '))
    b = int(input('Lütfen ikinci sayıyı giriniz: '))
    c = int(input('Lütfen üçüncü sayıyı giriniz: '))

    print('a: {0} * b: {1} * c: {2} = {3}'.format(a, b, c, a*b*c))


def problem2():
    """
    Problem 2
    - Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.
        Ör: Beden Kitle İndeksi : Kilo / Boy(m) Boy(m)
    """

    boy = float(input("Lütfen boyunuzu giriniz: "))
    kilo = float(input("Lütfen kilonuzu giriniz: "))

    beden_kitle_indeksi = kilo / boy ** 2

    print(
        f"boyunuz: {boy}, kilonuz: {kilo}, beden kitle indekisiniz:{beden_kitle_indeksi} ")


def problem3():
    """
    Problem 3
    - Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı bilgilerini alın ve sürücünü toplam ne kadar ödemesini gerektiğini hesaplayın.
    """

    fuel_efficiency = float(
        input("Kilometrede yakıt tüketimi (km/lt): "))  # yakıt verimliliği
    distance_traveled = float(
        input("Toplam yol mesafesi (km): "))  # Katedilen mesafe
    fuel_cost = float(input("Yakıt maliyeti (TL/lt): "))  # Yakıt maaliyeti

    # print("Toplam maliyet:", total_fuel_cost, "TL")
    total_fuel_cost = (distance_traveled / fuel_efficiency) * fuel_cost
    print("Toplam maliyet:", total_fuel_cost, "TL")

    # Bu kod, sürücünün kilometrede ne kadar yaktığını ve kaç kilometre yol yaptığını kullanarak toplam maliyeti hesaplar ve sonuç olarak ekrana yazdırır.


def problem4():
    """
    Problem 4
    - Kullanıcıdan ad,soyad ve numara bilgisini alarak bunları alt alta ekrana yazdırın.
    """

    ad = input("Lütfen adınızı giriniz: ")
    soyad = input("Lütfen soyadınızı giriniz: ")
    numara = input("Lütfen numaranızı giriniz: ")

    print(f"Adınız: {ad}\nSoyadnız: {soyad}\nTelefon Numarınız: {numara}\n")


def problem5():
    """
    Problem 5
    - Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin.
    """
    a = input("Lütfen birinci sayı giriniz: ")
    b = input("Lütfen ikinci sayıyı giriniz: ")

    a, b = b, a
    print(f"a'nın değeri:{a}, b'nin değeri:{b} ")


def problem6():
    """
    Problem 6
    - Kullanıcıdan bir dik üçgenin dik olan iki kenarını(a,b) alın ve hipotenüs uzunluğunu bulmaya çalışın.
    - Hipotenüs Formülü: a^2 + b^2 = c^2
    """

    a = int(input("Lütfen dik üçgenin a kenarını giriniz: "))
    b = int(input("Lütfen dik üçgenin b kenarını giriniz: "))

    hipotenus = (a**2 + b**2) ** 0.5  # hipotenus c deniyor.

    print(f"Hipotenüs: {hipotenus}")


if __name__ == "__main__":
    problem6()
