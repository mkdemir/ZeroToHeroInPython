"""
Homework
"""
import logging

def problem1():
    """
    Elinizde stringlerin bulunduğu bir liste bulunduğunu düşünün.

    liste = ["345","sadas","324a","14","kemal"]

    Bu listenin içindeki stringlerden içinde sadece rakam bulunanları ekrana yazdırın. Bunu yaparken try,except bloklarını kullanmayı unutmayın.
    """

    liste = ["345","sadas","324a","14","kemal"]

    for i in liste:
        try:
            i = int(i)
            print(i)
        except:
            pass

def cift_mi(sayi):
    """
    Bir sayinın çift olup olmadığını sorgulayan bir fonksiyon yazın. Bu fonksiyon, eğer sayi çift ise *return* ile bu değeri dönsün. Ancak sayi tek sayi ise fonksiyon *raise* ile *ValueError* hatası fırlatsın. Daha sonra, içinde çift ve tek sayilar bulunduran bir liste tanımlayın ve liste üzerinde gezinerek ekrana sadece çift sayiları bastırın.
    """
    
    if (sayi % 2 == 0):
        return sayi
    else:
        raise ValueError

def configure_logging():
    """
    Logger
    """
    logging.basicConfig(
        filename='remote_controller.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    logging.getLogger()
    #logger.addHandler(logging.StreamHandler())

def main():
    """
    Def main
    """

    problem1()

    liste = [34,2,1,3,33,100,61,1800]

    for i in liste:
        try:
            print(cift_mi(i))
        except ValueError:
            pass




if __name__ == '__main__':
    main()
