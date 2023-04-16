"""
Kullanıcıdan Girdi Alma - input() Fonksiyonu

Programlama yaparkeb kullanıcıdan girdi almak oldukça önemlidir. Python'da kullanıcıdan girdi almamızı sağlayan input() fonksiyonu bulunmaktadır.
"""

# input fonksiyonu kullanımı
# Çalıştırdığınız zaman input fonksiyonu bizden bir girdi bekler.
x = input("Lütfen bir sayı giriniz: ")
print(f'x: {x}')
print('x\'değeri: ', x)
print('({1} = x * 3): {0}'.format(x*3, x))
print(f'type(x): {type(x)}')
print(f'(int(x) * 3): {int(int(x)) * 3}')

# Bir tane örnek bir program yazalım:

a = int(input("Birinci Sayı: "))
b = int(input("İkinci Sayı: "))
c = int(input("Üçüncü Sayı: "))
print(f'a + b + c: {a+b+c}')

try:
    x = int(input("a: "))
    print(x)
except ValueError as e:
    print(
        f"ValueError: {e} hatasını almaktayız. Bunun nedeni int bir değere string bir değer girdik.")

isim = input('İsim: ')
print(f"İsminiz, {isim}")
