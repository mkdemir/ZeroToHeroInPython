"""
Veri Tipi Dönüşümleri:
"""

# Tamsayısı Ondalıklı Sayıya Çevirme
a = 43
print(f'a : {float(a)}')
b = -123.222232
print(f'b : {float(b)}')
c = 9
print(f'c : {float(c)}')

# Ondalıklı Sayıyı Tamsayıya Çevirme
d = 2321.9
print(f'd : {int(d)}')
e = 234234234234234231.43423423424323423423432423432423423423432
print(f'e : {int(e)}')

# Sayıları Stringlere Çevirme
f = 34234234324324
print(f'f : {str(f)}')
f = str(f)
print(f'len(f) : {len(f)}')
g = 3.14
print(f'f : {str(g)}')

# Stringleri Tamsayıya Çevirme
h = "3434adasd"
# int(a) # ValueError: invalid literal for int() with base 10: '3434adasd' hatasını alırız. Hata bize diyorki her bir karakter 10'luk tabanda olmalı.
i = '343423423'
print(f'i : {int(i)}')

# Stringleri Ondalıklı Sayıya Çevirme
j = '43.2323'
print(f'j : {float(j)}')

k = '434.34234.234234'  # Böyle bir ondalık bir form yok.
float(k)  # Böyle bir string'i ondalıklı sayıya çeviremiyoruz.
