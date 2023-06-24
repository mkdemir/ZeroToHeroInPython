"""
Mantıksal Değerler ve Karşılaştırma Operatörleri
"""

# Mantıksal Değerler (Boolean): 2 değer sahiptir. True veya False. Boolean python'da bir veri tipidir (Bir koşulun sağlanıp sağlanmadığını kontrol ediyor).

a = True
print(f'type(a): {type(a)}')

b = True
print(f'type(b): {type(b)}')

# Python'da bir sayı değeri 0'dan farklıysa True 0 ise False olarak anlam kazanır. Bunu bool() fonksiyonuyla dönüştürme yaparak görebiliriz.
print(f'bool(12.4): {bool(12.4)}')
print(f'bool(1): {bool(1)}')
print(f'bool(-12.4): {bool(-12.4)}')
print(f'bool(0.0): {bool(0.0)}')
print(f'bool(0): {bool(0)}')

print(f'1 == 1: {1==1}')
print(f'1 == 2: {1==2}')

# Ayrıca pythonda eğer bir değişkenin değerini sonradan belirlemek isterseniz geçici olarak bu değişken None (atanmamış anlamında) değerine eşitleyebilirsiniz.

a = None  # Henüz değer atamadık.
print(a)

"""
Karşılaştırma Operatörleri:
- Toplam 6 tanedir.
    - == : Eşit eşit
    - != : Eşit değil mi
    - >  : Büyüktür
    - <  : Küçüktür
    - >= : Büyük eşit
    - <= : Küçük eşit
"""
print(f"'Mehmet'=='Mehmet': {'Mehmet'=='Mehmet'}")
# Listeleride kontrol edebiliyoruz.
print(f"[1,2,3] == [1,2,3]: {[1,2,3] == [1,2,3]}")

# Araba sözlükte Zula'dan daha önce geldiğinden dolayı True diyor.
print(f"'Araba'>'Zula': {'Araba' < 'Zula'}")

print(f'"Mehmet" != "Mustafa":{"Mehmet" != "Mustafa"}')

# Mantıksal Bağlaçlar: Mantıksal bağlaçlar daha çok karşılaştırma işlemini kontrol ettiğimiz zamanlarda kullanılır. Bu konuda bunları öğrenmeye çalışacağız.

# and Operatörü: Bu mantıksal bağlaç, bütün karşılaştırma işlemlerinin sonucunun True olmasına bakar.
print(1 < 2 and "Mustafa" == "Kaan")
print(1 < 2 and "Mustafa" == "Kaan" and -1 < 12)

# or Operatörü: Bu mantıksal bağlaç, bütün karşılaştırma işlemlerinin sonucunun True olmasına bakar (Ya da).
print(1 < 2 or 42 > 54)

# not Operatörü: not operatörü aslında bir mantıksal bağlaç değildir. Bu operatör sadece bir mantıksal değeri veya karşılaştırma işleminin tam tersi sonucu çevirir. Yani not operatörü True olan bir sonucu False, False olan bir sonucu True sonucuna çevirir. Kullanımı şu şekildedir.
print(not 2 == 2)
