"""
Print Fonksiyonu ve Formatlama
"""

print('34')
print('3.14')
print('mkdemir')

a = 4
b = 15
print(a+b)

print(23, 231, 2, 23.12, "Python")

print('Mustafa', 'Kaan', 'Demir')

# Stringlerdeki Özel Karakterler
# \n
print('Mustafa\nKaan\nDemir')

# \t
print('Ocak\tMart\tŞubat')  # \t -> 1 Tab boşluk bırak. (Tab 4 boşluk bırakır.)

# type(): İçine gönderilen değerin hangi veri tipinden olduğunu söyler.
deger = 44545
print(f'type(deger): {type(deger)}')  # type(deger): <class 'int'>

# Print() Fonksiyonunun Özellikleri

# sep parametresi:
print(23, 43, 42, 3423, sep='/')

print('Mustafa', 'Kaan', 'Demir', sep='\n')

print("06", "04", '2022', sep='/')

# Eğer başında yıldız varsa buradaki her bir karakter arasındaki boşluk yazıldığında biz görebiliyoruz. * Buradaki her bir karakteri ayırarak fonksiyona o şekilde gönderiyor.
print(*'Python')

print(*'Python', sep='-')

print('T', 'B', 'M', 'M', sep='.')

print(*'TBMM', sep='.')

# Stringlerde Formatlama (Biçimlendirme)
print("{} {} {}".format(231, 23123, 23))

a = 3
b = 4
print('{} + {}\'nin toplamı {}\'dır.'.format(a, b, a+b))
print('{1} {0} {2}'.format(34, 'Kaan', 343))

# Süslü parantezlerin içindeki kullanım ondalıklı kısmın sadece 2 basamağına kadar almak istediğimizi söylüyoruz.
print('2.3234= {:.2f} 334.3423423= {:.2f} 67645.245538= {:.3f}'.format(
    2.3234, 334.3423423, 67645.245538))
# https://pyformat.info/:Format fonksiyonun tüm özellikleri var.
