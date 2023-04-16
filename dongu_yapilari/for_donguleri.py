# For Döngüleri

# in Operatörü: Pythondaki in operatörü bir elemanın başka bir listede, demet'te veya stringde (karakter dizeleri) bulunup bulunmadığını kontrol eder.
print(5 in [1, 2, 3, 4, 5])
print(10 in [1, 2, 3, 4, 5])

# for Döngüsü: Listelerin, demetlerin, stringlerin ve hatta sözlüklerin üzerinde dolaşmamızı sağlayan bir döngü türüdür.

# Liste Elemanlarını Yazdırma
liste = [1, 2, 3, 4, 5, 6, 7]
for eleman in liste:
    print(eleman)

# Liste Elemanlarını Topplama
toplam = 0
for eleman in liste:
    toplam = toplam + eleman
    print(f"Toplam: {toplam} Eleman Değeri: {eleman}")
print(toplam)

# Kalanı Bulma Operatörü
print(54 % 7)

liste = [1, 2, 3, 4, 5, 423, 54, 75, 125, 233]
print(f'Listem: {liste}')
for eleman in liste:
    if eleman % 2 == 0:
        print(f"Çift Sayılar: {eleman}")

# Karakterler Dizinleri Üzerinde Gezinmek (Stringler)
s = "Python"
for karakter in s:
    print(karakter)

# Her bir karakterleri 3 ile çarpma
s = "Python"
for karakter in s:
    print(karakter * 3)

# Demetler üzerinde gezinmek (Demetler)
demet = (1, 2, 3, 4, 5)
for a in demet:
    print(a)

liste = [(1, 2), (3, 4), (5, 6), (7, 8)]
for eleman in liste:
    print(eleman)

for (i, j) in liste:
    print(f"i: {i} j: {j}")

liste = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)]
for (i, j, k) in liste:
    print(f'i: {i}, j: {j}, k: {k}')

# Demetler içindek elemanları çarpalım.
liste = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)]
for (i, j, k) in liste:
    print(f'i * j *k: {i*j*k}')

# Sözlükler Üzerinde Gezinmek (Dictionary): Sözlükler konusunda 3 adet metod görmüştük. (keys(), values(), items())

sozluk = {"bir": 1,
          "iki": 2,
          "üç": 3,
          "dört": 4}
print(sozluk.keys())
print(sozluk.values())
print(sozluk.items())  # Değerleri tuple şeklinde alabiliriz.

# Metodları kullanmadan sözlük üzerinde gezinmek.
sozluk = {"bir": 1,
          "iki": 2,
          "üç": 3,
          "dört": 4}

for eleman in sozluk:
    print(eleman)
for eleman in sozluk.values():
    print(eleman)

print(sozluk.items())

for i, j in sozluk.items():
    print(f"Anahtar: {i}, Değer: {j}")
