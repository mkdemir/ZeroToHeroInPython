"""
Programlama Ödevi - Gömülü Fonksiyonlar
"""
from functools import reduce



def problem1():
    """
Problem 1
Elinizde bir dikdörtgenin kenarlarını ifade eden sayı çiftlerinin bulunduğu bir liste olsun.

         [(3,4),(10,3),(5,6),(1,9)]

Şimdi kenar uzunluklarına göre dikdörtgenin alanını hesaplayan bir fonksiyon yazın ve bu listenin her bir elemanına bu fonksiyonu uygulayarak ekrana şöyle bir liste yazdırın.

         [12, 30, 30, 9]

*Not : map() fonksiyonunu kullanmaya çalışın.*
    """
    def alan_hesapla(demet):
        return demet[0] * demet[1]


    liste = [(3,4),(10,3),(5,6),(1,9)]

    print(list(map(alan_hesapla,liste)))

def problem2():
    """
Problem 2
Elinizden her bir elemanı 3'lü bir demet olan bir liste olsun.

     [(3,4,5),(6,8,10),(3,10,7)]

Şimdi kenar uzunluklarına göre bu kenarların bir üçgen olup olmadığını dönen bir fonksiyon yazın ve sadece üçgen belirten kenarları bulunduran listeyi ekrana yazdırın.

     [(3, 4, 5), (6, 8, 10)]

*** Not: filter() fonksiyonunu kullanmaya çalışın. ***    
    """
    def üçgen_mi(demet):
        
        if (abs(demet[0]+demet[1]) > demet[2] and abs(demet[0]+demet[2]) > demet[1] and abs(demet[1]+demet[2]) > demet[0]):
            return True
        else:
            return False


    liste = [(3,4,5),(6,8,10),(3,10,7)]

    print(list(filter(üçgen_mi,liste)))


def problem3():
    """
Problem 3
Elinizde şöyle bir liste bulunsun.

    [1,2,3,4,5,6,7,8,9,10]

Bu listenin içindeki çift sayıların toplamını ekrana yazdıran bir fonksiyon yazın.

*Not: İlk önce filter() fonksiyonu ile çift sayıları ayıklayın. Daha sonra reduce() fonksiyonunu kullanın.*
    """

    # from functools import reduce
    liste = [1,2,3,4,5,6,7,8,9,10]

    filtre = list(filter(lambda x : x % 2 == 0,liste))

    print(reduce(lambda x,y : x + y,filtre))

def problem4():
    """
Problem 4
Elinizde isimlerin ve soyisimlerin bulunduğu iki tane liste olsun.

        isimler -----> ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]

        soyisimler -----> ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

Bu isimleri ve soyisimleri sırasıyla eşleştirin ve ekrana alt alta isimleri ve soyisimleri yazdırın.

*Not: zip() fonksiyonunu kullanmaya çalışın. *
    """
    isimler = ["Fatih","Polat","Elif","Pınar","Beyza","Hatice","Selim"]

    soyisimler = ["Yılmaz","Öztürk","Dağdeviren","Türk","Dikmen","Kaya","Polat"]

    for i,j in zip(isimler,soyisimler):
        print(i,j)

def main():
    """
    Def main
    """
    problem4()


if __name__ == '__main__':
    main()