"""
Matematik Operatörleri
"""

# Pythonda her bir anlamı satır bir ifadedir.
k = 34
l = 24
m = 54
print('k + + l + m : ', k+l+m)
print('k - m :', k-m)
print('k * l * m : {}'.format(k*l*m))
print('k/l :', k/l)

# Tamsayı Bölmesi (//): Bu operatör, bir sayının başka bir sayıya bölümünden ortaya çıkan bölüm sonucunu vermektedir.
a = 442
b = 341

print(f'a / b: {a/b}')
print(f'a // b: {a//b}')  # Sonuç bir tam değer çıktı.

print('22.5 / 12.32: {}'.format(22.5 / 12.32))
# 1.0 Tam bir değer çıkardı değer float gösterim olabilir.
print('22.5 // 12.32: {}'.format(22.5 // 12.32))

# Kalanı Bulma (%)
print('13%4 : {}'.format(13 % 4))
print('23.132%23.23213 : {}'.format(23.132 % 23.23213))

# Üst Bulma Operatörü (**): Bir sayının üstünü bulmamıza yarıyor.
print(f'2^4 : {2**4}')
print(f'3^6 : {3**6}')

# Kare Kök Bulma -> Bir sayını 1/2 kuvveti
# 8.0 python daha doğru sonuç vermesi için.
print('64 ** 0.5: {}'.format(64**0.5))
print('25 ** 0.5: {}'.format(25**0.5))

# Küp Kök Alma -> 1/3
print(f'8 ** (1/3): {8**(1/3)}')

# İşaret Değiştirme
a = -4
print(-a)

"""
Operatörleri Beraber Kullanma ve İşlem Sırası:

1. Parantez içi her zaman önce yapılır.
2. Çarpma ve Bölme her zaman Toplama ve Çıkarma İşlemine göre önce yapılır.
3. İşlemler soldan sağa değerlendirilir.

"""

print("8+4*3/2-18: {}".format(8+4*3/2-18))
print("(8+4)*3/2-18: {}".format((8+4)*3/2-18))
