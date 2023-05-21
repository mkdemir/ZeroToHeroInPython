"""
Programlama Ödevi - Koşullu Durumlar
"""


def problem1():

    """
    # Problem 1

    1'den 1000'e kadar olan sayilardan mükemmel sayi olanları ekrana yazdırın. Bunun için bir sayinın mükemmel olup olmadığını dönen bir tane fonksiyon yazın.

    Bir sayinın bölenlerinin toplamı kendine eşitse bu sayi mükemmel bir sayidır. Örnek olarak 6 mükemmel bir sayidır (1 + 2 + 3 = 6).
    """

    def mukemmel(sayi):
        
        toplam = 0
        
        for i in range(1,sayi):
            
            if (sayi % i == 0):
                toplam += i
                
        return toplam == sayi


    for i in range(1,1001):
        if (mukemmel(i)):
            print("Mukemmel sayi:",i)
        
def problem2():
    """
    # Problem 2

    Kullanıcıdan 2 tane sayi alarak bu sayiların en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazın.

    Problem için şu siteye bakabilirsiniz; 

    http://www.matematikciler.com/6-sinif/matematik-konu-anlatimlari/1020-en-kucuk-ortak-kat-ve-en-buyuk-ortak-bolen-ebob-ekok
    """
    def ebob_bulma(sayi1,sayi2):
        
        i = 1
        ebob = 1
        while (i <= sayi1 and i <= sayi2 ):

            if ( not (sayi1 % i) and not (sayi2 % i)):
                ebob = i
            i += 1
        return ebob
    sayi1 = int(input("sayi-1:"))
    sayi2 = int(input("sayi-2:"))

    print("Ebob:",ebob_bulma(sayi1,sayi2))

def problem3():
    """
    # Problem 3

    Kullanıcıdan 2 tane sayı alarak bu sayıların en küçük ortak katlarını (EKOK) dönen bir tane fonksiyon yazın.

    Problem için şu siteye bakabilirsiniz;

    http://www.matematikciler.com/6-sinif/matematik-konu-anlatimlari/1020-en-kucuk-ortak-kat-ve-en-buyuk-ortak-bolen-ebob-ekok
    """
    def ekok_bulma(sayı1,sayı2):
        
        i = 2
        ekok = 1
        while True:
            if (sayı1 % i == 0 and sayı2 % i == 0):
                ekok *= i

                sayı1 //= i
                sayı2 //= i


            elif (sayı1 % i ==  0 and sayı2 % i != 0):
                ekok *= i

                sayı1 //= i


            elif (sayı1 % i != 0 and sayı2 % i == 0):
                ekok *= i

                sayı2 //= i
            else:
                i += 1
            if (sayı1 == 1 and sayı2 == 1):
                break
        return ekok

    sayı1 = int(input("Sayı-1:"))
    sayı2 = int(input("Sayı-2:"))

    print("Ekok:",ekok_bulma(sayı1,sayı2))

def problem4():
    """
    # Problem 4

    Kullanıcıdan 2 basamaklı bir sayı alın ve bu sayının okunuşunu bulan bir fonksiyon yazın.

    Örnek: 97 ---------> Doksan Yedi
    """
    birler =  ["","Bir","İki","Üç","Dört","Beş","Altı","Yedi","Sekiz","Dokuz"]
    onlar = ["","On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]

    def okunus(sayı):
        birinci = sayı % 10
        ikinci = sayı // 10
        
        return onlar[ikinci] + " " + birler[birinci]

        
    sayı =  int(input("Sayı:"))

    print(okunus(sayı))

def problem5():
    """
    # Problem 5

    1'den 100'e kadar olan sayılardan pisagor üçgeni oluşturanları ekrana yazdıran bir fonksiyon yazın.(a <= 100,b <= 100)
    """

    def pisagor_bulma():
        
        pisagor_listesi = list()
        for i in range(1,101):
            for j in range(1,101):

                c = (i ** 2 + j ** 2) ** 0.5

                if (c == int(c) ):
                    pisagor_listesi.append((i,j,int(c)))

        return pisagor_listesi

    for i in pisagor_bulma():
        print(i)

if __name__ == "__main__":
    # problem1()
    problem2()