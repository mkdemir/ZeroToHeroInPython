"""
# Koşullu Durumlar - if-else Koşullu Durumlar

- Çoğu zaman python programlarımız belirli bloklardan oluşur ve bu bloklar her zaman çalışmak zorunda olmaz.
- Python'da blok tanımlama işlemi Girintiler sayesinde olmaktadır.
- Bu girintiler tab tuşu ile yapılıyor. 4 boşluk yani
"""

a = 2  # Blok 1'e ait kod.
if (a == 2):
    print(a)  # Blok 2'ye ait kod
print("Merhaba")  # Blok 1'e ait kod

# Koşullu Durumlar
yas = int(input("Yaşınızı Girin:"))
# If Bloğu: Eğer koşul sağlanırsa anlmaı taşır.
if yas < 18:
    print("Mekana Girmezsiniz!")
# Else Bloğu: Else blokları if koşulu sağlanmadığı zaman (false) çalışan bloklardır.
else:
    print("Mekana Girebilirsiniz :D")

sayi = int(input("Sayı: "))

if sayi < 0:
    print("Negatif Sayı")
else:
    print("Sıfır veya Pozitif Sayı")


islem = int(input("İşlemi Seçiniz:"))  # 3 tane işleminiz olsun

if islem == 1:
    print("1. işlem seçildi")
# Elif: başka bir koşul
elif islem == 2:
    print("2. işlem seçildi")
elif islem == 3:
    print("3. işlem seçildi")
elif islem == 4:
    print("4. işlem seçildi")
else:
    print("Hiç bir koşul sağlanmadı")

note = float(input("Notunuzu Giriniz:"))
if (note >= 90):
    print("AA")
elif (note >= 85):
    print("BA")
elif (note >= 80):
    print("BB")
elif (note >= 75):
    print("CB")
elif (note >= 70):
    print("CC")
elif (note >= 65):
    print("DC")
elif (note >= 60):
    print("DD")
else:
    print("Kaldınız....")
