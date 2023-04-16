"""
Listeler:

- Tıpki stringler gibi, indekslenirler, parçalanırlar ve üzerlerinde değişik işlemler yapabildiğimiz metodlar bulunur.

- Ancak stringlerden en önemli farkları, stringler konusunda bildiğimiz kadarıyla stringler değiştirilemez bir veri tipidir. Ancak listelerimiz değiştirilebilir bir veri tipidir.

- Bir listede her veri tipinden elemanı saklayabiliriz. Bu anlamda sıralı bir diziye benzer 

- Bu konuda neler öğreneceğiz.

1. Liste oluşturma
2. Indeksleme ve Parçalama
3. Temel Liste ve Metodları ve İşlemleri
4. İç içe Listeler

"""

# Liste Oluşturma: Listeler [] (Köşeli Parantez) içine veriler veya değerler konularak oluşturulabilir.

# liste = [] Örnek liste

liste = ['Arch Linux', 34, "Selam", 2, 12, 4]
# <class 'list'> veri tipi list olarak görünüyor.
print(f'type(liste): {type(liste)}, print(liste): {liste}')

liste = []  # Boş bir liste
print(f'liste[]: {liste}')  # []

liste = list()  # Boş bir liste tanımlama için
print(f'liste = list() : {liste}')

# len() fonksiyonu listeler üzerinde de kullanılabilir.
liste2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f'len(liste2): {len(liste2)}')

# Bir string list() fonksiyonu yardımıyla listeye dönüştürebiliriz.
x = 'Merhaba'
liste = list(x)
print(f'liste: {liste}')  # ['M', 'e', 'r', 'h', 'a', 'b', 'a']
print(f'len(liste): {len(liste)}')  # Elemanları görmek için

# Listeleri Indeksleme ve Parçalama: Listeleri indeksleme ve parçalama stringlerle birebir olarak aynıdır.
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(liste)

# 0.eleman
print(f'liste[0]: {liste[0]}')
# 4.eleman
print(f'liste[4]: {liste[4]}')

# sondaki elemanı almak istersek
print(f'liste[-1]: {liste[-1]}')  # Sondaki elemanı alıyoruz.

print(f'liste[len(liste)-1]: {liste[len(liste)-1]}')
print(f'liste[4:]: {liste[4:]}')
print(f'liste[:5]: {liste[:5]}')
print(f'liste[::2]: {liste[::2]}')
print(f'liste[::-1]:{liste[::-1]}')

# Temel Liste Metodları ve İşlemleri: Listelerin daha bir çok metodunu kursun ileriki kısımlarında görüyor olacağız.

# Bu listeyi birbirine toplama işlemini strinflerdeki gibi yapabiliriz.
liste1 = [1, 2, 3, 4, 5]
liste2 = [6, 7, 8, 8, 9]
print(f'liste1 + liste2: {liste1 + liste2}')
print(f'liste1 * 3: {liste1*3}')

liste1 = liste1 * 3
print(f'liste1: {liste1}')

# Listeler direk olarak değiştirilebilirler.
# a = "Kaan"
# a[1] = 'p' Python buna izin vermez.

liste2[1] = 10
print(liste2)

liste = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(liste[:2])

liste[:2] = [10, 11]
print(liste)

# Metodlar: Listeler, diğer programlama dillerindeki arraylere göre oldukça esnektir. Belli bir boyutları yoktur ve ekleme, çıkarma yapmak oldukça kolaydır.

# append metodu: Verdiğimiz değer listeye eklememizi sağlar.

liste = [3, 4, 5, 6]
liste.append("Kaan")
print(f'liste: {liste}')

# pop metodu: İçine değer vermezsek listenin son indeksindeki elemanı, değer verirsek verdiğimiz değere karşılık gelen indeksteki elemanı listeden atar ve attığı elemanı ekrana basar.

liste = [1, 2, 3, 4, 5, 6]
liste.pop()
print(liste)

liste = [1, 2, 3, 4, 5, 6]
liste.pop(1)
print(liste)

# sort metodu: Sort metodu listenin elemanlarını sıralmamızı sağlar.
liste = [33, 234, 254, 23]
liste.sort()
print(liste)  # [23, 33, 234, 254]

# Eğer tersini yapmak istiyorsak.
liste.sort(reverse=True)
print(liste)

liste = ["Go", "Rust", "C#", "C++", "Lua"]
liste.sort()
# ['C#', 'C++', 'Go', 'Lua', 'Rust'] alfabetik sıraya göre tersine çevirdik.
print(liste)

liste = [1, 2, 3, 4, 5, 6, 7]
# liste[40] # IndexError: list index out of range (Olmayan bir indekse ulaşmaya çalışıyorsun)

# İç İçe Listeler: Bir listenin içinde başka bir liste bulundurmak mümkündür. Bunlara Python'da içiçe listeler denmektedir. Bu tip bir özellik, Pythonda ağaç yapılarında veya matris yapılarında oldukça kullanışlı olmaktadır.

liste = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f'liste: {liste}')
print(f'liste[1][0]: {liste[1][0]}')

# 3 Tane Liste Oluşturalım.
liste1 = [1, 2, 3]
liste2 = [4, 5, 6]
liste3 = [7, 8, 9]
yeniliste = [liste1, liste2, liste3]
print(f'yeniliste = [liste1,liste2,liste3]: {yeniliste}')
print(f'yeniliste[1][2]: {yeniliste[1][2]}')
