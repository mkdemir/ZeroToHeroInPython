import math

"""
# Pythonda Sayılar

- Tam Sayılar (Integer) Ör: -1000,2,0
- Ondalıklı Sayılar (Float) Ör: -23,32, 34,2, 43,222
"""

# Basit Matematik Operatörleri

# F-strings kullanarak yazdırmak (Python 3.6 ve üzeri sürümlerde)
# 3+4 ifadesi python'da bir ifade olarak geçiyor. Python'da çalıştırılabilir her kod bir ifade olarak geçer.
print(f'3 + 4: {3+4}')

print('3 - 4: {}'.format(3-4))

print(f'3 * 4 : {3*4}')

print(f'4 * 4 * 4 : {4*4*4}')

# Sonuç 8.0 yani ondalıklı sayı çıktı bu python'ının kendi içinde tasarladığı bir şey sonucu ondalıklı sayı olarak çıkartıyor.
print('56 / 7 : {}'.format(56/7))
print(f'2.1 + 4.2 :{2.1 + 4.2}')

print(f'2.6 - 4.6 : {2.6 - 4.6}')

print(f'2.4* 4.2 : {2.4* 4.2}')

print(f'43.342 / 5.2334 : {43.342 / 5.2334}')

print(f'2 + 4 + 4 - 5 : {2 + 4 + 4 - 5}')

# Değişkenler ve Değişken Tanımlama

# Değişkenler bir programalama dilinde olmazsa olmaz bir kavramdır. Değişkenler aslında bir veri tipinden değer tutan birimlerdir.

# Belleğimizde sayi isimli bir değişken oluşuyor. Ve daha sonra bunun içine 10 değeri atılıyor.
sayi = 10
print('sayi : {}'.format(sayi))
sayi = 15
print('sayi : {}'.format(sayi))

# Python güzel bir özellik var. Bir değişkenin değeri dinamik olarak güncelleniyor (C ve Java'da bu özellik yok).
sayi = 3.4
print('sayi : {}'.format(sayi))

nickname = 'mkdemir'
print(f'nickname * nickname * nickname : {nickname * 3}')

value = 3.4
print(f'value * value * value : {value * value * value}')

a = 4
b = 3  # Çalıştırılabilir kodlarımız
c = a + 2 * b

print(f'c = a + 2 * b : {c}')

"""
# Değişken İsmi Verirken Dikkat Etmemiz Gereken Şeyler:

1. Değişken isimleri bir sayi ile başlayamaz.
2. Değişken ismi kelimelerden oluşuyorsa aralarına boşluk olmaz.
3. Sadece _ sembolü değişken ismi olarak kullanılabilir.
4. Pythonda tanımlı anahtar kelimeler değişken ismi olarak kullanılmaz (while, not vs.)

## Hatalı 
i? = 5
3mkd = 10

"""
__test__ = 10

# Bir dairenin çevresini hesaplayalım.

# çevre = 2 * pi * r
_pi_sayisi_ = math.pi
_r_ = 4
_cevre_ = _pi_sayisi_ * _r_ * 2
print(f'_cevre_ = _pi_sayisi_ * _r_ : {_cevre_}')

# Değişken Değiştirme
degisken1 = 5
degisken2 = 4

degisken3 = degisken1
degisken1 = degisken2
degisken2 = degisken3
print(f'Degisken 1 : {degisken1}, Degisken 2 : {degisken2}')

# Veya
degisken1 = 5
degisken2 = 4
degisken1, degisken2 = degisken2, degisken1
print(f'Degisken 1 : {degisken1}, Degisken 2 : {degisken2}')

i = 4
i = i + 1

print(f'i = i + 1 : {i}')

i = 4
i += 1
print(f'i += 1 : {i}')

i = 4
i += 2
print(f'i += 1 : {i}')

b = 3
b *= 4
print('b *= 4 : {}'.format(b))

# Yorum Satırları

# Tekli Yorum Satırı
"""
Çoklu Yorum Satırı
"""

print("3+4 : {} ".format(3+4))
print("Test 1: {} Test 3: {}".format(2, 3))

a = 3
b = 3
print('a + b :', a+b)
