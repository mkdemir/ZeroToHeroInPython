"""
# range() Fonksiyonu:

Pythondaki bu hazır fonksiyon bizim verdiğimiz değerlere göre "range" isimli bir yapı oluşturur vr bu yapı listelere oldukça benzerdir.

Bu yapı başlangıç, bitiş ve opsiyonel olarak artırma değeri alarak listelere benzeyen bir sayı dizisi oluşturur.

"""

range(0, 20)  # 0'dan 20'e kadar (dahil değil) sayı dizisi oluşturur.

print(*range(0, 20))  # Yazdırmak için başına * koymamız gerekiyor.

print(*range(15))  # Başlangıç değeri 0'dan başlar.

print(*range(1, 100, 2))

print(*range(5, 100, 5))

print(*range(20, 0, -1))  # 20'den 0'a kadar git

liste = [1, 2, 3, 4, 5]
for i in liste:
    print(i)

for i in range(1, 101):
    print(i)

for i in range(1, 100):
    print("*" * i)
