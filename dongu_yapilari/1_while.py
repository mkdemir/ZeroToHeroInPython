"""
While Döngüleri

while döngüleri belli bir koşul sağlandığı sürece bloğundaki işlemleri gerçekleştirmeye devam eder.
"""

# Döngüde i değerlerini ekrana yazdıralım.
i = 0
while (i < 10):  # Bu işlem true olduğu sürece işlemler devam ediyor.
    print("i'nin değeri: {}".format(i))
    i += 1

i = 0
while (i < 20):
    print(f"i'nin değeri: {i}")
    i += 2

# for ile yapma
# Bir liste belirtilir ve her elemanı için for döngüsü kullanarak her elemanı ekrana yazdırılır
liste = [1, 2, 3, 4, 5]
for i in liste:
    print(i)

# while ile yapma
index = 0
while (index < len(liste)):
    # While döngüsü kullanarak liste elemanlarını ve index değerlerini ekrana yazdırılır.
    print("Index:", index, "Liste Elemanı:", liste[index])
    index += 1

# Sonsuz Döngü Olayları
# While döngüsünün belirli bir süre sonra 'false' olması gerekiyor. Yoksa döngü sonsuza gidiyor.
#i = 0
#while (i < 10):
#    print(i)
