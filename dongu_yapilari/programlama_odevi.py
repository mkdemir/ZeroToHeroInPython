def problem1():
    """
    Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.

    Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir. Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)
    """

    number = int(input("What is number: "))

    numbers = []
    count = 0

    for i in range(1, number):
        if number % i == 0:
            numbers.append(i)

    for z in numbers:
        count += z

    if count == number:
        print(f"{number} is perfect number")

def problem2():
    """
    1'den 10'kadar olan sayılarla ekrana çarpım tablosu bastırmaya çalışın.

    *İpucu: İç içe 2 tane for döngüsü kullanın. Aynı zamanda sayıları range() fonksiyonunu kullanarak elde edin.
    """

def main():
    problem1()

if __name__ == "__main__":
    main()
