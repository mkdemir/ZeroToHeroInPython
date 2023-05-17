def problem1():
    """
    # Problem 1

    Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.

    Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir. Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)
    """
    # 1. Yöntem:

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
    else:
        print(f"{number} isn't perfect number")

    # # 2. Yöntem:
    # sayı = int(input("Sayı:"))
    # i = 1
    # toplam = 0
    # while (i < sayı):
    #     if (sayı % i == 0):
    #         toplam += i
    #     i += 1

    # if (toplam == sayı):
    #     print(sayı,"mükemmel bir sayıdır.")
    # else:
    #     print(sayı,"mükemmel bir sayı değildir.")

def problem2():
    """
    # Problem 2
    Kullanıcıdan aldığınız bir sayının "Armstrong" sayısı olup olmadığını bulmaya çalışın.

    Örnek olarak, Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan herbirinin 4. kuvvetinin toplamı( 3 basamaklı sayılar için 3.kuvveti ) o sayıya eşitse bu sayıya "Armstrong" sayısı denir.

    Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4
    """
    number = int(input('Please enter a number: '))

    number_len = len(str(number))

    total = 0
    temp_number = number
    while temp_number > 0:
        dijit = temp_number % 10
        total += dijit ** number_len
        temp_number //= 10

    if number == total:
        print(f'{number} is a Armstrong number')
    else:
        print(f"{number} isn't a Armstrong number")

def problem3():
    """
    # Problem 3
    1'den 10'kadar olan sayılarla ekrana çarpım tablosu bastırmaya çalışın.

    *İpucu: İç içe 2 tane for döngüsü kullanın. Aynı zamanda sayıları range() fonksiyonunu kullanarak elde edin.*
    """
    # 1. Yöntem
    for i in range(1,11):
        print("**********************************")
        print(i)
        for m in range(1,11):
            print(i*m)

    # # 2. Yöntem
    # for i in range(1,11):
    # print("*************************************************")
    # for j in range(1,11):
        
    #     print("{} x {} = {}".format(i,j,i*j))
    
def problem4():
    """
    # Problem 4
    Her bir while döngüsünde kullanıcıdan bir sayı alın ve kullanıcının girdiği sayıları "toplam" isimli bir değişkene ekleyin. Kullanıcı "q" tuşuna bastığı zaman döngüyü sonlandırın ve ekrana "toplam değişkenini" bastırın.

    *İpucu : while döngüsünü sonsuz koşulla başlatın ve kullanıcı q'ya basarsa döngüyü break ile sonlandırın.*
    """

    # 1. Yöntem
    total = 0

    while True:

        number = input("Please enter a number: ")

        if (str(number) == "q" or str(number) == "Q"):
            print(f"Total is {total}")
            break
    
        total += int(number)
    
    # # 2. Yöntem

    # toplam = 0

    # while True:
        
    #     sayı = input("Sayı:")
        
    #     if (sayı == "q"):
    #         break
    #     sayı = int(sayı)
        
    #     toplam += sayı
        
    # print("Girdiğiniz Sayıların Toplamı:",toplam)

def problem5():
    """
    # Problem 5

    1'den 100'e kadar olan sayılardan sadece 3'e bölünen sayıları ekrana bastırın. Bu işlemi *continue* ile yapmaya çalışın.
    """

    for i in range(1,101):

        if i % 3 != 0:
            continue
        print(i)

def problem6():
    """
    Buradaki problemin çözümünü derslerimizde özellikle öğrenmedik. Burada mantık yürüterek ve list comprehension kullanarak 1'den 100'e kadar olan sayılardan sadece çift sayıları bir listeye atmayı yapmayı çalışın.

    Not: Programlamada her detayı öğrenemeyiz. Bunun için bazı yerlerde deneme yanılma yoluyla da öğrendiğimiz şeyler olur. Bu problemde deneme yanılma yoluyla list comprehension'ın koşullu durumlarla kullanımını öğreneceksiniz.

    İpucu: Basit düşünmeye çalışın
    """

    # liste = [ifade for eleman in dizi if koşul]
    numbers = [i for i in range(1,101) if i % 2==0]
    print(numbers)

def main():
    # problem1()
    # problem2()
    # problem3()
    # problem4()
    # problem5()
    problem6()

if __name__ == "__main__":
    main()
